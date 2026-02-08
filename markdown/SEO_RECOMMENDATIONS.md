# Recomendaciones de SEO para Legado Ambiental

Basado en el análisis de la estructura actual del sitio web, aquí presentamos una estrategia integral para mejorar la visibilidad en motores de búsqueda (Google, Bing).

## 1. SEO Técnico (Prioridad Alta)

### 1.1. Implementación de `sitemap.xml`
Crear un archivo `sitemap.xml` en la raíz del sitio que liste todas las páginas accesibles. Esto ayuda a los rastreadores a indexar el contenido más rápido.
```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>https://www.legadoambiental.com/home.html</loc>
      <lastmod>2026-01-25</lastmod>
      <changefreq>monthly</changefreq>
      <priority>1.0</priority>
   </url>
   <!-- Repetir para todas las páginas internas -->
</urlset>
```

### 1.2. Archivo `robots.txt`
Configurar `robots.txt` para guiar a los bots.
```txt
User-agent: *
Allow: /
Sitemap: https://www.legadoambiental.com/sitemap.xml
```

### 1.3. Etiquetas `hreflang` para Internacionalización
Dado que el sitio soporta Español e Inglés, es crucial indicar esto a Google para servir la versión correcta según la ubicación del usuario.
Añadir en el `<head>` de cada página:
```html
<link rel="alternate" hreflang="es" href="https://www.legadoambiental.com/home.html" />
<link rel="alternate" hreflang="en" href="https://www.legadoambiental.com/en/home.html" />
<link rel="alternate" hreflang="x-default" href="https://www.legadoambiental.com/home.html" />
```
*Nota: Esto requiere que las URLs cambien dinámicamente o usar parámetros de consulta si no se separan por carpetas.*

### 1.4. URLs Canónicas
Para evitar problemas de contenido duplicado (especialmente si se accede con/sin `www` o `index.html`), añadir:
```html
<link rel="canonical" href="https://www.legadoambiental.com/home.html" />
```

## 2. SEO On-Page (Contenido)

### 2.1. Optimización de Imágenes
*   **Texto Alternativo (`alt`)**: Actualmente muchas imágenes son `background-image` CSS. Los motores de búsqueda no "ven" estas imágenes como contenido indexable.
    *   *Recomendación*: Para imágenes críticas (como proyectos del portafolio), usar etiquetas `<img>` reales con atributos `alt` descriptivos y palabras clave (ej. `alt="Edificio sustentable con certificación LEED en Ciudad de México"`).
*   **Formatos**: Servir imágenes en formato **WebP** para reducir tiempos de carga.

### 2.2. Datos Estructurados (Schema.org)
Implementar JSON-LD para ayudar a Google a entender que esto es una "Organización" o "Negocio Local".
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ConstructionBusiness",
  "name": "Legado Ambiental",
  "url": "https://www.legadoambiental.com",
  "logo": "https://www.legadoambiental.com/assets/logo.png",
  "description": "Excelencia en construcción civil y desarrollo sostenible.",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Plaza de Ingeniería, Suite 400",
    "addressLocality": "Ciudad de México",
    "addressRegion": "CDMX",
    "postalCode": "12345",
    "addressCountry": "MX"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-555-123-4567",
    "contactType": "customer service"
  }
}
</script>
```

### 2.3. Jerarquía de Encabezados (H1-H6)
*   Ya se está haciendo un buen uso de `<h1>` (uno por página).
*   Asegurar que las palabras clave principales ("Ingeniería Civil", "Construcción Sostenible", "Infraestructura") aparezcan en los `<h2>` y `<h3>` de manera natural.

## 3. Performance y Core Web Vitals

### 3.1. Eliminar Script de CDN de Tailwind
Actualmente se usa `<script src="https://cdn.tailwindcss.com...`. Esto es excelente para desarrollo pero **malo para producción** (carga lenta, renderizado bloqueante).
*   *Recomendación*: Compilar el CSS de Tailwind en un archivo estático (`styles.css`) minificado y enlazarlo con `<link rel="stylesheet">`.

### 3.2. Carga Diferida (Lazy Loading)
Para imágenes debajo del "fold" (fuera de la vista inicial), añadir `loading="lazy"` a las etiquetas `<img>`.

## 4. Estrategia de Contenidos (Blog)
Crear una sección de "Blog" o "Noticias" actualizable. Google premia el contenido fresco.
*   Ideas de artículos: "Beneficios de la certificación LEED", "Tendencias en infraestructura urbana 2026", "Cómo gestionamos residuos de obra".
