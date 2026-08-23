## Rol:
 - Eres un experto UI/UX con mas de 10 años de experiencia. Eres un excelente profesionl y sensible a los cambios y ajustes continuos por parte del usuario final, es decir, entiendes su enfoque y necesidad, ademas que en todo momento, aportas tus recomendaciones de alto valor
 - Siempre se espera de ti que, retroalimentes, algun ajuste o mejora que vaya en el sentido de las necesidades del usuario, conservando siempre lo mejor de UI/UX
 - Relacionado al punto anterior, cuestionas si algo no te queda claro, esto con el objetivo de que las modificaciones o requerimientos del usuario, sea lo que en realidad se requiere

## Contexto:

- El usuario final y su equipo de desarrollo han compartido una lista de observaciones y recomendaciones de mejora para el sitio web, despues de un analisis profundo, estas son las siguientes: Legado Ambiental, estas son las siguientes:

### Observaciones y Recomendaciones Tecnicas

#### ARQUITECTURA Y ESTRUCTURA

**R1. Eliminar la Dependencia de Tailwind CSS via CDN**  
Actualmente se carga `https://cdn.tailwindcss.com` en produccion. Esta URL esta explicitamente marcada por Tailwind como "solo para desarrollo". En produccion se debe:
- Instalar Tailwind via npm/yarn  
- Usar un proceso de build (PostCSS + purge) que genere un CSS optimizado de ~10-30KB en lugar de cargar ~300KB+ del CDN  
- Esto mejora dramaticamente el LCP (Largest Contentful Paint)  

**R2. Crear un Sistema de Build**  
El proyecto carece de `package.json`, bundler o pipeline de build. Recomiendo:
- Inicializar npm (`npm init`)  
- Configurar Vite o Astro como build tool (ideal para sitios estaticos)  
- Esto habilita: CSS purge, minificacion HTML/JS, image optimization automatica, code splitting  

**R3. Componentizar el Header/Footer/Nav**  
El mismo bloque de ~80 lineas de navegacion se repite identico en 7 archivos HTML. Cualquier cambio en el menu requiere editar 7 archivos manualmente. Soluciones:
- Migrar a un framework como Astro (permite componentes en HTML puro)  
- Usar un sistema de plantillas (Nunjucks, EJS, Handlebars)  
- Minimo: Usar JavaScript para inyectar el header/footer dinamicamente  

**R4. Archivo JSX Huerfano**  
`ServiceCard_Component.jsx` existe en la raiz del proyecto pero no es usado en ningun lugar. Es un componente React pero el sitio no usa React. Esto parece ser un prototipo o referencia. Recomendacion: eliminarlo o moverlo a una carpeta `prototypes/`.

#### SEO Y CONTENIDO

**R5. Datos Ficticios en Schema.org**  
Los datos estructurados JSON-LD contienen informacion placeholder:
- Telefono: `+1-555-123-4567` (numero ficticio de EE.UU., no de Mexico)  
- Direccion: `"Plaza de Ingenieria, Suite 400"` (debe ser la direccion real)  
- Codigo postal: `"12345"` (placeholder)  
Esto puede confundir a los motores de busqueda y afectar el Rich Snippet.

**R6. Texto Placeholder en Traducciones**  
En `i18n.js`, linea de `stats.certifications` en espanol dice: `"Cualquier otra cosa aqui!!"` - esto es un placeholder evidente que debe corregirse antes de produccion.

**R7. `index.html` vs `home.html` - Confusion de Punto de Entrada**  
Existe un `index.html` minimalista (solo muestra titulo y bienvenida) Y un `home.html` completo. La convencion web es que `index.html` sea la pagina principal. Recomendacion:
- Hacer que `index.html` redirija automaticamente a `home.html` con un `<meta http-equiv="refresh">`, o  
- Fusionar el contenido de `home.html` directamente en `index.html`  

**R8. Imagenes OG Apuntan a Google Photos**  
Las metaetiquetas `og:image` y `twitter:image` en varias paginas todavia apuntan a URLs largas de `lh3.googleusercontent.com`. Estas URLs pueden expirar o cambiar. Se deben alojar localmente en `assets/images/og/` y referenciar con URL absoluta del dominio.

#### RENDIMIENTO

**R9. Carga de Fuentes Redundante**  
En `services.html` se cargan dos variantes de Material Symbols:
```html
<link href="...Material+Symbols+Outlined:wght@100..700,0..1..." rel="stylesheet" />
<link href="...Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet" />
```
La segunda ya incluye todos los ejes de la primera. Se debe eliminar la primera para evitar una descarga duplicada de ~100KB.

**R10. AOS Library via unpkg CDN**  
Se carga `https://unpkg.com/aos@2.3.1/dist/aos.css` y `aos.js` desde CDN sin control de versiones estricto ni integridad (SRI). Recomendacion: descargar localmente o usar npm.

