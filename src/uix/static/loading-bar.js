let loadingBarInterval = null;

function createLoadingBar() {
    const bar = document.createElement('div');
    bar.id = 'loading-bar';
    Object.assign(bar.style, {
        position: 'absolute',
        top: '0',
        width: '0%',
        height: '10px',
        backgroundColor: '#00573d',
        zIndex: '9999',
        transition: 'width 0.1s ease'
    });
    return bar;
}

function animateLoadingBar(bar) {
    let barWidth = 0;
    loadingBarInterval = setInterval(() => {
        if (barWidth <= 30) {
            barWidth += Math.floor(Math.random() * 10) + 1;
            bar.style.width = `${barWidth}%`;
        } else if (barWidth < 90) {
            barWidth += Math.floor(Math.random() * 3) + 1;
            bar.style.width = `${barWidth}%`;
        } 
        else {
            clearInterval(loadingBarInterval);
        }
    }, 50);
}

function startLoadingBar() {
    // Remove existing bar and interval if present
    stopLoadingBar();
    
    const bar = createLoadingBar();
    document.body.appendChild(bar);
    animateLoadingBar(bar);
}

function stopLoadingBar() {
    const existingBars = document.querySelectorAll('#loading-bar');
    existingBars.forEach(bar => {
        bar.style.width = '100%';
        setTimeout(() => bar.remove(), 500);
    });

    if (loadingBarInterval) {
        clearInterval(loadingBarInterval);
        loadingBarInterval = null;
    }
}

function completeLoadingBar() {
    const bar = document.getElementById('loading-bar');
    if (bar) {
        clearInterval(loadingBarInterval);
        loadingBarInterval = null;
        bar.style.width = '100%';
        setTimeout(() => bar.remove(), 500);
    }
}