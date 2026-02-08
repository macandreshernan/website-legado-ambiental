# Internationalization (i18n) Walkthrough

We have successfully implemented internationalization for the Legado Ambiental website, allowing users to switch between Spanish (es-MX) and English (en-US).

## Changes Implemented

1.  **Translation Files**:
    *   Created `assets/i18n/es-MX.json` and `assets/i18n/en-US.json` containing all text content for the site.
    *   Structured the JSONs by page sections (e.g., `home`, `about`, `services` etc.) for better maintainability.

2.  **JavaScript Logic**:
    *   Created `assets/js/i18n.js` which handles:
        *   Loading translations from an embedded JavaScript object (optimized for local file usage).
        *   Saving user preference to `localStorage`.

> [!NOTE]
> **Fix for Local Testing (CORS):**
> Initially, translations were loaded via `fetch` from external JSON files. This caused CORS errors when opening HTML files directly from the file system (`file://`).
> To fix this, we embedded the translations directly into `i18n.js`. This ensures the language switcher works perfectly in all environments (local file system or web server).
        *   Applying text to elements with `data-i18n` attribute.
        *   Handling placeholders with `data-i18n-placeholder`.
        *   Supporting subdirectory paths via `data-base-path` attribute.

3.  **HTML Updates**:
    *   Updated all HTML pages (`home.html`, `about_us.html`, `services.html`, `portfolio.html`, `our_experience.html`, `contact_faq.html`, `index.html`).
    *   Replaced hardcoded text with `data-i18n` keys.
    *   Added Language Switcher buttons (ES | EN) to the navigation bar.
    *   Included the `i18n.js` script with appropriate base path configuration.

## How to Test

1.  **Open any page** of the website (e.g., `home.html`).
2.  **Click the "EN" button** in the top navigation bar.
    *   Verify that the text changes to English immediately.
    *   Verify that the page title and placeholders (in contact form) also change.
3.  **Navigate to another page** (e.g., Services).
    *   Verify that the language preference persists (it should stay in English).
4.  **Click "ES"** to switch back to Spanish.
5.  **Refresh the page** to ensure the preference is remembered.

## Directory Support
The system correctly handles files in subdirectories (like `about_us/about_us.html`) by using the `data-base-path="../"` attribute on the script tag to locate the JSON files correctly.

## Verification Results

The following media demonstrates the successful language switching functionality after the fix:

**Language Switching Demo (ES -> EN)**
![Click Feedback - EN Selection](file:///home/andrew/.gemini/antigravity/brain/64d65ad4-eeba-413b-af97-cd5e0db4b1ab/.system_generated/click_feedback/click_feedback_1769394140456.png)

**Full Verification Recording**
![Verification Recording](file:///home/andrew/.gemini/antigravity/brain/64d65ad4-eeba-413b-af97-cd5e0db4b1ab/verify_i18n_fix_1769394021307.webp)
