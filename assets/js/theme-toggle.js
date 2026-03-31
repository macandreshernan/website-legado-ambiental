// assets/js/theme-toggle.js

/**
 * Script for managing Dark/Light Mode toggle and persistence
 * Automatically applies the saved preference on load to avoid flickering.
 */

// Define icon references (Material Symbols)
const ICON_DARK = "light_mode"; // Sun icon when in dark mode
const ICON_LIGHT = "dark_mode"; // Moon icon when in light mode

function applyTheme(isDark) {
    const htmlElement = document.documentElement;
    if (isDark) {
        htmlElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
    } else {
        htmlElement.classList.remove('dark');
        localStorage.setItem('theme', 'light');
    }
    
    // Update all toggle buttons on the page
    document.querySelectorAll('.theme-toggle-btn .material-symbols-outlined').forEach(icon => {
        icon.textContent = isDark ? ICON_DARK : ICON_LIGHT;
    });
}

function initTheme() {
    // Check local storage first, then system preference
    const storedTheme = localStorage.getItem('theme');
    let isDark = false;
    
    if (storedTheme) {
        isDark = storedTheme === 'dark';
    } else {
        isDark = globalThis.matchMedia?.('(prefers-color-scheme: dark)')?.matches;
    }
    
    applyTheme(isDark);
}

// Global toggle function to attach to buttons
globalThis.toggleDarkMode = function() {
    const htmlElement = document.documentElement;
    const isCurrentlyDark = htmlElement.classList.contains('dark');
    applyTheme(!isCurrentlyDark);
};

// Listen for system changes
globalThis.matchMedia?.('(prefers-color-scheme: dark)')?.addEventListener('change', event => {
    if (!localStorage.getItem('theme')) {
        applyTheme(event.matches);
    }
});

// Run immediately to prevent FOUC (Flash of Unstyled Content)
initTheme();
