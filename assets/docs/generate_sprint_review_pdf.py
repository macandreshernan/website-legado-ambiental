import os
import subprocess
import base64

# 1. Load corporate logo
logo_path = 'assets/images/logo/logo_final_v2.png'
if os.path.exists(logo_path):
    with open(logo_path, 'rb') as f:
        logo_b64 = f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"
else:
    logo_b64 = ""

# 2. Load QR code
qr_path = 'assets/images/qr/qr-legadoambiental-brand.png'
if os.path.exists(qr_path):
    with open(qr_path, 'rb') as f:
        qr_b64 = f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"
else:
    qr_b64 = ""

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Informe Ejecutivo de Sprint Review y Plan de Acción - Legado Ambiental</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800;900&family=Merriweather:ital,wght@0,300;0,400;0,700;1,400&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['Manrope', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
            serif: ['Merriweather', 'Georgia', 'serif'],
          }},
          colors: {{
            brand: {{
              50: '#f0fdf4',
              100: '#dcfce7',
              500: '#22c55e',
              700: '#15803d',
              800: '#166534',
              900: '#1e6040',
              950: '#0d3822',
            }},
            navy: {{
              800: '#1e293b',
              900: '#0f172a',
              950: '#020617',
            }},
            charcoal: '#334155',
          }}
        }}
      }}
    }}
  </script>

  <style>
    @page {{
      size: letter;
      margin: 0;
    }}
    * {{
      box-sizing: border-box;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}
    body {{
      background-color: #e2e8f0;
      font-family: 'Manrope', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: #334155;
      margin: 0;
      padding: 0;
    }}
    .page-container {{
      width: 8.5in;
      height: 11in;
      max-height: 11in;
      margin: 8mm auto;
      background: white;
      padding: 8mm 12mm;
      box-sizing: border-box;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      page-break-after: always;
    }}
    @media print {{
      body {{
        background-color: white;
      }}
      .page-container {{
        width: 8.5in;
        height: 11in;
        max-height: 11in;
        margin: 0;
        padding: 8mm 12mm;
        box-shadow: none;
        page-break-after: always;
        overflow: hidden;
      }}
      .no-print {{
        display: none !important;
      }}
    }}
    .table-custom th {{
      background-color: #0f172a;
      color: #ffffff;
      font-size: 8.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 5px 7px;
    }}
    .table-custom td {{
      font-size: 8px;
      padding: 4.5px 7px;
      border-bottom: 1px solid #e2e8f0;
      vertical-align: middle;
      line-height: 1.25;
    }}
    .badge-pill {{
      display: inline-flex;
      align-items: center;
      padding: 1.5px 6px;
      border-radius: 9999px;
      font-size: 7.5px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    code.tech-code {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 8px;
      background-color: #f1f5f9;
      color: #0f172a;
      padding: 1px 3.5px;
      border-radius: 3px;
      border: 1px solid #e2e8f0;
    }}
    pre.code-block {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 7.2px;
      background-color: #f8fafc;
      color: #1e293b;
      padding: 5px 8px;
      border-radius: 5px;
      border: 1px solid #cbd5e1;
      white-space: pre-wrap;
      line-height: 1.25;
      margin: 0;
    }}
  </style>
</head>
<body class="text-charcoal font-sans antialiased">

  <!-- ========================================== -->
  <!-- PÁGINA 1: PORTADA & ESTADO GENERAL SPRINT  -->
  <!-- ========================================== -->
  <div class="page-container">
    <div>
      <!-- Header Superior -->
      <header class="flex items-center justify-between border-b-2 border-slate-200 pb-2 mb-2.5 shrink-0">
        <div class="flex items-center gap-2.5">
          <img src="{logo_b64}" alt="Legado Ambiental" class="h-10 w-auto object-contain">
          <div>
            <h1 class="text-navy-900 font-black text-base tracking-tight leading-none uppercase">Legado Ambiental</h1>
            <p class="text-[9px] font-semibold text-brand-700 tracking-wide mt-0.5">Consultoría Ambiental &bull; Topografía de Alta Precisión &bull; Obra Civil &bull; STPS</p>
          </div>
        </div>
        <div class="text-right">
          <div class="inline-flex items-center gap-1.5 px-2 py-0.5 bg-emerald-50 border border-emerald-300 rounded text-emerald-900 text-[8.5px] font-bold">
            <span class="w-2 h-2 rounded-full bg-emerald-600 animate-pulse"></span>
            CEREMONIA SPRINT REVIEW &bull; V2.0
          </div>
          <p class="text-[8px] font-mono text-slate-400 mt-0.5">DOC: INF-LA-SR-2026-006 | OCT 2026</p>
        </div>
      </header>

      <!-- Banner de Título Principal -->
      <div class="bg-gradient-to-r from-navy-950 via-navy-900 to-slate-900 rounded-xl p-3 text-white shadow-md mb-2.5 border-l-4 border-emerald-500">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[8px] font-extrabold tracking-widest text-emerald-400 uppercase bg-emerald-950/80 px-2 py-0.5 rounded border border-emerald-500/30">
              Plan Estratégico 40 Horas &bull; Sprint 1 Concluido &bull; Cierre Sprint 2
            </span>
            <h2 class="text-base font-black tracking-tight text-white mt-1 leading-tight">
              Informe Ejecutivo de Sprint Review y Plan de Acción de Cierre B2B
            </h2>
            <p class="text-[10px] text-slate-300 mt-0.5 max-w-xl font-normal leading-relaxed">
              Consolidación integral de avances para Dirección General y Equipo Técnico: Culminación de PB5, Estabilidad UI/UX, SEO Local verificado en Google Maps, Dictamen Google Ads y Guía de Ejecución para los Primeros 100 Leads B2B.
            </p>
          </div>
          <div class="bg-emerald-500/10 border border-emerald-500/30 rounded-lg p-2 text-center shrink-0 ml-3">
            <span class="text-[7.5px] font-bold text-emerald-300 uppercase block">Progreso Global</span>
            <span class="text-base font-black text-emerald-400 block">78% LISTO</span>
            <span class="text-[7px] text-slate-300 font-mono">31 / 40 hrs efectivas</span>
          </div>
        </div>
      </div>

      <!-- Resumen Ejecutivo de Estado -->
      <div class="bg-emerald-50 border-2 border-emerald-600 rounded-xl p-2.5 mb-2.5 shadow-sm">
        <div class="flex items-center justify-between mb-1">
          <div class="flex items-center gap-1.5">
            <span class="flex h-4 w-4 items-center justify-center rounded-full bg-emerald-600 text-white font-bold text-[9px]">✓</span>
            <h3 class="text-[10.5px] font-black uppercase tracking-wider text-emerald-950">
              Dictamen de la Ceremonia de Sprint Review
            </h3>
          </div>
          <span class="badge-pill bg-emerald-700 text-white font-extrabold text-[8px]">
            INFRAESTRUCTURA Y EMBUDO ON-SITE AL 100%
          </span>
        </div>
        <p class="text-[9.5px] text-emerald-900 font-medium leading-relaxed">
          Los <strong>cimientos técnicos y comerciales del ecosistema web han sido completados y blindados</strong>. El hito PB5 culminó en 5 módulos (deep-linking semántico, micro-landings técnicas, erradicación de Google Forms y enlace institucional a LinkedIn). El perfil de <strong>Google Business Profile está formalmente verificado con 199+ interacciones</strong> y catálogo audiovisual HD. Para optimizar el capital de trabajo, se formalizó la <strong>suspensión temporal de Google Ads</strong> ($8,120 MXN ahorrados), orientando las 9.0 horas restantes hacia la autoridad de contenido (PB6), prospección en frío (PB8 a PB10) y recolección de reseñas en Google Maps.
        </p>
      </div>

      <!-- Grid 4 Tarjetas de Resumen de Hitos -->
      <div class="grid grid-cols-4 gap-2 mb-2.5">
        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
          <div class="flex items-center justify-between mb-0.5">
            <span class="text-[7.5px] font-bold text-slate-500 uppercase tracking-wider">Web CRO & PB5</span>
            <span class="text-emerald-600 font-black text-[9.5px]">100%</span>
          </div>
          <span class="text-[10px] font-black text-slate-900 block">Conversión On-Site</span>
          <p class="text-[7.5px] text-slate-600 mt-0.5 leading-tight">Mobile-first, Formulario 6 campos, Sticky Bar + FAB WhatsApp, 0% fuga de tráfico.</p>
        </div>

        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
          <div class="flex items-center justify-between mb-0.5">
            <span class="text-[7.5px] font-bold text-slate-500 uppercase tracking-wider">Pilar 5: SEO Local</span>
            <span class="text-emerald-600 font-black text-[9.5px]">100%</span>
          </div>
          <span class="text-[10px] font-black text-slate-900 block">GBP Verificado</span>
          <p class="text-[7.5px] text-slate-600 mt-0.5 leading-tight">Ficha verificada en vivo, 11 fotos HD (1200x896), video demo 3D y suite QR.</p>
        </div>

        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
          <div class="flex items-center justify-between mb-0.5">
            <span class="text-[7.5px] font-bold text-slate-500 uppercase tracking-wider">Analítica Digital</span>
            <span class="text-emerald-600 font-black text-[9.5px]">100%</span>
          </div>
          <span class="text-[10px] font-black text-slate-900 block">GTM & GA4 Activo</span>
          <p class="text-[7.5px] text-slate-600 mt-0.5 leading-tight">ID G-1MLGHB4E6G en 8 páginas, telemetría B2B completa y compatibilidad CSP.</p>
        </div>

        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
          <div class="flex items-center justify-between mb-0.5">
            <span class="text-[7.5px] font-bold text-slate-500 uppercase tracking-wider">Pilar 6: Google Ads</span>
            <span class="text-amber-600 font-black text-[9.5px]">POSPUESTO</span>
          </div>
          <span class="text-[10px] font-black text-slate-900 block">Dictamen Formal</span>
          <p class="text-[7.5px] text-slate-600 mt-0.5 leading-tight">Ahorro neto de $8,120 MXN; priorización de canales orgánicos a costo cero.</p>
        </div>
      </div>

      <!-- Sección 1: Capacidad del Equipo y Filosofía de Ejecución -->
      <div>
        <div class="flex items-center gap-1.5 mb-1">
          <div class="w-1.5 h-3 bg-brand-700 rounded-full"></div>
          <h3 class="text-[10px] font-black text-navy-900 uppercase tracking-wide">
            1. Modelo de Asignación y Capacidad de Equipo (Ventana de 40 Horas)
          </h3>
        </div>

        <p class="text-[8.8px] text-slate-600 leading-relaxed mb-1.5">
          El plan de trabajo ágil distribuye 40 horas en dos Sprints semanales entre dos roles especializados:
        </p>

        <div class="grid grid-cols-2 gap-2 text-[8.5px]">
          <div class="bg-white border border-slate-200 rounded-lg p-2">
            <h4 class="font-bold text-slate-900 text-[9px] mb-0.5 flex items-center justify-between">
              <span class="flex items-center gap-1"><span class="text-brand-700 font-black">&bull;</span> Persona A (Estratega / Dirección Técnica)</span>
              <span class="font-mono text-emerald-700 font-bold">10.0 hrs totales</span>
            </h4>
            <p class="text-slate-600 leading-snug text-[8px]">
              Responsable de los copys persuasivos B2B, diseño del marco técnico normativo (SEMARNAT/STPS), contacto institucional para alianzas comerciales y solicitud de reseñas clave a clientes históricos.
            </p>
          </div>

          <div class="bg-white border border-slate-200 rounded-lg p-2">
            <h4 class="font-bold text-slate-900 text-[9px] mb-0.5 flex items-center justify-between">
              <span class="flex items-center gap-1"><span class="text-brand-700 font-black">&bull;</span> Persona B (Desarrollador / Ejecutor Digital)</span>
              <span class="font-mono text-emerald-700 font-bold">30.0 hrs totales</span>
            </h4>
            <p class="text-slate-600 leading-snug text-[8px]">
              Responsable de la maquetación en Tailwind CSS, router semántico JS, blindaje contra pantallas blancas, instrumentación de telemetría GA4/GTM, pruebas E2E e identificación/envío de prospectos en frío.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer Página 1 -->
    <footer class="border-t border-slate-200 pt-1.5 mt-1 flex items-center justify-between text-[8px] text-slate-400 shrink-0">
      <div class="flex items-center gap-2">
        <span class="font-bold text-slate-600 uppercase">Legado Ambiental S.A. de C.V.</span>
        <span>&bull;</span>
        <span>Sprint Review &bull; Optimización UI/UX y Embudo B2B</span>
      </div>
      <div class="flex items-center gap-3">
        <span>Uso Interno</span>
        <span class="font-bold text-slate-700 bg-slate-100 px-2 py-0.5 rounded">Página 1 de 5</span>
      </div>
    </footer>
  </div>

  <!-- ========================================== -->
  <!-- PÁGINA 2: MATRIZ DE CUMPLIMIENTO DEL BACKLOG-->
  <!-- ========================================== -->
  <div class="page-container">
    <div>
      <!-- Header Superior Compacto -->
      <header class="flex items-center justify-between border-b border-slate-200 pb-2 mb-2 shrink-0">
        <div class="flex items-center gap-2">
          <img src="{logo_b64}" alt="Legado Ambiental" class="h-7 w-auto object-contain">
          <span class="text-[11px] font-black uppercase text-navy-900 tracking-tight">Informe de Estado: Plan de Trabajo y Avances</span>
        </div>
        <span class="text-[8px] font-mono text-slate-400">SECCIÓN 2: MATRIZ COMPLETA DEL BACKLOG</span>
      </header>

      <!-- Sección 2: Matriz Comparativa del Backlog -->
      <div class="mb-2">
        <div class="flex items-center gap-1.5 mb-1">
          <div class="w-1.5 h-3 bg-brand-700 rounded-full"></div>
          <h3 class="text-[10px] font-black text-navy-900 uppercase tracking-wide">
            2. Matriz de Cumplimiento: Tareas Planificadas vs. Realidad en Producción
          </h3>
        </div>

        <!-- Tabla del Backlog -->
        <div class="overflow-hidden border border-slate-200 rounded-lg shadow-sm mb-2">
          <table class="w-full table-custom text-left border-collapse">
            <thead>
              <tr>
                <th class="w-[7%] text-center">ID</th>
                <th class="w-[27%]">Historia / Tarea Original</th>
                <th class="w-[8%] text-center">Horas</th>
                <th class="w-[18%] text-center">Estado Real</th>
                <th class="w-[40%]">Entregables y Evidencia Técnica</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="text-center font-bold text-slate-900">PB1</td>
                <td class="font-semibold text-slate-900">Rediseño Hero Section JTBD</td>
                <td class="text-center font-mono">3.0 h</td>
                <td class="text-center"><span class="badge-pill bg-emerald-100 text-emerald-800">100% Concluido</span></td>
                <td class="text-slate-600">Copys orientados a dolor en <code class="tech-code">home.html</code>, trust banner normativo (`NOM-052`, `STPS`) y paridad `i18n.js`.</td>
              </tr>
              <tr class="bg-slate-50/50">
                <td class="text-center font-bold text-slate-900">PB2</td>
                <td class="font-semibold text-slate-900">CTAs Estratégicos & Contacto</td>
                <td class="text-center font-mono">3.0 h</td>
                <td class="text-center"><span class="badge-pill bg-emerald-100 text-emerald-800">100% Concluido</span></td>
                <td class="text-slate-600">Botones "Cotizar", "WhatsApp" y "Descargar Portafolio"; Sticky Bar + FAB WhatsApp en móvil.</td>
              </tr>
              <tr>
                <td class="text-center font-bold text-slate-900">PB3</td>
                <td class="font-semibold text-slate-900">Simplificación de Formularios</td>
                <td class="text-center font-mono">3.0 h</td>
                <td class="text-center"><span class="badge-pill bg-emerald-100 text-emerald-800">100% Concluido</span></td>
                <td class="text-slate-600">Formulario de 6 campos en <code class="tech-code">contact_faq.html</code>, trampa Honeypot anti-spam y entrega AJAX FormSubmit.</td>
              </tr>
              <tr class="bg-slate-50/50">
                <td class="text-center font-bold text-slate-900">PB4</td>
                <td class="font-semibold text-slate-900">Google Business Profile (SEO Local)</td>
                <td class="text-center font-mono">3.0 h</td>
                <td class="text-center"><span class="badge-pill bg-emerald-100 text-emerald-800">100% Concluido</span></td>
                <td class="text-slate-600">Ficha verificada con badge oficial, 11 fotos HD (1200x896), video demo 3D y suite completa de QR.</td>
              </tr>
              <tr>
                <td class="text-center font-bold text-slate-900">PB7</td>
                <td class="font-semibold text-slate-900">Optimización Portafolio PDF & QR</td>
                <td class="text-center font-mono">3.0 h</td>
                <td class="text-center"><span class="badge-pill bg-emerald-100 text-emerald-800">100% Concluido</span></td>
                <td class="text-slate-600">Plantilla editorial Carta (8.5x11 in) con `@media print`, flexbox `mt-auto` y tarjeta QR de mostrador.</td>
              </tr>
              <tr class="bg-slate-50/50">
                <td class="text-center font-bold text-slate-900">PB12</td>
                <td class="font-semibold text-slate-900">Analítica Digital (GA4 & GTM)</td>
                <td class="text-center font-mono">3.0 h</td>
                <td class="text-center"><span class="badge-pill bg-emerald-100 text-emerald-800">100% Concluido</span></td>
                <td class="text-slate-600">Tag `G-1MLGHB4E6G` en 8 páginas, cabeceras CSP actualizadas, 8 eventos de conversión en <code class="tech-code">analytics.js</code>.</td>
              </tr>
              <tr class="bg-blue-50/60">
                <td class="text-center font-bold text-blue-900">PB5</td>
                <td class="font-semibold text-blue-950">Landings de Servicios & Embudo</td>
                <td class="text-center font-mono">6.0 h</td>
                <td class="text-center"><span class="badge-pill bg-emerald-100 text-emerald-800">100% Concluido</span></td>
                <td class="text-blue-950">Módulos 1-5 completados en <code class="tech-code">services.html</code>: deep linking, micro-landings, 0% fuga Google Forms y LinkedIn institucional.</td>
              </tr>
              <tr>
                <td class="text-center font-bold text-slate-900">PB6</td>
                <td class="font-semibold text-slate-900">Artículo Técnico Normativo (STPS/NOM)</td>
                <td class="text-center font-mono">4.0 h</td>
                <td class="text-center"><span class="badge-pill bg-amber-100 text-amber-800">Pendiente Sprint 2</span></td>
                <td class="text-slate-600">Trust badges normativos activos en Hero; pendiente artículo editorial extendido para prospección.</td>
              </tr>
              <tr class="bg-slate-50/50">
                <td class="text-center font-bold text-slate-900">PB8</td>
                <td class="font-semibold text-slate-900">Plantillas y Preparación B2B</td>
                <td class="text-center font-mono">3.0 h</td>
                <td class="text-center"><span class="badge-pill bg-amber-100 text-amber-800">Parcial Sprint 2</span></td>
                <td class="text-slate-600">Perfil LinkedIn oficial integrado en 8 páginas; pendiente redacción formal de las 3 plantillas de frío.</td>
              </tr>
              <tr>
                <td class="text-center font-bold text-slate-900">PB9-10</td>
                <td class="font-semibold text-slate-900">Prospección Directa & Red Alianzas</td>
                <td class="text-center font-mono">3.0 h</td>
                <td class="text-center"><span class="badge-pill bg-slate-100 text-slate-700">Fase Operativa</span></td>
                <td class="text-slate-600">Embudo web listo; pendiente envío de 15 prospectos cualificados y vinculación con 5 aliados.</td>
              </tr>
              <tr class="bg-slate-50/50">
                <td class="text-center font-bold text-slate-900">Prueb.</td>
                <td class="font-semibold text-slate-900">Pruebas de Embudo & Cero Regresión</td>
                <td class="text-center font-mono">1.5 h</td>
                <td class="text-center"><span class="badge-pill bg-emerald-100 text-emerald-800">100% Concluido</span></td>
                <td class="text-slate-600">Auditoría i18n (449 claves), seguridad `rel="noopener"`, erradicación de AOS y global-loader.</td>
              </tr>
              <tr class="bg-amber-50/40">
                <td class="text-center font-bold text-amber-900">PB13</td>
                <td class="font-semibold text-amber-950">Google Ads Local (Pauta Pagada)</td>
                <td class="text-center font-mono">Post-Proj</td>
                <td class="text-center"><span class="badge-pill bg-amber-100 text-amber-800">Pospuesto</span></td>
                <td class="text-amber-900">Dictamen formal emitido (<code class="tech-code">DOC-LA-MKT-2026-004</code>). Ahorro de $8,120 MXN netos para liquidez.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Detalle de la Culminación de PB5 -->
        <div class="bg-blue-50/70 border border-blue-200 rounded-lg p-2 text-[8px] text-blue-950">
          <div class="flex items-center justify-between mb-0.5">
            <span class="font-black text-[9px] uppercase tracking-wide text-blue-900">Hito Destacado: PB5 Micro-Landings & Conversión On-Site</span>
            <span class="badge-pill bg-blue-700 text-white font-mono">Módulos 1 al 5 Culminados</span>
          </div>
          <p class="leading-relaxed">
            Se transformó <code class="tech-code">services.html</code> en un motor de micro-landings con identificadores semánticos (<code class="tech-code">#ambiental</code>, <code class="tech-code">#construccion</code>, <code class="tech-code">#topografia</code>, <code class="tech-code">#seguridad-hidraulica</code>), 4 cabeceras de autoridad técnica, erradicación del 100% de Google Forms externos y auto-selección inteligente guiada con <em>smooth scroll</em> en <code class="tech-code">contact_faq.html?service=[slug]</code>.
          </p>
        </div>
      </div>
    </div>

    <!-- Footer Página 2 -->
    <footer class="border-t border-slate-200 pt-1.5 mt-1 flex items-center justify-between text-[8px] text-slate-400 shrink-0">
      <div class="flex items-center gap-2">
        <span class="font-bold text-slate-600 uppercase">Legado Ambiental S.A. de C.V.</span>
        <span>&bull;</span>
        <span>Evaluación de Cumplimiento &bull; Sprints 1 y 2</span>
      </div>
      <div class="flex items-center gap-3">
        <span>Uso Interno</span>
        <span class="font-bold text-slate-700 bg-slate-100 px-2 py-0.5 rounded">Página 2 de 5</span>
      </div>
    </footer>
  </div>

  <!-- ========================================== -->
  <!-- PÁGINA 3: ORIENTACIÓN CONCRETA: PB6 Y PB8   -->
  <!-- ========================================== -->
  <div class="page-container">
    <div>
      <!-- Header Superior Compacto -->
      <header class="flex items-center justify-between border-b border-slate-200 pb-2 mb-2 shrink-0">
        <div class="flex items-center gap-2">
          <img src="{logo_b64}" alt="Legado Ambiental" class="h-7 w-auto object-contain">
          <span class="text-[11px] font-black uppercase text-navy-900 tracking-tight">Informe de Estado: Plan de Trabajo y Avances</span>
        </div>
        <span class="text-[8px] font-mono text-slate-400">SECCIÓN 3: GUÍA TÉCNICA PB6 Y PLANTILLAS PB8</span>
      </header>

      <!-- Bloque PB6: Artículo Técnico Normativo -->
      <div class="mb-2.5">
        <div class="flex items-center justify-between mb-1">
          <div class="flex items-center gap-1.5">
            <div class="w-1.5 h-3 bg-brand-700 rounded-full"></div>
            <h3 class="text-[10px] font-black text-navy-900 uppercase tracking-wide">
              3. Orientación y Ejemplo de Ejecución: Tarea PB6 (Artículo Técnico)
            </h3>
          </div>
          <span class="badge-pill bg-slate-100 text-slate-700 font-mono">4.0 hrs &bull; Persona A & B</span>
        </div>

        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2 text-[8px] text-slate-700 leading-relaxed">
          <p class="mb-1">
            <strong class="text-slate-900">Título Propuesto:</strong> <em>“Guía de Cumplimiento Ambiental y Laboral en Obras Civiles en el Bajío: Evitando Clausuras de SEMARNAT y Sanciones de la STPS (2026)”</em>
          </p>
          <div class="grid grid-cols-2 gap-1.5 mb-1.5">
            <div class="bg-white border border-slate-200 rounded p-1.5">
              <span class="font-bold text-navy-900 block text-[8px]">&bull; Bloque 1: SEMARNAT / PROFEPA</span>
              <p class="text-[7.5px] text-slate-600">Trámite de Manifestación de Impacto Ambiental (MIA), autorizaciones de cambio de uso de suelo y clasificación de residuos peligrosos (NOM-052-SEMARNAT).</p>
            </div>
            <div class="bg-white border border-slate-200 rounded p-1.5">
              <span class="font-bold text-navy-900 block text-[8px]">&bull; Bloque 2: STPS y DRO</span>
              <p class="text-[7.5px] text-slate-600">Servicios preventivos en construcción (NOM-031), comisiones de seguridad (NOM-019), constancias DC-3 y firma de bitácora por Director Responsable de Obra.</p>
            </div>
          </div>
          <div class="bg-emerald-50 border border-emerald-200 rounded p-1.5 text-emerald-950 text-[7.5px]">
            <strong>CTA On-Site Integrado al Final:</strong> <em>“¿Tiene una inspección o trámite ambiental en puerta? Solicite un diagnóstico técnico preliminar sin costo con nuestro equipo colegiado.”</em> &rarr; Botones a <code class="tech-code">contact_faq.html?service=ambiental</code> y WhatsApp directo.
          </div>
        </div>
      </div>

      <!-- Bloque PB8: Las 3 Plantillas de Prospección B2B -->
      <div>
        <div class="flex items-center justify-between mb-1">
          <div class="flex items-center gap-1.5">
            <div class="w-1.5 h-3 bg-brand-700 rounded-full"></div>
            <h3 class="text-[10px] font-black text-navy-900 uppercase tracking-wide">
              4. Orientación y Textos Listos para Usar: Tarea PB8 (Plantillas B2B)
            </h3>
          </div>
          <span class="badge-pill bg-slate-100 text-slate-700 font-mono">3.0 hrs &bull; Persona A & B</span>
        </div>

        <div class="space-y-1.5">
          <!-- Plantilla 1 -->
          <div class="border border-slate-200 rounded-lg p-1.5 bg-white">
            <span class="text-[8px] font-black text-navy-900 uppercase block mb-0.5">
              Plantilla 1: Directores de Obra / Superintendentes (Enfoque: Bitácora DRO y Topografía 24-48h)
            </span>
            <pre class="code-block">Estimado/a [Nombre], observo el avance constructivo que lideran en [Empresa]. En etapas críticas de terracerías y cimentación, uno de los mayores dolores de cabeza para la superintendencia suele ser el retraso de brigadas topográficas o demoras en la firma de bitácoras DRO. En Legado Ambiental entregamos memorias topográficas GPS RTK y drones LiDAR con planos ejecutivos en 24 a 48h, con respaldo de Director Responsable de Obra colegiado. ¿Tendría 5 min esta semana para una llamada rápida? Portafolio: https://www.legadoambiental.com.mx/project_portfolio_gallery/portfolio.html</pre>
          </div>

          <!-- Plantilla 2 -->
          <div class="border border-slate-200 rounded-lg p-1.5 bg-white">
            <span class="text-[8px] font-black text-navy-900 uppercase block mb-0.5">
              Plantilla 2: Gerentes de Proyecto / Desarrolladores (Enfoque: Permisos Ambientales MIA y PTAR)
            </span>
            <pre class="code-block">Hola [Nombre], un gusto saludarte. En desarrollos industriales y residenciales en el Bajío, los tiempos de resolución ante dependencias ambientales (SEMARNAT, PROFEPA) son cuellos de botella críticos. En Legado Ambiental contamos con más de 10 años elaborando Manifestaciones de Impacto Ambiental (MIA), estudios de daño y proyectos ejecutivos de tratamiento de agua residual (PTAR) bajo la NOM-001 que aceleran la dictaminación sin observaciones costosas. ¿Tienen proyectos en fase de trámite normativo? División ambiental: https://www.legadoambiental.com.mx/services_overview/services.html#ambiental</pre>
          </div>

          <!-- Plantilla 3 -->
          <div class="border border-slate-200 rounded-lg p-1.5 bg-white">
            <span class="text-[8px] font-black text-navy-900 uppercase block mb-0.5">
              Plantilla 3: Responsables de Seguridad e Higiene / EHS (Enfoque: Auditorías STPS y Constancias DC-3)
            </span>
            <pre class="code-block">Estimado/a [Nombre], con la intensificación en las inspecciones laborales en centros de trabajo y obras, mantener expedientes STPS al 100% es indispensable. En Legado Ambiental somos Agentes Capacitadores Externos certificados ante la STPS. Capacitamos en sitio o híbrido, emitiendo constancias DC-3 con validez oficial, carpetas NOM-019/031 y planes de emergencia. ¿Tienen capacitaciones o auditorías programadas para este trimestre? Módulos STPS: https://www.legadoambiental.com.mx/services_overview/services.html#seguridad-hidraulica</pre>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer Página 3 -->
    <footer class="border-t border-slate-200 pt-1.5 mt-1 flex items-center justify-between text-[8px] text-slate-400 shrink-0">
      <div class="flex items-center gap-2">
        <span class="font-bold text-slate-600 uppercase">Legado Ambiental S.A. de C.V.</span>
        <span>&bull;</span>
        <span>Materiales de Venta B2B &bull; Sprint 2</span>
      </div>
      <div class="flex items-center gap-3">
        <span>Uso Interno</span>
        <span class="font-bold text-slate-700 bg-slate-100 px-2 py-0.5 rounded">Página 3 de 5</span>
      </div>
    </footer>
  </div>

  <!-- ========================================== -->
  <!-- PÁGINA 4: PB9, PB10 Y CAMPAÑA DE RESEÑAS    -->
  <!-- ========================================== -->
  <div class="page-container">
    <div>
      <!-- Header Superior Compacto -->
      <header class="flex items-center justify-between border-b border-slate-200 pb-2 mb-2 shrink-0">
        <div class="flex items-center gap-2">
          <img src="{logo_b64}" alt="Legado Ambiental" class="h-7 w-auto object-contain">
          <span class="text-[11px] font-black uppercase text-navy-900 tracking-tight">Informe de Estado: Plan de Trabajo y Avances</span>
        </div>
        <span class="text-[8px] font-mono text-slate-400">SECCIÓN 4: PROSPECCIÓN B2B Y RESEÑAS GBP</span>
      </header>

      <!-- Bloque PB9 y PB10: Prospección Activa y Alianzas -->
      <div class="mb-2.5">
        <div class="flex items-center justify-between mb-1">
          <div class="flex items-center gap-1.5">
            <div class="w-1.5 h-3 bg-brand-700 rounded-full"></div>
            <h3 class="text-[10px] font-black text-navy-900 uppercase tracking-wide">
              5. Orientación y Protocolo: Tareas PB9 y PB10 (Prospección y Alianzas)
            </h3>
          </div>
          <span class="badge-pill bg-slate-100 text-slate-700 font-mono">3.0 hrs &bull; Persona A & B</span>
        </div>

        <div class="grid grid-cols-2 gap-2 text-[8px]">
          <div class="bg-white border border-slate-200 rounded-lg p-2">
            <span class="font-black text-navy-900 block text-[8.5px] mb-0.5">&bull; PB9: 15 Prospectos Directos (LinkedIn Bajío)</span>
            <p class="text-slate-600 mb-1 leading-tight">
              <strong>Filtro:</strong> Directores de Obra, Gerentes de Proyecto y Residentes en Querétaro, San Juan del Río, Celaya y Edomex.
            </p>
            <p class="text-slate-600 leading-tight">
              <strong>Cadencia:</strong> <em>Día 1:</em> Conexión personalizada con contexto de su obra. <em>Día 3:</em> Envío de Plantilla 1, 2 o 3 con enlace a landing. <em>Día 7:</em> Mensaje de seguimiento compartiendo guía técnica.
            </p>
          </div>

          <div class="bg-white border border-slate-200 rounded-lg p-2">
            <span class="font-black text-navy-900 block text-[8.5px] mb-0.5">&bull; PB10: 5 Alianzas Estratégicas Clave</span>
            <p class="text-slate-600 mb-1 leading-tight">
              <strong>Aliados:</strong> 1) Laboratorios de Mecánica de Suelos, 2) Despachos de Cálculo Estructural, 3) Contratistas de Pavimentación, 4) Gestores de Licencias.
            </p>
            <p class="text-slate-600 leading-tight">
              <strong>Propuesta:</strong> Presentar a Legado Ambiental como su brazo técnico especializado para disciplinas no cubiertas, con reciprocidad o comisión por referencia.
            </p>
          </div>
        </div>
      </div>

      <!-- Bloque Campaña de Reseñas en Google Maps -->
      <div class="mb-2">
        <div class="flex items-center justify-between mb-1">
          <div class="flex items-center gap-1.5">
            <div class="w-1.5 h-3 bg-amber-600 rounded-full"></div>
            <h3 class="text-[10px] font-black text-amber-950 uppercase tracking-wide">
              6. Campaña Inmediata de Recolección de Reseñas en Google Maps
            </h3>
          </div>
          <span class="badge-pill bg-amber-100 text-amber-900 font-bold">Meta: 5 a 8 reseñas 5★</span>
        </div>

        <div class="bg-amber-50/70 border border-amber-300 rounded-lg p-2 text-[8px] text-amber-950 leading-relaxed mb-2">
          <p class="mb-1 text-slate-800">
            <strong>Objetivo Crítico:</strong> Blindar la prueba social antes de recibir prospectos en frío. Persona A contactará vía WhatsApp directo a los 10 principales clientes históricos y contratistas de confianza.
          </p>

          <!-- Script WhatsApp -->
          <div class="bg-white border border-amber-200 rounded p-1.5 mb-1.5">
            <span class="font-bold text-slate-900 block text-[8px] mb-0.5">Mensaje de WhatsApp para Clientes Históricos:</span>
            <pre class="code-block">Estimado/a [Nombre], le saluda con gusto [Nombre] de Legado Ambiental. Recordamos con agrado la colaboración con su equipo en [proyecto/servicio, ej. el levantamiento topográfico en San Juan del Río]. Actualmente estamos actualizando nuestro perfil oficial verificado en Google Maps. Para nuestro equipo sería un gran apoyo si pudiera regalarnos una breve reseña de 1 minuto sobre su experiencia:
