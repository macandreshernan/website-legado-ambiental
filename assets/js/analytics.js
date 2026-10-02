/**
 * Legado Ambiental - GA4 / GTM Analytics Event Tracking Helper
 * Tracks high-intent conversion events for the 100 B2B Leads Plan.
 */

window.dataLayer = window.dataLayer || [];

function trackEvent(eventName, eventParams = {}) {
    const payload = {
        event: eventName,
        timestamp: new Date().toISOString(),
        page_location: window.location.href,
        page_title: document.title,
        ...eventParams
    };
    
    window.dataLayer.push(payload);
    console.log(`[GA4 Tracked]: ${eventName}`, payload);
}

// Auto-instrumentation on DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
    // 1. Track WhatsApp Clicks (click_whatsapp)
    document.addEventListener('click', (e) => {
        const waLink = e.target.closest('a[href*="wa.me"], a[href*="whatsapp.com"]');
        if (waLink) {
            trackEvent('click_whatsapp', {
                link_url: waLink.href,
                click_location: waLink.closest('header') ? 'header' :
                               waLink.closest('.fixed') ? 'sticky_fab_mobile' :
                               waLink.closest('footer') ? 'footer' : 'hero_content'
            });
        }

        // 2. Track PDF Portfolio & Resume Downloads (download_portfolio)
        const pdfLink = e.target.closest('a[href$=".pdf"], a[download]');
        if (pdfLink) {
            trackEvent('download_portfolio', {
                file_name: pdfLink.getAttribute('download') || pdfLink.href.split('/').pop(),
                link_url: pdfLink.href
            });
        }
    });
});
