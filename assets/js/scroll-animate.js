// assets/js/scroll-animate.js

document.addEventListener('DOMContentLoaded', () => {
    // Check if AOS is loaded
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            once: true,
            offset: 50,
            easing: 'ease-in-out',
        });
    }

    // Auto-apply basic scroll animations to maintain HTML cleanliness
    // Apply fade-up to all major grid items (cards, services, portfolio)
    const cardSelectors = [
        '.grid > div', // General cards inside grids
        'section > div > div', // Some generic section wrappers
        '.portfolio-item' // Specific items if any
    ];

    cardSelectors.forEach(selector => {
        document.querySelectorAll(selector).forEach((el, index) => {
            // Only apply if it doesn't already have one
            if (!('aos' in el.dataset)) {
                // Add staggered delay based on DOM order
                const delay = (index % 3) * 100;
                el.dataset.aos = 'fade-up';
                if (delay > 0) {
                    el.dataset.aosDelay = delay.toString();
                }
            }
        });
    });

    // Apply fade-in to explicit section headers
    document.querySelectorAll('section h2, section .text-center > span').forEach(el => {
        if (!('aos' in el.dataset)) {
            el.dataset.aos = 'fade-in';
        }
    });
});
