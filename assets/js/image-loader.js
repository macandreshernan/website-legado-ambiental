// assets/js/image-loader.js

/**
 * Image Load Progress script
 * Removes pulse animations and skeleton backgrounds once images finish loading
 * without using inline HTML handlers.
 */

function handleImageLoad(img) {
    img.classList.remove('opacity-0');
    const parent = img.parentElement;
    if (parent) {
        parent.classList.remove('animate-pulse', 'bg-gray-200', 'dark:bg-gray-800');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const lazyImages = document.querySelectorAll('img[loading="lazy"].opacity-0');
    
    lazyImages.forEach(img => {
        if (img.complete) {
            handleImageLoad(img);
        } else {
            img.addEventListener('load', () => handleImageLoad(img));
            // Failsafe if image breaks
            img.addEventListener('error', () => handleImageLoad(img));
        }
    });
});
