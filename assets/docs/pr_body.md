## 🚀 Resumen del Pull Request

Este Pull Request consolida la evolución integral de la plataforma digital de **Legado Ambiental S.A. de C.V.** desde un catálogo informativo estático hacia un **embudo de conversión B2B de alto rendimiento**, alineado con la meta de captación de los **Primeros 100 Leads Calificados** (constructoras, dependencias y plantas industriales del Bajío y Valle de México).

---

## 📦 Alcance Total de los Cambios

### 1. Optimización UI/UX, CRO y Mobile-First (Fases 1 a 5 de CRO)
- **Header Responsivo & Design Tokens:** Eliminación de desbordamiento horizontal en 320px–375px, botones de idioma y tema con zonas táctiles de 48x48px (WCAG 2.1 AAA).
- **Hero Section JTBD (Jobs-To-Be-Done):** Rediseño con propuesta de valor orientada a soluciones técnicas, Trust Banner con normativas oficiales (`NOM-052-SEMARNAT`, `STPS`, `NOM-001`) y 3 CTAs principales (*Cotizar*, *WhatsApp*, *Portafolio PDF*).
- **Pestañas de Servicios Adaptativas:** Navegación por pestañas con deep-linking por hash y select táctil en móvil; separación de contenedor de impresión PDF `@media print` en tamaño Carta.
- **Formulario B2B Simplificado (6 Campos):** Rediseño a campos indispensables con validación, protección anti-spam **Honeypot** y notificaciones flotantes Toast UI.
- **Patrón Híbrido B2B en Móvil:** Barra fija inferior (*Sticky Mobile CTA Bar*) al 100% de ancho con botón *"Cotizar Proyecto"* + Botón flotante circular (FAB) de WhatsApp directo.
- **Garantía de Internacionalización (i18n):** Paridad estricta 1:1 en `assets/js/i18n.js` entre Español (`es-MX`) e Inglés (`en-US`), con persistencia en `localStorage` y cero textos estáticos quemados.

### 2. Google Business Profile (Pilar 5: SEO Local Concluido)
- **Ficha Verificada en Vivo:** Perfil verificado por Google con más de 199 interacciones registradas.
- **Catálogo Multimedia Remasterizado:** 11 imágenes de servicios en alta resolución a proporción óptima 4:3 (1200x896 px) para Topografía, Georreferenciación GPS RTK, Supervisión de Obra Civil, Infraestructura Hidráulica y Saneamiento PTAR.
- **Modelado 3D y Cálculo Volumétrico:** Creación de carátula HD y clip de video demo de 20 segundos remasterizado para GBP (`generacion-entorno.tridimensional-services-gbp-2026-remastered-demo.mp4`).
- **Suite de Códigos QR Institucionales:** Generación de archivos vectoriales (SVG) y rasterizados (300 DPI, Nivel H), junto con la tarjeta/credencial de mostrador interactiva para recepción (`tarjeta-qr-legadoambiental.html`).

### 3. Medición y Analítica Digital (GA4 y GTM Concluidos)
- **Inyección de Contenedor GTM/GA4:** Etiqueta oficial con Measurement ID `G-1MLGHB4E6G` en el `<head>` de las 8 páginas HTML (`home.html`, `about_us.html`, `services.html`, `portfolio.html`, `our_experience.html`, `contact_faq.html`, `index.html`, `404.html`).
- **Seguridad CSP:** Actualización de encabezados `Content-Security-Policy` para autorizar telemetría de Google Tag Manager y Google Analytics.
- **Instrumentación de Embudo B2B (`assets/js/analytics.js`):** Eventos de conversión `form_start`, `select_service_interest`, `generate_lead`, `click_whatsapp`, `click_phone`, `filter_portfolio` y `scroll_depth`.

### 4. Dictamen Financiero y Suspensión de Google Ads (Pilar 6)
- **Análisis de la Oferta Promocional:** Evaluación del cupón de $7,000 MXN en Google Ads. Se constató que es un esquema *Spend-Match 1:1* que requiere gastar primero $7,000 MXN + IVA propios en 60 días, con riesgo de cobro ininterrumpido al agotarse.
- **Resolución Directiva:** Suspensión formal de Google Ads para optimizar liquidez (ahorro de $8,120 MXN netos) y concentrar los esfuerzos en canales orgánicos (Google Maps, SEO Local y prospección directa B2B en LinkedIn).

### 5. Documentación y Reportes Ejecutivos
- `INFORME_ESTADO_PLAN_TRABAJO_OCT_2026.md` / `assets/docs/Informe_Ejecutivo_Plan_Trabajo_y_Avances_2026.pdf` (Reporte ejecutivo a 4 páginas para el equipo y junta).
- `assets/docs/Dictamen_Credito_Google_Ads_7000_MXN.pdf` (Dictamen financiero sobre Google Ads).
- `README.md` actualizado con arquitectura técnica, ficha del sistema y bitácora de fases.

---

## 🧪 Pruebas y Validación Realizadas
- [x] Cero desbordamiento horizontal en viewports móviles (320px, 375px, 414px).
- [x] Prueba de alternancia bilingüe ES ↔ EN sin excepciones ni llaves sin traducir en `assets/js/i18n.js`.
- [x] Prueba de envío de formulario con validación de Honeypot y recepción de lead.
- [x] Verificación de eventos `dataLayer` y telemetría GA4/GTM en consola del navegador.
- [x] Generación y auditoría visual de PDFs de 4 páginas en Google Chrome Headless.