👉 [ENLACE CORTO DE RESEÑAS DE GOOGLE MAPS / CÓDIGO QR]
¡Agradecemos mucho su confianza y apoyo de siempre!</pre>
          </div>

          <!-- Protocolo de Respuesta SEO -->
          <div class="bg-white border border-amber-200 rounded p-1.5 text-[7.5px] text-slate-700">
            <strong class="text-slate-900 block mb-0.5">Protocolo de Respuesta SEO (responder en menos de 24 horas):</strong>
            <em>“Muchas gracias por la confianza, Ing. [Apellido]. En Legado Ambiental nos alegra haber respaldado su proyecto de obra civil en Querétaro con la mayor precisión topográfica. ¡Seguimos a sus órdenes!”</em>
          </div>
        </div>
      </div>

      <!-- Banner de la Tarjeta QR -->
      <div class="bg-navy-900 text-white rounded-lg p-2 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <img src="{qr_b64}" alt="QR" class="w-8 h-8 rounded bg-white p-0.5 object-contain shrink-0">
          <div>
            <span class="text-[8.5px] font-bold text-emerald-400 block">Credencial y Tarjeta QR Lista para Recepción</span>
            <span class="text-[7.5px] text-slate-300">Generada en <code class="tech-code text-white bg-slate-800">tarjeta-qr-legadoambiental.html</code> para escaneo presencial de clientes.</span>
          </div>
        </div>
        <span class="badge-pill bg-emerald-600 text-white text-[7.5px]">Activo en Oficina</span>
      </div>
    </div>

    <!-- Footer Página 4 -->
    <footer class="border-t border-slate-200 pt-1.5 mt-1 flex items-center justify-between text-[8px] text-slate-400 shrink-0">
      <div class="flex items-center gap-2">
        <span class="font-bold text-slate-600 uppercase">Legado Ambiental S.A. de C.V.</span>
        <span>&bull;</span>
        <span>Activación Comercial y Reputación Local</span>
      </div>
      <div class="flex items-center gap-3">
        <span>Uso Interno</span>
        <span class="font-bold text-slate-700 bg-slate-100 px-2 py-0.5 rounded">Página 4 de 5</span>
      </div>
    </footer>
  </div>

  <!-- ========================================== -->
  <!-- PÁGINA 5: PLAN DE SIGUIENTES PASOS Y CIERRE-->
  <!-- ========================================== -->
  <div class="page-container">
    <div>
      <!-- Header Superior Compacto -->
      <header class="flex items-center justify-between border-b border-slate-200 pb-2 mb-2 shrink-0">
        <div class="flex items-center gap-2">
          <img src="{logo_b64}" alt="Legado Ambiental" class="h-7 w-auto object-contain">
          <span class="text-[11px] font-black uppercase text-navy-900 tracking-tight">Informe de Estado: Plan de Trabajo y Avances</span>
        </div>
        <span class="text-[8px] font-mono text-slate-400">SECCIÓN 5: CRONOGRAMA, DOD Y FORMALIZACIÓN</span>
      </header>

      <!-- Sección 7: Cronograma Día a Día de Cierre -->
      <div class="mb-2.5">
        <div class="flex items-center justify-between mb-1">
          <div class="flex items-center gap-1.5">
            <div class="w-1.5 h-3 bg-brand-700 rounded-full"></div>
            <h3 class="text-[10px] font-black text-navy-900 uppercase tracking-wide">
              7. Plan de Siguientes Pasos y Cronograma de Cierre (Día a Día)
            </h3>
          </div>
          <span class="badge-pill bg-emerald-700 text-white font-mono">11.5 hrs restantes para cierre</span>
        </div>

        <div class="overflow-hidden border border-slate-200 rounded-lg shadow-sm mb-2">
          <table class="w-full table-custom text-left border-collapse">
            <thead>
              <tr>
                <th class="w-[12%] text-center">Jornada</th>
                <th class="w-[12%] text-center">Tarea</th>
                <th class="w-[50%]">Actividad Concreta y Entregable</th>
                <th class="w-[16%] text-center">Responsable</th>
                <th class="w-[10%] text-center">Horas</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="text-center font-bold text-slate-900">Día 1</td>
                <td class="text-center font-mono font-bold text-brand-700">PB6</td>
                <td class="text-slate-700">Redacción y maquetación web de la guía técnica sobre normativas STPS/SEMARNAT con CTAs.</td>
                <td class="text-center text-[7.5px]">Persona A (2h) / B (2h)</td>
                <td class="text-center font-mono">4.0 h</td>
              </tr>
              <tr class="bg-slate-50/50">
                <td class="text-center font-bold text-slate-900">Día 2</td>
                <td class="text-center font-mono font-bold text-brand-700">PB8 + GBP</td>
                <td class="text-slate-700">Aprobación de 3 plantillas B2B, filtrado de 15 prospectos y solicitud de reseñas por WhatsApp.</td>
                <td class="text-center text-[7.5px]">Persona A (1h) / B (2h)</td>
                <td class="text-center font-mono">3.0 h</td>
              </tr>
              <tr>
                <td class="text-center font-bold text-slate-900">Día 3</td>
                <td class="text-center font-mono font-bold text-brand-700">PB9-10</td>
                <td class="text-slate-700">Envío de 15 prospectos en LinkedIn y contacto a 5 aliados estratégicos (laboratorios/calculistas).</td>
                <td class="text-center text-[7.5px]">Persona B (2.5h) / A (0.5h)</td>
                <td class="text-center font-mono">3.0 h</td>
              </tr>
              <tr class="bg-slate-50/50">
                <td class="text-center font-bold text-slate-900">Día 4</td>
                <td class="text-center font-mono font-bold text-brand-700">Cierre</td>
                <td class="text-slate-700">Verificación de conversiones en GA4, análisis de respuestas, Review Final y Cierre del Proyecto.</td>
                <td class="text-center text-[7.5px]">Persona A (0.5h) / B (1.0h)</td>
                <td class="text-center font-mono">1.5 h</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Sección 8: Definición de Terminado (DoD) -->
      <div class="mb-2.5">
        <div class="flex items-center gap-1.5 mb-1">
          <div class="w-1.5 h-3 bg-brand-700 rounded-full"></div>
          <h3 class="text-[10px] font-black text-navy-900 uppercase tracking-wide">
            8. Definición de Terminado (Definition of Done - DoD)
          </h3>
        </div>

        <div class="grid grid-cols-2 gap-2 text-[7.8px]">
          <div class="bg-emerald-50 border border-emerald-300 rounded p-1.5 text-emerald-950">
            <span class="font-bold block mb-0.5 text-emerald-900 text-[8px]">✓ Criterios Técnicos Cumplidos:</span>
            <ul class="space-y-0.5 list-disc list-inside">
              <li>Plataforma responsive, bilingüe y sin fugas externas (100%).</li>
              <li>Google Business Profile verificado con multimedia HD (100%).</li>
              <li>Medición GA4/GTM activa con 8 eventos B2B (100%).</li>
            </ul>
          </div>
          <div class="bg-amber-50 border border-amber-300 rounded p-1.5 text-amber-950">
            <span class="font-bold block mb-0.5 text-amber-900 text-[8px]">⏳ Criterios de Cierre por Completar:</span>
            <ul class="space-y-0.5 list-disc list-inside">
              <li>Guía técnica PB6 publicada con botones hacia cotización.</li>
              <li>15 prospectos contactados en frío y 5 aliados vinculados.</li>
              <li>Mínimo 5 reseñas 5★ registradas en Google Maps.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Sección 9: Formalización y Cuadro de Firmas -->
      <div class="border-t-2 border-slate-200 pt-2 mb-2">
        <div class="flex items-center justify-between mb-1">
          <div>
            <h3 class="text-[9.5px] font-black text-navy-900 uppercase tracking-wide">
              9. Formalización del Sprint Review y Compromiso de Cierre
            </h3>
            <p class="text-[7.5px] text-slate-500">Aprobación del estado técnico actual y validación del cronograma de 4 días.</p>
          </div>
          <span class="text-[7.5px] font-mono font-bold text-slate-600">OCTUBRE 2026</span>
        </div>

        <div class="grid grid-cols-3 gap-2.5 pt-2">
          <div class="border-t border-slate-400 pt-1 text-center">
            <p class="text-[7.5px] font-bold text-slate-800 uppercase">Persona A</p>
            <p class="text-[6.5px] text-slate-500">Estratega Técnico / Dirección Comercial</p>
            <p class="text-[6.5px] font-mono text-slate-400 mt-2">FIRMA / FECHA</p>
          </div>

          <div class="border-t border-slate-400 pt-1 text-center">
            <p class="text-[7.5px] font-bold text-slate-800 uppercase">Persona B</p>
            <p class="text-[6.5px] text-slate-500">Desarrollador / Operador Digital</p>
            <p class="text-[6.5px] font-mono text-slate-400 mt-2">FIRMA / FECHA</p>
          </div>

          <div class="border-t border-slate-400 pt-1 text-center">
            <p class="text-[7.5px] font-bold text-emerald-900 uppercase">Dirección General</p>
            <p class="text-[6.5px] text-slate-500">Aprobación Final Corporativa</p>
            <p class="text-[6.5px] font-mono text-slate-400 mt-2">FIRMA / FECHA</p>
          </div>
        </div>
      </div>

      <!-- Tarjeta Institucional de Pie -->
      <div class="bg-navy-950 text-white rounded-lg p-1.5 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <img src="{qr_b64}" alt="QR Web Legado" class="w-7 h-7 rounded bg-white p-0.5 object-contain shrink-0">
          <div>
            <p class="text-[8px] font-bold uppercase tracking-wide text-emerald-400">Legado Ambiental S.A. de C.V.</p>
            <p class="text-[7px] text-slate-300">San Juan del Río, Qro. &bull; Cobertura Bajío y Nacional &bull; https://legadoambiental.com.mx</p>
          </div>
        </div>
        <div class="text-right">
          <span class="text-[7px] font-bold uppercase text-slate-400 block">Certificación de Estado</span>
          <span class="text-[7.5px] font-extrabold text-white">Plan 100 Leads B2B &bull; 2026</span>
        </div>
      </div>
    </div>

    <!-- Footer Página 5 -->
    <footer class="border-t border-slate-200 pt-1.5 mt-1 flex items-center justify-between text-[8px] text-slate-400 shrink-0">
      <div class="flex items-center gap-2">
        <span class="font-bold text-slate-600 uppercase">Legado Ambiental S.A. de C.V.</span>
        <span>&bull;</span>
        <span>Documento Oficial de Cierre &bull; Hoja de Ruta B2B</span>
      </div>
      <div class="flex items-center gap-3">
        <span>Uso Interno</span>
        <span class="font-bold text-slate-700 bg-slate-100 px-2 py-0.5 rounded">Página 5 de 5</span>
      </div>
    </footer>
  </div>

