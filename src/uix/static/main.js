
let socket;
let event_handlers = {};
let page_loaded = false;
let logged_history = [];

// Socket event handlers
const socketEvents = {
    'start-loading-bar' : (data) => { startLoadingBar(); },
    'stop-loading-bar' : (data) => { stopLoadingBar(); },
    'navigate': (data) => { window.location = data.value; },
    'location-reload': (data) => { window.location.reload(); },
    'update-document': (data) => { pushClient(data) },
    'scroll-to': (data) => { document.getElementById(data.id).scrollIntoView({ behavior: "smooth", block: "center", inline: "nearest" }); },
    'alert': (data) => { alert(data.value); },
    'focus': (data) => { document.getElementById(data.id).focus(); },
    "init-content": async (data) => {
        const contentElement = document.getElementById(data.id);
        const { htmlContent = "", resources = {}, root_id } = data.value;
        resetResources()
        
        // Helper function to load resources
        const loadResource = async (command, type) => {
            const regex = new RegExp(`load${type}\\('([\\s\\S]+)',\\s*({[\\s\\S]+?})\\);`);
            const match = command.match(regex);
            if (!match) {
                console.error(`Regex failed to match ${type} command:`, command);
                return;
            }
            const [, content, optionsString] = match;
            const options = JSON.parse(optionsString.replace(/'/g, '"'));
            await (type === 'Style' ? loadStyle : loadScript)(content, options);
        };

        // Load styles in parallel
        await Promise.all((resources.styles || []).map(command =>
            loadResource(command, 'Style').catch(error =>
                console.error("Error processing style command:", command, error)
            )
        ));

        // Set HTML content
        contentElement.outerHTML = htmlContent;

        // Load scripts sequentially
        for (const command of resources.scripts || []) {
            try {
                await loadResource(command, 'Script');
            } catch (error) {
                console.error("Error processing script command:", command, error);
            }
        }

        if (root_id) {
            window.root_id = root_id
            clientEmit(root_id, "flush", "flush-mq");
        }
    },
    'toggle-class': (data) => { document.getElementById(data.id).classList.toggle(data.value); },
    'add-class': (data) => { document.getElementById(data.id).classList.add(data.value); },
    'remove-class': (data) => { document.getElementById(data.id).classList.remove(data.value); },
    'set-timeout': (data) => { setTimeout(() => { clientEmit(data.id, data.value, "timeout"); }, data.value); },
};

function pushClient(data) {
    const newPath = data.value.path;
    const lastPath = logged_history[logged_history.length - 1];
    const secondLastPath = logged_history[logged_history.length - 2];

    // Check if the new path is the same as the last or second-to-last path
    if (newPath === lastPath || newPath === secondLastPath) return

    // Limit the history to 10 entries
    if (logged_history.length >= 10) {
        logged_history.shift();
    }

    // Add the new path to the logged history
    logged_history.push(newPath);

    // Update the browser history and document title
    history.pushState({path: newPath}, '', newPath);
    document.title = data.value.title;
}

function handleNavigation(event) {
    if (!window.root_id) return;

    const currentPath = window.location.pathname;
    console.log("Current path:", currentPath);

    // Find the index of the current path in the logged history
    const pathIndex = logged_history.lastIndexOf(currentPath);

    if (pathIndex !== -1) {
        // If found, update the logged_history to remove any entries after this path
        logged_history = logged_history.slice(0, pathIndex + 1);
    } else {
        // If not found, add it to the logged_history
        if (logged_history.length >= 10) {
            logged_history.shift();
        }
        logged_history.push(currentPath);
    }

    clientEmit(window.root_id, currentPath, "reload");
}


function clientEmit(id, value, event_name) {
    socket.emit('from_client', { id: id, value: value, event_name: event_name });
}

function mouseEvent(event) {
    const keys = ['x', 'y', 'screenX', 'screenY', 'pageX', 'pageY', 'offsetX', 'offsetY', 'movementX', 'movementY', 'button', 'buttons', 'altKey', 'ctrlKey', 'metaKey', 'shiftKey']
    value = {};
    keys.forEach(key => {value[key] = event[key];});
    clientEmit(event.target.id, value, event.type);
}

function keyboardEvent(event) {
    const keys = ['key', 'code', 'location', 'ctrlKey', 'shiftKey', 'altKey', 'metaKey', 'repeat', 'isComposing', 'charCode', 'keyCode', 'which']
    value = {};
    keys.forEach(key => {value[key] = event[key];});
    clientEmit(event.target.id, value, event.type);
}

const getSocketInstance = () => {
    if (!socket) {
        socket = io.connect(`${window.location.origin}`, {
            query: {
                //clientPublicData: JSON.stringify(clientPublicData),
                //session_id: session_id,
            },
            reconnection: true,
            reconnectionAttempts: 15,
            reconnectionDelay: 500,
            transports: ['websocket']
        });
    }
    return socket;
};

const handleDynamicEvents = (data) => {
    if (data.event_name.startsWith("change-")) {
        if (data.event_name.split("-")[1] === "location") {
            window.location = data.value;
            return true;
        }
        const el = document.getElementById(data.id);
        el[data.event_name.split("-")[1]] = data.value;
        return true;
    }
    if (data.event_name.startsWith("set-")) {
        const el = document.getElementById(data.id);
        el['style'][data.event_name.split("-")[1]] = data.value;
        return true;
    }
    if (data.event_name.startsWith("get-")) {
        const el = document.getElementById(data.id);
        const attr_name = data.event_name.split("-")[1];
        const value = el[attr_name];
        clientEmit(data.id, value, data.event_name);
        return true;
    }
    return false;
};

const eventQueue = [];
let isProcessing = false;
const MAX_RETRIES = 3;
async function processEventQueue() {
    if (isProcessing) return;

    isProcessing = true;

    while (eventQueue.length > 0) {
        const { event, retries } = eventQueue.shift();
        try {
            await handleEvent(event);
        } catch (error) {
            console.error("Error processing event:", event, error);
            if (retries < MAX_RETRIES) {
                eventQueue.push({ event, retries: retries + 1 });
            } else {
                console.error("Max retries reached for event:", event);
            }
        }
    }

    isProcessing = false;
}

async function handleEvent(data) {
    if (socketEvents[data.event_name]) {
        await socketEvents[data.event_name](data);
    } else if (handleDynamicEvents(data)) {
        return;
    } else if (event_handlers[data.event_name]) {
        event_handlers[data.event_name](data.id, data.value, data.event_name);
    } else {
        console.warn("Unhandled event:", data);
    }
}

const initSocketEvents = () => {
    socket = getSocketInstance();

    if (socket.disconnected) {
        socket.connect();
    }

    socket.on('connect', () => {
        if (page_loaded) {
            window.location.reload();
        }
        page_loaded = true;
        clientEmit('ait-uix', {path:window.location.pathname, search:window.location.search}, 'init');

    });

    socket.on('disconnect', () => {});

    socket.on('from_server', (data) => {
        eventQueue.push({ event: data, retries: 0 });
        processEventQueue();
    });

    socket.on('error', (error) => {});
};


const detachSocketEvents = () => {
    socket = getSocketInstance();
    socket.off('connect');
    socket.off('disconnect');
    socket.off('from_server');
    socket.disconnect();
    socket.close();
    socket = null;
};


window.addEventListener('load', initSocketEvents);

window.addEventListener('beforeunload', detachSocketEvents);

window.addEventListener("popstate", handleNavigation);