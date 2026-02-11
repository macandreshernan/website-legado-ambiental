# Implementation Plan - Standardize Navigation Menu

This plan outlines the steps to standardize the header and navigation menu across all subpages to match the design and functionality of `home.html`.

## Analysis
- **Source of Truth**: `home.html`
    - Features: Sticky header, responsive container (`max-w-7xl`), specific typography (`font-black uppercase`), Mobile Menu (hamburger button + dropdown), JS toggle logic.
- **Current State of Subpages**:
    - mismatched styling (padding, borders, max-width).
    - Missing mobile menu functionality completely.
    - Inconsistent link styles.

## Proposed Changes

I will replace the `<header>` section in the following files with the adapted version from `home.html`:
1.  `about_us/about_us.html`
2.  `experience_timeline/our_experience.html`
3.  `faq/contact_faq.html`
4.  `project_portfolio_gallery/portfolio.html`
5.  `services_overview/services.html`

### Steps for each file:

1.  **Replace Header HTML**:
    -   Use the `header` structure from `home.html`.
    -   **Path Adjustment**: Update image sources (logo) and link hrefs to be relative (prefix with `../`).
    -   **Active State**: Apply the active class (`border-b-2 border-primary pb-1 text-primary`) to the current page's link and reset others to default.

2.  **Add Mobile Menu**:
    -   Include the `#mobile-menu` div within the header container (hidden by default).
    -   Ensure mobile menu links also have corrected paths.

3.  **Inject JavaScript**:
    -   Add the mobile menu toggle script before the closing `</body>` tag.

### Code Pattern to Apply

**Header Structure:**
```html
<header class="sticky top-0 z-50 w-full bg-white/95 dark:bg-background-dark/95 backdrop-blur-sm border-b border-gray-200 dark:border-gray-800 shadow-sm transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-20">
            <!-- Logo (Path adjusted to ../assets/...) -->
            <!-- Desktop Nav (Paths adjusted, Active state applied) -->
            <!-- Language/Quote Buttons -->
            <!-- Mobile Menu Button -->
        </div>
        <!-- Mobile Menu Div (Paths adjusted) -->
    </div>
</header>
```

**Script to Add:**
```html
<script>
    const menuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileLinks = mobileMenu.querySelectorAll('a, button');

    function toggleMenu() {
        mobileMenu.classList.toggle('hidden');
        mobileMenu.classList.toggle('flex');
    }

    function closeMenu() {
        mobileMenu.classList.add('hidden');
        mobileMenu.classList.remove('flex');
    }

    menuBtn.addEventListener('click', () => {
        if (mobileMenu.classList.contains('hidden')) {
            mobileMenu.classList.remove('hidden');
            mobileMenu.classList.add('flex');
        } else {
            closeMenu();
        }
    });

    mobileLinks.forEach(link => {
        link.addEventListener('click', closeMenu);
    });
</script>
```

## Verification Plan
- Manual check of all pages to ensure the header looks identical to home (except for the active link).
- Verify mobile menu opens/closes on all pages.
- Verify navigation links work correctly from subpages.
