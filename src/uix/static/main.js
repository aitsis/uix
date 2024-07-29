
let socket;
let event_handlers = {};
let page_loaded = false;
// Socket event handlers
const socketEvents = {
    'navigate': (data) => { window.location = data.value; },
    'location-reload': (data) => { window.location.reload(); },
    'update-document': (data) => { history.replaceState({}, '', data.value.path); document.title = data.value.title; },
    'scroll-to': (data) => { document.getElementById(data.id).scrollIntoView({ behavior: "smooth", block: "center", inline: "nearest" }); },
    'alert': (data) => { alert(data.value); },
    'focus': (data) => { document.getElementById(data.id).focus(); },
    'init-content': (data) => { document.getElementById(data.id).outerHTML = data.value; },
    'toggle-class': (data) => { document.getElementById(data.id).classList.toggle(data.value); },
    'add-class': (data) => { document.getElementById(data.id).classList.add(data.value); },
    'remove-class': (data) => { document.getElementById(data.id).classList.remove(data.value); },
    'set-timeout': (data) => { setTimeout(() => { clientEmit(data.id, data.value, "timeout"); }, data.value); },
    'add-child': (data) => { document.getElementById(data.id).insertAdjacentHTML('beforeend', data.value); },
    'remove-child': (data) => { document.getElementById(data.id).removeChild(document.getElementById(data.value)); },
};

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
        if (socketEvents[data.event_name]) {
            socketEvents[data.event_name](data);
        } else if (handleDynamicEvents(data)) {
            return;
        } else if (event_handlers[data.event_name]) {
            event_handlers[data.event_name](data.id, data.value, data.event_name);
        }
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