</body>
</html>
"""

# Write HTML file
html_path = 'assets/docs/Informe_Ejecutivo_Plan_Trabajo_y_Avances_2026.html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"HTML updated successfully: {html_path}")

# Run headless Chrome to generate PDF for Informe Ejecutivo
pdf_path_1 = 'assets/docs/Informe_Ejecutivo_Plan_Trabajo_y_Avances_2026.pdf'
cmd_1 = [
    'google-chrome',
    '--headless',
    '--disable-gpu',
    '--no-pdf-header-footer',
    '--virtual-time-budget=5000',
    '--run-all-compositor-stages-before-draw',
    f'--print-to-pdf={pdf_path_1}',
    html_path
]

print("Generating primary PDF:", pdf_path_1)
res_1 = subprocess.run(cmd_1, capture_output=True, text=True)
print("Return code 1:", res_1.returncode)

if os.path.exists(pdf_path_1):
    size_kb = os.path.getsize(pdf_path_1) / 1024
    print(f"SUCCESS: Primary PDF created at {pdf_path_1} ({size_kb:.1f} KB)")
else:
    print("ERROR: Primary PDF was not created!")

# Also generate Sprint Review specific PDF name for clear access
pdf_path_2 = 'assets/docs/Sprint_Review_y_Plan_Accion_Octubre_2026.pdf'
cmd_2 = [
    'google-chrome',
    '--headless',
    '--disable-gpu',
    '--no-pdf-header-footer',
    '--virtual-time-budget=5000',
    '--run-all-compositor-stages-before-draw',
    f'--print-to-pdf={pdf_path_2}',
    html_path
]

print("Generating Sprint Review PDF:", pdf_path_2)
res_2 = subprocess.run(cmd_2, capture_output=True, text=True)
print("Return code 2:", res_2.returncode)

if os.path.exists(pdf_path_2):
    size_kb = os.path.getsize(pdf_path_2) / 1024
    print(f"SUCCESS: Sprint Review PDF created at {pdf_path_2} ({size_kb:.1f} KB)")
else:
    print("ERROR: Sprint Review PDF was not created!")
