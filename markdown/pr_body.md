## 🚀 Resumen del Pull Request

Este Pull Request consolida la transformación integral del ecosistema digital de **Legado Ambiental S.A. de C.V.** de un sitio web informativo estático hacia un **embudo de alta conversión B2B y captación directa de prospectos**, culminando con éxito los hitos de **Google Business Profile**, **Analítica GA4/GTM**, el **Dictamen Financiero de Google Ads** y la totalidad del pilar **PB5: Micro-Landings de Servicios Específicos con Conversión On-Site e Integración Institucional de LinkedIn**.

---

## 📦 Alcance Total de los Cambios

### 1. PB5: Micro-Landings de Servicios Específicos & Conversión On-Site (Módulos 1 al 5)
- **Módulo 1 (Arquitectura de Navegación & Deep-Linking Semántico):**
  - Identificadores semánticos amigables (`#ambiental`, `#construccion`, `#topografia`, `#seguridad-hidraulica`) con retrocompatibilidad para `#tab-1..4`.
  - Enrutador JavaScript con `history.replaceState` para navegación fluida sin recargas ni saltos en el historial del navegador.
  - Sincronización bidireccional en tiempo real entre pestañas de escritorio (`.tab-btn`), menú desplegable táctil en móvil (`#services-mobile-select`) y el hash de la URL.
  - Telemetría en analítica digital (`select_service_tab`) en cada cambio de división técnica.
- **Módulo 2 (Cabeceras UI/UX de Autoridad Técnica por División):**
  - 4 cabeceras micro-landing de ancho completo (`col-span-1 md:col-span-2`) en `services.html` con gradientes oscuros, bordes estilizados y propuesta de valor enfocada en dolores reales del cliente B2B (evasión de multas PROFEPA, respaldo DRO, entregas geodésicas en 24-48h, plantas PTAR).
  - 3 badges de alta credibilidad técnica por división (`SEMARNAT/PROFEPA`, `CRETI`, `DRO`, `GPS RTK`, `PTAR`, `Protección Civil`).
  - Barras de acción dual: cotización on-site directa y botón de asesoría técnica por WhatsApp con texto precargado.
- **Módulo 3 (Conversión On-Site & Erradicación de Google Forms):**
  - **0% Fuga de Tráfico:** Sustitución del 100% de los botones externos a Google Forms (`forms.gle` y `docs.google.com/forms`) por el embudo interno nativo del sitio web.
  - **Auto-selección Inteligente en `contact_faq.html`:** Detección de parámetro de URL (`?service=...`), activación automática de la pestaña de contacto (`switchTab(1)`), selección programática de la categoría en el desplegable y desplazamiento suave guiado (*smooth scroll*) al formulario.
  - **Entregables Oficiales Tangibles:** Inclusión de viñetas con entregables ejecutivos en fichas clave (AutoCAD DWG/PDF 24-48h, memorias de cálculo PTAR, bitácoras DRO y carpetas NOM-019 STPS).
- **Módulo 4 (Integración Institucional de LinkedIn `legado-ambiental-mx`):**
  - Unificación del perfil corporativo oficial: `https://www.linkedin.com/in/legado-ambiental-mx`.
  - Integración en pie de página (*Footer*) de todo el ecosistema (`home.html`, `about_us.html`, `services.html`, `portfolio.html`, `our_experience.html`, `contact_faq.html` y `404.html`) con logotipo SVG oficial e interactividad.
  - Inclusión de LinkedIn como canal directo B2B en la tarjeta de información de contacto de `contact_faq.html`.
  - Marcado estructurado Schema.org JSON-LD enriquecido con la propiedad `"sameAs": ["https://www.linkedin.com/in/legado-ambiental-mx"]` en las 6 páginas clave para SEO y Google Knowledge Graph.
- **Módulo 5 (Verificación E2E, Accesibilidad y Hardening):**
  - **Auditoría i18n automatizada:** 449 atributos `data-i18n` analizados con 0 llaves faltantes en `es-MX` y 0 en `en-US` (100% de paridad bilingüe comprobada).
  - **Validación de mapeo:** 100% de los enlaces `?service=` probados contra `SERVICE_MAPPING`.
  - **Hardening de seguridad:** Inclusión estricta de `rel="noopener noreferrer"` en todos los enlaces con `target="_blank"` y descargas de PDFs corporativos.

---

