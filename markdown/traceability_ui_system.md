# Trazabilidad y Arquitectura del Sistema de Footers 

## 1. Patrón Dual de Footers
Se determinó implementar dos estándares de navegación de cierre en `Legado Ambiental` con objetivos distintos pero unificados estéticamente mediante variables comunes y el uso de la identidad Glassmorphic.

- **Mega Footer (`home.html`)**: Exclusivo para el aterrizaje principal debido a que es el primer contacto SEO e interaccional. Reúne a detalle las ubicaciones corporativas, correos, y el Sitemap desglosado mediante links a las sub-pantallas del negocio.
- **Mini Footer (Páginas Secundarias)**: Ocupa apenas un tercio del Mega Footer. Implementado en `about_us.html`, `services.html`, `our_experience.html` y `contact_faq.html`. Concede espacio visual limpio y presenta exclusivamente botones rápidos (`share`, `mail`, `location_on`) para no agobiar visualmente interacciones directas con su vista principal.

## 2. Redirecciones con Anclaje (Deep Links)
Para las secciones de `home.html` donde el cliente explora servicios pre-concebidos, se redirige inteligentemente al archivo base abriendo de facto el panel en Javascript.
- Enlaces de la sección Servicios en Home apuntan a `services_overview/services.html#tab-[N]`.
- Al recibir el parámetro `#tab-[N]`, el script del sitio extrae el ancla, dispara el método `switchTab(tabId)` instantáneamente e ignora la pantalla por defecto, creando una sensación de navegación interna muy inmersiva.

## 3. Ítem Click-To-Mail Mejorado (`#tab-1`)
Dado que el correo en texto sin procesar puede generar rebotes u obligar al cliente a abrir un cliente ajeno, hemos redirigido todas las representaciones del "Pellízco al icono de Mensaje" hacia la zona estandarizada de Contacto donde captará el nombre, apellido e intención del visitante.
- Si el usuario se halla fuera de la vista general, el enlace relativo es: `../faq/contact_faq.html#tab-1`.
- Si el usuario *ya* habita dentro de `contact_faq.html`, la inyección nativa del `#tab-1` ejecuta un _smooth scroll_ para mover la ventana hacia la zona útil, activando automáticamente la pestaña de "Envíanos un Mensaje" en lugar del submenú ajeno.

## 4. Evitando Deuda Técnica (Integridad i18n Mantenida)
Toda modificación o inmersión de texto ha mantenido vigente el patrón estricto de utilizar `data-i18n` o bien, ser excluido donde el elemento DOM requiere reaccionar independientemente a transiciones HTML o variables de entorno. 
