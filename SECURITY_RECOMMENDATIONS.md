# Análisis y Recomendaciones de Seguridad

## Resumen Ejecutivo
El sitio web es estático, lo que elimina muchas vulnerabilidades del lado del servidor (SQL Injection, RCE). Sin embargo, existen riesgos de seguridad del lado del cliente (Client-Side) y mejores prácticas que no se están siguiendo.

### Nivel de Riesgo Global: MODERADO
El uso de scripts vía CDN (Tailwind Play CDN) es la vulnerabilidad más crítica para un entorno de producción.

---

## 1. Análisis del Sitio (Global)

### A. Dependencia de CDN Inseguro (Crítico)
**Hallazgo:** El sitio carga TailwindCSS mediante un script de Play CDN (`cdn.tailwindcss.com`).
> `<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>`
**Riesgo:**
1.  **Ejecución de Código Arbitrario:** Si el CDN es comprometido, un atacante puede inyectar JavaScript malicioso en su sitio.
2.  **Rendimiento:** Este script compila CSS en el navegador, causando lentitud en dispositivos móviles.
3.  **Avisos de Consola:** Tailwind advierte que este script *no* debe usarse en producción.
**Recomendación:** Reemplazar el script CDN por un archivo CSS estático compilado durante el desarrollo.

### B. Cabeceras de Seguridad (Faltantes)
**Hallazgo:** No se detectan metaetiquetas para políticas de seguridad.
**Riesgo:** Mayor superficie de ataque para XSS y Clickjacking.
**Recomendación:** Implementar las siguientes cabeceras vía servidor o Meta Tags:
*   `Content-Security-Policy` (CSP)
*   `X-Content-Type-Options: nosniff`
*   `Referrer-Policy: strict-origin-when-cross-origin`

### C. Manejo de DOM en i18n.js (Advertencia)
**Hallazgo:** El sistema de traducción usa `element.innerHTML = text`.
**Riesgo:** Si bien los archivos de traducción son locales y confiables hoy, el uso de `innerHTML` es un vector clásico de XSS (Cross-Site Scripting) si en el futuro se cargan traducciones desde una API externa o input de usuario.
**Recomendación:**
1.  Sanitizar el HTML antes de insertarlo (usando librerías como DOMPurify).
2.  Usar `textContent` para claves que no requieran formato HTML (la mayoría).

---

## 2. Análisis del Formulario de Contacto (`contact_faq.html`)

El formulario actual es puramente visual (sin `action` definida), pero debe protegerse como si fuera funcional.

### A. Ausencia de Validación de Entrada (Importante)
**Hallazgo:** Los campos `input` y `textarea` carecen de atributos de restricción.
**Riesgos:**
1.  **Denegación de Servicio (DoS) en Navegador:** Un usuario puede pegar 1GB de texto en el mensaje, colapsando el navegador.
2.  **Datos Basura:** Envío de formularios vacíos o mal formados.
**Recomendación:** Añadir atributos HTML5 nativos.
*   `required`: Para campos obligatorios.
*   `maxlength="N"`: Limitar longitud (ej. 100 caracteres para nombre, 500 para mensaje).
*   `pattern`: Para validación básica de teléfonos.

### B. Prevención de Bots (Spam)
**Hallazgo:** No hay CAPTCHA ni campos ocultos (Honeypot).
**Riesgo/Molestia:** Recepción masiva de spam automatizado.
**Recomendación:** Implementar un "Honeypot" (campo oculto CSS que si se llena, descarta el envío) o hCaptcha.

---

## 3. Lista de Acciones Inmediatas (Plan de Corrección)

A continuación, la lista de cambios técnicos a aplicar en esta iteración para mitigar los riesgos detectados sin requerir infraestructura compleja.

### [ ] Hardening del Formulario (`contact_faq.html`)
- [ ] Agregar atributo `required` a: Nombre, Apellidos, Email/Teléfono, Mensaje.
- [ ] Agregar `maxlength="50"` a Nombre/Apellidos.
- [ ] Agregar `maxlength="100"` a Email.
- [ ] Agregar `maxlength="15"` a Teléfono y `pattern="[0-9+ ]*"`.
- [ ] Agregar `maxlength="500"` a Mensaje.

### [ ] Metaetiquetas de Seguridad (`contact_faq.html` y Globales)
- [ ] Agregar `X-Content-Type-Options`.
- [ ] Agregar CSP básico (permitiendo el CDN actual por ahora, pero restringiendo otros orígenes).

Nota: El reemplazo del CDN de Tailwind es una tarea de infraestructura (Build Step) que podría requerir Node.js instalado en el entorno de despliegue, por lo que se marca como recomendación a futuro, pero se mitigará con CSP.
