# **Plan Estratégico de Trabajo y Arquitectura UI/UX**

# **Optimización del Sitio Web Empresarial \- Legado Ambiental**

# **1\. Resumen Ejecutivo y Visión del Proyecto**

El presente documento establece el plan integral para la reestructuración y optimización técnica de la plataforma digital de **Legado Ambiental**. El objetivo central es evolucionar el sitio web actual desde un catálogo informativo estático hacia un embudo de conversión B2B activo y altamente eficiente. En el ámbito corporativo B2B, un embudo de conversión es un sistema estructurado diseñado para guiar de manera progresiva a los tomadores de decisiones a través de etapas clave de evaluación: desde la atracción e identificación de una necesidad normativa o técnica, hasta la consideración de soluciones y la toma de contacto formal. En este contexto, la plataforma se optimizará para **capturar el interés de decisiones de compra de alto valor, automatizar la calificación de prospectos corporativos y facilitar la solicitud de cotizaciones especializadas**.

La visión estratégica se orienta a captar a los primeros 100 visitantes altamente cualificados (tales como empresas constructoras, despachos de ingeniería y dependencias públicas con proyectos, licitaciones o trámites ambientales en puerta), canalizándolos mediante llamados a la acción claros y flujos de contacto optimizados.

Para garantizar una ejecución viable, el proyecto está delimitado a una **ventana temporal estricta de 2 semanas (10 días hábiles)** con una **capacidad total ajustada de 40 horas efectivas de trabajo**, resultado de una reestructuración estratégica del backlog original de 70 horas. Esta priorización concentrará los esfuerzos en la infraestructura base de conversión, el posicionamiento local y la prospección activa.

# **2\. Arquitectura UI/UX y Estilos Visuales del Sitio**

La estrategia de diseño combina una experiencia web fluida tipo Single Page Application (SPA) con un sistema editorial apto para generación e impresión de reportes en PDF sin pérdida de fidelidad visual.

# **Stack Tecnológico y Librerías**

* **Motor CSS:** Tailwind CSS v3 (vía CDN). Garantiza un renderizado determinista y ligero mediante clases utilitarias.  
* **Tipografías:** Integradas desde Google Fonts.  
* **Manrope (Principal):** Tipografía sans-serif geométrica moderna (pesos 300 a 800). Aporta una estética limpia, de ingeniería y altamente legible.  
* **Merriweather (Secundaria):** Tipografía serif utilizada para contrastes editoriales y citas de respaldo.  
* **Iconografía:** SVG nativo integrado directamente en el HTML para evitar dependencias externas pesadas.

# **Tokens de Color Corporativos (Design Tokens)**

El sistema cromático respeta y jerarquiza la identidad institucional de Legado Ambiental:

| Token de Color | Hex / Utility | Aplicación en Interfaz |
| :---- | :---- | :---- |
| **Primary (Verde Esmeralda)** | `#22c55e` | Bordes de tarjetas, botones de acción principales (CTAs) y acentos de sustentabilidad. |
| **Secondary (Azul Rey)** | `#3b82f6` | Acentos en secciones técnicas, ingeniería civil y elementos de saneamiento. |
| **Navy (Azul Pizarra Oscuro)** | `#0f172a` | Encabezados principales (`h1`, `h2`, `h3`), fondos de cabecera y footers. Sustituye al negro puro para reducir la fatiga visual. |
| **Charcoal (Gris Carbón)** | `#334155` | Texto de párrafos y cuerpo principal sobre fondos claros. |
| **Categorización** | `emerald-500`, `cyan-500`, `indigo-500`, `orange-500`, `teal-500` | Identificación cromática en los bordes de tarjetas de clientes y etiquetas temporales. |

# **Sistema de Layout y Arquitectura de Impresión PDF**

El maquetado utiliza un contenedor maestro (`.page-container`) dimensionado exactamente en `8.5in` x `11in` (Tamaño Carta estándar).

