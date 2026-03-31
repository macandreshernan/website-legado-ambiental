// assets/js/toast-service.js

/**
 * Toast Notification Service for Legado Ambiental
 * Provides non-blocking feedback (success/error/info) to the user.
 */

globalThis.ToastService = {
    init: function() {
        if (!document.getElementById('toast-container')) {
            const container = document.createElement('div');
            container.id = 'toast-container';
            container.className = 'fixed bottom-5 right-5 z-[9999] flex flex-col gap-3 pointer-events-none';
            document.body.appendChild(container);
        }
    },

    show: function(message, type = 'success', duration = 4000) {
        this.init();
        
        const container = document.getElementById('toast-container');
        const toast = document.createElement('div');
        
        // Define colors based on type
        let bgColors = 'bg-primary text-white';
        let icon = 'check_circle';
        
        if (type === 'error') {
            bgColors = 'bg-red-600 text-white';
            icon = 'error';
        } else if (type === 'info') {
            bgColors = 'bg-blue-600 text-white';
            icon = 'info';
        }
        
        toast.className = `transform transition-all duration-300 translate-y-8 opacity-0 flex items-center gap-3 px-5 py-3 rounded-lg shadow-xl font-sans text-sm font-semibold pointer-events-auto ${bgColors}`;
        
        toast.innerHTML = `
            <span class="material-symbols-outlined text-lg">${icon}</span>
            <span>${message}</span>
        `;
        
        container.appendChild(toast);
        
        // Trigger animation
        requestAnimationFrame(() => {
            toast.classList.remove('translate-y-8', 'opacity-0');
        });
        
        // Remove after duration
        setTimeout(() => {
            toast.classList.add('opacity-0', 'translate-y-8');
            setTimeout(() => {
                toast.remove();
            }, 300); // Wait for transition
        }, duration);
    }
};