### 2. Google Business Profile (Pilar 5: SEO Local Concluido)
- **Ficha Verificada en Vivo:** Perfil corporativo verificado por Google Maps con métricas de interacción registradas.
- **Catálogo Multimedia Remasterizado:** 11 imágenes de servicios en alta resolución a proporción óptima 4:3 (1200x896 px) para Topografía, Georreferenciación GPS RTK, Supervisión de Obra Civil, Infraestructura Hidráulica y Saneamiento PTAR.
- **Modelado 3D y Cálculo Volumétrico:** Creación de carátula HD y clip de video demo de 20 segundos remasterizado para GBP (`generacion-entorno.tridimensional-services-gbp-2026-remastered-demo.mp4`).
- **Suite de Códigos QR Institucionales:** Generación de archivos vectoriales (SVG) y rasterizados (300 DPI, Nivel H), junto con la tarjeta/credencial de mostrador interactiva para recepción (`tarjeta-qr-legadoambiental.html`).

---

### 3. Medición y Analítica Digital (GA4 y GTM Concluidos)
- **Inyección de Contenedor GTM/GA4:** Etiqueta oficial con Measurement ID `G-1MLGHB4E6G` en el `<head>` de las 8 páginas HTML del proyecto.
- **Seguridad CSP:** Actualización de directivas `Content-Security-Policy` para autorizar telemetría de Google Tag Manager y Google Analytics.
- **Instrumentación de Embudo B2B (`assets/js/analytics.js`):** Eventos de conversión `form_start`, `select_service_interest`, `generate_lead`, `click_whatsapp`, `click_phone`, `filter_portfolio` y `scroll_depth`.

---

### 4. Dictamen Financiero y Suspensión Estratégica de Google Ads (Pilar 6)
- **Análisis de la Oferta Promocional:** Dictamen técnico y financiero formal sobre el cupón de $7,000 MXN en Google Ads (`DOC-LA-MKT-2026-004`).
- **Resolución Directiva:** Suspensión preventiva de la pauta pagada para cuidar el flujo de caja (ahorro de $8,120 MXN netos con IVA) y canalizar la prospección hacia canales orgánicos de alta rentabilidad (Google Maps, SEO Local y prospección B2B en LinkedIn).

---

### 5. CRO & Optimización Mobile-First (Fases 1 a 5)
- **Header Responsivo & Design Tokens:** Eliminación de desbordamiento horizontal en pantallas compactas (320px–375px) y botones con áreas táctiles de 48x48px (WCAG 2.1 AAA).
- **Hero Section JTBD:** Rediseño enfocado en resolución de problemas técnicos, Trust Banner de normativas (`NOM-052-SEMARNAT`, `STPS`, `NOM-001`) y 3 CTAs principales (*Cotizar*, *WhatsApp*, *Portafolio PDF*).
- **Formulario B2B Simplificado (6 Campos):** Reducción de fricción, protección anti-spam con campo señuelo **Honeypot** y notificaciones flotantes Toast UI.
- **Patrón Híbrido B2B en Móvil:** Barra fija inferior (*Sticky Mobile CTA Bar*) al 100% de ancho con botón *"Cotizar Proyecto"* complementada con botón flotante circular (FAB) de WhatsApp.

---

## 🧪 Pruebas Automatizadas y Validación

- [x] **Internacionalización (i18n):** 449/449 claves `data-i18n` verificadas sin faltantes en `es-MX` y `en-US`.
- [x] **Sintaxis JavaScript:** 100% de los scripts en `assets/js/*.js` validados con Node.js (`node -c`) sin errores.
- [x] **Schema.org JSON-LD:** 6/6 páginas principales con marcado estructurado validado computacionalmente con Python `json.loads`.
- [x] **Rutas y Preselección:** 100% de los parámetros `?service=` verificados contra `SERVICE_MAPPING` y `<select id="service_type">`.
- [x] **Seguridad de Enlaces:** 100% de los enlaces `target="_blank"` cuentan con `rel="noopener noreferrer"`.
- [x] **Cero Regresiones:** Libre de enlaces residuales a Google Forms externos.

---

## 📁 Archivos Principales Impactados

- `services_overview/services.html` (Cabeceras micro-landing, router semántico, conversión dual en 15 tarjetas)
- `faq/contact_faq.html` (Lectura de `?service=`, auto-selección, scroll guiado, canal directo LinkedIn)
- `home.html` (Header mobile-first, hero JTBD, sticky bar, enlaces semánticos, LinkedIn corporativo, Schema.org)
- `about_us/about_us.html`, `project_portfolio_gallery/portfolio.html`, `experience_timeline/our_experience.html` (Footers con LinkedIn, Schema.org `sameAs`, hardening de seguridad)
- `404.html` (Pie de página con enlace a LinkedIn corporativo)
- `assets/js/i18n.js` (Paridad bilingüe completa para cabeceras, tarjetas, entregables y redes)
- `assets/js/analytics.js` (Instrumentación de eventos del embudo B2B)
- `README.md` (Documentación integral de Fases 36, 37 y 38 Módulos 1 al 5)
- `assets/docs/` (Informes ejecutivos en PDF/Markdown, dictamen de Google Ads, assets multimedia de GBP)
