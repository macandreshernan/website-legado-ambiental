/**
 * Contact Form Logic
 * Handles validation, input masking, and client-side captcha.
 */

document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const phoneInput = document.getElementById('phone');
    const emailInput = document.getElementById('email');
    const submitBtn = form.querySelector('button');

    // --- 1. Phone Masking & Validation ---
    if (phoneInput) {
        // Enforce max length programmatically (also in HTML)
        phoneInput.addEventListener('input', (e) => {
            let value = e.target.value.replaceAll(/\D/g, ''); // Remove non-digits

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
        const rawValue = input.value.replaceAll(/\D/g, '');
        const errorSpan = document.getElementById('phone-error');

        // Simple check: must be exactly 10 digits
        if (rawValue.length > 0 && rawValue.length < 10) {
            input.classList.add('border-red-500', 'focus:border-red-500', 'focus:ring-red-500/20');
            input.classList.remove('border-slate-200', 'focus:border-primary');
            if (errorSpan) errorSpan.classList.remove('hidden');
        } else {
            input.classList.remove('border-red-500', 'focus:border-red-500', 'focus:ring-red-500/20');
            input.classList.add('border-slate-200', 'focus:border-primary');
            if (errorSpan) errorSpan.classList.add('hidden');
        }
        return rawValue.length === 10;
    }

    // --- 2. Email Validation ---
    if (emailInput) {
        emailInput.addEventListener('blur', () => validateEmail(emailInput));
        emailInput.addEventListener('input', () => {
            // Remove error state while typing to be less annoying, 
            // strictly validate on blur or submit
            if (emailInput.classList.contains('border-red-500')) {
                // optional: re-validate on input only if already in error state
                validateEmail(emailInput);
            }
        });
    }

    function validateEmail(input) {
        // User @ Domain . Extension
        const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        const isValid = emailRegex.test(input.value);
        const errorSpan = document.getElementById('email-error');

        if (!isValid && input.value.trim() !== '') {
            input.classList.add('border-red-500', 'focus:border-red-500', 'focus:ring-red-500/20');
            input.classList.remove('border-slate-200', 'focus:border-primary');
            if (errorSpan) errorSpan.classList.remove('hidden');
        } else {
            input.classList.remove('border-red-500', 'focus:border-red-500', 'focus:ring-red-500/20');
            input.classList.add('border-slate-200', 'focus:border-primary');
            if (errorSpan) errorSpan.classList.add('hidden');
        }
        return isValid;
    }

    // --- 3. Submit Handling ---
    form.addEventListener('submit', (e) => {
        e.preventDefault(); // Siempre prevenimos el reload para UX fluida
        let isValid = true;

        // Validaciones básicas de regex
        if (!validatePhone(phoneInput)) isValid = false;
        if (!validateEmail(emailInput)) isValid = false;

        // --- Honeypot Validation (Anti-spam) ---
        const honeypotInput = document.getElementById('website_url');
        if (honeypotInput && honeypotInput.value.trim() !== '') {
            // Es un bot, silently reject sin dar pistas
            console.warn("Spam detectado (Honeypot).");
            // Mostramos éxito falso para despistar al bot
            if (globalThis.ToastService) {
                globalThis.ToastService.show('Mensaje enviado correctamente.', 'success');
            }
            form.reset();
            return;
        }

        if (!isValid) {
            // Error de usuario real
            if (globalThis.ToastService) {
                globalThis.ToastService.show('Por favor revisa los campos en rojo.', 'error');
            }
            return;
        }

        // Si es válido y humano:
        submitBtn.disabled = true;
        const originalText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<span class="material-symbols-outlined animate-spin text-lg">autorenew</span> Enviando...';

        // Fake API Call Delay
        setTimeout(() => {
            if (globalThis.ToastService) {
                globalThis.ToastService.show('¡Su mensaje ha sido enviado con éxito! Nos pondremos en contacto pronto.', 'success', 5000);
            }
            form.reset();
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalText;
        }, 1200);
    });
});
