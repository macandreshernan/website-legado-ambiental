# Resumen Detallado de Arquitectura UI/UX y Estilos
**Proyecto:** Currícula Empresarial - Legado Ambiental

La estrategia principal fue crear un documento que funcione como una **Single Page Application (SPA) para visualización web** y, simultáneamente, como una **Plantilla Editorial de Alto Rendimiento para impresión PDF**, sin perder fidelidad visual.

---

## 1. Stack Tecnológico y Librerías
*   **Motor CSS:** **Tailwind CSS v3** (vía CDN). Se utiliza para aplicar estilos mediante clases utilitarias, garantizando que el diseño sea determinista (siempre se renderizará igual en cualquier navegador).
*   **Tipografías:** Integradas desde Google Fonts.
    *   **Manrope (Principal):** Fuente sans-serif geométrica moderna (usada en pesos 300 a 800). Aporta una estética de ingeniería limpia, tecnológica y altamente legible, reemplazando fuentes anticuadas como Arial o Times New Roman.
    *   **Merriweather (Secundaria):** Tipografía serif para contrastes (disponible en la configuración como respaldo elegante).
*   **Iconografía:** SVG nativo integrado directamente en el HTML (usado en el botón flotante de imprimir) para evitar dependencias externas.

---

## 2. Paleta de Colores Corporativa (Design Tokens)
Se configuró el archivo `tailwind.config` con colores hexadecimales específicos para mantener la identidad de Legado Ambiental:
*   🟢 **Primary (`#22c55e` / Verde Esmeralda Vibrante):** Color principal de acción. Usado en bordes de tarjetas, botones y acentos de títulos para representar sustentabilidad y medio ambiente.
*   🔵 **Secondary (`#3b82f6` / Azul Rey):** Usado como color de acento secundario (ej. la sección de escuelas/Nogver) para representar ingeniería civil y fluidez.
*   🌑 **Navy (`#0f172a` / Azul Pizarra Ultra Oscuro):** Reemplaza al negro puro (`#000000`). Usado en los títulos principales (`h1`, `h2`, `h3`) y fondos de cabeceras. Da un toque premium, serio y reduce la fatiga visual.
*   🔘 **Charcoal (`#334155` / Gris Carbón):** Usado para todo el texto de párrafos y descripciones. Ofrece un contraste elegante sobre fondos blancos sin ser agresivo a la vista.
*   🎨 **Colores de Categorización:** Se usaron utilidades de Tailwind (`emerald-500`, `cyan-500`, `indigo-500`, `orange-500`, `teal-500`) para darle a cada tarjeta de cliente un "hilo conductor" de color único en su borde izquierdo y en su etiqueta de año.

---

## 3. Sistema de Layout y Arquitectura de Impresión
La parte más compleja del UX fue la reescritura del motor de impresión para garantizar hojas tamaño carta perfectas:
*   **Contenedor Maestro (`.page-container`):**
    *   **Dimensiones:** Exactamente `8.5in` de ancho por `11in` de alto (Tamaño Carta estándar).
    *   **Márgenes (Screen):** `margin: 10mm auto` con un sutil sombreado (`box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1)`) para que en pantalla parezca una hoja de papel física flotando sobre el fondo (`bg-slate-50`).
*   **Sistema de Flexbox para Paginación:** 
    *   El contenedor usa `display: flex; flex-direction: column`.
    *   El pie de página y los números de página utilizan la clase `mt-auto` (Margin-Top: Auto). Esto empuja mágicamente los textos *"Página 1 de 2"* hasta el fondo absoluto de la hoja, calculando el espacio vacío de forma matemática, evitando que los textos se empalmen.
*   **Reglas CSS `@media print`:**
    *   `@page { margin: 0; }`: Un hack avanzado que engaña a Google Chrome para que desactive y oculte la URL, fecha y hora automáticas que suelen ensuciar los PDF.
    *   `padding: 15mm`: Como eliminamos el margen del navegador, le inyectamos 15 milímetros de "zona segura" por dentro al contenedor para que el texto nunca toque el borde del papel físico.

---

## 4. Micro-Componentes y Detalles de UI
*   **Tarjetas de Cliente (Cards):**
    *   **Cabecera:** Usa `bg-navy` con texto blanco, redondeado superior (`rounded-t-lg`), y texto en Mayúsculas (`uppercase`) para jerarquizar rápidamente el nombre del cliente.
    *   **Cuerpo:** Fondo blanco puro, con una sutil línea lateral de color (`border-l-2`) que guía el ojo a través del texto del proyecto.
*   **Badges de Años (Etiquetas):**
    *   Se diseñaron utilizando un fondo translúcido (ej. `bg-primary/10`, que significa 10% de opacidad) con texto denso (`text-[10px] font-bold`). Este es un patrón UI moderno llamado *"Glassmorphism/Soft UI"* que permite leer años clave sin robar el protagonismo al texto descriptivo.
*   **Botón Interactivo de Impresión:**
    *   Posicionado absolutamente (`fixed bottom-8 right-8`), usa la clase `@print { .no-print { display: none; } }` para asegurar que el botón exista en la pantalla para ayudar al usuario, pero desaparezca como un fantasma al generar el PDF.

Este sistema asegura que el documento de Legado Ambiental no luzca como un documento de Word tradicional, sino como un reporte anual generado por un estudio de diseño gráfico.
