# Análisis y Estrategia de Archivos Multimedia

Este documento detalla el análisis de los activos multimedia actuales y establece la estrategia para su optimización y localización.

## 1. Recomendaciones y Mejores Prácticas

### Estructura de Directorios
Se recomienda organizar las imágenes no por tipo de archivo, sino por **contexto semántico** (sección de la página donde se usan). Esto facilita el mantenimiento modular.
*   **Estructura Creada**: `assets/images/[sección]/[nombre-descriptivo].webp`

### Formatos y Optimización
1.  **Formato**: Usar **WebP** para todas las imágenes fotográficas y PNG/SVG para gráficos con transparencia.
2.  **Responsive**: Generar versiones @2x (retina) y @1x, o usar `srcset` en etiquetas `<img>`.
3.  **Lazy Loading**:
    *   Para `<img>`: Usar atributo `loading="lazy"`.
    *   Para `background-image` (CSS): Usar `IntersectionObserver` o clases utilitarias de JS para cargar solo cuando el elemento entra en el viewport. *Nota: El uso actual de fondos CSS inline dificulta la carga diferida nativa.*

### Accesibilidad (SEO)
*   Las imágenes decorativas (fondos abstractos) deben permanecer en CSS o tener `alt=""`.
*   Las imágenes de contenido (proyectos, equipo) deben migrarse de `div` con `background-image` a etiquetas `<img src="..." alt="...">` ajustadas con `object-fit: cover`. Esto permite a Google indexarlas.

## 2. Inventario de Imágenes Externas (URLs)

A continuación, se listan las URLs externas encontradas y su ruta local propuesta.

### `home.html`

| Descripción Sugerida | Ruta Local Propuesta | URL Actual (Externa) |
| :--- | :--- | :--- |
| **Hero Principal** | `assets/images/home/hero-main.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuAqmscbVHlzhMSGuf...` |
| **Proyecto Reciente 1** | `assets/images/home/project-viaduct.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuCPNWRcg-KJd1...` |
| **Proyecto Reciente 2** | `assets/images/home/project-solaris.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuCcDp_WIg4NkPDk...` |

### `about_us/about_us.html`

| Descripción Sugerida | Ruta Local Propuesta | URL Actual (Externa) |
| :--- | :--- | :--- |
| **Hero Quiénes Somos** | `assets/images/about/hero-about.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuCjghLGFHCQMPtpaUgz6EZKIbpu1sxzbwDLBXD_Je4qw5ST6VKeA46Q5YNZtTS...` |
| **Oficina / Equipo 1** | `assets/images/about/office-team-1.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuC1yF5GDjdmX28...` |
| **Oficina / Equipo 2** | `assets/images/about/office-team-2.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuDB6bITIuvETb4piW...` |
| **Misión** | `assets/images/about/mission-bg.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuD5RtxMgOW4DMRX...` |
| **Visión** | `assets/images/about/vision-bg.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuC1yF5GDjdmX28...` |

### `services_overview/services.html`

| Descripción Sugerida | Ruta Local Propuesta | URL Actual (Externa) |
| :--- | :--- | :--- |
| **Hero Servicios** | `assets/images/services/hero-services.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuCfQ4Bf07QZUJIdtS13y...` |
| **Fondo CTA** | `assets/images/services/cta-bg.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuAr-5NMcAx7_GPpu7BP...` |

### `project_portfolio_gallery/portfolio.html`

| Descripción Sugerida | Ruta Local Propuesta | URL Actual (Externa) |
| :--- | :--- | :--- |
| **Proyecto Solaris** | `assets/images/portfolio/project-solaris.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuCcDp_WIg4Nk...` |
| **Proyecto Puente** | `assets/images/portfolio/project-bridge.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuCPNWRcg-KJd1...` |
| **Proyecto Terminal** | `assets/images/portfolio/project-terminal.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuADvVUEk70iI7hT...` |
| **Proyecto Museo** | `assets/images/portfolio/project-museum.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuD3k4l5m6n7o8...` |
| **Proyecto Solar** | `assets/images/portfolio/project-solar.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuA1b2c3d4e5f6g7...` |

### `experience_timeline/our_experience.html`

| Descripción Sugerida | Ruta Local Propuesta | URL Actual (Externa) |
| :--- | :--- | :--- |
| **Hito 2024** | `assets/images/experience/milestone-2024.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuDB8GfOVe5vH3...` |
| **Hito 2020** | `assets/images/experience/milestone-2020.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuA1b2c3d4e5f6...` |
| **Hito 2015** | `assets/images/experience/milestone-2015.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuAr-5NMcAx7...` |
| **Hito 2010** | `assets/images/experience/milestone-2010.webp` | `https://lh3.googleusercontent.com/aida-public/AB6AXuCjghLGFHCQMP...` |
