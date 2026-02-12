# Legado Ambiental - Refactorización del Sitio Web

Este documento detalla los ajustes y mejoras realizados al proyecto `website-legado` para asegurar su optimización, responsividad y localización para el mercado latinoamericano.

## Resumen de Ajustes Realizados

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