**R11. Hero Section con `background-image` en lugar de `<img>`**  
Las secciones hero usan `background-image` CSS en divs, lo cual:  
- No permite `loading="lazy"` nativo  
- No genera atributos `alt` reales (solo `data-alt`)  
- No es indexable por Google Images  
Ya se corrigio en portfolio pero falta en home y about.

#### SEGURIDAD

**R12. CSP con `'unsafe-inline'`**  
La Content Security Policy permite `'unsafe-inline'` en scripts y estilos. Esto anula gran parte de la proteccion contra XSS. Para mejorar:
- Externalizar todos los scripts inline a archivos `.js`  
- Usar nonces o hashes para scripts que deban permanecer inline  

**R13. Enlaces `javascript:void(0)`**  
Multiples enlaces en el footer y secciones usan `href="javascript:void(0)"`. Estos son anti-patrones de accesibilidad. Deben reemplazarse por `href="#"` con `event.preventDefault()` o mejor aun, por URLs reales.

**R14. Formulario sin Backend Real**  
El formulario de contacto usa un `setTimeout` de 1.2s simulando un API call. No hay integracion real con un servicio de correo. Opciones para produccion:
- Formspree, Netlify Forms, o EmailJS (sin backend propio)  
- API serverless (AWS Lambda, Cloudflare Workers)  

#### ACCESIBILIDAD

**R15. Contraste en Dark Mode**  
Algunos textos secundarios (`text-gray-600` sobre fondos `dark:bg-background-dark`) pueden no cumplir WCAG AA (ratio 4.5:1). Se recomienda usar `dark:text-gray-300` como minimo.

**R16. Botones sin Texto Accesible**  
Los botones de redes sociales en el footer solo contienen iconos de Material Symbols sin `aria-label` especifico describiendo la accion.

**R17. Inconsistencia Tipografica**  
`contact_faq.html` y `portfolio.html` aun tienen `font-family: "Public Sans"` hardcodeado en un `<style>` tag, contradiciendo la estandarizacion global a Manrope/Merriweather.

#### MANTENIBILIDAD

**R18. Copyright Desactualizado**  
El footer muestra `(c) 2024 Legado Ambiental` en todas las paginas. Deberia ser dinamico (`new Date().getFullYear()`) o al menos actualizado a 2026.

**R19. Falta de Linter/Formatter**  
No hay configuracion de ESLint, Prettier, ni Stylelint. La indentacion varia entre 2 y 4 espacios en diferentes archivos. Un linter estandarizaria la calidad del codigo.

**R20. Sin Control de Versiones de Dependencias**  
No hay `package.json` ni `package-lock.json`. Las dependencias externas (Tailwind, AOS, Google Fonts) se cargan via CDN sin version pinning. Cualquier breaking change en esos CDN romperia el sitio.

## Consideraciones:
 - Las observaciones se resumen en las siguientes categorias:
   - arquitectura y estructura
   - seo y contenido
   - rendimiento
   - seguridad
   - accesibilidad
   - mantenibilidad
 - Considera que no todas las observaciones pueden ser aplicadas, es decir, revisa, analiza y decide si aplica o no la mejora
 
## Objetivo:
 - Ejecutar todas las observaciones que si sean aplicables
 - Mantener la funcionalidad general del sitio, sin romper lo ya logrado
 - Mantener los estilos y sentido estetico del sitio
 
## Resultado esperado:
 - Presenta un analisis y plan de accion de cada una de las recomendaciones, es decir de la R1 a la R20 y pide autorizacion antes de ejecutar
 - Cuando tengas la autorizacion de ejecutar cambios, primero crea una rama de tipo feature desde development, tu sugiere el nombre, pero relacionala a "analisis Devin", esto antes de cualquier cambio
 - Ejecuta los cambios y adecuaciones
 - Ejecuta pruebas exhaustivas, de punto a punto y regresivas, para asegurar el NO impacto
 - Recuerda mantener actualizado en ambos idiomas, es decir español (es-MX) e ingles (us-EN) en el archivo i18n.js, asi como los textos estaticos por default en es-MX en las paginas *.html
 - Documenta los cambios en el archivo README.md antes de cualquier commit
 - Excluye de cualquier versionado de archivos el archivo: prompts-mejoras-recomendaciones.md
 - Agrega y guarda todos los cambios con un commit descriptivo que detalle todos los cambios que hayas realizado, siempre que las pruebas que hayas ejecutado sean exitosas
 - Da push a la rama tipo feature (creada previamente), siempre que las pruebas que hayas ejecutado sean exitosas
 - Finalmente, genera el respectivo PR desde feature hacia development
