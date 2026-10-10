/**
 * Contact Form Logic - Legado Ambiental
 * Handles validation, input masking, Honeypot anti-spam, and AJAX FormSubmit integration.
 */

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contact-form') || document.querySelector('form');
    if (!form) return;

    const nameInput = document.getElementById('name');
    const companyInput = document.getElementById('company');
    const phoneInput = document.getElementById('phone');
    const emailInput = document.getElementById('email');
    const serviceInput = document.getElementById('service_type');
    const locationInput = document.getElementById('location');
    const messageInput = document.getElementById('message');
    const honeypotInput = document.getElementById('website_url');

    const submitBtn = document.getElementById('submit-btn') || form.querySelector('button[type="submit"]');
    const submitText = document.getElementById('submit-text');
    const submitSpinner = document.getElementById('submit-spinner');
    const phoneError = document.getElementById('phone-error');
    const emailError = document.getElementById('email-error');

    // --- 1. Phone Masking & Validation ---
    if (phoneInput) {
        phoneInput.addEventListener('input', (e) => {
            let value = e.target.value.replace(/\D/g, ''); // Remove non-digits

            // Prevent starting with 0 or 1 (LADA rule)
            if (value.length > 0 && (value[0] === '0' || value[0] === '1')) {
                value = value.substring(1);
            }

            // Limit to 10 digits before formatting
            if (value.length > 10) value = value.substring(0, 10);

            // Format as (XX) XXXX XXXX
            let formattedValue = '';
            if (value.length > 0) {
                formattedValue += '(' + value.substring(0, 2);
            }
            if (value.length >= 3) {
                formattedValue += ') ' + value.substring(2, 6);
            }
            if (value.length >= 7) {
                formattedValue += ' ' + value.substring(6, 10);
            }

            e.target.value = formattedValue;
            validatePhone(e.target);
        });
    }

    function validatePhone(input) {
        if (!input) return false;
        const rawValue = input.value.replace(/\D/g, '');

        if (rawValue.length > 0 && rawValue.length < 10) {
            input.classList.add('border-red-500', 'focus:border-red-500', 'focus:ring-red-500/20');
            input.classList.remove('border-slate-200', 'focus:border-primary');
            if (phoneError) phoneError.classList.remove('hidden');
            return false;
        } else if (rawValue.length === 10) {
            input.classList.remove('border-red-500', 'focus:border-red-500', 'focus:ring-red-500/20');
            input.classList.add('border-slate-200', 'focus:border-primary');
            if (phoneError) phoneError.classList.add('hidden');
            return true;
        } else {
            // Empty
            if (phoneError) phoneError.classList.add('hidden');
            return false;
        }
    }

    // --- 2. Email Validation ---
    if (emailInput) {
        emailInput.addEventListener('blur', () => validateEmail(emailInput));
        emailInput.addEventListener('input', () => {
            if (emailInput.classList.contains('border-red-500')) {
                validateEmail(emailInput);
            }
        });
    }

    function validateEmail(input) {
        if (!input) return false;
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        const isValid = emailRegex.test(input.value.trim());

        if (!isValid && input.value.trim() !== '') {
            input.classList.add('border-red-500', 'focus:border-red-500', 'focus:ring-red-500/20');
            input.classList.remove('border-slate-200', 'focus:border-primary');
            if (emailError) emailError.classList.remove('hidden');
        } else {
            input.classList.remove('border-red-500', 'focus:border-red-500', 'focus:ring-red-500/20');
            input.classList.add('border-slate-200', 'focus:border-primary');
            if (emailError) emailError.classList.add('hidden');
        }
        return isValid;
    }

    // --- 3. Submit Handling ---
    form.addEventListener('submit', function (e) {
        e.preventDefault();

        // Prevent double submit
        if (submitBtn && submitBtn.disabled) return;

        let isValid = true;

        // Validar Teléfono (requerido, 10 dígitos)
        const isPhoneValid = validatePhone(phoneInput);
        if (!isPhoneValid) {
            isValid = false;
            if (phoneError) phoneError.classList.remove('hidden');
            if (phoneInput) {
                phoneInput.classList.add('border-red-500');
                phoneInput.focus();
            }
        }

        // Validar Email (requerido, formato válido)
        const isEmailValid = validateEmail(emailInput);
        if (!isEmailValid) {
            isValid = false;
            if (emailError) emailError.classList.remove('hidden');
            if (emailInput) {
                emailInput.classList.add('border-red-500');
                if (isPhoneValid) emailInput.focus();
            }
        }

        // Honeypot Anti-Spam Check
        if (honeypotInput && honeypotInput.value.trim() !== '') {
            console.warn("Spam detectado vía Honeypot.");
            if (globalThis.ToastService) {
                const msg = (globalThis.i18n && globalThis.i18n.t)
                    ? globalThis.i18n.t('contact_page.form.toast_success')
                    : '¡Solicitud enviada con éxito!';
                globalThis.ToastService.show(msg, 'success');
            }
            form.reset();
            return;
        }

        if (!isValid) {
            if (globalThis.ToastService) {
                const errMsg = (globalThis.i18n && globalThis.i18n.t)
                    ? globalThis.i18n.t('contact_page.form.toast_error')
                    : 'Por favor revisa los campos en rojo.';
                globalThis.ToastService.show(errMsg, 'error');
            }
            return;
        }

        // --- Estado de Carga UI ---
        const originalBtnText = submitText
            ? submitText.textContent
            : ((globalThis.i18n && globalThis.i18n.t) ? globalThis.i18n.t('contact_page.form.btn') : 'Enviar Solicitud de Cotización');

        if (submitBtn) submitBtn.disabled = true;
        if (submitSpinner) submitSpinner.classList.remove('hidden');
        if (submitText) {
            submitText.textContent = (globalThis.i18n && globalThis.i18n.t)
                ? globalThis.i18n.t('contact_page.form.sending')
                : 'Enviando...';
        }

        // Captura de Atribución (Google Ads Local / Campañas)
        const attribution = (typeof window.getMarketingAttribution === 'function')
            ? window.getMarketingAttribution()
            : {};

        const selectedService = serviceInput ? serviceInput.value : 'General';
        const clientCompany = companyInput ? companyInput.value.trim() : '';

        // Timeout de seguridad con AbortController (12 segundos)
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 12000);

        fetch("https://formsubmit.co/ajax/legado.ambiental.mx@gmail.com", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                name: nameInput ? nameInput.value.trim() : '',
                company: clientCompany || 'No especificada',
                phone: phoneInput ? phoneInput.value.trim() : '',
                email: emailInput ? emailInput.value.trim() : '',
                service_type: selectedService,
                location: (locationInput && locationInput.value.trim()) ? locationInput.value.trim() : 'No especificada',
                message: messageInput ? messageInput.value.trim() : '',
                origen_campana: attribution.utm_campaign || (attribution.gclid ? 'Google Ads Local' : 'Orgánico / Directo'),
                google_click_id: attribution.gclid || 'N/A',
                _subject: "Nuevo Lead B2B - Solicitud de Cotización Legado Ambiental",
                _captcha: "false",
                _template: "table"
            }),
            signal: controller.signal
        })
        .then(async (response) => {
            clearTimeout(timeoutId);
            let data = {};
            try {
                data = await response.json();
            } catch (jsonErr) {
                // Posible respuesta de texto plano o HTML
            }

            if (!response.ok || (data && (data.success === "false" || data.success === false))) {
                throw new Error((data && data.message) ? data.message : 'Error al procesar la solicitud');
            }

            // Disparar telemetría GA4 / GTM Lead Event
            if (typeof trackEvent === 'function') {
                trackEvent('generate_lead', {
                    service_category: selectedService,
                    lead_company: clientCompany
                });
            }

            // UI: Éxito
            if (submitSpinner) submitSpinner.classList.add('hidden');
            if (submitBtn) submitBtn.classList.replace('bg-primary', 'bg-green-600');
            if (submitText) {
                submitText.textContent = (globalThis.i18n && globalThis.i18n.t)
                    ? globalThis.i18n.t('contact_page.form.toast_success')
                    : '¡Solicitud Enviada!';
            }

            const successMsg = (globalThis.i18n && globalThis.i18n.t)
                ? globalThis.i18n.t('contact_page.form.toast_success')
                : '¡Su mensaje ha sido enviado con éxito! Nos pondremos en contacto pronto.';
            if (globalThis.ToastService) {
                globalThis.ToastService.show(successMsg, 'success', 5000);
            }

            // Restauración limpia del formulario y botón tras 3 segundos
            setTimeout(() => {
                form.reset();
                if (submitBtn) {
                    submitBtn.classList.replace('bg-green-600', 'bg-primary');
                    submitBtn.disabled = false;
                }
                if (submitText) submitText.textContent = originalBtnText;
                if (submitSpinner) submitSpinner.classList.add('hidden');
            }, 3000);
        })
        .catch(error => {
            clearTimeout(timeoutId);
            console.error('[ContactForm Error]:', error);

            if (submitSpinner) submitSpinner.classList.add('hidden');
            if (submitBtn) submitBtn.classList.replace('bg-primary', 'bg-red-600');
            if (submitText) submitText.textContent = 'Error al enviar';

            const isTimeout = error.name === 'AbortError';
            const errorMsg = isTimeout
                ? 'El servidor tardó en responder. Por favor contáctanos directamente vía WhatsApp o teléfono.'
                : ((globalThis.i18n && globalThis.i18n.t) ? globalThis.i18n.t('contact_page.form.toast_error') : 'Error al enviar la solicitud.');

            if (globalThis.ToastService) {
                globalThis.ToastService.show(errorMsg, 'error', 6000);
            }

            // Restaurar botón tras 3.5 segundos
            setTimeout(() => {
                if (submitBtn) {
                    submitBtn.classList.replace('bg-red-600', 'bg-primary');
                    submitBtn.disabled = false;
                }
                if (submitText) submitText.textContent = originalBtnText;
                if (submitSpinner) submitSpinner.classList.add('hidden');
            }, 3500);
        });
    });
});