* **Comportamiento en Pantalla:** Se presenta centrado con un margen superior de `10mm` y sombra suave (`box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1)`) sobre fondo neutro (`bg-slate-50`).  
* **Paginación Flexbox:** Utiliza `display: flex; flex-direction: column` con la propiedad `mt-auto` en el pie de página. Esto empuja matemáticamente las numeraciones de página (*"Página X de Y"*) al extremo inferior sin solapamientos.  
* **Reglas de Impresión `@media print`:** Aplica `@page { margin: 0; }` para desactivar las cabeceras automáticas del navegador. Incorpora un relleno interno de seguridad de `15mm` (`padding: 15mm`) para proteger el contenido dentro del área imprimible.

# **Micro-Componentes y Detalle de UI**

* **Tarjetas de Cliente (Cards):** Cabeceras en `bg-navy` con texto blanco en mayúsculas (`uppercase`). El cuerpo posee fondo blanco y una línea border lateral izquierda (`border-l-2`) en color de categoría.  
* **Badges Soft UI:** Diseñados con fondos translúcidos (`bg-primary/10`) y tipografía densa (`text-[10px] font-bold`), facilitando la lectura de fechas y datos clave sin distraer del texto principal.  
* **Botón Interactivo de Impresión:** Posicionado en la esquina inferior derecha (`fixed bottom-8 right-8`). Incluye la regla CSS `@print { .no-print { display: none; } }` para ocultarse automáticamente al exportar a PDF.

# **3\. Diagnóstico del Estado Actual y Pilares Estratégicos**

# **Diagnóstico**

Actualmente, Legado Ambiental cuenta con un sitio web operativo que describe su oferta integral en consultoría ambiental, topografía, obras de saneamiento y seguridad e higiene. Sin embargo, la plataforma funciona como un catálogo informativo estático, careciendo de un mecanismo estructurado para la captación, calificación y conversión de prospectos comerciales.

# **Audiencia Objetivo**

* **Sector Privado:** Empresas constructoras, despachos de ingeniería civil, desarrolladores inmobiliarios, plantas industriales y contratistas generales.  
* **Sector Público:** Dependencias de gobierno a nivel municipal, estatal y federal.

# **Estrategia de Acción: 6 Pilares Estratégicos**

1. **Pilar 1: Optimización Técnica y de Conversión Web:** Rediseño de la sección principal (Hero) hacia un enfoque orientado a resolver problemas directos, incorporación de llamadas a la acción (CTAs) visibles y simplificación de formularios de contacto.  
2. **Pilar 2: Estrategia de Contenidos y Autoridad:** Publicación de artículos técnico-comerciales sobre normativas clave (ej. NOM-052-SEMARNAT, STPS) orientados a búsquedas de alta intención.  
3. **Pilar 3: Prospección B2B y Distribución:** Difusión periódica en LinkedIn y contacto directo estructurado con directores de obra y responsables ambientales.  
4. **Pilar 4: Herramientas de Ventas y Alianzas:** Portafolio ejecutivo descargable con código QR e iniciación de alianzas estratégicas con laboratorios y topógrafos.  
5. **Pilar 5: Búsqueda Local y Visibilidad (SEO Local):** Optimización completa de Google Business Profile y gestión de reseñas de clientes.  
6. **Pilar 6: Adquisición de Pago (Google Ads Local):** Campaña diferida para la fase post-proyecto dirigida a búsquedas de alta intención.

# **4\. Capacidad del Equipo y Matriz de Roles**

El proyecto se ejecutará con un equipo técnico de 2 personas, sumando una capacidad total de **40 horas de trabajo efectivo distribuidas en 10 días hábiles**:

* **Persona A (Estratega / Dirección Técnica):** Asignación de 1 hora/día (10 horas totales \= 25% de la capacidad). Responsable de la redacción de copys persuasivos, creación de contenido normativo especializado (STPS/SEMARNAT) y dirección de las ceremonias ágiles.  
* **Persona B (Desarrollador / Ejecutor):** Asignación de 3 horas/día (30 horas totales \= 75% de la capacidad). Responsable de la maquetación web en Tailwind CSS, optimización de formularios, configuración SEO local, integración de analítica y prospección B2B directa.

