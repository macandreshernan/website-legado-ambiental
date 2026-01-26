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
        const rawValue = input.value.replace(/\D/g, '');
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

    // --- 3. Math Captcha ---
    const captchaContainer = document.getElementById('captcha-container');
    let captchaResult = 0;

    if (captchaContainer) {
        generateCaptcha();
    }

    function generateCaptcha() {
        const num1 = Math.floor(Math.random() * 10) + 1; // 1-10
        const num2 = Math.floor(Math.random() * 10) + 1; // 1-10
        captchaResult = num1 + num2;

        const numbersSpan = document.getElementById('captcha-numbers');
        if (numbersSpan) {
            numbersSpan.textContent = `${num1} + ${num2} = ?`;
        }
    }

    // Exposed for re-generation if needed, but for now we just run it on load.
    // We removed the complex updateCaptchaLabel logic aimed at i18n since we now use a separate span.
    function updateCaptchaLabel() {
        // No-op for now, kept for API compatibility if called elsewhere or later extended.
    }

    // --- 4. Submit Handling ---
    form.addEventListener('submit', (e) => {
        let isValid = true;

        if (!validatePhone(phoneInput)) isValid = false;
        if (!validateEmail(emailInput)) isValid = false;

        const captchaInput = document.getElementById('captcha-input');
        const captchaError = document.getElementById('captcha-error');

        if (parseInt(captchaInput.value) !== captchaResult) {
            isValid = false;
            captchaInput.classList.add('border-red-500');
            if (captchaError) captchaError.classList.remove('hidden');
        } else {
            captchaInput.classList.remove('border-red-500');
            if (captchaError) captchaError.classList.add('hidden');
        }

        if (!isValid) {
            e.preventDefault(); // Block submission
        } else {
            // In a real app, this would submit. Since it's static/demo:
            alert("Validación exitosa (Simulación de envío)");
            e.preventDefault(); // Stop actual reload for demo purposes? Or let it go?
            // User prompt didn't say to stop reload, but verify functionality.
            // We'll let it execute default if valid to see the reload/action behavior or just block to show success.
            // Let's block to keep context.
        }
    });
});

// Expose generation to global if needed for i18n re-trigger
window.generateCaptcha = function () {
    // Logic to refresh numbers if needed
    // Not strictly required if we separate DOM elements
};
