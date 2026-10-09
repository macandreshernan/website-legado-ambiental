/**
 * Legado Ambiental - GA4 / GTM & Google Ads Analytics Event Tracking Engine
 * Plan de Trabajo: Primeros 100 Leads B2B
 * Tracks full customer journey: attribution (gclid, UTMs), navigation, high-intent micro-conversions,
 * and lead generation funnel events (form_start, service selection, generate_lead, WhatsApp, Phone).
 */

window.dataLayer = window.dataLayer || [];
if (typeof window.gtag !== 'function') {
    window.gtag = function() {
        window.dataLayer.push(arguments);
    };
}

// --- 1. Marketing Attribution & Google Ads Click ID (gclid) Capture ---
(function initMarketingAttribution() {
    try {
        const urlParams = new URLSearchParams(window.location.search);
        const attributionKeys = ['gclid', 'wbraid', 'gbraid', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
        let captured = {};
        
        // Check existing session attribution first
        const stored = sessionStorage.getItem('legado_marketing_attribution');
        if (stored) {
            try { captured = JSON.parse(stored) || {}; } catch (e) { captured = {}; }
        }

        // Overwrite or append if current URL contains campaign parameters
        let hasNewParams = false;
        attributionKeys.forEach(key => {
            const val = urlParams.get(key);
            if (val) {
                captured[key] = val;
                hasNewParams = true;
            }
        });

        if (hasNewParams || !captured.landing_time) {
            captured.landing_time = captured.landing_time || new Date().toISOString();
            captured.landing_page = captured.landing_page || window.location.pathname;
            sessionStorage.setItem('legado_marketing_attribution', JSON.stringify(captured));
        }

        // Push attribution state to dataLayer for GTM / GA4 custom dimensions
        if (captured.gclid || captured.utm_campaign || captured.utm_source) {
            window.dataLayer.push({
                event: 'marketing_attribution_loaded',
                attribution: captured
            });

            // Set user properties in GA4 if gtag is available
            if (typeof window.gtag === 'function') {
                window.gtag('set', 'user_properties', {
                    traffic_source: captured.utm_source || (captured.gclid ? 'google_ads' : 'organic/direct'),
                    campaign_name: captured.utm_campaign || 'none',
                    google_click_id: captured.gclid || 'none'
                });
            }
        }
    } catch (err) {
        console.warn('[Analytics] Error processing attribution params:', err);
    }
})();

/**
 * Public helper to retrieve current marketing attribution data (e.g. for contact forms)
 * @returns {Object} Attribution parameters (gclid, utm_source, utm_campaign, etc.)
 */
window.getMarketingAttribution = function () {
    try {
        const stored = sessionStorage.getItem('legado_marketing_attribution');
        return stored ? JSON.parse(stored) : {};
    } catch (e) {
        return {};
    }
};

/**
 * Main event dispatcher for GA4 / GTM and Google Ads
 * @param {string} eventName Name of the analytics event
 * @param {Object} eventParams Additional event properties
 */
function trackEvent(eventName, eventParams = {}) {
    const attribution = window.getMarketingAttribution();
    const payload = {
        event: eventName,
        timestamp: new Date().toISOString(),
        page_location: window.location.href,
        page_title: document.title,
        campaign_source: attribution.utm_source || (attribution.gclid ? 'google_ads' : 'direct/organic'),
        campaign_name: attribution.utm_campaign || undefined,
        gclid: attribution.gclid || undefined,
        ...eventParams
    };
    
    window.dataLayer.push(payload);
    console.log(`[GA4 / GTM Tracked]: ${eventName}`, payload);

    // If gtag is directly configured, trigger gtag event as well
    if (typeof window.gtag === 'function') {
        window.gtag('event', eventName, payload);
    }
}

// Make trackEvent available globally
window.trackEvent = trackEvent;

/**
 * Helper to dispatch Google Ads specific conversions (when Google Ads tag is linked)
 * @param {string} conversionIdOrSendTo e.g. "AW-XXXXXXXXX/YYYYYYYY"
 * @param {number} value Optional value of conversion
 * @param {string} currency Currency code (default MXN)
 */
window.trackGoogleAdsConversion = function(conversionIdOrSendTo, value = 0, currency = 'MXN') {
    if (typeof window.gtag === 'function') {
        window.gtag('event', 'conversion', {
            'send_to': conversionIdOrSendTo,
            'value': value,
            'currency': currency
        });
        console.log(`[Google Ads Conversion Sent]: ${conversionIdOrSendTo}`);
    } else {
        window.dataLayer.push({
            event: 'google_ads_conversion',
            send_to: conversionIdOrSendTo,
            value: value,
            currency: currency
        });
    }
};

// --- 2. Automated Event Instrumentation on DOMContentLoaded ---
document.addEventListener('DOMContentLoaded', () => {
    
    // Track 404 Error page view if present
    if (document.title.includes('404') || window.location.pathname.includes('404')) {
        trackEvent('error_404_view', {
            requested_url: window.location.href
        });
    }

    // A. Click Event Delegation for High-Intent User Actions
    document.addEventListener('click', (e) => {
        // 1. Track WhatsApp Clicks (click_whatsapp) - High-intent B2B conversation
        const waLink = e.target.closest('a[href*="wa.me"], a[href*="whatsapp.com"]');
        if (waLink) {
            trackEvent('click_whatsapp', {
                link_url: waLink.href,
                click_location: waLink.closest('header') ? 'header' :
                               waLink.closest('.fixed') ? 'sticky_fab_mobile' :
                               waLink.closest('footer') ? 'footer' :
                               waLink.closest('#tab-section-1') ? 'contact_tab' : 'body_content'
            });
            return;
        }

        // 2. Track Phone Calls (click_phone) - Direct purchase intention
        const phoneLink = e.target.closest('a[href^="tel:"]');
        if (phoneLink) {
            const rawNumber = phoneLink.getAttribute('href').replace('tel:', '').trim();
            trackEvent('click_phone', {
                phone_number: rawNumber,
                click_location: phoneLink.closest('header') ? 'header' :
                               phoneLink.closest('footer') ? 'footer' :
                               phoneLink.closest('.tab-section') ? 'contact_form_area' : 'body_content'
            });
            return;
        }

        // 3. Track Google Reviews & Google Maps Clicks (Google Business Profile)
        const reviewLink = e.target.closest('a[data-action="google-review"], a[href*="review"], a[href*="search?q=Legado+Ambiental+resenas"]');
        if (reviewLink) {
            trackEvent('click_google_review', {
                link_url: reviewLink.href,
                click_location: reviewLink.closest('footer') ? 'footer' : 'contact_info_card'
            });
            return;
        }

        const mapsLink = e.target.closest('a[data-action="google-maps"], a[href*="maps.google.com"], a[href*="goo.gl/maps"]');
        if (mapsLink) {
            trackEvent('click_google_maps', {
                link_url: mapsLink.href,
                click_location: mapsLink.closest('footer') ? 'footer' : 'contact_info_card'
            });
            return;
        }

        // 4. Track PDF Portfolio & Resume Downloads (download_portfolio)
        const pdfLink = e.target.closest('a[href$=".pdf"], a[download]');
        if (pdfLink) {
            trackEvent('download_portfolio', {
                file_name: pdfLink.getAttribute('download') || pdfLink.href.split('/').pop(),
                link_url: pdfLink.href
            });
            return;
        }

        // 5. Track Portfolio Filter Category Clicks (filter_portfolio)
        const filterBtn = e.target.closest('.filter-btn, [data-filter]');
        if (filterBtn) {
            const filterCategory = filterBtn.getAttribute('data-filter') || filterBtn.textContent.trim();
            trackEvent('filter_portfolio', {
                filter_category: filterCategory
            });
            return;
        }

        // 6. Track Service Cards & High-Intent Navigation CTAs
        const serviceLink = e.target.closest('a[href*="services.html#"], a[href*="contact_faq.html"]');
        if (serviceLink && !serviceLink.closest('nav') && !serviceLink.closest('footer')) {
            trackEvent('view_service_detail', {
                target_url: serviceLink.href,
                cta_text: serviceLink.textContent.trim().substring(0, 50)
            });
            return;
        }

        // 7. Track Generic Call to Action (CTA) clicks
        const ctaBtn = e.target.closest('.btn-cta, [data-cta]');
        if (ctaBtn) {
            trackEvent('cta_click', {
                cta_label: ctaBtn.getAttribute('data-cta') || ctaBtn.textContent.trim().substring(0, 50)
            });
        }
    });

    // B. FAQ Accordion Interaction Tracking
    document.querySelectorAll('details').forEach(detailsEl => {
        detailsEl.addEventListener('toggle', () => {
            if (detailsEl.open) {
                const questionText = detailsEl.querySelector('summary')?.textContent?.trim().substring(0, 100) || 'Pregunta frecuente';
                trackEvent('click_faq_accordion', {
                    faq_question: questionText
                });
            }
        });
    });

    // C. B2B Contact Form Funnel Tracking (form_start & select_service_interest)
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        let formStarted = false;
        
        // Detect form_start on first interaction with any form input
        contactForm.addEventListener('focusin', () => {
            if (!formStarted) {
                formStarted = true;
                trackEvent('form_start', {
                    form_id: 'contact_form_b2b',
                    form_name: 'Solicitud de Cotización'
                });
            }
        }, { once: true });

        // Detect service interest selection
        const serviceSelect = document.getElementById('service_type');
        if (serviceSelect) {
            serviceSelect.addEventListener('change', () => {
                trackEvent('select_service_interest', {
                    selected_service: serviceSelect.value
                });
            });
        }
    }

    // D. Scroll Depth Tracking (25%, 50%, 75%, 90%)
    (function initScrollTracking() {
        const thresholds = [25, 50, 75, 90];
        const triggered = new Set();

        function checkScroll() {
            const h = document.documentElement;
            const b = document.body;
            const scrollTop = h.scrollTop || b.scrollTop;
            const scrollHeight = (h.scrollHeight || b.scrollHeight) - h.clientHeight;
            if (scrollHeight <= 0) return;

            const percentage = Math.round((scrollTop / scrollHeight) * 100);

            thresholds.forEach(th => {
                if (percentage >= th && !triggered.has(th)) {
                    triggered.add(th);
                    trackEvent('scroll_depth', {
                        depth_percentage: th,
                        page_path: window.location.pathname
                    });
                }
            });

            if (triggered.size === thresholds.length) {
                window.removeEventListener('scroll', scrollListener);
            }
        }

        let ticking = false;
        function scrollListener() {
            if (!ticking) {
                window.requestAnimationFrame(() => {
                    checkScroll();
                    ticking = false;
                });
                ticking = true;
            }
        }

        window.addEventListener('scroll', scrollListener, { passive: true });
    })();

});