# **Matriz de Distribución de Horas**

| Rol / Integrante | Perfil y Enfoque | Horas Sprint 1 | Horas Sprint 2 | Total Proyecto |
| :---- | :---- | :---- | :---- | :---- |
| **Persona A** | Estratega y Dirección Técnica | 5.0 hrs | 5.0 hrs | **10.0 hrs** |
| **Persona B** | Desarrollador y Ejecutor | 15.0 hrs | 15.0 hrs | **30.0 hrs** |
| **Total Combinado** | **Capacidad Total del Equipo** | **20.0 hrs** | **20.0 hrs** | **40.0 hrs** |

# **5\. Plan de Trabajo Ágil y Backlog Ajustado a 2 Semanas**

El backlog original ha sido optimizado para concentrar 40 horas en dos Sprints semanales de 20 horas cada uno.

# **Sprint 1: Fundamentos de Conversión y Presencia Local (20 Horas)**

Objetivo del Sprint: Consolidar la arquitectura base de conversión web, simplificación de puntos de contacto y activación de SEO local.

| ID | Tarea / Historia de Usuario | Horas Totales | Asignación por Rol | Criterios de Aceptación |
| :---- | :---- | :---- | :---- | :---- |
| **PB1** | Rediseño de la Hero Section. | 3.0 h | Persona A: 1.0hPersona B: 2.0h | Encabezado actualizado con propuesta de valor clara y enfocada en soluciones. |
| **PB2** | Integración de CTAs estratégicos. | 3.0 h | Persona B: 3.0h | Botones de "Cotizar", "WhatsApp" y "Descargar Portafolio" visibles y funcionales. |
| **PB3** | Simplificación de formularios. | 3.0 h | Persona B: 3.0h | Formularios reducidos a 6 campos esenciales con pruebas de envío exitosas. |
| **PB4** | Google Business Profile (SEO Local). | 3.0 h | Persona A: 1.0hPersona B: 2.0h | Perfil verificado, áreas de servicio configuradas y fotografías añadidas. |
| **PB7** | Optimización del Portafolio PDF. | 3.0 h | Persona A: 1.0hPersona B: 2.0h | Documento ajustado a plantilla editorial con código QR de contacto. |
| **PB12** | Configuración de Analíticas (GA4/GTM). | 3.0 h | Persona B: 3.0h | Eventos de conversión configurados para clics en WhatsApp y envíos de formulario. |
| **Cer.** | Ceremonias Ágiles del Sprint 1\. | 2.0 h | Persona A: 2.0h | Sprint Planning, seguimiento diario y Sprint Review realizados. |

# **Sprint 2: Páginas de Servicios, Contenido Técnico y Prospección B2B (20 Horas)**

*Objetivo del Sprint:* Desplegar landing pages de servicios específicos, publicar el contenido normativo clave e iniciar la prospección comercial.

| ID | Tarea / Historia de Usuario | Horas Totales | Asignación por Rol | Criterios de Aceptación |
| :---- | :---- | :---- | :---- | :---- |
| **PB5** | Páginas de Servicios Específicos. | 6.0 h | Persona A: 1.0hPersona B: 5.0h | Landings independientes redactadas y maquetadas para Consultoría, Topografía y Saneamiento. |
| **PB6** | Artículo Técnico Normativo (STPS/SEMARNAT). | 4.0 h | Persona A: 2.0hPersona B: 2.0h | Artículo especializado enfocado en cumplimiento normativo publicado con CTAs. |
| **PB8** | Plantillas y Preparación B2B. | 3.0 h | Persona A: 1.0hPersona B: 2.0h | Perfiles optimizados y 3 plantillas de contacto con enfoque de valor redactadas. |
| **PB9-10** | Prospección Directa y Alianzas. | 3.0 h | Persona A: 0.5hPersona B: 2.5h | Primeros 15 contactos de prospección realizados y 5 aliados contactados. |
| **Prueb.** | Pruebas de Embudo y Cierre. | 1.5 h | Persona B: 1.5h | Pruebas integrales de flujo de conversión y validación de links. |
| **Cer.** | Ceremonias Ágiles del Sprint 2\. | 2.5 h | Persona A: 1.5hPersona B: 1.0h | Cierre de proyecto, revisión de métricas orgánicas y retrospectiva final. |

