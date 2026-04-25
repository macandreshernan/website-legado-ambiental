# Plan de Modificaciones UI/UX (Legado Ambiental)

A continuación, presento el plan detallado para aplicar las modificaciones de acuerdo a los requerimientos y mis consideraciones como experto UX/UI.

## 1. Menú Principal y Menú Flotante (Archivos afectados: todos los HTML)
- **Ocultar Botón "Cotizar":** Se comentará el bloque de código del botón "Cotizar" dentro del contenedor del menú móvil (`mobile-menu`). Como recomendación de UI/UX, para evitar inconsistencias cognitivas, se ocultará también el botón "Cotizar" del header de escritorio si aplica, ya que su funcionalidad será cubierta por la nueva opción del menú.
- **Cambiar Etiqueta "Servicios":** Se reemplazará el texto "Servicios" por "Servicios y Cotización". Esto optimiza el menú, ya que ambas intenciones (conocer servicios y cotizar) van de la mano.

## 2. Mini-Footer (Archivos afectados: todos excepto `home.html`)
- **Acción Copiar URL:** El icono `share` se conectará a un evento `onclick` con `navigator.clipboard.writeText(window.location.href)` y mostrará un tooltip o pequeña alerta visual confirmando "Enlace copiado".
- **Eliminar Ubicación:** Se removerá el icono `location_on` del mini-footer para simplificar visualmente esta barra.

## 3. Sección "Quiénes Somos" (`about_us/about_us.html`)
- **Footer CTA:** El botón "Iniciar consulta" se enlazará para asegurar la redirección correcta a la vista `../services_overview/services.html`.

## 4. Sección "Servicios" (`services_overview/services.html`)
- **Cintilla "CTA":** Se eliminarán (o comentarán) los botones "Obtener Cotización" y "Nuestro Proceso".
- **Acomodo de Diseño:** Al retirar estos botones, revisaré y reajustaré la distribución (flexbox) de los elementos que queden en esa cintilla para que el diseño siga luciendo premium, limpio y balanceado.

## 5. Sección "Experiencia" (`experience_timeline/our_experience.html`)
- **Footer CTA:** Se modificará el enlace de "Contactar Ahora" para que dirija a `../faq/contact_faq.html`.

## 6. Integración Final y Git
- Una vez verificados todos los cambios, documentaré brevemente los ajustes en el archivo `README.md`.
- Procederé a empaquetar todos los cambios con el commit: `"Se agregan las observaciones recolectadas con el usuario. Se atienden observaciones del 1 al 10"`. (Nota: Mencionas del 1 al 10 en tu instrucción de commit, aunque hemos enlistado objetivos del 1 al 6; usaré exactamente tu mensaje propuesto).

---
**¿Estás de acuerdo con este plan para proceder inmediatamente con los ajustes técnicos en el código?**
