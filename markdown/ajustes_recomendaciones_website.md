# Ajustes y Recomendaciones de Diseño - Legado Ambiental

Este documento detalla el análisis de la experiencia de usuario (UX) y la interfaz (UI) del sitio web de Legado Ambiental, con sugerencias específicas para modernizar y optimizar la plataforma.

## 1. Descripción Detallada del Diseño

El diseño propuesto evoluciona la identidad actual hacia un enfoque "Eco-Industrial Moderno", combinando la robustez de la ingeniería con la frescura de la sostenibilidad.

### Sistema de Color (Extraído y Optimizado)
Se mantienen los colores base detectados pero se refina su uso para jerarquía y accesibilidad.

- **Primario (Acción/Marca):** `#2E7D32` (Verde Bosque) - Usar en CTAs principales, iconos destacados y enlaces activos.
- **Secundario (Soporte):** `#D7CCC8` (Arcilla/Tierra) - Usar en fondos de secciones secundarias o detalles sutiles.
- **Neutro Oscuro (Texto/Fondos):** `#101922` (Navy Profundo) - Para encabezados y pies de página.
- **Neutro Claro (Fondos):** `#F6F7F8` (Blanco Humo) - Fondo general para descanso visual.
- **Acento (Hover/Estados):** `#1B5E20` (Verde Oscuro) - Para estados hover de botones.

### Tipografía
**Conflicto Detectado:** Los archivos HTML actuales declaran "Public Sans" en el `body`, pero `theme-config.js` define "Manrope" y "Merriweather".
**Recomendación:** Unificar a la configuración del tema para consistencia.
- **Títulos (Serif):** `Merriweather` (Pesos: 700, 900) - Aporta autoridad y tradición.
- **Cuerpo/UI (Sans):** `Manrope` (Pesos: 400, 500, 600) - Moderna, técnica y legible.

### Medidas y Espaciado (Sistema de 4px/8px)
- **Contenedor Máximo:** `1200px` (o `max-w-7xl` de Tailwind).
- **Márgenes Laterales (Padding):** Móvil `16px` (`px-4`), Tablet `32px` (`px-8`), Escritorio `0` (centrado).
- **Espaciado Vertical de Secciones:** `80px` (`py-20`) para dar aire y elegancia.
- **Espaciado entre Elementos:** `24px` (`gap-6`) o `32px` (`gap-8`).

## 2. Jerarquía y Componentes

### Jerarquía Visual
1.  **H1 (Héroe):** 48px - 60px (Desktop), 36px (Móvil). Merriweather Bold.
2.  **H2 (Títulos Sección):** 36px - 48px. Manrope ExtraBold o Merriweather Bold.
3.  **H3 (Títulos Tarjetas):** 24px. Manrope Bold.
4.  **Cuerpo:** 16px - 18px. Manrope Regular. Altura de línea 1.6 para legibilidad.

### Tarjetas de Servicio (Componente Clave)
Deben destacar los nuevos servicios: *Gestión de residuos*, *Tratamiento de agua*, *Consultoría técnica*.
- **Estructura:** Icono grande (flotante o enmarcado) + Título + Descripción breve + Link "Leer más".
- **Sombra:** `shadow-sm` en reposo, `shadow-xl` y `translate-y-[-4px]` en hover.
- **Borde:** Sutil `border-gray-100` que cambia a `border-primary` en hover.

## 3. Estados de Interacción

- **Botones Primarios:**
    - Reposo: Fondo `#2E7D32`, Texto Blanco, Sombra `shadow-md`.
    - Hover: Fondo `#1B5E20`, Escala 1.02.
    - Active: Fondo `#1B5E20`, Escala 0.98.
    - Focus: Ring de 2px color `#2E7D32` con offset.
- **Enlaces de Navegación:**
    - Reposo: Texto `#101922` o Gris Oscuro.
    - Hover: Color Primary `#2E7D32`, Subrayado animado o cambio de peso.
    - Active: Color Primary, Negrita.

## 4. Comportamiento Responsivo

- **Móvil First:** El diseño debe apilarse verticalmente en pantallas < 768px.
- **Navegación:**
    - Escritorio: Menú horizontal visible.
    - Móvil: Menú hamburguesa (`hamburger menu`) que despliega un panel lateral o `dropdown` completo. Asegurar botones de cierre accesibles (44x44px mínimo).
- **Imágenes:** Usar `object-cover` y alturas fijas en móvil (ej. `h-64`) para evitar saltos de contenido.

## 5. Consideraciones de Accesibilidad

- **Contraste:** Verificar que el texto gris claro sobre fondo blanco tenga radio 4.5:1. Usar grises más oscuros (ej. `text-gray-600` en lugar de `text-gray-400`) para textos pequeños.
- **Etiquetas ARIA:** Añadir `aria-label` a botones de iconos (ej. redes sociales, menú).
- **Foco Visible:** Nunca eliminar `outline-none` sin proveer un estilo de foco alternativo (ej. `focus:ring`).
- **Texto Alt:** Asegurar que todas las imágenes en `/assets/images` tengan atributos `alt` descriptivos.

## 6. Sugerencias Paso a Paso

1.  **Unificar Tipografía:** Eliminar `font-family: "Public Sans"` de `home.html` y usar las clases de utilidad de Tailwind (`font-sans`, `font-serif`) definidas en `theme-config.js`.
2.  **Actualizar Servicios:** Reemplazar el contenido de las tarjetas de servicio en `home.html` y `services.html` para reflejar "Gestión de residuos", "Tratamiento de agua" y "Consultoría técnica".
3.  **Modernizar Tarjetas:** Aplicar el estilo de tarjeta con efecto "glassmorphism" o borde sutil (ver código componente) para un look más minimalista.
4.  **Revisar Contraste:** Oscurecer los textos secundarios (`text-gray-400` -> `text-gray-600`).
5.  **Optimizar Imágenes:** Asegurar que las imágenes en `/assets` estén optimizadas (WebP) y tengan dimensiones adecuadas para no afectar el LCP (Largest Contentful Paint).