# **6\. Cronograma Detallado y Cajas de Tiempo Día a Día**

El plan de trabajo se ejecuta en un periodo secuencial de 10 días hábiles:

* **Día 01:** Inicio del proyecto. Ejecución del rediseño del Hero Section (PB1) y maquetación de botones CTAs principales (PB2).  
* **Día 02:** Finalización de integración de CTAs (PB2) y arranque en la simplificación de formularios de contacto (PB3).  
* **Día 03:** Conclusión y pruebas de formularios (PB3) e inicio de configuración de Google Business Profile (PB4).  
* **Día 04:** Finalización del perfil de SEO Local (PB4) y maquetación del portafolio corporativo descargable (PB7).  
* **Día 05:** Configuración de eventos en Google Analytics 4 / Tag Manager (PB12). Ejecución de la Review y Retrospectiva del Sprint 1\.  
* **Día 06:** Inicio de desarrollo de Páginas de Servicios Específicos (PB5 \- Parte 1).  
* **Día 07:** Finalización de Páginas de Servicios (PB5 \- Parte 2\) e inicio de redacción del Artículo Técnico Normativo (PB6).  
* **Día 08:** Publicación del Artículo Técnico (PB6) y elaboración de perfiles/plantillas para prospección B2B (PB8).  
* **Día 09:** Envío de mensajes de prospección en LinkedIn (PB9) y contacto inicial para red de alianzas (PB10).  
* **Día 10:** Pruebas integrales del embudo de conversión, verificación de métricas de analítica, Review Final y Cierre del Proyecto.

# **7\. Marco de Gobernanza Ágil y Ceremonias Adaptadas**

Para no saturar las 3 horas diarias de ejecución de la Persona B ni la hora diaria de la Persona A, se adopta un marco Scrum aligerado:

* **Daily Stand-up (5 a 10 min \- Asíncrono):** Realizado mediante mensajes rápidos en canal interno. Cada integrante responde: ¿Qué se logró ayer?, ¿Qué se ejecutará hoy? y ¿Existe algún bloqueo?.  
* **Sprint Planning (Lunes \- 30 min):** Revisión de los objetivos semanales y entrega de insumos/copys redactados por la Persona A a la Persona B.  
* **Sprint Review & Retrospective (Viernes \- 45 min):** Demostración visual de los avances desplegados en la plataforma, revisión de conversiones registradas y ajustes al backlog.

# **8\. Factores Clave de Éxito y Fase Post-Proyecto**

# **Diferenciador Normativo STPS / SEMARNAT**

El principal factor de atracción de tráfico cualificado reside en la capacidad técnica del equipo para traducir normativas complejas (ej. NOM-001-SEMARNAT, normativas de seguridad STPS) en guías de acción prácticas. La creación de este contenido técnico por parte de la Persona A establece una barrera competitiva frente a agencias de marketing genéricas.

# **Medición Continua Obligatoria**

El éxito del embudo se evaluará semanalmente mediante el monitoreo de dos métricas clave de conversión:

1. Tasa de clics e inicios de conversación hacia el canal directo de WhatsApp.  
2. Número de formularios de cotización completados y enviados con éxito.

# **Fase Post-Proyecto: Pauta Pagada (Google Ads Local)**

Una vez concluida la ventana de 10 días y validado el correcto funcionamiento del embudo de conversión de forma orgánica, se evaluará el inicio de la tarea PB13 (Google Ads Local) a partir de la Semana 3\. Esta campaña se enfocará en palabras clave de alta intención comercial (*"estudio de impacto ambiental"*, *"levantamiento topográfico para obra"*) dirigiendo el tráfico pagado directamente a las landing pages de servicios específicos construidas durante el proyecto.