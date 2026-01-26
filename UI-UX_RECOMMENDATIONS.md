# Recomendaciones Expertas de UI/UX para Legado Ambiental

Basado en el análisis de la identidad visual proporcionada (Logo, Infografía de Identidad Estratégica) y el código actual del sitio, he elaborado la siguiente guía de optimización para alinear el sitio web con la visión de "Certeza Técnica y Desarrollo Sustentable".

## 1. Análisis de Identidad Visual vs. Implementación Actual

| Componente | Identidad de Marca (Imágenes) | Implementación Actual (`home.html`) | Diagnóstico |
| :--- | :--- | :--- | :--- |
| **Paleta de Colores** | Dominio de **Verde Naturaleza** (hojas, maíz), **Tierra/Marrón** (nido, tierra), **Azul Marino** (agua, texto corporativo). | **Azul Eléctrico** (`#137fec`) como primario, Gris Oscuro/Navy como fondo. | **Desalineado.** El azul actual es demasiado "tecnológico/software". La marca pide tonos más orgánicos y corporativos (construcción + eco). |
| **Tipografía** | Fuentes Sans Serif sólidas, geométricas, con peso en los títulos (parecido a Montserrat o Gotham). | "Public Sans" (Google Fonts). | **Aceptable**, pero se puede reforzar la jerarquía usando una fuente con más "carácter" para los títulos "Legado". |
| **Estilo Visual** | Ilustraciones limpias, líneas técnicas (planos), fotografía realista. | Diseño limpio, uso de sombras (`shadow-xl`), bordes redondeados (`rounded-xl`). | **Bueno**, el estilo moderno funciona, pero faltan elementos que evoquen los "planos técnicos" de la identidad. |

---

## 2. Recomendaciones de Diseño y Estilo (Look & Feel)

### A. Refinamiento de la Paleta de Colores
Para proyectar **Sostenibilidad** y **Ingeniería**, sugerimos migrar de la paleta "Azul Tech" a una "Paleta Eco-Industrial".

*   **Color Primario (Acción/Marca):** Cambiar `#137fec` (Azul Brillante) a **`#2E7D32` (Verde Bosque Institucional)** o **`#00695C` (Verde Azulado Profundo)**. Esto conecta directamente con el "Maíz/Hojas" del logo.
*   **Color Secundario (Soporte/Fondos):** Mantener el `#101922` (Navy Oscuro) para modos oscuros y pies de página, ya que transmite solidez y "Certeza Técnica".
*   **Color de Acento (Detalles):** Un tono **Tierra/Dorado** (`#BCAAA4` o `#D7CCC8`) para detalles sutiles, evocando la tierra del logo, o un **Azul Acero** para connotar metal/construcción.

**Acción Sugerida:** Actualizar `tailwind.config` con estos nuevos tokens de color.

### B. Tipografía y Jerarquía
*   **Títulos (Headings):** Cambiar a una fuente con más presencia estructural.
    *   *Opción 1 (Moderna/Técnica):* **"Manrope"** o **"Inter"** (excelente legibilidad numérica para datos técnicos).
    *   *Opción 2 (Legado/Tradición):* **"Merriweather"** o **"Lora"** (Serif) solo para títulos grandes (H1, H2), transmitiendo la idea de "Legado" y "Trayectoria".
*   **Cuerpo (Body):** "Public Sans" es buena, pero asegúrate de tener suficiente contraste (gris `#374151` en lugar de negros puros o grises muy claros).

### C. Elementos Gráficos
*   **Texturas de Fondo:** Incorporar sutiles patrones de **grilla (grid)** o **líneas topográficas** en secciones con fondo blanco (`bg-background-light`). Esto refuerza el concepto de "Rigor Geométrico" y "Topografía" mencionado en la infografía.
*   **Iconografía:** Los iconos actuales (`material-symbols`) son funcionales. Se recomienda usarlos en estilo "Outlined" con un grosor de trazo fino (light/thin) para imitar el dibujo técnico.

---

## 3. Experiencia de Usuario (UX) y Navegabilidad

### A. Navegación y Estructura
1.  **Sticky Header (Ya implementado):** Excelente decisión. Sugiero añadir una ligera reducción de altura al hacer scroll para dar más espacio al contenido visible en laptops.
2.  **Menú Móvil:** Asegurar que el botón de menú tenga un área de toque (tap target) de al menos 44x44px.
3.  **Breadcrumbs (Migas de Pan):** En páginas internas (`faq/contact_faq.html`, `about_us/...`), agregar una línea de rastro (Inicio > FAQ > Contacto) para mejorar la orientación del usuario.

### B. Formularios (Optimización realizada)
1.  **Feedback Visual:** La implementación de bordes rojos y mensajes de error es crucial. 
    *   *Mejora:* Añadir iconos de "check" verde dentro del input cuando el campo es válido (refuerzo positivo).
2.  **Agrupación Lógica:** La decisión de poner Nombre/Apellido juntos y Contacto/Email en ancho completo es correcta para la escaneabilidad.

### C. Responsividad (Mobile-First)
1.  **Espaciado (Padding):** En móviles, reducir los paddings verticales de las secciones (`py-24` a `py-16`) para evitar áreas vacías excesivas que obliguen a mucho scroll.
2.  **Tamaño de Fuente:** Ajustar los H1 en móvil. Actualmente `text-5xl` puede ser muy grande y romper palabras. Usar `text-4xl` o `text-3xl` en viewports pequeños (`< 640px`).
3.  **Tablas/Grillas de Datos:** Si se presentan tablas de especificaciones técnicas (común en ingeniería), asegurar que tengan scroll horizontal (`overflow-x-auto`) en móviles.

---

## 4. Plan de Ejecución Inmediata

Si el usuario aprueba estas recomendaciones, los pasos técnicos serían:

1.  **Fase 1 (Estilo):** Reconfigurar `tailwind.config` con la nueva paleta (Verde/Tierra).
2.  **Fase 2 (Atmósfera):** Añadir un archivo CSS global con un patrón de fondo SVG (patrón de ingeniería) para secciones clave.
3.  **Fase 3 (Refinamiento):** Ajustar tamaños de tipografía H1/H2 para móviles y añadir breadcrumbs a las páginas secundarias.
