// resource-loader.js

(function () {
    let loadedResources = new Map();
    window.loadedResources = loadedResources;

    function appendElement(element, beforeMain) {
        if (beforeMain) {
            document.head.appendChild(element);
        } else {
            document.body.appendChild(element);
        }
    }

    function handleResourceLoading(content, options) {
        const { isUrl, type, beforeMain, defer, module, async } = options;

        if (isUrl && loadedResources.has(content)) {
            return loadedResources.get(content);
        }

        const promise = new Promise((resolve, reject) => {
            let element;
            if (type === "script") {
                element = document.createElement("script");
                element.type = module ? "module" : "text/javascript";
                if (defer) element.defer = true;
                if (async) element.async = true;
            } else if (type === "style") {
                element = document.createElement(isUrl ? "link" : "style");
                if (isUrl) {
                    element.rel = "stylesheet";
                    element.href = content;
                }
            }

            if (isUrl) {
                if (type === "script") element.src = content;
                element.onload = () => {
                    loadedResources.set(content, promise);
                    resolve();
                };
                element.onerror = () => {
                    loadedResources.delete(content);
                    reject(new Error(`Failed to load ${type}: ${content}`));
                };
            } else {
                element.textContent = content;
                setTimeout(resolve, 0);
            }

            appendElement(element, beforeMain);
        });

        if (isUrl) {
            loadedResources.set(content, promise);
        }

        return promise;
    }

    async function loadScript(content, options = {}) {
        const defaultOptions = {
            isUrl: false,
            beforeMain: false,
            defer: false,
            module: false,
            async: false
        };
        const mergedOptions = { ...defaultOptions, ...options, type: "script" };
        return handleResourceLoading(content, mergedOptions);
    }

    async function loadStyle(content, options = {}) {
        const defaultOptions = {
            isUrl: false,
            beforeMain: true
        };
        const mergedOptions = { ...defaultOptions, ...options, type: "style" };
        return handleResourceLoading(content, mergedOptions);
    }

    window.loadScript = loadScript;
    window.loadStyle = loadStyle;
    

})();