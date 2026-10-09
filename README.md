# Legado Ambiental - Plataforma Digital B2B & Embudo de Conversión

Plataforma corporativa de **Legado Ambiental S.A. de C.V.** orientada a la captación y conversión de prospectos empresariales e institucionales en el sector de **Topografía de Alta Precisión**, **Infraestructura Hidráulica**, **Obra Civil**, **Consultoría Ambiental (SEMARNAT)** y **Seguridad e Higiene (STPS)**.

---

## 🏛️ Ficha Técnica y Arquitectura del Sistema

* **Dominio Oficial:** [https://legadoambiental.com.mx](https://legadoambiental.com.mx)
* **Punto de Entrada Primario:** `home.html` (con redirección 301 desde raíz `/` e `index.html`)
* **Framework y Estilos:** Tailwind CSS v3 (vía CDN con configuración extendida y container queries)
* **Tipografías Corporativas:** `Manrope` (Cuerpo y UI técnica) y `Merriweather` (Títulos y acentos editoriales)
* **Motor de Internacionalización (i18n):** Sistema nativo modular (`assets/js/i18n.js`) con paridad 1:1 entre Español (`es-MX`) e Inglés (`en-US`), persistencia en `localStorage` y cero textos estáticos quemados.
* **Telemetría y Analítica Digital:** Google Tag Manager y Google Analytics 4 (`G-1MLGHB4E6G`) integrados en las 8 páginas con directivas CSP y 8 eventos B2B en `assets/js/analytics.js` (`form_start`, `select_service_interest`, `generate_lead`, `click_whatsapp`, `click_phone`, `scroll_depth`).
* **Seguridad y Captura de Leads:** Formulario simplificado de 6 campos en `faq/contact_faq.html` con validación cliente, protección anti-spam **Honeypot**, notificaciones flotantes Toast UI y procesamiento vía FormSubmit API.
* **Patrón de Contacto Móvil:** Patrón Híbrido B2B que combina una barra fija inferior (*Sticky Mobile CTA Bar*) para cotizaciones formales y un botón flotante circular (FAB) para WhatsApp directo.
* **Generación de Reportes PDF:** Entorno de compilación determinista vía Google Chrome Headless (`google-chrome --headless --print-to-pdf`) con arquitectura modular `@media print` en tamaño Carta (8.5" x 11").

---

## 📂 Estructura General del Proyecto

```text
website-legado/
├── home.html                       # Página principal / Hero JTBD y Trust Banner
├── index.html                      # Enrutamiento canónico con redirección 301
├── 404.html                        # Página de error personalizada y rescate de navegación
├── about_us/about_us.html          # Nosotros: Visión, misión y trayectoria directiva
├── services_overview/services.html # Catálogo de servicios con pestañas adaptativas y deep linking
├── project_portfolio_gallery/      # Galería de proyectos y casos de éxito
│   └── portfolio.html
├── experience_timeline/            # Línea de tiempo y experiencia institucional
│   └── our_experience.html
├── faq/contact_faq.html            # Preguntas frecuentes, formulario de 6 campos y mapa
├── assets/
│   ├── css/                        # Estilos complementarios y overrides
│   ├── js/
│   │   ├── analytics.js            # Telemetría GTM/GA4 y captura de parámetros UTM / gclid
│   │   ├── i18n.js                 # Diccionario maestro bilingüe (es-MX / en-US)
│   │   └── theme-config.js         # Tokens de diseño y alternador de tema claro/oscuro
│   ├── images/
│   │   ├── logo/                   # Logotipo institucional en PNG, WebP y SVG
│   │   ├── gbp-services/           # 11 imágenes de servicios HD (1200x896) y video 3D para GBP
│   │   ├── qr/                     # Suite de códigos QR vectoriales y tarjeta de mostrador
│   │   └── services/               # Fotografías históricas de proyectos
│   └── docs/                       # Documentación ejecutiva, dictámenes y generadores PDF
│       ├── Dictamen_Credito_Google_Ads_7000_MXN.pdf
│       ├── Informe_Ejecutivo_Plan_Trabajo_y_Avances_2026.pdf
│       ├── Guia_Estrategica_Google_Business_Profile_y_Ads_Local.pdf
│       └── generate_informe_equipo_pdf.py
├── INFORME_ESTADO_PLAN_TRABAJO_OCT_2026.md # Informe maestro de estado del proyecto
├── plan-mejoras-uiux-100.md        # Plan técnico de CRO y puntos de control Git
├── Plan de Trabajo y Arquitectura UI_UX - Legado Ambiental.md # Plan estratégico de 6 Pilares
└── README.md                       # Bitácora técnica y registro de cambios
```

---

## 📊 Estado Actual de los 6 Pilares Estratégicos

1. **Pilar 1: Optimización Técnica y de Conversión Web (CRO):** `[100% CONCLUIDO]`  
   Fases 1 a 5 concluidas, mobile-first, formulario de 6 campos, Sticky Bar + FAB WhatsApp, paridad bilingüe.
2. **Pilar 2: Estrategia de Contenidos y Autoridad Técnica:** `[EN CURSO - SPRINT 2]`  
   Trust banner normativo (`NOM-052`, `STPS`) activo en Hero; artículo técnico normativo extendido programado en PB6.
3. **Pilar 3: Prospección B2B y Distribución:** `[PREPARADO / EN EJECUCIÓN]`  
   Embudo digital listo para recibir tráfico directo de tomadores de decisión (directores de obra y contratistas).
4. **Pilar 4: Herramientas de Ventas y Alianzas:** `[100% CONCLUIDO]`  
   Portafolio PDF descargable, suite QR de alta definición y credencial para mostrador.
5. **Pilar 5: Búsqueda Local y Visibilidad (Google Business Profile):** `[100% CONCLUIDO]`  
   Ficha formalmente verificada por Google (199+ interacciones), 11 fotografías HD a 4:3, video 3D y suite QR.
6. **Pilar 6: Adquisición de Pago (Google Ads Local):** `[POSPUESTO POR DICTAMEN]`  
   Suspendido formalmente para optimizar capital de trabajo (ahorro de $8,120 MXN netos) y priorizar captación orgánica a costo $0.

---

## 📈 Historial y Registro Detallado de Fases Técnicas

### Resumen de Ajustes Iniciales (Fase 1)

### 1. Localización y Traducción
- **Idioma del Sitio**: Se actualizó el atributo `lang` en la etiqueta `<html>` de `en` a `es` en todas las páginas para mejorar el SEO y la accesibilidad en español.
- **Traducción Completa**: Todo el contenido textual (títulos, descripciones, botones, menús) fue traducido del inglés al **Español de América Latina**, con enfoque en terminología mexicana profesional.
  - Páginas traducidas: Inicio, Nosotros, Servicios, Portafolio, Experiencia, Contacto/FAQ.

### 2. Estructura y Navegación
- **Menú de Navegación Global**: Se implementó una barra de navegación superior consistente en todas las páginas.
- **Rutas Relativas**: Se corrigieron todos los enlaces internos para usar rutas relativas precisas, asegurando la navegación fluida entre directorios (ej. ir de `home.html` a `about_us/about_us.html` y regresar).
  - Enlace "Inicio": `../home.html` (desde subpáginas).
  - Enlaces entre secciones: Referencias cruzadas correctas (ej. desde Servicios a Portafolio).

### 3. Optimización Técnica y Diseño
- **Responsividad**: Se verificó y ajustó el diseño utilizando **Tailwind CSS** para asegurar una visualización correcta en dispositivos móviles, tabletas y escritorio.
- **Formularios**: Se adaptó el formulario de contacto en `contact_faq.html` con etiquetas y marcadores de posición en español.
- **Imágenes y Medios**: Se mantuvieron las referencias a imágenes de alta calidad, asegurando que los atributos `alt` (texto alternativo) fueran descriptivos (aunque en este paso nos enfocamos principalmente en la interfaz visible).

### 4. Archivos Refactorizados
Lista de archivos principales modificados:
1.  `home.html` - Página de inicio.
2.  `about_us/about_us.html` - Sección "Quiénes Somos".
3.  `services_overview/services.html` - Descripción de servicios.
4.  `project_portfolio_gallery/portfolio.html` - Galería de proyectos.
5.  `experience_timeline/our_experience.html` - Línea de tiempo de la empresa.
6.  `faq/contact_faq.html` - Preguntas frecuentes y contacto.

## Fase 2: Optimización Avanzada y Mejoras UX

### 1. Mejoras de Navegación (Sticky Header)
- **Cabecera Persistente**: Se implementó una cabecera "sticky" manual con clases Tailwind (`sticky top-0 z-50`). Se resolvió un conflicto de CSS (wrapper con `overflow-x-hidden`) que impedía el funcionamiento correcto en páginas interiores. Ahora el menú permanece visible al hacer scroll en todas las páginas.

### 2. SEO y Redes Sociales
- **Open Graph (Facebook/LinkedIn)**: Etiquetas `og:title`, `og:description`, `og:image` añadidas a todas las páginas principales para compartir enlaces visualmente atractivos.
- **Twitter Cards**: Etiquetas `twitter:card` (summary_large_image) añadidas.
- **Metadatos**: Descripciones únicas y relevantes para cada página.

### 3. Rendimiento y Accesibilidad
- **Fuentes Web**: Se añadió `&display=swap` a las importaciones de Google Fonts para mejorar la carga visible del texto (FOUT en lugar de FOIT).
- **Caché**: Se añadió una etiqueta meta `Cache-Control` (simulada) para sugerir caché de largo plazo.
- **Contraste y Etiquetas**: Revisión de contraste en modo claro/oscuro y mejora de etiquetas ARIA implícitas mediante HTML semántico.

## Verificación Final
Se realizaron pruebas automatizadas de navegación y comportamiento de scroll (sticky header) con éxito en todas las secciones del sitio.


## Registro de Cambios - 20 de Enero 2026

### Archivos Modificados
- `home.html`
- `about_us/about_us.html`
- `services_overview/services.html`
- `project_portfolio_gallery/portfolio.html`
- `experience_timeline/our_experience.html`
- `faq/contact_faq.html`

### Detalles Técnicos
1.  **Sticky Header**: Se añadió `sticky top-0 z-50` a la etiqueta `<header>` y se eliminó `overflow-x-hidden` de los contenedores principales para permitir el funcionamiento correcto de `position: sticky`.
2.  **Metaetiquetas**: Inclusión de `og:title`, `og:description`, `og:image` y tarjetas de Twitter.
3.  **Performance**: Adición de `font-display: swap` y metaetiqueta `Cache-Control`.

## Fase 3: Internacionalización (i18n)

Se implementó un sistema de internacionalización robusto para soportar Español (México) e Inglés (EE. UU.).

### 1. Sistema de Traducción
- **Archivos JSON**: Se crearon archivos de traducción en `assets/i18n/` (`es-MX.json` y `en-US.json`).
- **Carga Dinámica**: Script `assets/js/i18n.js` que gestiona las traducciones mediante un objeto integrado para asegurar compatibilidad offline y local.
- **Persistencia**: La preferencia de idioma del usuario se guarda en `localStorage` para mantenerse entre sesiones y navegación.

> **Nota Técnica (Fix de CORS)**: 
> Originalmente el sistema usaba `fetch` para cargar archivos JSON. Para permitir el funcionamiento local sin un servidor web (protocolo `file://`), se optimizó `i18n.js` para incluir las traducciones directamente en el script, eliminando bloqueos de seguridad por CORS.

### 2. Interfaz de Usuario
- **Selector de Idioma**: Se añadieron botones (ES | EN) en la barra de navegación de todas las páginas.
- **Atributos de Datos**: El contenido HTML ahora usa `data-i18n="clave"` en lugar de texto estático, permitiendo cambios instantáneos sin recargar la página.
- **Soporte de Rutas**: El sistema maneja correctamente la carga de archivos JSON desde subdirectorios (ej. `about_us/`) mediante el atributo `data-base-path`.

## Fase 4: Optimización SEO Técnica

Se implementaron las recomendaciones de la auditoría SEO para mejorar la indexación y visibilidad.

### 1. Archivos de Indexación
- **Sitemap.xml**: Mapa del sitio completo generado para facilitar el rastreo de todas las secciones.
- **Robots.txt**: Archivo de configuración para permitir el acceso a los bots de búsqueda.

### 2. Metadatos y Estructura
- **Etiquetas Hreflang**: Implementadas en todas las páginas para distinguir entre `es-MX` y `en-US`.
- **URLs Canónicas**: Añadidas para prevenir contenido duplicado.
- **Datos Estructurados (JSON-LD)**: Schema.org tipo `ConstructionBusiness` inyectado en todas las páginas para mejorar la presentación en resultados de búsqueda (Rich Snippets).

### 3. Actualización de Enrutamiento
- Ajuste en `i18n.js` para soportar parámetros de consulta (ej. `?lang=en-US`), permitiendo que existan URLs únicas para cada idioma, requisito indispensable para un SEO correcto en sitios estáticos.
- Ajuste en `i18n.js` para soportar parámetros de consulta (ej. `?lang=en-US`), permitiendo que existan URLs únicas para cada idioma, requisito indispensable para un SEO correcto en sitios estáticos.

## Fase 5: Optimización Multimedia

Siguiendo las mejores prácticas modernas para velocidad y accesibilidad, se reorganizaron los activos visuales.

### 1. Localización y Formato
- **Centralización**: Se eliminaron las dependencias de URLs externas de Google Photos. Todas las imágenes ahora residen localmente en `assets/images/`.
- **Formato WebP**: Todas las imágenes fueron convertidas a formato **WebP** para reducir drásticamente el peso del archivo sin perder calidad visual.
- **Estructura Semántica**: Las imágenes se organizaron en carpetas por contexto (`home`, `about`, `portfolio`, etc.) en lugar de una sola carpeta masiva.

### 2. Accesibilidad y SEO Visual
- **Refactorización de Portafolio**: En `portfolio.html`, se reemplazaron los `<div>` con `background-image` por etiquetas `<img>` semánticas.
    - Esto permite el uso de atributos `alt` reales (crucial para lectores de pantalla y SEO).
    - Permite la carga diferida nativa del navegador (`loading="lazy"`).
- **Carga Diferida**: Se aplicó `loading="lazy"` a las nuevas etiquetas de imagen para mejorar la métrica de Largest Contentful Paint (LCP).

### 3. Lista de Archivos Modificados

**Documentación**
*   `README.md`
*   `WALKTHROUGH.md`
*   `SEO_RECOMMENDATIONS.md`
*   `SEO_WALKTHROUGH.md`
*   `MEDIA_ANALYSIS.md`

**Configuración SEO (Raíz)**
*   `sitemap.xml`
*   `robots.txt`

**Activos Multimedia (Nuevos)**
*   `assets/images/home/*`
*   `assets/images/about/*`
*   `assets/images/services/*`
*   `assets/images/portfolio/*`
*   `assets/images/experience/*`

**Código Fuente (Lógica y Datos)**
*   `assets/js/i18n.js` (Actualizado con llaves para formulario extendido)
*   `assets/i18n/es-MX.json`
*   `assets/i18n/en-US.json`

**Páginas Web (HTML) - Actualizadas con rutas locales e <img>**
*   `home.html` (Imágenes locales)
*   `index.html`
*   `about_us/about_us.html` (Imágenes locales)
*   `services_overview/services.html` (Imágenes locales)
*   `project_portfolio_gallery/portfolio.html` (Refactor a `<img>` tags)
*   `experience_timeline/our_experience.html` (Imágenes locales)
*   `faq/contact_faq.html` (Formulario extendido y optimizado)

## Fase 6: Optimización del Formulario de Contacto

Para mejorar la captación de información y la usabilidad, se rediseñó el formulario de contacto.

### 1. Nuevos Campos de Datos
Se agregaron campos adicionales para obtener información más precisa del cliente potencial:
- **Apellidos (Last Name)**: Separado del nombre para mejor gestión de datos CRM.
- **Teléfono (Phone)**: Campo dedicado para contacto directo.
- **Preferencia de Contacto**: Selector (Radio Button) para elegir entre Email o Llamada.

### 2. Redistribución de Diseño (UX)
Se optimizó el layout para priorizar el espacio de escritura ("Capture Space"):
- **Grid de Nombres**: Nombre y Apellidos comparten fila (50%/50%) para mantener lógica visual.
- **Campos Full-Width**: El **Correo Electrónico** y **Teléfono** ahora ocupan el 100% del ancho del contenedor en filas separadas. Esto facilita la escritura de correos largos y números sin sentirse apretados, mejorando la experiencia tanto en escritorio como en móvil.
- **Internacionalización Total**: Todos los nuevos campos y placeholders fueron integrados al sistema `i18n.js`.

## Fase 7: Seguridad y Validación del Formulario

Se implementó una capa de seguridad y validación robusta para el formulario de contacto, enfocada en la protección contra spam y la integridad de datos del lado del cliente.

### 1. Hardening de Seguridad
- **Cabeceras HTTP**: Se añadieron metaetiquetas para `Content-Security-Policy` (CSP) y `X-Content-Type-Options`, restringiendo la carga de recursos solo a orígenes confiables (Tailwind CDN, Google Fonts/Images).
- **Control de Entrada**: Se aplicaron atributos HTML5 (`required`, `maxlength`) a todos los campos para prevenir envío de datos excesivos o vacíos.

### 2. Validaciones Lógicas (Nuevo Script)
Se creó el archivo `assets/js/contact_form.js` para manejar la lógica de negocio en el cliente:
- **Máscara Telefónica**: Formato automático `(XX) XXXX XXXX` mientras se escribe. Restricción estricta de la regla LADA (no puede iniciar con 0 ni 1).
- **Validación de Correo**: Verificación visual de regex estricto (usuario@dominio) al salir del campo.
- **Math Captcha**: Desafío numérico aleatorio (ej. "3 + 5 = ?") generado dinámicamente que bloquea el envío del formulario si la respuesta es incorrecta.

### 3. Archivos Nuevos y Modificados
- `SECURITY_RECOMMENDATIONS.md` - Análisis inicial de riesgos.
- `assets/js/contact_form.js` - Lógica de validación y Captcha.
- `assets/js/i18n.js` - Nuevas claves de traducción para errores y etiquetas de Captcha.
- `faq/contact_faq.html` - Implementación de UI de Captcha y atributos de seguridad.

## Fase 8: Refinamiento UI/UX y Estandarización Visual

Se realizó una revisión integral de la interfaz de usuario bajo la identidad de marca "Eco-Ingeniería", enfocada en la consistencia visual y la legibilidad.

### 1. Sistema de Diseño Global
- **Centralización (Config)**: Se creó `assets/js/theme-config.js` para estandarizar los valores de Tailwind globalmente, facilitando el mantenimiento.
- **Identidad Cromática**: Se reemplazó el color azul eléctrico por **Verde Bosque (`#2E7D32`)** como primario y **Verde Profundo (`#1B5E20`)** para secciones de énfasis (CTAs), alineándose con el logo y la temática sostenible.
- **Tipografía**: Migración completa a **Manrope** (cuerpo técnico) y **Merriweather** (títulos elegantes/serif) a través de Google Fonts.

### 2. Mejoras de Navegación e Iconografía
- **breadcrumbs (Migas de Pan)**: Implementación de navegación semántica (`Inicio > Sección`) en todas las páginas internas para mejorar la orientación del usuario.
- **Corrección de Iconos**: Se reparó la carga de fuentes "Material Symbols" (eje `FILL` faltante), restaurando la visibilidad de iconos críticos como flechas y checks.

### 3. Rediseño de Secciones CTA (Llamada a la Acción)
- **Estandarización**: Se replicó el diseño de "Alto Impacto" de la página `Nosotros` en `Inicio`, `Servicios` y `Experiencia`.
  - **Fondo**: `bg-primary-dark` (Verde Profundo).


  - **Botones**: Sistema de jerarquía claro: Botón Principal (Blanco/Texto Verde) y Secundario (Outline Blanco).
  - **Legibilidad**: Mejora de contraste en textos descriptivos (`text-gray-100` y peso normal), eliminando problemas de lectura del diseño anterior (azul pálido fino).

### 4. Correcciones de Layout (Línea de Tiempo)
- **Refactorización de Timeline**: En `our_experience.html`, se solucionó un error de superposición (encimado) entre los años y los gráficos en versión escritorio.
  - Se migró de un posicionamiento absoluto conflictivo a un layout **Flex/Columnar** robusto.
  - Ahora las fechas se alinean limpiamente a la izquierda y el contenido a la derecha del eje central.

### Archivos Afectados
- `assets/js/theme-config.js` (Nuevo)
- `home.html`
- `about_us/about_us.html`
- `services_overview/services.html`
- `experience_timeline/our_experience.html`
- `project_portfolio_gallery/portfolio.html`
- `faq/contact_faq.html`

## Ajustes Visuales del Logo (Detalle por Archivo)
Se implementó la nueva imagen de marca (`logo_gral4_v1.1.png`) sustituyendo los logotipos SVG genéricos en todas las páginas.

### Cambios Generales
- **Header**: Se reemplazó el contenedor SVG por una etiqueta `<img>` con altura ajustada (`h-10` o `h-12`) para mantener la proporción visual.
- **Footer**: Se actualizó el icono del pie de página con una versión más pequeña (`h-8` o `h-10`) del mismo logotipo.

### Lista de Archivos Modificados
1.  **home.html**:
    - Header: Reemplazo de SVG `size-8` por imagen logo.
    - Footer: Reemplazo de SVG `size-6` por imagen logo.
2.  **about_us/about_us.html**:
    - Header: Logo actualizado.
    - Footer: Logo actualizado con ruta relativa `../assets`.
3.  **services_overview/services.html**:
    - Header: Logo actualizado.
    - Footer: Logo actualizado con ruta relativa `../assets`.
4.  **project_portfolio_gallery/portfolio.html**:
    - Header: Logo actualizado.
    - Footer: Logo actualizado con ruta relativa `../assets`.
5.  **experience_timeline/our_experience.html**:
    - Header: Logo actualizado.
    - Footer: Logo actualizado con ruta relativa `../assets`.
6.  **faq/contact_faq.html**:
    - Header: Logo actualizado.
    - Footer: Logo actualizado con ruta relativa `../assets`.

## Fase 9: Modernización del Diseño y Servicios

Se implementó una actualización integral del diseño para alinear el sitio con una estética "Eco-Industrial Moderna", priorizando la jerarquía visual y la claridad de la oferta de servicios.

### 1. Tipografía Unificada
- **Estandarización**: Se eliminaron las definiciones hardcoded de `Public Sans` en los archivos HTML individualmente.
- **Jerarquía**: Se estableció un sistema tipográfico consistente gestionado globalmente:
    - **Manrope (`font-sans`)**: Para cuerpo de texto y elementos de UI, aportando modernidad y legibilidad técnica.
    - **Merriweather (`font-serif`)**: Para títulos y encabezados, evocando autoridad y tradición profesional.

### 2. Restructuración de Servicios
Se actualizó la sección de servicios en `home.html` y `services_overview/services.html` para reflejar con precisión las áreas de especialización solicitadas:

- **Nueva Oferta**:
    1.  **Gestión de Residuos** (Icono: `delete_sweep`)
    2.  **Tratamiento de Agua** (Icono: `water_drop`)
    3.  **Consultoría Técnica** (Icono: `engineering`)

- **Rediseño de Tarjetas (UI)**:
    - Implementación de estilo **minimalista/glassmorphism**.
    - Fondos limpios con bordes sutiles que reaccionan al **hover** (cambio a verde primario).
    - Contenedores de iconos flotantes y sombras dinámicas para mayor interactividad.

### 3. Accesibilidad y Contraste
- **Mejora de Legibilidad**: Se oscurecieron los tonos de gris en textos secundarios (`text-gray-600` en lugar de `text-gray-400`/`slate`) para garantizar un radio de contraste adecuado sobre fondos claros.
- **Etiquetas Semánticas**: Se añadieron atributos `aria-label` faltantes en elementos de navegación para mejorar la compatibilidad con lectores de pantalla.

## Fase 10: Estandarización del Menú de Navegación

Se unificó el diseño y funcionalidad del menú de navegación en todas las subpáginas para garantizar una experiencia de usuario consistente y profesional.

### 1. Cabecera Unificada
- **Diseño**: Implementación del header "sticky" con efecto backdrop-blur de `home.html` en todas las secciones (`Nosotros`, `Servicios`, `Portafolio`, `Experiencia`, `Contacto`).
- **Funcionalidad Móvil**: Inclusión del menú hamburguesa y su lógica JavaScript para despliegue en dispositivos móviles, corrigiendo la ausencia de navegación en versiones anteriores.

### 2. Mejoras de Usabilidad y Accesibilidad
- **Estado Activo**: Configuración visual para resaltar la página actual en la barra de navegación.
- **Rutas Relativas**: Corrección de enlaces e imágenes para funcionar desde cualquier subdirectorio.
- **Accesibilidad**: Adición de etiquetas `aria-label="Main navigation"` para cumplimiento de estándares.

### Archivos Modificados
- `about_us/about_us.html`
- `experience_timeline/our_experience.html`
- `faq/contact_faq.html`
- `project_portfolio_gallery/portfolio.html`
- `services_overview/services.html`

## Fase 11: Optimización de la Sección de Estadísticas

Se rediseñó la sección de transparencia (Años de experiencia y Proyectos) en la página de inicio para corregir desbalances visuales y mejorar la experiencia en móviles.

### 1. Reestructuración del Layout
- **Grid Balanceado**: Se migró de un sistema de 3 columnas (con espacios vacíos) a un **Grid de 2 Columnas** centrado, proporcionando simetría perfecta en pantallas grandes.
- **Restricción de Ancho**: Se aplicó `max-w-5xl` para evitar que las tarjetas se estiren excesivamente en monitores anchos.

### 2. Optimización Móvil (Mobile-First)
- **Apilamiento Vertical**: En dispositivos móviles, las tarjetas ahora ocupan el ancho completo y se apilan verticalmente para máxima legibilidad.
- **Escalado Tipográfico**: Ajuste dinámico del tamaño de los números (`text-4xl` en móvil vs `text-5xl` en desktop) para evitar roturas de línea.
- **Áreas Táctiles**: Aumento de padding y márgenes para facilitar la interacción táctil.

### 3. Mejoras Visuales (UI)
- **Glassmorphism Refinado**: Bordes más redondeados (`rounded-2xl`) y sombras profundas con efecto de elevación al pasar el cursor (Hover).
- **Feedback Interactivo**: Los iconos cambian de color (relleno sólido) al interactuar con la tarjeta.

### Archivos Modificados
- `home.html`

## Fase 12: Pestañas Interactivas y Categorización de Servicios

Se implementó un sistema de navegación por pestañas (Tabs) en la página principal de servicios, dotando a la interfaz de mayor dinamismo y permitiendo agrupar la oferta de valor de la compañía en categorías claras sin saturar la pantalla.

### 1. Sistema de Pestañas (Tabs)
- **Navegación Dinámica**: Se transformaron los enlaces estáticos en botones interactivos controlados por JavaScript (`switchTab`).
- **Transiciones Suaves**: Se incorporaron clases de *Tailwind CSS* (`transition-opacity`, `duration-300`, `opacity-0` a `opacity-100`) para lograr un recambio de contenido fluido y estilizado al alternar entre secciones.

### 2. Categorización de Contenido
- **Expansión de Servicios**: Se definieron 4 grandes divisiones estratégicas:
    1. **Ingeniería Ambiental** (Activo por defecto)
    2. **Construcción**
    3. **Topografía**
    4. **Seguridad e Higiene**
- **Nuevas Tarjetas (Cards)**: Se generaron 12 nuevas tarjetas de servicios (3 categorías adicionales) conservando estrictamente el lenguaje de diseño UI original (*Glassmorphism*, *hover effects*, escalas y bordes redondeados).
- **Iconografía Consistente**: Se asignaron íconos específicos de *Material Symbols* para cada nuevo servicio (ej. `house`, `satellite_alt`, `health_and_safety`), garantizando coherencia visual en todo el documento.

### Archivos Modificados
- `services_overview/services.html`

## Fase 13: Auditoría UI/UX y Estandarización de Interfaz

Se enfocó en unificar comportamientos interactivos, mejorar la experiencia de usuario general (navegación y accesibilidad) y avanzar significativamente en el mapeo de internacionalización del sitio.

### 1. Sistema de Filtrado de Portafolio
- **Lógica Refactorizada**: Se actualizó el motor de filtrado en `portfolio.html` empleando atributos nativos (`dataset`) en lugar de funciones anidadas redundantes, reduciendo la complejidad cognitiva y resolviendo alertas de calidad de código (*SonarQube/Clean Code*).
- **UX Consistente**: Transiciones suaves al filtrar las categorías de los proyectos (Infraestructura, Comercial, etc.).

### 2. Navegación Móvil (Animaciones Fluidas)
- **Nuevas Animaciones**: Se rediseñó el menú en dispositivos móviles para abandonar los cambios bruscos de estado (`display: hidden/flex`). Ahora utiliza transformaciones CSS (`opacity-0 scale-y-0` a `opacity-100 scale-y-100`) para lograr un cierre y apertura gradual y elegante.
- **Implementación Global**: Aplicado a todas las páginas clave (`home.html`, `about_us.html`, `services.html`, `portfolio.html`, `our_experience.html`, `contact_faq.html`).
- **Estado Activo (Active State)**: El menú móvil ahora marca visualmente (color verde primario, fondo destacado) sobre qué página se encuentra posicionado el usuario actualmente, mejorando notablemente la orientación espacial.

### 3. Acordeones Modernos (FAQ)
- **Semántica HTML5**: Transformación de divs estáticos y pesados en `contact_faq.html` a etiquetas nativas estructuradas (`<details>` y `<summary>`).
- **Comportamiento Nativo**: Resolución de problemas de espacio vertical, permitiendo al usuario comprimir o expandir preguntas de forma accesible, estándar y controlada por el propio navegador.

### 4. Accesibilidad e Internacionalización Global
- **Lints de Accesibilidad**: Integración de `<fieldset>` y `<legend>` alrededor de grupos de opciones (radio buttons) de contacto. Asociación directa de `<label>` con inputs para asistencia por lectores de pantalla.
- **Estandarización i18n (Textos)**:
  - Adición minuciosa de los atributos `data-i18n` faltantes dentro de los enlaces de menú móviles para todas las secciones.
  - El script administrador de internacionalización (`assets/js/i18n.js`) fue actualizado para resaltar nítidamente la selección de idioma (ES/EN) activo usando `font-bold` y color primario (Verde), mejorando la retroalimentación de estado.

### Archivos Afectados

- `assets/js/i18n.js`
- `home.html`
- `about_us/about_us.html`
- `services_overview/services.html`
- `project_portfolio_gallery/portfolio.html`
- `experience_timeline/our_experience.html`
- `faq/contact_faq.html`

## Fase 14: Optimización Empresarial y Reducción de Fricción UX

Se implementó una serie de características avanzadas enfocadas en posicionar el sitio a nivel corporativo, mejorando la seguridad, interactividad y optimización de carga sin comprometer el framerate.

### 1. Sistema Dinámico de Tema (Dark/Light Mode)
- **Persistencia Inteligente**: Se implementó `theme-toggle.js` con soporte para detectar preferencias del sistema operativo (`prefers-color-scheme`) y guardar la elección manual en `localStorage`.
- **UI Consistente**: Botón de acción con iconos interactivos integrados en Desktop y Mobile, previniendo el Flash of Unstyled Content (FOUC) al ubicarse críticamente en el atributo `<head>`.

### 2. Micro-Interacciones de Scroll (AOS)
- **Animaciones Secuenciales**: Integración fluida de la librería AOS (*Animate On Scroll*) vía CDN.
- **Instrumentación Automatizada**: El script `scroll-animate.js` se encarga de aplicar los atributos `data-aos` a grid containers e identificadores clave sin saturar u obstaculizar la semántica en el HTML estático.

### 3. Fricción Cero en Contacto (Honeypot + Toasts)
- **Reemplazo de Math Captcha**: El antiguo método numérico agresivo se sustituyó por una técnica de **Honeypot**. Un campo oculto invisible al ojo humano engaña a los bots, validando transparentemente a favor de los usuarios reales.
- **Notificaciones Asíncronas**: Eliminación de las alertas arcaicas del navegador (`alert`) reemplazándolas por notificaciones emergentes Toast construidas totalmente sobre el motor de Tailwind en `toast-service.js`.

### 4. Optimizadores de Interfaz y Carga
- **Indicador de Lectura**: Desarrollo e integración de `reading-progress.js`, una fina barra en la parte superior que monitorea dinámicamente el scroll de la página para acompañar lecturas largas (ej. Quiénes Somos y Servicios).
- **Skeleton Loaders Inteligentes**: Las fotografías de alto peso en `portfolio.html` (.webp) ahora muestran contenedores pulsantes al cargar (`animate-pulse`). Las utilidades de `image-loader.js` extraen y finalizan la animación sólo cuando la textura está 100% lista en DOM.
- **Página 404 Responsiva**: Diseño completo de `404.html` para un manejo de errores robusto y coherente con el mapa de i18n y la capa de estilos principal.

### Archivos Nuevos y Modificados

- `assets/js/theme-toggle.js`
- `assets/js/scroll-animate.js`
- `assets/js/toast-service.js`
- `assets/js/reading-progress.js`
- `assets/js/image-loader.js`
- `assets/js/contact_form.js`
- `404.html`
- `assets/i18n/es-MX.json` y `en-US.json`
- Todas las páginas maestras HTML.

## Fase 15: Integración de Deep Linking para Navegación de Pestañas

Se implementó un sistema de ruteo nativo con anclaje (Hash) para conectar las tarjetas visuales de la "Página de Inicio" con el módulo de "Servicios y Pestañas", reduciendo la fricción de búsqueda (Clicks-To-Value).

### 1. Intercepción de Hash en DOMContentLoaded
- **Lectura Automática**: El script principal de `services.html` ahora intercepta la carga de la página, leyendo la métrica `window.location.hash`. Extrae dinámicamente el índice numérico destino usando Regex (`/#tab-(\d+)/`).
- **Scroll Inteligente**: Adicionalmente a desplegar visualmente la pestaña correcta según el ancla, un micro-retraso (`setTimeout`) autodesplaza al usuario suavemente (Smooth Scroll) hacia las tarjetas informativas esquivando el Header fijo.

### Listado de Archivos Modificados

- `home.html`
- `services_overview/services.html`

## Fase 16: Arquitectura y Estandarización de Footers

Se aplicó una reingeniería de interfaz orientada a resolver las inconsistencias visuales del final de página (Footer) implementando una arquitectura dual: Mega Footer para la vista del Home, y Mini Footer para vistas secundarias.

### 1. Estandarización de Diseño Dual
- **Eliminación de Redundancias**: Se retiró el "Mega Footer" (cúmulo de mapas de sitio y texto descriptivo) de `about_us.html` reemplazándolo por el "Mini Footer" moderno (con logo minimalista y 3 enlaces) estandarizándolo en alineación con `services.html`, `our_experience.html` y `contact_faq.html`.
- Se preservaron las texturas de origen para que conservara el tema visual acorde al sistema UI de Tailwind.

### 2. Navegación e Intercepción (Deep Linking y Mapeo JavaScript)
- **Mega Footer de Home**: Los enlaces mudos que apuntaban a `<a href="javascript:void(0)">` en las secciones "Servicios" y "Compañía" se convirtieron en anclas reales. 
  - Ingeniería Ambiental redirige a: `services_overview/services.html#tab-1`
  - Quiénes Somos redirige a: `about_us/about_us.html`
- **Mini Footer (Icono Correo)**: Reconfiguración del ícono "mail" para evitar un cliente de navegador. Pulsarlo re-dirige limpiamente al formulario central: `../faq/contact_faq.html#tab-1`, abriéndolo.
- **Scroll Inteligente (Contact_FAQ)**: Si el usuario ya está posicionado en la página de Contacto/FAQ e intenta dar click al icono de mail al fondo, se inyectó una función en el DOM `onclick="..."` que neutraliza la recarga, hace "click" virtual al tab n.º 1, y ejecuta un "Smooth scroll" nativo devolviendo al usuario al área de escritura sin demora asíncrona.

### Listado de Archivos Modificados

- `home.html`
- `about_us/about_us.html`
- `services_overview/services.html`
- `faq/contact_faq.html`
- `experience_timeline/our_experience.html`
- `traceability_ui_system.md` (Nuevo registro de arquitectura de Footers)

## Fase 17: Rediseño Premium de la Sección "Proyectos Recientes"

Se refactorizó el bloque de portafolio destacado en la página principal para estar en plena sintonía con la nueva identidad de estética de primer nivel, integrando elementos de diseño avanzado.

### 1. Evolución Estética (Glassmorphism)
- **Paneles Translúcidos**: Se reemplazó el tradicional degradado oscuro de fondo por paneles de cristal con la técnica *Glassmorphism* (`backdrop-blur-md`, `bg-white/10`, `border-white/20`).
- **Elevación Compartida**: Se estandarizó el radio de los bordes (`rounded-3xl` / `2rem`) y las sombras de levitación para ser idénticos a las secciones de *Estadísticas* y *Servicios*, dando gran consistencia general.
- **Tipografía Avanzada**: Inclusión inteligente de efectos `drop-shadow-sm` para asegurar absoluta legibilidad del texto en modo claro y oscuro.

### 2. Micro-Interacciones (UX)
- **Call-to-Action Dinámico**: Para estimular el CTR (Click-Through Rate), se agregó una flecha animada y encapsulada que reacciona con un desplazamiento (`translate-x`) y un brillo en tono verde primaria (`shadow-[0_0_15px_rgba...]`) resaltando la zona de manera elegante e indicando explícitamente al usuario que el elemento es clickeable.
- **Transiciones y Overlay**: Implementación de una sutil máscara de opacidad inicial que se desvanece suavemente al posicionarse encima y resalta fuertemente la nitidez del proyecto bajo el cristal interactivo.

### Archivos Modificados e Impactados
- `home.html`
- `markdown/proyectos_recientes_home.md` (Análisis UX previo)

## Fase 18: Refinamiento Global de Menús y Navegación UX

Se ejecutó una revisión integral de los menús (escritorio y móvil), botones de llamado a la acción (CTAs) y utilidades en el footer para mejorar la conversión y evitar redundancias visuales en todo el sitio.

### 1. Refinamiento de Menú (Global)
- **Consistencia de Etiquetado**: Se actualizó el texto "Servicios" a **"Servicios y Cotización"** en todas las páginas (menú principal y menú móvil/flotante) para dejar clara la oferta desde la navegación superior.
- **Limpieza Visual**: Se ocultaron (mediante comentarios) los botones independientes de "Cotizar" tanto en la cabecera como en el menú móvil, previniendo redundancias con la opción anterior.

### 2. Footer y Redirecciones CTA (Global)
- **Copiado al Portapapeles**: Se implementó una funcionalidad dinámica de JavaScript en todos los iconos de "Compartir" (`share`) del mini-footer que, al hacer clic, copia la URL de la página actual al portapapeles y notifica al usuario.
- **Limpieza de Footer**: Se removió el icono de ubicación sobrante en los mini-footers de páginas internas para un acabado más limpio.
- **Optimización de Conversión**: Se recableó el botón central de "Iniciar Consulta" en `about_us.html` hacia `services_overview/services.html` y el CTA de `our_experience.html` directo a `contact_faq.html`, simplificando los flujos del usuario final.

### Archivos Modificados
- `home.html`
- `about_us/about_us.html`
- `services_overview/services.html`
- `experience_timeline/our_experience.html`
- `project_portfolio_gallery/portfolio.html`
- `faq/contact_faq.html`

## Fase 19: Accesibilidad, Rendimiento, Formulario y SEO Avanzado

Se implementó una serie de optimizaciones técnicas vitales para asegurar el cumplimiento con estándares de producción, mejorando tanto el desempeño para los usuarios finales como para los motores de búsqueda.

### 1. Formulario de Contacto Funcional (FormSubmit)
- Se actualizó el formulario de `contact_faq.html` para conectarse con `formsubmit.co` hacia la bandeja oficial `legado.ambiental.mx@gmail.com`.
- Se integró **Validación Avanzada** por JavaScript (Regex para correos y control de longitud mínima).
- Se implementó un **Loader Interactivo y Bloqueo** sobre el botón al momento del envío para prevenir correos duplicados y mejorar la UX de confirmación.

### 2. Accesibilidad (A11y) y Rendimiento
- **Aria-Labels**: Se añadieron etiquetas `aria-label` a los elementos interactivos que contenían solo iconos (botón de menú móvil, toggle de modo oscuro) a través de todas las páginas para una accesibilidad óptima con lectores de pantalla.
- **Micro-Interacción de Carga Global**: Se inyectó un spinner global `<div id="global-loader">` que aparece en lo que procesa el contenido, asegurando que la página se vea pulida sin "parpadeos" del JavaScript.

### 3. SEO Completo (Meta Tags)
- Se inyectaron metaetiquetas estructuradas de **OpenGraph** y **Twitter Cards** para la página raíz (`index.html`) y página de error (`404.html`), asegurando consistencia en la generación de previsualizaciones.

### Archivos Modificados e Impactados
- `assets/js/i18n.js` (Lógica Global de Loader)
- Todos los archivos `.html` (`home.html`, `about_us.html`, `contact_faq.html`, `index.html`, etc.)

## Fase 20: Corrección y Perfeccionamiento de Internacionalización (i18n)

Se solucionaron errores estructurales de sincronización para perfeccionar el cambio instantáneo de idiomas en todo el ecosistema web.

### 1. Refactorización del Generador de Rutas JSON
- **Resolución de Anidamiento**: El script maestro `i18n.js` (`getValueByPath`) fue reprogramado para resolver un bug estructural originado por llaves anidadas. Ahora es capaz de procesar valores anidados duplicados (ej. buscar `auto_generated.text_057` directamente en la raíz de su categoría).
- **Traducción Completada en Inglés**: Todos los fragmentos autogenerados en el archivo maestro de configuración fueron auditados y traducidos correctamente de `es-MX` a `en-US`, reteniendo intactos sus contenedores HTML para un rendering seguro.

### 2. Sanitización HTML (Service Grid)
- Se detectó y eliminó una duplicación de etiquetas `data-i18n` (múltiples llamadas en un solo nodo) en los botones de "Realizar cotización" dentro de `services.html`.
- Se mapeó el atributo de internacionalización (`data-i18n="auto_generated.text_077"`) de manera uniforme a los 15 botones distribuidos en las diferentes pestañas interactivas, asegurando un switch de idiomas impecable.

### Archivos Modificados
- `assets/js/i18n.js`
- `services_overview/services.html`

## Fase 21: Actualización de Contenido y Estandarización de Formato

Se implementaron mejoras en el formato del código fuente y se actualizaron contenidos institucionales y gráficos.

### 1. Limpieza y Estandarización de Código HTML
- **Remoción de Saltos de Línea**: Se eliminaron los saltos de línea innecesarios dentro de los nodos de texto en todos los archivos HTML (`home.html`, `portfolio.html`, `our_experience.html`, `services.html`, etc.). Esto previene renderizados extraños en navegadores y mantiene un DOM más limpio y legible para los desarrolladores.
- **Traducciones UI Móvil**: Se agregaron los atributos faltantes `data-i18n` a los botones del menú móvil (menú hamburguesa) para garantizar su integración completa con el ecosistema de traducción.

### 2. Actualización Institucional y Assets
- **Copyright 2026**: Se actualizó la leyenda legal en el pie de página (footer) de todas las páginas web, transicionando a **"© 2026 Legado Ambiental S.A. de C.V."**.
- **Nuevos Activos Gráficos**: Se cargaron e integraron al repositorio las nuevas creatividades visuales para servicios (`servicios-legado-ambiental-2026` en formato WebP, PNG y fuente XCF).

### Archivos Modificados
- Todas las páginas maestras `.html`.
- Directorio de imágenes de servicios (`assets/images/services/`).

## Fase 22: Actualización de Preguntas Frecuentes, Formularios de Cotización y Revisión de UI Bilingüe

Se realizó una actualización profunda de contenidos dinámicos para incrementar la conversión de clientes y estandarizar la experiencia en ambos idiomas.

### 1. Reingeniería de la Sección FAQ (Preguntas Frecuentes)
- **Contenido de Alto Valor**: Se sustituyeron 3 preguntas de relleno por 6 consultas técnicas reales basadas en las necesidades del cliente final (ej. Validez DC-3, Retorno de inversión en supervisión ambiental, Creación de departamentos SST).
- **Mejora UI/UX en Acordeón**: Se asignaron nuevos iconos de la suite `material-symbols-outlined` (`analytics`, `architecture`, `eco`, `workspace_premium`, `description`, `health_and_safety`) acordes al tema de cada pregunta para facilitar el escaneo visual rápido.
- **Sincronización Bilingüe Estricta**: Las 6 nuevas preguntas fueron dadas de alta en el diccionario `i18n.js` bajo el objeto `contact_page.faq` asegurando la traducción especializada de términos como "OHS" (Seguridad y Salud en el Trabajo) y "DC-3" para la versión `en-US`.

### 2. Optimización de Flujo de Conversión (Leads)
- **Integración de Google Forms**: Los 15 botones de "Realizar cotización" distribuidos en las tarjetas interactivas de `services.html` ahora dirigen a los formularios dinámicos específicos mediante URLs cortas (`https://forms.gle/...`).
- **Comportamiento Seguro**: Se añadió el atributo `target="_blank"` a estos botones para abrir los formularios en pestañas separadas y evitar que el usuario pierda la navegación principal.

### 3. Reparación de Vínculos de Idioma (UI Translations)
- Se corrigió un error crítico de UI en `about_us.html` en la sección "Los Pilares de Nuestra Transformación Ambiental". La etiqueta principal `<h3>` carecía de su atributo traductor, lo que causaba que el texto estuviera quemado en español. Al integrarlo, el texto y su gradiente (gradient text clip) ahora se visualizan perfectamente en inglés ("The Pillars of Our Environmental Transformation").

### Archivos Modificados
- `faq/contact_faq.html`
- `assets/js/i18n.js`
- `services_overview/services.html`
- `about_us/about_us.html`

## Fase 23: Corrección de Dominio SEO y Archivos de Configuración de Servidor

Se solucionaron errores de indexación para motores de búsqueda y se ajustó la configuración del servidor web Hostinger.

### 1. Actualización de Metaetiquetas y Sitemaps
- **Corrección de Dominio Base**: Se reemplazó el dominio erróneo `legadoambiental.com` por el dominio correcto `legadoambiental.com.mx` en todas las referencias de metadatos SEO (OpenGraph, Twitter Cards, JSON-LD), URLs canónicas, enlaces `hreflang`, `robots.txt` y `sitemap.xml`.
- **Prevención de Errores de Rastreo**: Esta actualización crítica evita que Google Search Console se confunda de dominio y rechace la indexación del sitio.

### 2. Configuración de Servidor (Apache/LiteSpeed)
- **Directiva de Directorio**: Se generó el archivo `.htaccess` en la raíz del proyecto instruyendo al servidor (`DirectoryIndex home.html index.html index.php`) que priorice cargar `home.html` por defecto al visitar la raíz del dominio.

### Archivos Modificados e Impactados
- `.htaccess` (Nuevo)
- `robots.txt`
- `sitemap.xml`
- `home.html`
- `about_us/about_us.html`
- `services_overview/services.html`
- `project_portfolio_gallery/portfolio.html`
- `experience_timeline/our_experience.html`
- `faq/contact_faq.html`
- `index.html`
- `markdown/SEO_RECOMMENDATIONS.md`

## Fase 24: Actualización de Enlaces de Formularios de Cotización

Se solucionó un problema de duplicación de enlaces en los botones de "Realizar cotización" dentro de la sección "Ingeniería Ambiental". Anteriormente todos los servicios apuntaban al mismo formulario.

### 1. Corrección de Direccionamiento (Google Forms)
- Se actualizaron las tarjetas (Cards 1 al 4) para redirigir a los clientes potenciales a su respectivo cuestionario técnico de Google Forms.
- Se aseguró que los parámetros query solicitados (ej. `?usp=dialog`, `?usp=header`) estuvieran presentes para una experiencia de usuario óptima y limpia.

### Archivos Modificados
- `services_overview/services.html`

## Fase 25: Prueba de Webhook CI/CD
- Test commit to trigger Hostinger auto-deployment via GitHub Webhooks.

## Fase 26: Consolidación de Punto de Entrada (home.html) y Redirección SEO
Se consolidó `home.html` como el único punto de entrada autorizado, previniendo el contenido duplicado con `index.html`.

### 1. Configuración de Redirección y Fallbacks
- **Redirección de Servidor**: Se añadió una regla `RewriteRule` (301 permanente) en `.htaccess` para redirigir cualquier acceso directo de `/index.html` hacia `/home.html`.
- **Fallback HTML**: Se inyectó la etiqueta `<meta http-equiv="refresh" content="0; url=/home.html">` en `index.html` garantizando una redirección inmediata en cualquier entorno.

### 2. Optimización y Consolidación de Autoridad (SEO)
- **Canonicalización**: Se actualizaron las etiquetas `<link rel="canonical">` e `hreflang` dentro de `index.html` para que apunten a `https://www.legadoambiental.com.mx/home.html`.
- **Actualización de Sitemap**: Se comprobó la remoción de `index.html` del mapa del sitio (`sitemap.xml`) forzando a los motores a indexar la página principal.
- **Documentación**: Se versionó el reporte de auditoría técnica (`prompt-mejoras-recomendaciones.md`).

## Fase 27: Rediseño UI/UX de CTA y Enlace a Documentos Oficiales

Se optimizó la sección CTA (Call to Action) en la página de Experiencia (`our_experience.html`) aplicando principios de UX para evitar "Parálisis de Decisión" (Ley de Hick) y mejorar la conversión.

### 1. Reestructuración Visual (Glassmorphism)
- **Layout Asimétrico:** Se abandonó el diseño centrado con botones del mismo tamaño. Ahora, el CTA primario ("Contactar Ahora") domina el lado izquierdo con un diseño de alto impacto y mayor peso visual.
- **Tarjeta de Descargas:** Las acciones secundarias (Descargar Currículum Empresarial y Portafolio) se agruparon en el lado derecho dentro de una tarjeta translúcida (Glassmorphism).
- **Micro-Interacciones:** Se aplicaron animaciones AOS (Scroll Reveal) secuenciales y efectos sutiles de levitación al interactuar con la tarjeta de cristal.

### 2. Sincronización i18n y Enlace a Recursos
- Se actualizaron las traducciones correctas en `assets/js/i18n.js` bajo `experience_page.cta` (Español e Inglés) usando terminología corporativa.
- Se vincularon los botones de descarga directamente a los documentos PDF oficiales alojados en `assets/docs/`.

### Archivos Modificados
- `experience_timeline/our_experience.html`
- `assets/js/i18n.js`

## Fase 28: Actualización de Currículum Empresarial (HTML y PDF)

Se realizaron ajustes de precisión técnica y gramatical sobre el documento oficial de currículum de la empresa, garantizando que el PDF generado a partir del HTML refleje información histórica fidedigna y redacción estandarizada.

### 1. Correcciones de Contenido (Curricula_Legado_Ambiental_2026.html)
- **Fechas Precisas:** Se reemplazó el marcador temporal indefinido "S/F" (Sin Fecha) por las fechas exactas de ejecución de los proyectos históricos (ej. "Ago 2006", "1999, 2003, 2005, 2006") en los registros de Industrias Sagma y Capacitaciones corporativas (SS, ILADE/PEMEX, ITESM).
- **Estandarización Geográfica:** Se corrigió la abreviatura de "Estado de México" pasando de "Edo. Mex." a la convención formal "Edo. de Méx." en múltiples descripciones de proyectos (Conjunto Urbano Arcángel la Paz, Planta Huehuetoca).

### 2. Generación de Artefacto (PDF)
- Tras la modificación del código fuente HTML, se regeneró el artefacto final `Curricula_Empresarial_Legado_Ambiental_2026.pdf` para heredar las correcciones y mantener sincronizado el recurso descargable del sitio web.

### Archivos Modificados
- `assets/docs/Curricula_Legado_Ambiental_2026.html`
- `assets/docs/Curricula_Empresarial_Legado_Ambiental_2026.pdf`

## Fase 28: Revisión Ortográfica y Gramatical del Currículum (HTML)

Se ejecutó una revisión integral del archivo `Curricula_Legado_Ambiental_2026_v2.html`, aplicando rigurosamente las normas ortográficas y gramaticales de la Real Academia Española (RAE) para purgar vicios corporativos (uso excesivo de mayúsculas).

### 1. Correcciones de Mayúsculas (Capitalización)
- **Sustantivos Comunes y Adjetivos**: Se pasaron a minúscula sustantivos comunes que estaban erróneamente en mayúscula (estilo título de inglés), como "Evaluación", "Corrección", "Planta", "Tratamiento", "Agencias automotrices", etc.
- **Documentos y Listados**: Las descripciones de proyectos (ej. "Diagnóstico técnico", "Proyectos ejecutivos") ahora siguen las reglas del español, donde solo la primera letra lleva mayúscula.
- **Topónimos y Nombres Propios**: Se validó y corrigió el uso de mayúsculas en artículos y preposiciones que forman parte de nombres propios (ej. "La Paz", "Los Reyes", Edificio Pablo "La Llave").

### 2. Prefijos y Palabras Compuestas
- Se unieron prefijos a sus respectivas bases sin utilizar guion, pasando de `hidro-meteorológico` a `hidrometeorológico`.
- Las palabras compuestas (como `físico-químico`) se unificaron eliminando la tilde del primer elemento, quedando como `fisicoquímico` / `fisicoquímica`.

### 3. Ajustes Varios
- Se modificaron conjunciones (`Y` a `y`).
- Se insertaron comas de rigor en denominaciones jurídicas (`Impramex, S.A. de C.V.`).
- Se estandarizó la presentación visual respetando los espaciadores de diseño (`<span>`) y las palabras clave en negrita (`<strong>`).

### Archivos Modificados
- `assets/docs/Curricula_Legado_Ambiental_2026_v2.html`

## Fase 29: Actualización del CTA de Descarga de Portafolio

Se optimizó el botón de "Ver Portafolio" en la sección final de la página "Quiénes Somos" para transformarlo en un enlace de descarga directa del documento oficial, mejorando así la funcionalidad y la retroalimentación visual (UI/UX).

### 1. Refactorización del Botón (Descarga de PDF)
- **Transformación de Etiqueta**: Se reemplazó la etiqueta `<button>` estática por un enlace `<a>` funcional.
- **Enrutamiento y Descarga**: Se vinculó directamente al archivo PDF oficial (`Portafolio_Proyectos_Legado_Ambiental_2026.pdf`). Se añadieron los atributos `target="_blank"` para visualización segura en una nueva pestaña y `download` para forzar la descarga en navegadores compatibles.

### 2. Mejoras de UI e Interactividad
- **Rediseño Visual**: Se actualizó el diseño abandonando el estilo contorno por un botón sólido en color primario (`bg-primary`). Esto mejora el contraste sobre el fondo oscuro y equilibra el peso visual respecto al botón de "Iniciar Consulta".
- **Sombra y Enfoque**: Inclusión de sombras profundas (`shadow-[0_4px_16px_rgba(0,0,0,0.3)]`) y anillos de accesibilidad por teclado (`focus:ring-offset-[#101922]`).
- **Micro-Interacción (Ícono)**: Se agregó el ícono de "download" de la suite Material Symbols con un efecto de desplazamiento vertical en "Hover" (`group-hover:translate-y-1`), brindando al usuario una señal intuitiva e interactiva sobre la acción.

### Archivos Modificados
- `about_us/about_us.html`

## Fase 30: Plan de Mejoras UI/UX 100 Leads - Fase 1 (Infraestructura Mobile-First, Design Tokens y Header Responsivo)

Se ejecutó la Fase 1 del plan de optimización UI/UX y CRO (`plan-mejoras-uiux-100.md`), enfocada en resolver los problemas de responsividad en móviles (320px-375px), estandarizar los Design Tokens globales y garantizar la accesibilidad (WCAG 2.1 AAA) y la integridad de internacionalización (`i18n.js`).

### 1. Refactorización de Cabecera (Header Mobile-First)
- **Eliminación de Overflow Horizontal**: Se ajustó el ancho contenedor a `w-[calc(100%-1rem)] sm:w-[calc(100%-2rem)]` con padding adaptativo `px-3 sm:px-6`, evitando que la cabecera desborde o genere scroll lateral en dispositivos de 320px a 375px.
- **Escalado de Logo y Título**: Se ajustó la altura del logo a `h-10 sm:h-16` en móviles y se aplicó truncado tipográfico (`truncate max-w-[150px] sm:max-w-none`) al texto del título para prevenir colisiones con el menú hamburguesa.
- **Touch Targets de 48px (WCAG 2.1 AAA)**: Se actualizaron las áreas de interacción del botón de menú hamburguesa (`#mobile-menu-btn`), toggles de tema oscuro y selectores de idioma (`ES | EN`) a un tamaño mínimo de **48x48px**.

### 2. Optimización del Menú Móvil Desplegable (#mobile-menu)
- **Posicionamiento Fijo y Scroll Suave**: Se configuró `#mobile-menu` con `position: fixed`, `top-20`, `left-3`, `right-3`, `max-h-[85vh]` y `z-50`, permitiendo un desplazamiento interno independiente sin bloquear el viewport.
- **Controles Integrados de Idioma y Tema**: Se añadieron selectores táctiles destacados de idioma (ES/EN) y tema dentro del propio menú móvil.

### 3. Validación de Cero Regresión e Internacionalización (i18n)
- **Pruebas de Conmutación bilingüe**: Se validó el funcionamiento del diccionario `assets/js/i18n.js` al cambiar entre `es-MX` y `en-US` en todas las páginas del sitio, verificando cero excepciones en consola y paridad de claves traducidas.

### 4. Corrección de Maquetado Responsivo en Línea de Tiempo (`our_experience.html`)
- **Resolución de Solapamiento Móvil**: Se solucionó el fallo visual donde la línea de tiempo vertical (`border-l-2`) quedaba oculta detrás de las tarjetas o desbordada por etiquetas de categoría absolutas (`-left-[9px] top-6`) en pantallas móviles (`< 768px`).
- **Ocultamiento de Etiquetas Absolutas en Móvil**: La div de etiqueta lateral se reconfiguró como `hidden md:block` para escritorio (preservando la columna de 160px a la izquierda de la línea).
- **Inclusión de Insignias de Categoría en Tarjeta Móvil**: En pantallas móviles (`< 768px`), las etiquetas de categoría ("Hidro Meteorológico", "Escuelas", "Saneamiento de Río", "Salud", "Especialidad", "Industria") se presentan mediante insignias/badges responsivas (`md:hidden badge`) integradas limpiamente en el encabezado de cada tarjeta.
- **Puntos Unificados con `z-10` y Relleno Adaptativo**: Se consolidaron los puntos de hito en un único elemento responsivo (`z-10`, `w-4 h-4 md:w-5 md:h-5`) perfectamente centrado sobre la línea continua, y se optimizó el relleno interno de las tarjetas a `p-5 sm:p-8` para evitar apretamiento de contenido en dispositivos de 320px a 390px.

### Escenarios de Prueba Ejecutados (QA & No Afectación)
1. **Verificación Visual Mobile (320px, 360px, 390px, 414px)**: Inspección de visibilidad continua de la línea vertical y puntos de color en `our_experience.html`, confirmando cero desbordamiento horizontal y lectura nítida de títulos e insignias.
2. **Prueba de Menú Hambuerguesa & Sticky Header**: Apertura/cierre en 6 páginas principales en vistas móviles, comprobando touch targets de 48px y z-index 50.
3. **Verificación i18n Bilingüe**: Alternancia fluida `ES` <-> `EN` en la línea de tiempo y menú sin pérdida de claves ni desestructuración de tarjetas.

### Archivos Modificados
- `home.html`
- `about_us/about_us.html`
- `services_overview/services.html`
- `project_portfolio_gallery/portfolio.html`
- `experience_timeline/our_experience.html`
- `faq/contact_faq.html`
- `README.md`

## Fase 31: Plan de Mejoras UI/UX 100 Leads - Fase 2 (Hero Section JTBD, Trust Banner & 3 CTAs)

Se ejecutó la Fase 2 del plan técnico de optimización UI/UX y CRO (`plan-mejoras-uiux-100.md`), reestructurando la sección principal de la página de inicio (`home.html`) hacia una propuesta de valor basada en Jobs-To-Be-Done (JTBD), incorporando 3 llamados a la acción (CTAs) de alta conversión y un banner de confianza normativa (Trust Banner).

### 1. Rediseño del Hero Section Orientado a JTBD (`home.html`)
- **Titular y Copys Directos**: Se reemplazó el titular estático por preguntas directas de necesidad de negocio: *"¿Necesitas resolver un estudio de impacto ambiental, proyecto de obra o levantamiento topográfico?"*.
- **Padding Adaptativo y Eliminación de Altura Fija**: Se eliminó la restricción `min-h-[450px]` en móvil y se implementó `min-h-auto py-8 md:py-14` con padding elástico `p-5 sm:p-8 md:p-12`.

### 2. Integración de 3 llamados a la Acción (CTAs)
- **Botón Primario ("Cotizar Proyecto")**: Redirección directa al formulario de contacto (`faq/contact_faq.html#tab-1`) con estilo verde `primary` de alto contraste.
- **Botón Secundario ("Hablar por WhatsApp")**: Enlace directo a la API de WhatsApp Business (`https://wa.me/527226727212`) con mensaje inicial prellenado sobre cotizaciones.
- **Botón Terciario ("Ver Portafolio PDF")**: Enlace de descarga directa del documento `Portafolio_Proyectos_Legado_Ambiental_2026.pdf` con atributos `target="_blank"` y `download`.

### 3. Hero Trust Banner (Barra de Confianza Normativa)
- **Franja Normativa Integrada**: Se incorporó un banner estilizado `backdrop-blur-md` en la base del Hero destacando normativas y licencias clave:
  - `NOM-052-SEMARNAT` (Residuos Peligrosos)
  - `NOM-001-SEMARNAT` (Aguas Residuales)
  - `Normativas STPS` (Seguridad e Higiene)
  - `RCDF y Licencias` (Construcción Urbana)

### 4. Garantía de Internacionalización (`assets/js/i18n.js`)
- Registradas las llaves `hero.jtbd_title`, `hero.jtbd_subtitle`, `hero.quote_btn`, `hero.whatsapp_btn`, `hero.portfolio_btn`, `hero.trust_label`, `hero.norm_1`, `hero.norm_2`, `hero.norm_3`, `hero.norm_4` en los diccionarios `es-MX` y `en-US`.

### Escenarios de Prueba Ejecutados (QA & No Afectación)
1. **Verificación Visual Fluid (320px a 1440px)**: Confirmada la fluidez del contenedor Glassmorphism y apilamiento limpio de los 3 CTAs en pantallas pequeñas.
2. **Descarga de Portafolio PDF & Enlace WhatsApp**: Probada la apertura de WhatsApp con mensaje inicial y descarga directa del archivo PDF sin errores 404.
3. **Verificación i18n Bilingüe**: Alternancia `ES` <-> `EN` en el Hero y Trust Banner comprobando paridad completa de traducción.

### Archivos Modificados
- `home.html`
- `assets/js/i18n.js`
- `README.md`
- `plan-mejoras-uiux-100.md`

## Fase 32: Plan de Mejoras UI/UX 100 Leads - Fase 3 (Pestañas de Servicios Adaptativas y Aislamiento de Layout PDF)

Se ejecutó la Fase 3 del plan técnico de optimización UI/UX y CRO (`plan-mejoras-uiux-100.md`), convirtiendo la barra de pestañas de servicios en una interfaz táctil adaptativa para móviles e aislando la arquitectura de impresión PDF Carta (`8.5in x 11in`).

### 1. Navegación por Pestañas Adaptativa (`services.html`)
- **Selector Móvil (< 640px)**: Se implementó un elemento Select UI de alta visibilidad (`#services-mobile-select`) con borde interactivo verde `primary` y chevron `unfold_more`. Esto elimina el desbordamiento ciego en pantallas pequeñas y permite a los usuarios de teléfonos inteligentes seleccionar cualquiera de las 4 divisiones (*Ingeniería Ambiental*, *Construcción*, *Topografía*, *Seguridad e Higiene*) con un solo toque.
- **Pestañas Desktop (>= 640px)**: Se conservaron las pestañas horizontales con indicador de estado activo (`bg-primary`, sombra verde y texto blanco).
- **Sincronización Bidireccional en JS**: Se sincronizó la función `switchTab(tabIndex)` para actualizar simultáneamente la pestaña activa en desktop, la opción seleccionada en el dropdown móvil y el panel de tarjetas de servicio activo.

### 2. Aislamiento de la Arquitectura PDF vs Pantalla Web (`Curricula_Legado_Ambiental_2026_v2.html`)
- **Visualización Web Responsiva (`@media screen`)**: Se actualizó la clase `.page-container` a `width: 100%; max-width: 8.5in; min-height: auto;`, garantizando que en dispositivos móviles y monitores de escritorio el documento sea 100% fluido y no genere desbordamientos laterales ni barras de desplazamiento forzadas.
- **Formato Carta Estricto en Impresión (`@media print`)**: Se encapsularon las reglas fijas `width: 8.5in; height: 11in; page-break-after: always;` dentro del bloque `@media print`, asegurando que al exportar a PDF o imprimir (Ctrl+P / Cmd+P) se mantenga la maquetación en tamaño Carta exacto sin elementos interactivos (`.no-print { display: none !important; }`).

### Escenarios de Prueba Ejecutados (QA & No Afectación)
1. **Verificación de Pestañas Adaptativas (320px a 1200px)**: Comprobado el funcionamiento del selector táctil en pantallas de 320px, 375px y 414px, así como el cambio de pestañas en escritorio.
2. **Prueba Deep Linking por Hash**: Verificado que al acceder a `services.html#tab-3` se active automáticamente la pestaña de *Topografía* y se sincronice con el selector móvil.
3. **Prueba de Impresión PDF `@media print`**: Validada la vista previa de impresión en `Curricula_Legado_Ambiental_2026_v2.html`, confirmando páginas Carta exactas y ocultamiento de botones interactivos.
4. **Verificación i18n Bilingüe**: Alternancia `ES` <-> `EN` en la página de servicios y etiquetas del selector móvil sin errores.

### Archivos Modificados
- `services_overview/services.html`
- `assets/docs/Curricula_Legado_Ambiental_2026_v2.html`
- `assets/js/i18n.js`
- `README.md`
## Fase 33: Plan de Mejoras UI/UX 100 Leads - Fase 4 (Formulario Simplificado de 6 Campos, Honeypot & Sticky Mobile CTA Bar)

Se ejecutó la Fase 4 del plan técnico de optimización UI/UX y CRO (`plan-mejoras-uiux-100.md`), simplificando el formulario de contacto para eliminar la fricción de conversión e implementando la barra persistente de llamadas a la acción (Sticky Mobile CTA Bar) en todo el sitio web.

### 1. Formulario de Contacto Ultra-Simplificado (6 Campos) (`faq/contact_faq.html`)
- **Reducción a 6 Campos Clave**: Se rediseñó el formulario a 6 campos esenciales para la calificación de prospectos B2B: *Nombre*, *Empresa*, *Correo Electrónico*, *Teléfono*, *Servicio de Interés* y *Mensaje / Detalles del Proyecto*.
- **Integración Anti-Spam Invisible (Honeypot)**: Implementación de un campo trampero no visible (`website_hp`) para atrapar bots automatizados sin afectar la usabilidad del usuario humano.
- **Envío Asíncrono AJAX & Toast Notifications**: Envío de datos vía `fetch()` a FormSubmit integrado con `ToastService` (`assets/js/toast-service.js`) para desplegar notificaciones flotantes de éxito o error al instante.

### 2. Sticky Mobile CTA Bar en Todo el Sitio (6 Páginas)
- **Barra Fija en Pantallas Móviles (< 768px)**: Se añadió el componente flotante `fixed bottom-0 left-0 right-0 z-40 md:hidden bg-white/95 dark:bg-[#121c27]/95 backdrop-blur-lg` con dos botones de contacto de respuesta inmediata:
  - **Botón WhatsApp Directo**: Enlace a la API de WhatsApp (`+52 55 8367 1036`).
  - **Botón Cotizar**: Redirección rápida al formulario de cotización.
- **Resguardo de Contenido (`pb-20 md:pb-0`)**: Aplicado a los tags `<body>` en las 6 páginas principales para evitar que la barra flotante cubra información relevante del pie de página.

### 3. Garantía de Internacionalización (`assets/js/i18n.js`)
- Actualizadas las claves de traducción `contact_page.form.*` en los diccionarios `es-MX` y `en-US` garantizando cero textos duros en la interfaz de contacto.

### Escenarios de Prueba Ejecutados (QA & No Afectación)
1. **Verificación de Envío de Formulario AJAX**: Probado el envío en `contact_faq.html` validando el despliegue del mensaje Toast de confirmación y limpieza del formulario.
2. **Prueba de Sticky Mobile CTA Bar**: Comprobada la visibilidad e interactividad de los botones en pantallas móviles (320px, 375px, 414px) y su ocultamiento automático en pantallas de escritorio (`md:hidden`).
3. **Validación Anti-Spam Honeypot**: Confirmado que envíos con el campo oculto completo son descartados silenciosamente sin distorsionar la experiencia.
4. **Verificación i18n Bilingüe**: Alternancia `ES` <-> `EN` en los formularios y la barra CTA verificando 100% de cobertura de llaves.

### Archivos Modificados
- `faq/contact_faq.html`
- `home.html`
- `about_us/about_us.html`
- `services_overview/services.html`
- `project_portfolio_gallery/portfolio.html`
- `experience_timeline/our_experience.html`
- `assets/js/i18n.js`
- `README.md`
## Fase 34: Plan de Mejoras UI/UX 100 Leads - Fase 5 (Analítica GA4/GTM, SEO Local & Validación Final de Cero Regresión)

Se ejecutó la Fase 5 del plan técnico de optimización UI/UX y CRO (`plan-mejoras-uiux-100.md`), concluyendo de forma integral el plan de captación de 100 leads con la instrumentación de eventos de analítica automatizada, optimización de metadatos de SEO Local y la auditoría final de cero regresión.

### 1. Instrumentación de Analítica Automatizada (`assets/js/analytics.js`)
- **Script Unificado de Eventos (`analytics.js`)**: Creado para capturar y enviar eventos clave a la capa de datos (`dataLayer` para GA4 y Google Tag Manager):
  - `click_whatsapp`: Registra clics en cualquier botón o enlace de WhatsApp con atribución del origen (*header*, *hero*, *sticky_fab_mobile*, *footer*).
  - `generate_lead`: Registra conversiones exitosas del formulario de contacto simplificado con la categoría de servicio seleccionada.
  - `download_portfolio`: Registra la descarga o visualización del portafolio PDF y currículum empresarial.
- **Inclusión en Todo el Sitio**: Inyectado en las 6 páginas principales HTML.

### 2. SEO Local & Datos Estructurados (Schema.org)
- **Schema.org Enriquecido**: Actualizado en los `<head>` de todas las páginas principales (`home.html`, `about_us.html`, `services.html`, `portfolio.html`, `our_experience.html`, `contact_faq.html`) con los tipos combinados `["ConstructionBusiness", "EnvironmentalConsultancy"]`, teléfono verificado `+52-55-8367-1036` y dirección de Ecatepec, Estado de México.
- **Redirección `.htaccess`**: Confirmada la regla de redirección 301 limpia de `index.html` hacia `home.html`.

### 3. Auditoría Final de Internacionalización & Cero Regresión
- **Paridad i18n 1:1**: Verificada la paridad completa entre los diccionarios `es-MX` y `en-US` en `assets/js/i18n.js` mediante script automatizado de Node.js.
- **Patrón Híbrido B2B CTA Móvil**: Confirmado el funcionamiento del botón 100% ancho "Cotizar Proyecto" en la barra fija base y el botón circular flotante (FAB) de WhatsApp.

### Escenarios de Prueba Ejecutados (QA & No Afectación)
1. **Verificación `dataLayer.push` en Consola**: Probada la emisión de eventos al hacer clic en WhatsApp, enviar formularios y descargar portafolio PDF.
2. **Prueba Cross-Browser & Multidispositivo**: Comprobada la maquetación en resoluciones de 320px, 375px, 768px, 1024px y 1440px sin distorsión visual.
3. **Auditoría Estructurada Schema.org**: Validada la estructura JSON-LD sin advertencias ni errores sintácticos.
4. **Auditoría Final i18n**: Conmutación bilingüe sin textos quemados ni excepciones en consola.

### Archivos Modificados
- `assets/js/analytics.js` (Nuevo)
- `assets/js/contact_form.js`
- `home.html`
- `about_us/about_us.html`
- `services_overview/services.html`
- `project_portfolio_gallery/portfolio.html`
- `experience_timeline/our_experience.html`
- `faq/contact_faq.html`
- `README.md`
- `plan-mejoras-uiux-100.md`

## Fase 35: Optimización de Previsualización Social (Open Graph / LinkedIn) y Depuración Integral de Activos Multimedia

Esta fase aborda la corrección de los metadatos de compartición en redes sociales (Open Graph / Twitter Cards) para la URL pública del dominio, la optimización de los activos visuales y la limpieza exhaustiva de archivos no utilizados en el proyecto.

### 1. Diagnóstico y Corrección de Metadatos Open Graph (`home.html` e `index.html`)
- **Problema Detectado**: Al ingresar la URL del sitio web (`https://legadoambiental.com.mx/`) en LinkedIn ("Añadir contenido multimedia") u otras plataformas sociales, se mostraba una vista previa con una fotografía de edificios en construcción ajena a la identidad institucional, proveniente de una URL provisional externa de Google Photos (`lh3.googleusercontent.com/aida-public/...`).
- **Solución Implementada**:
  - Se actualizaron las etiquetas `og:image` y `twitter:image` en `home.html` e `index.html` para apuntar a la imagen oficial corporativa de *Metodología Estructurada de Proyectos Integrales*.
  - Se añadieron directivas completas de Open Graph para evitar retrasos en el cálculo asíncrono de dimensiones por parte de los crawlers sociales:
    - `og:image:secure_url`: URL HTTPS absoluta.
    - `og:image:type`: Declaración de tipo MIME (`image/png`).
    - `og:image:width`: `1200` píxeles.
    - `og:image:height`: `876` píxeles.
    - `og:image:alt`: Texto descriptivo de accesibilidad.

### 2. Generación y Optimización de Imagen Social (`servicios-legado-ambiental-2026-og.png`)
- **Optimización de Peso y Dimensiones**:
  - El activo original en alta resolución (`servicios-legado-ambiental-2026.png`) tenía una resolución de 2412x1760 px y un peso de **6.30 MB**, superando el límite máximo estricto de **5 MB** de LinkedIn.
  - Se procesó una versión web-optimizada en `assets/images/services/servicios-legado-ambiental-2026-og.png`:
    - **Resolución**: 1200 x 876 px (proporción óptima para que ninguna columna de la metodología ni los textos se recorten en feeds o tarjetas).
    - **Peso final**: **1.33 MB** (~78% de reducción respecto al original y ampliamente por debajo del umbral de 5 MB de LinkedIn).
    - **Calidad**: Formato PNG de 24 bits con compresión nivel 9, conservando el 100% de la fidelidad visual, colores y nitidez.

### 3. Auditoría e Inventario de Activos Multimedia (`assets/images/`)
Se auditó la totalidad de archivos en `assets/images/` y se contrastó contra todas las referencias en código HTML, JS, CSS y configuraciones:
- **Total de archivos iniciales**: 49 archivos (150 MB).
- **Archivos activos en producción**: 18 archivos esenciales (6.05 MB).
- **Archivos huérfanos / no utilizados**: 31 archivos (146.20 MB).

### 4. Respaldo de Archivos Editables de Diseño GIMP (`design_sources/`)
Para garantizar la preservación de los recursos de edición sin sobrecargar la distribución web en producción:
- Se creó el directorio de respaldo `design_sources/` en la raíz del repositorio.
- Se trasladaron los 8 archivos de proyecto editables con capas (`.xcf`, **86.62 MB**):
  - `design_sources/about/about-legado-comp-2026.xcf`
  - `design_sources/about/about_us_resume.xcf`
  - `design_sources/about/mision-legado-2026.xcf`
  - `design_sources/about/vision-legado-2026.xcf`
  - `design_sources/home/proyecto_1_legado_2026.xcf`
  - `design_sources/home/proyecto_2_legado_2026.xcf`
  - `design_sources/services/metodologia.xcf`
  - `design_sources/services/servicios-legado-ambiental-2026.xcf`
- Se agregó documentación interna en `design_sources/README.md`.

### 5. Depuración y Reducción del Directorio Web (`assets/images/`)
- Se eliminaron del directorio público `assets/images/` los 31 archivos huérfanos:
  - 8 archivos `.xcf` respaldados en `design_sources/`.
  - 12 archivos `.png` pesados o versiones preliminares reemplazadas por formatos modernos WebP.
  - 11 archivos `.webp` de maquetación temprana no implementados en las plantillas HTML finales.
- **Resultado**: La carpeta `assets/images/` pasó de **150 MB a solo 6.05 MB** (reducción del 96% de carga en el despliegue del hosting).

### 6. Restauración y Distribución del Menú Superior Flotante (Paridad 1:1 con Hostinger)
- **Problema Detectado en Entorno Local**: En la versión en desarrollo, el título de la marca se cortaba a *"LEGADO AMBIENT..."* y los enlaces de navegación ("Quiénes Somos", "Servicios y Cotización") se distorsionaban o rompían en múltiples líneas debido a clases restrictivas (`truncate`, `max-w-[150px]`, `overflow-hidden` y dimensiones excesivas en botones de tema/idioma) añadidas en commits anteriores.
- **Ajuste Aplicado**:
  - Se sincronizó el diseño y estructura exacta del componente `<header>` con la versión estable y funcional desplegada en producción en Hostinger (`menu-superior-pro.png`).
  - Se eliminó el truncamiento y `overflow-hidden` del bloque de marca, permitiendo que "LEGADO AMBIENTAL" luzca completo en mayúsculas negritas con `text-xl` y `shrink-0`.
  - Se añadió la regla `whitespace-nowrap` en todos los enlaces de escritorio y textos del menú para asegurar que ningún elemento se divida en dos líneas.
  - Se restableció la altura (`h-20`) y espaciados originales (`px-4 sm:px-6 lg:px-8`, `gap-8`) que proporcionan una distribución equilibrada y estética en las 6 páginas web.
  - Se mantuvo la funcionalidad responsiva para móviles (menú desplegable de pantalla completa y botón hamburguesa interactivo).

### 7. Actualización del Número Oficial de WhatsApp Business
- **Ajuste Realizado**: Se sustituyó el número de contacto en todos los botones y enlaces interactivos hacia la API de WhatsApp (`wa.me`) por el nuevo número: **`72 2672 7212`** (formato internacional México: `527226727212`).
- **Puntos de Enlace Actualizados**:
  - Botón secundario del Hero en [`home.html`](home.html).
  - Botones flotantes circulares (Floating Action Button - FAB) presentes en las 6 páginas principales (`home.html`, `about_us.html`, `services.html`, `portfolio.html`, `our_experience.html` y `contact_faq.html`).
- **Enlace Unificado**:
  `https://wa.me/527226727212?text=Hola,%20quisiera%20cotizar%20un%20proyecto%20con%20Legado%20Ambiental`

### 8. Actualización del Teléfono Fijo Principal
- **Ajuste Realizado**: Se sustituyó el número telefónico anterior (`55 7312 6918`) por el nuevo número: **`55 8367 1036`** (formato internacional: `+52 55 8367 1036`, Schema.org: `+52-55-8367-1036`).
- **Puntos de Actualización**:
  - Datos estructurados Schema.org JSON-LD en todas las páginas HTML (`home.html`, `about_us.html`, `services.html`, `portfolio.html`, `our_experience.html`, `faq/contact_faq.html`).
  - Pie de página (Footer) en `home.html` y diccionarios de internacionalización `assets/js/i18n.js` (`es-MX` y `en-US`).
  - Tarjeta de contacto directo y placeholders del formulario en `faq/contact_faq.html`.

### Escenarios de Prueba Ejecutados (QA & No Afectación)
1. **Auditoría de Enlaces Rotos**: Validación automatizada de las 34 referencias a imágenes en todas las páginas del sitio (`home.html`, `index.html`, `about_us.html`, `services.html`, `portfolio.html`, `our_experience.html`, `contact_faq.html`, `404.html` y currícula), reportando **0 enlaces rotos** y 100% de recursos resueltos.
2. **Validación de Metadatos Open Graph**: Comprobada la sintaxis y URLs absolutas en `index.html` y `home.html` con parámetros compatibles para LinkedIn Post Inspector y Facebook Sharing Debugger.
3. **Verificación de Respaldo**: Confirmada la integridad de los 8 archivos `.xcf` en `design_sources/`.
4. **Verificación de Menú Superior en las 6 Páginas**: Validación de paridad visual y estructural con la versión de Hostinger en `home.html`, `about_us.html`, `services.html`, `portfolio.html`, `our_experience.html` y `contact_faq.html`, confirmando cero truncamiento y diseño responsivo intacto.
5. **Verificación de Enlaces WhatsApp**: Validación de los 7 botones de WhatsApp confirmando que todos apuntan correctamente a `https://wa.me/527226727212` con el mensaje inicial de cotización predefinido.
6. **Verificación Telefónica Global**: Confirmadas las 21 coincidencias actualizadas al número `55 8367 1036` sin números obsoletos en código fuente.

### Archivos Modificados / Creados
- `home.html` (Modificado - metadatos `og:image`, menú superior Hostinger, botones WhatsApp y teléfono actualizado)
- `index.html` (Modificado - metadatos `og:image` actualizados)
- `about_us/about_us.html` (Modificado - menú superior Hostinger, botón WhatsApp y teléfono Schema.org actualizado)
- `services_overview/services.html` (Modificado - menú superior Hostinger, botón WhatsApp y teléfono Schema.org actualizado)
- `project_portfolio_gallery/portfolio.html` (Modificado - menú superior Hostinger, botón WhatsApp y teléfono Schema.org actualizado)
- `experience_timeline/our_experience.html` (Modificado - menú superior Hostinger, botón WhatsApp y teléfono Schema.org actualizado)
- `faq/contact_faq.html` (Modificado - menú superior Hostinger, botón WhatsApp y teléfonos actualizados)
- `assets/js/i18n.js` (Modificado - diccionarios de teléfono actualizados para ES y EN)
- `assets/images/services/servicios-legado-ambiental-2026-og.png` (Nuevo - versión optimizada de 1.33 MB)
- `design_sources/` (Nuevo directorio de respaldo de archivos `.xcf`)
- `design_sources/README.md` (Nuevo - documentación de fuentes de diseño)
- `README.md` (Modificado - documentación de la Fase 35)

---

## 📈 Registro de Cambios: Fase 36 - Infraestructura Web y Soporte Técnico para Google Business Profile (Pilar 5) y Google Ads Local (Pilar 6)

### 1. Contexto y Objetivos
Complementando el *Plan Estratégico de Trabajo y Arquitectura UI/UX* (Pilar 5: Búsqueda Local / SEO Local y Pilar 6: Adquisición de Pago / Google Ads Local), se implementó la infraestructura de código, analítica y metadatos necesaria para la captación activa de clientes en el Valle de México y la trazabilidad de campañas publicitarias.

### 2. Manual y Guía Estratégica Completa
Se creó la guía técnica y comercial integral en [`markdown/guia-google-business-profile-y-ads-local.md`](markdown/guia-google-business-profile-y-ads-local.md), que detalla:
- **Google Business Profile:** Proceso de verificación en México, estandarización NAP 1:1, selección de categorías (`Consultor ambiental`, `Ingeniero consultor`, `Empresa constructora`, `Agrimensor`), delimitación de áreas de servicio (Estado de México, CDMX y nacional), catálogo de servicios B2B, estrategia de fotografías con EPP y protocolo para recolección y respuesta de reseñas en Google.
- **Google Ads Local:** Vinculación de cuentas con GBP para recursos de ubicación, arquitectura de 4 grupos de anuncios por intención transaccional (Impacto Ambiental, Topografía, Saneamiento/PTAR, Seguridad STPS), matriz de palabras clave con concordancia de frase y exacta, lista exhaustiva de palabras clave negativas, modelos de anuncios responsivos (RSAs), extensiones obligatorias y estrategia de puja de aprendizaje a conversión.

### 3. Adecuaciones Técnicas en el Sitio Web
1. **Atribución de Marketing y Captura de Google Ads Click ID (`assets/js/analytics.js`):**
   - Captura automática de `gclid`, `wbraid`, `gbraid`, `utm_source`, `utm_medium` y `utm_campaign` desde la URL al aterrizar en el sitio, persistidos en `sessionStorage`.
   - Exposición de la función utilitaria global `window.getMarketingAttribution()`.
   - Disparo de eventos enriquecidos con la procedencia de la campaña (`campaign_source`, `campaign_name`, `gclid`).
   - Auto-instrumentación global para clics en enlaces de llamada telefónica (`click_phone`), reseñas de Google (`click_google_review`) y mapas (`click_google_maps`).
   - Función puente `window.trackGoogleAdsConversion()` para enviar conversiones directas a la etiqueta de Google Ads (`gtag`).
2. **Formulario de Cotización con Trazabilidad Publicitaria (`faq/contact_faq.html`):**
   - El script de envío por AJAX ahora recupera los datos de campaña y adjunta `origen_campana` y `google_click_id` en el cuerpo del correo enviado a `formsubmit.co`, permitiendo al equipo de ventas identificar clientes de Google Ads.
3. **Tarjeta Interactiva de Reseñas de Google Business Profile (`faq/contact_faq.html`):**
   - Inserción de una tarjeta visual con insignia de verificación y 5 estrellas, invitando a directores de obra y empresas a dejar reseñas en Google.
   - Botón directo *"Escribir Reseña en Google"* (`data-action="google-review"`) y *"Ver en Google Maps"* (`data-action="google-maps"`).
4. **Teléfonos y Direcciones Clicables (`home.html` y `faq/contact_faq.html`):**
   - Conversión de números telefónicos en enlaces táctiles interactivos `tel:+525583671036` y `tel:+527226727212`.
   - Enlace directo a la ubicación en Google Maps en el footer y módulo de contacto.
   - Enlaces rápidos a *Google Maps* y *Reseñas en Google* en la barra inferior del footer.
5. **Enriquecimiento del Schema.org JSON-LD LocalBusiness (6 Páginas):**
   - Actualización del marcado estructurado en `home.html`, `about_us.html`, `services.html`, `portfolio.html`, `our_experience.html` y `contact_faq.html` incorporando `@type: ["LocalBusiness", "ConstructionBusiness", "EnvironmentalConsultancy"]`, geolocalización GPS (`geo`: `19.6018, -99.0494`), horarios comerciales (`openingHoursSpecification`), cobertura geográfica (`areaServed`) y múltiples puntos de atención técnica y comercial.
6. **Internacionalización y Cero Errores (Regla de Oro `assets/js/i18n.js`):**
   - Registro de todas las nuevas llaves textuales en español (`es-MX`) e inglés (`en-US`).

---

## 🚀 Registro de Cambios: Fase 37 - Culminación de Google Business Profile, Integración GTM/GA4 y Dictamen Ejecutivo de Proyecto

### 1. Contexto y Logros
Se alcanzó la culminación de los pilares técnicos y de presencia local establecidos en el plan de trabajo para la captación de los **Primeros 100 Leads B2B**:
- **Google Business Profile (Pilar 5: SEO Local Concluido):** Ficha formalmente verificada por Google con panel de control en vivo (199+ interacciones), 11 fotografías de servicios profesionales remasterizadas a alta definición (1200x896 px, proporción 4:3), material audiovisual de Modelado 3D y cálculo volumétrico de tierras (carátula HD y video demo de 20 segundos), y suite completa de códigos QR vectoriales/rasterizados con credencial de mostrador (`tarjeta-qr-legadoambiental.html`).
- **Medición y Analítica Digital (GA4 y GTM):** Implementación de la etiqueta de Google Tag Manager y Google Analytics (`G-1MLGHB4E6G`) en las 8 páginas del ecosistema web, adecuación de directivas CSP en cabeceras HTML y rastreo de eventos del embudo de conversión en `assets/js/analytics.js` (`form_start`, `select_service_interest`, `generate_lead`, `click_whatsapp`, `click_phone`, `scroll_depth`).
- **Dictamen Financiero sobre Google Ads (Pilar 6):** Elaboración del análisis técnico y financiero formal sobre el cupón de $7,000 MXN (`DOC-LA-MKT-2026-004`). Se determinó por resolución corporativa suspender temporalmente la pauta pagada para cuidar el flujo de efectivo (ahorro inmediato de $8,120 MXN netos con IVA) y canalizar los esfuerzos inmediatos a la captación orgánica y prospección directa B2B.

### 2. Entregables Documentales y Reportes Ejecutivos
- **Informe de Estado del Proyecto (Markdown & PDF):**  
  - [`INFORME_ESTADO_PLAN_TRABAJO_OCT_2026.md`](INFORME_ESTADO_PLAN_TRABAJO_OCT_2026.md)  
  - [`assets/docs/Informe_Ejecutivo_Plan_Trabajo_y_Avances_2026.pdf`](assets/docs/Informe_Ejecutivo_Plan_Trabajo_y_Avances_2026.pdf)
- **Dictamen Técnico del Crédito Publicitario Google Ads:**  
  - [`assets/docs/Dictamen_Credito_Google_Ads_7000_MXN.pdf`](assets/docs/Dictamen_Credito_Google_Ads_7000_MXN.pdf)

---

## 🎯 Registro de Cambios: Fase 38 - PB5: Micro-Landings de Servicios Específicos & Conversión On-Site (Módulos 1, 2 y 3)

### 1. Módulo 1: Arquitectura de Navegación, Router JS y Deep-Linking Semántico
- **Identificadores Amigables (Slugs Semánticos):**
  - `#ambiental`: División 1 - Consultoría e Ingeniería Ambiental.
  - `#construccion`: División 2 - Construcción y Supervisión de Obra.
  - `#topografia`: División 3 - Topografía de Alta Precisión & Geodesia.
  - `#seguridad-hidraulica`: División 4 - Infraestructura Hidráulica, Saneamiento & STPS.
- **Sincronización Bidireccional y Limpieza de Historial:**
  - Uso de `history.replaceState` para mantener URLs limpias y legibles en la barra de direcciones sin saltos ni recargas.
  - Sincronización en vivo entre pestañas de escritorio (`.tab-btn`), menú desplegable móvil (`#services-mobile-select`) y el hash de la URL.
- **Navegación Guiada y Telemetría:**
  - Escucha de eventos `DOMContentLoaded` y `hashchange` con desplazamiento suave (*smooth scroll*) con compensación de cabecera fija.
  - Telemetría de analítica web en cada cambio de división disparando `dataLayer.push({ event: 'select_service_tab', ... })`.
- **Actualización de Enlaces Entrantes:**
  - Reescritura de los enlaces de las 4 tarjetas y del pie de página en `home.html` y diccionarios de `assets/js/i18n.js` hacia los nuevos slugs semánticos, manteniendo retrocompatibilidad intacta para `#tab-1..4`.

### 2. Módulo 2: Cabeceras UI/UX de Autoridad Técnica (Micro-Landing Headers)
- **Cabeceras Especializadas por División en `services.html`:**
  - Inserción de 4 tarjetas destacadas de ancho completo (`col-span-1 md:col-span-2`) al inicio de cada tab técnico con diseño en gradientes temáticos oscuros, bordes estilizados y efectos de iluminación (*glow*).
  - Propuesta de valor B2B dirigida a resolver dolores específicos: blindaje ante multas/clausuras PROFEPA/SEMARNAT, control de calidad y bitácora con Director Responsable de Obra (DRO), levantamientos con GPS RTK y drones LiDAR en 24-48h, y plantas de tratamiento PTAR con dictámenes STPS.
- **Badges de Autoridad Técnica & CTAs Duales:**
  - Inclusión de 3 insignias con iconografía técnica por cabecera (`SEMARNAT/PROFEPA`, `CRETI`, `DRO`, `GPS RTK`, `PTAR`, `Protección Civil`).
  - Botones de acción directa hacia cotización on-site (`contact_faq.html?service=[slug]`) y asesoría técnica directa por WhatsApp.
- **Paridad Total de Internacionalización (28 Nuevas Claves i18n):**
  - Registro y validación estricta de 28 claves bajo `services_page.headers.*` en `assets/js/i18n.js` para los idiomas `es-MX` y `en-US`.

### 3. Módulo 3: Enriquecimiento de Fichas de Servicio y Conversión On-Site (Eliminación de Fugas Externas)
- **Eliminación Total de Enlaces Externos a Google Forms:**
  - Sustitución del 100% de los botones con enlaces externos (`forms.gle` / `docs.google.com/forms`) en las 15 fichas de servicio por componentes nativos de conversión dual on-site, evitando la pérdida de tráfico cualificado y garantizando el seguimiento en GA4/GTM.
- **Acciones Duales de Alta Conversión B2B por Ficha:**
  - **Botón Primario On-Site:** Acceso a `../faq/contact_faq.html?service=[slug_especifico]` para captura formal de requerimientos en el sitio.
  - **Botón Secundario Inmediato:** Acceso directo a WhatsApp (`wa.me/525583671036`) con texto precargado según la especialidad consultada.
- **Enrutamiento y Auto-Selección Inteligente en `faq/contact_faq.html`:**
  - Captura del parámetro de consulta `?service=` vía `URLSearchParams`.
  - Mapeo semántico exhaustivo de los 15 servicios hacia el selector `<select id="service_type">` con fallback predictivo.
  - Activación automática del formulario (`switchTab(1)`) y desplazamiento guiado y suave (*smooth scroll*) con compensación de cabecera hacia `#contact-form`.
- **Enriquecimiento de Entregables Oficiales y Paridad Bilingüe:**
  - Especificación de entregables técnicos tangibles en tarjetas representativas (planos ejecutivos AutoCAD DWG/PDF 24-48h, memorias de cálculo PTAR y NOM-001/002/003, respaldo de firma DRO con bitácora oficial, y diagnósticos STPS con carpetas NOM-019).
  - Paridad estricta en `assets/js/i18n.js` (`es-MX` y `en-US`) bajo `services_page.cards.*` para todos los textos y entregables.











