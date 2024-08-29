function resetResources() {
    loadedResources.forEach((_, resource) => {
        if (resource.endsWith('.js')) {
            document.querySelector(`script[src="${resource}"]`).remove();
            loadedResources.delete(resource);
        }}
    );

    const inlineScripts = document.querySelectorAll('script:not([src])');
    inlineScripts.forEach((script) => script.remove());
    
}
