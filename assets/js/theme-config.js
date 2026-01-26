/**
 * Centralized Tailwind Configuration for Legado Ambiental
 * Implements the new "Eco-Engineering" visual identity.
 */
tailwind.config = {
    darkMode: "class",
    theme: {
        extend: {
            colors: {
                // New Brand Colors
                "primary": "#2E7D32", // Forest Green (Nature/Corn) - Was #137fec
                "primary-dark": "#1B5E20", // Darker shade for hover
                "secondary": "#D7CCC8", // Earth/Clay (Soil)

                // Established Neutrals (Kept for consistency)
                "navy": "#101922",
                "charcoal": "#333333",
                "background-light": "#f6f7f8", // Subtle gray/white
                "background-dark": "#101922",
            },
            fontFamily: {
                // Typography update
                "sans": ["Manrope", "sans-serif"], // Technical, precise (Replaces Public Sans)
                "serif": ["Merriweather", "serif"], // Legacy, tradition (New for headings)
                "display": ["Manrope", "sans-serif"] // Alias for backward compatibility
            },
            borderRadius: { "DEFAULT": "0.25rem", "lg": "0.5rem", "xl": "0.75rem", "full": "9999px" },
            boxShadow: {
                'eco': '0 4px 14px 0 rgba(46, 125, 50, 0.25)', // Custom green shadow
            }
        },
    },
}
