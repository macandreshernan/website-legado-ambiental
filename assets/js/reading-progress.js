// assets/js/reading-progress.js

/**
 * Reading Progress Indicator
 * Injects a 3px progress bar at the very top of the screen that fills as the user scrolls.
 */

document.addEventListener('DOMContentLoaded', () => {
    // Create progress bar container
    const progressBarContainer = document.createElement('div');
    progressBarContainer.className = 'fixed top-0 left-0 w-full h-[4px] bg-transparent z-[9999] pointer-events-none';
    progressBarContainer.setAttribute('aria-hidden', 'true');
    
    // Create the actual bar
    const progressIndicator = document.createElement('div');
    progressIndicator.className = 'h-full bg-primary w-0 transition-all duration-150 ease-out origin-left rounded-r-full shadow-[0_0_8px_rgba(46,125,50,0.8)]';
    
    progressBarContainer.appendChild(progressIndicator);
    
    // Prepend to body so it displays above everything
    document.body.prepend(progressBarContainer);

    // Update progress bar on scroll
    globalThis.addEventListener('scroll', () => {
        const scrollTop = globalThis.scrollY || document.documentElement.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        
        if (scrollHeight > 0) {
            const scrollPercent = (scrollTop / scrollHeight) * 100;
            progressIndicator.style.width = scrollPercent + '%';
        }
    }, { passive: true }); // Better scrolling performance
});
