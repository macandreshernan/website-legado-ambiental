// assets/js/scroll-animate.js

document.addEventListener('DOMContentLoaded', () => {
    // Check if AOS is loaded and initialize cleanly
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            once: true,
            offset: 50,
            easing: 'ease-in-out',
        });
    }

    // Safety fallback: ensure all data-aos elements are visible regardless of CDN state
    setTimeout(() => {
        document.querySelectorAll('[data-aos]').forEach(el => {
            el.style.opacity = '1';
            el.style.transform = 'none';
        });
    }, 400);
});
