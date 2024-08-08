// resource-loader.js

(function () {
    const loadedResources = new Map();

    function appendElement(element, beforeMain) {
        if (beforeMain) {
            document.head.appendChild(element);
        } else {
            document.body.appendChild(element);
        }
    }

    function handleResourceLoading(content, isUrl, type, beforeMain) {
        if (isUrl && loadedResources.has(content)) {
            return loadedResources.get(content);
        }

        const promise = new Promise((resolve, reject) => {
            let element;
            if (type === "script") {
                element = document.createElement("script");
                element.type = "text/javascript";
            } else if (type === "style") {
                element = document.createElement(isUrl ? "link" : "style");
                if (isUrl) {
                    element.rel = "stylesheet";
                    element.href = content;
                }
            }

            if (isUrl) {
                element.src = content;
                element.onload = () => {
                    loadedResources.set(content, promise);
                    resolve();
                };
                element.onerror = () => {
                    loadedResources.delete(content);
                    reject(new Error(`Failed to load ${type}: ${content}`));
                };
            } else {
                if (type === "script") {
                    element.textContent = content;
                } else {
                    element.textContent = content;
                }
                resolve();
            }

            appendElement(element, beforeMain);
        });

        if (isUrl) {
            loadedResources.set(content, promise);
        }

        return promise;
    }

    function loadScript(content, isUrl = false, beforeMain = false) {
        return handleResourceLoading(content, isUrl, "script", beforeMain);
    }

    function loadStyle(content, isUrl = false) {
        return handleResourceLoading(content, isUrl, "style", true);
    }

    window.loadScript = loadScript;
    window.loadStyle = loadStyle;
})();
