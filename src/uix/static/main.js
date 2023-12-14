
let socket;
let event_handlers = {};
document.cookie = `locale=${localStorage.getItem('locale') || navigator.language || navigator.userLanguage}; path=/`;


const COOKIE_ATTRIBUTES = ['maxAge', 'path', 'httponly', 'secure', 'samesite'];

const clientPublicData = {
    locale: localStorage.getItem('locale') ? localStorage.getItem('locale') : navigator.language || navigator.userLanguage,
    userAgent: navigator.userAgent,
};



// Utility functions
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2)
        return parts.pop().split(';').shift();
    else
        return null;
}

const setCookie = (data) => {
    const value = data.value;
    let cookieString = `${value.name}=${value.value};`;
    COOKIE_ATTRIBUTES.forEach(attr => {
        if (value[attr]) {
            cookieString += attr === 'maxAge' ? `max-age=${value[attr]};` : `${attr}=${value[attr]};`;
        }
    });
    document.cookie = cookieString;
};

// Socket event handlers
const socketEvents = {
    'set-cookie': setCookie,
    'delete-cookie': (data) => { document.cookie = `${data.value.name}=; max-age=0`; },
    'navigate': (data) => { window.location = data.value; },
    'scroll-to': (data) => { document.getElementById(data.id).scrollIntoView({ behavior: "smooth", block: "center", inline: "nearest" }); },
    'alert': (data) => { alert(data.value); },
    'focus': (data) => { document.getElementById(data.id).focus(); },
    'init-content': (data) => { document.getElementById(data.id).outerHTML = data.value; },
    'toggle-class': (data) => { document.getElementById(data.id).classList.toggle(data.value); },
    'add-class': (data) => { document.getElementById(data.id).classList.add(data.value); },
    'remove-class': (data) => { document.getElementById(data.id).classList.remove(data.value); },
};

function clientEmit(id, value, event_name) {
    socket.emit('from_client', { id: id, value: value, event_name: event_name });
}

const getSocketInstance = () => {
    if (!socket) {
        socket = io.connect(`${window.location.origin}`, {
            query: {
                //clientPublicData: JSON.stringify(clientPublicData),
                session_id: session_id,
            },
            reconnection: true,
            reconnectionAttempts: 5,
            reconnectionDelay: 5000,
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
    return false;
};

const initSocketEvents = () => {
    socket = getSocketInstance();

    if (socket.disconnected) {
        socket.connect();
    }

    socket.on('connect', () => {
        clientEmit('myapp', 'init', 'init');
    });

    socket.on('disconnect', () => { });

    socket.on('from_server', (data) => {
        if (socketEvents[data.event_name]) {
            socketEvents[data.event_name](data);
        } else if (handleDynamicEvents(data)) {
            return;
        } else if (event_handlers[data.event_name]) {
            event_handlers[data.event_name](data.id, data.value, data.event_name);
        }
    });

    socket.on('error', (error) => { });
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