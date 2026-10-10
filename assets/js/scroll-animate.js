// assets/js/scroll-animate.js
// Neutralized: AOS has been eradicated to eliminate white-screen blocking and FOUC.
// Guarantees immediate 100% visibility for any residual data-aos elements.
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[data-aos]').forEach(el => {
        el.style.opacity = '1';
        el.style.transform = 'none';
    });
});
