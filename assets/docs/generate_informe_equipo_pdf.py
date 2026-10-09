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
  <title>Informe Ejecutivo de Estado: Plan de Trabajo y Avances 2026 - Legado Ambiental</title>
  
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
      margin: 10mm auto;
      background: white;
      padding: 10mm 13mm;
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
        padding: 10mm 13mm;
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
      font-size: 9.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 6.5px 8px;
    }}
    .table-custom td {{
      font-size: 9px;
      padding: 6px 8px;
      border-bottom: 1px solid #e2e8f0;
      vertical-align: middle;
    }}
    .badge-pill {{
      display: inline-flex;
      align-items: center;
      padding: 2px 7px;
      border-radius: 9999px;
      font-size: 8.5px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    code.tech-code {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 8.5px;
      background-color: #f1f5f9;
      color: #0f172a;
      padding: 1px 4px;
      border-radius: 4px;
      border: 1px solid #e2e8f0;
    }}
  </style>
</head>
<body class="text-charcoal font-sans antialiased">

  <!-- ========================================== -->
  <!-- PÁGINA 1: PORTADA & ESTADO GENERAL         -->
  <!-- ========================================== -->
  <div class="page-container">
    <div>
      <!-- Header Superior -->
      <header class="flex items-center justify-between border-b-2 border-slate-200 pb-2.5 mb-3 shrink-0">
        <div class="flex items-center gap-3">
          <img src="{logo_b64}" alt="Legado Ambiental" class="h-11 w-auto object-contain">
          <div>
            <h1 class="text-navy-900 font-black text-lg tracking-tight leading-none uppercase">Legado Ambiental</h1>
            <p class="text-[9.5px] font-semibold text-brand-700 tracking-wide mt-0.5">Topografía de Precisión &bull; Infraestructura Hidráulica &bull; Obra Civil</p>
          </div>
        </div>
        <div class="text-right">
          <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 bg-emerald-50 border border-emerald-300 rounded text-emerald-900 text-[9.5px] font-bold">
            <span class="w-2 h-2 rounded-full bg-emerald-600 animate-pulse"></span>
            COMUNICACIÓN INTERNA DE EQUIPO
          </div>
          <p class="text-[8.5px] font-mono text-slate-400 mt-0.5">CÓDIGO: INF-LA-DIR-2026-005 | OCT 2026</p>
        </div>
      </header>

      <!-- Banner de Título Principal -->
      <div class="bg-gradient-to-r from-navy-950 via-navy-900 to-slate-900 rounded-xl p-3.5 text-white shadow-md mb-3 border-l-4 border-emerald-500">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[8.5px] font-extrabold tracking-widest text-emerald-400 uppercase bg-emerald-950/80 px-2 py-0.5 rounded border border-emerald-500/30">
              Gestión Estratégica &bull; Sprints 1 & 2 &bull; 100 Leads B2B
            </span>
            <h2 class="text-lg font-black tracking-tight text-white mt-1 leading-tight">
              Informe Ejecutivo de Estado: Plan de Trabajo y Avances Técnicos
            </h2>
            <p class="text-[11px] text-slate-300 mt-1 max-w-xl font-normal leading-relaxed">
              Consolidación de resultados para la Dirección y Equipo de Proyecto: Culminación de Fases UI/UX, Verificación de Google Business Profile, Medición GA4/GTM y Dictamen de Suspensión Temporal de Google Ads.
            </p>
          </div>
          <div class="bg-emerald-500/10 border border-emerald-500/30 rounded-lg p-2 text-center shrink-0 ml-3">
            <span class="text-[8px] font-bold text-emerald-300 uppercase block">Estatus General</span>
            <span class="text-lg font-black text-emerald-400 block">HITOS 100%</span>
            <span class="text-[7.5px] text-slate-300 font-mono">Infraestructura Lista</span>
          </div>
        </div>
      </div>

      <!-- Resumen Ejecutivo de Estado -->
      <div class="bg-emerald-50 border-2 border-emerald-600 rounded-xl p-3 mb-3 shadow-sm">
        <div class="flex items-center justify-between mb-1">
          <div class="flex items-center gap-1.5">
            <span class="flex h-4 w-4 items-center justify-center rounded-full bg-emerald-600 text-white font-bold text-[10px]">✓</span>
            <h3 class="text-[11px] font-black uppercase tracking-wider text-emerald-950">
              Resolución de Estado para el Equipo
            </h3>
          </div>
          <span class="badge-pill bg-emerald-700 text-white font-extrabold text-[8.5px]">
            FASE DE CONVERSIÓN CONCLUIDA
          </span>
        </div>
        <p class="text-[10px] text-emerald-900 font-medium leading-relaxed">
          Los <strong>cimientos técnicos y de conversión comercial de Legado Ambiental se encuentran completados con éxito</strong>. El sitio web se ha transformado en un embudo B2B de ultra-baja fricción con paridad bilingüe, Google Business Profile está formalmente <strong>verificado con catálogo HD y video 3D</strong>, y el flujo de analítica con GTM/GA4 se encuentra activo. Respecto a Google Ads, se determinó por dictamen <strong>congelar su adopción</strong> para cuidar el flujo de caja corporativo y concentrar la energía del equipo en la captación orgánica y prospección directa.
        </p>
      </div>

      <!-- Grid 4 Tarjetas de Resumen de Hitos -->
      <div class="grid grid-cols-4 gap-2 mb-3">
        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
          <div class="flex items-center justify-between mb-0.5">
            <span class="text-[8px] font-bold text-slate-500 uppercase tracking-wider">Web UI/UX & CRO</span>
            <span class="text-emerald-600 font-black text-[10px]">100%</span>
          </div>
          <span class="text-[11px] font-black text-slate-900 block">Fases 1 a 5 Listas</span>
          <p class="text-[8px] text-slate-600 mt-0.5 leading-tight">Mobile-first, Formulario 6 campos, Sticky Bar + FAB WhatsApp, paridad i18n.</p>
        </div>

        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
          <div class="flex items-center justify-between mb-0.5">
            <span class="text-[8px] font-bold text-slate-500 uppercase tracking-wider">Pilar 5: SEO Local</span>
            <span class="text-emerald-600 font-black text-[10px]">100%</span>
          </div>
          <span class="text-[11px] font-black text-slate-900 block">GBP Verificado</span>
          <p class="text-[8px] text-slate-600 mt-0.5 leading-tight">199+ interacciones, 11 fotos HD (1200x896), video 3D demo y suite QR.</p>
        </div>

        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
          <div class="flex items-center justify-between mb-0.5">
            <span class="text-[8px] font-bold text-slate-500 uppercase tracking-wider">Analítica Digital</span>
            <span class="text-emerald-600 font-black text-[10px]">100%</span>
          </div>
          <span class="text-[11px] font-black text-slate-900 block">GTM & GA4 Activo</span>
          <p class="text-[8px] text-slate-600 mt-0.5 leading-tight">ID G-1MLGHB4E6G en 8 páginas, CSP actualizado y 8 eventos de conversión B2B.</p>
        </div>

        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
          <div class="flex items-center justify-between mb-0.5">
            <span class="text-[8px] font-bold text-slate-500 uppercase tracking-wider">Pilar 6: Pauta Ads</span>
            <span class="text-amber-600 font-black text-[10px]">POSPUESTO</span>
          </div>
          <span class="text-[11px] font-black text-slate-900 block">Google Ads Detenido</span>
          <p class="text-[8px] text-slate-600 mt-0.5 leading-tight">Ahorro de $8,120 MXN; enfoque en prospección orgánica a costo marginal $0.</p>
        </div>
      </div>

      <!-- Sección 1: Análisis del Plan de Trabajo Original -->
      <div>
        <div class="flex items-center gap-2 mb-1.5">
          <div class="w-1.5 h-3.5 bg-brand-700 rounded-full"></div>
          <h3 class="text-[11px] font-black text-navy-900 uppercase tracking-wide">
            1. Antecedentes y Alcance del Plan Original de Trabajo
          </h3>
        </div>

        <p class="text-[9.5px] text-slate-600 leading-relaxed mb-2">
          El plan de trabajo formulado en los documentos <em>"Plan de Trabajo y Arquitectura UI/UX"</em> y <em>"plan-mejoras-uiux-100.md"</em> estableció como propósito transformar el sitio web corporativo de un catálogo estático a un embudo automatizado de captación para los <strong>Primeros 100 Leads B2B</strong>.
        </p>

        <div class="grid grid-cols-2 gap-2 text-[9px]">
          <div class="bg-white border border-slate-200 rounded-lg p-2">
            <h4 class="font-bold text-slate-900 text-[9.5px] mb-1 flex items-center gap-1.5">
              <span class="text-brand-700 font-black">&bull;</span> Capacidad y Recursos Asignados
            </h4>
            <p class="text-slate-600 leading-snug text-[8.5px]">
              Proyecto delimitado a <strong>2 semanas (10 días hábiles)</strong> con capacidad de <strong>40 horas efectivas</strong> entre <strong>Persona A</strong> (Estratega Técnico - 10 hrs) y <strong>Persona B</strong> (Desarrollador - 30 hrs), optimizado respecto al backlog inicial de 70 horas.
            </p>
          </div>

          <div class="bg-white border border-slate-200 rounded-lg p-2">
            <h4 class="font-bold text-slate-900 text-[9.5px] mb-1 flex items-center gap-1.5">
              <span class="text-brand-700 font-black">&bull;</span> Filosofía de Ejecución y Calidad
            </h4>
            <p class="text-slate-600 leading-snug text-[8.5px]">
              Adopción estricta de la <strong>Regla de Oro de Internacionalización</strong> (cero textos quemados en HTML; paridad 1:1 en <code class="tech-code">i18n.js</code>), puntos de control Git por fase y diseño orientado a toma de decisiones B2B de alto valor.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer Página 1 -->
    <footer class="border-t border-slate-200 pt-2 mt-2 flex items-center justify-between text-[8.5px] text-slate-400 shrink-0">
      <div class="flex items-center gap-2">
        <span class="font-bold text-slate-600 uppercase">Legado Ambiental S.A. de C.V.</span>
        <span>&bull;</span>
        <span>Informe de Estado de Proyecto &bull; Plan 100 Leads</span>
      </div>
      <div class="flex items-center gap-4">
        <span>Uso Interno</span>
        <span class="font-bold text-slate-700 bg-slate-100 px-2 py-0.5 rounded">Página 1 de 4</span>
      </div>
    </footer>
  </div>

  <!-- ========================================== -->
  <!-- PÁGINA 2: MATRIZ DE CUMPLIMIENTO BACKLOG   -->
  <!-- ========================================== -->
  <div class="page-container">
    <div>
      <!-- Header Superior Compacto -->
      <header class="flex items-center justify-between border-b border-slate-200 pb-2.5 mb-3 shrink-0">
        <div class="flex items-center gap-2">
          <img src="{logo_b64}" alt="Legado Ambiental" class="h-8 w-auto object-contain">
          <span class="text-xs font-black uppercase text-navy-900 tracking-tight">Informe de Estado: Plan de Trabajo y Avances</span>
        </div>
        <span class="text-[9px] font-mono text-slate-400">SECCIÓN 2: MATRIZ DE CUMPLIMIENTO DEL BACKLOG</span>
      </header>

      <!-- Sección 2: Matriz Comparativa del Backlog -->
      <div class="mb-3.5">
        <div class="flex items-center gap-2 mb-1.5">
          <div class="w-1.5 h-3.5 bg-brand-700 rounded-full"></div>
          <h3 class="text-xs font-black text-navy-900 uppercase tracking-wide">
            2. Matriz de Cumplimiento: Tareas Planificadas vs. Entregables en Producción
          </h3>
        </div>

        <p class="text-[9px] text-slate-600 mb-2 leading-relaxed">
          Contraste detallado de las Historias de Usuario contempladas en el plan de 40 horas efectivas contra los artefactos técnicos validados en el repositorio:
        </p>

        <!-- Tabla del Backlog -->
        <div class="overflow-hidden border border-slate-200 rounded-lg shadow-sm mb-2.5">
          <table class="w-full table-custom text-left border-collapse">
            <thead>
              <tr>
                <th class="w-[8%] text-center">ID</th>
                <th class="w-[28%]">Historia / Tarea Original</th>
                <th class="w-[9%] text-center">Horas</th>
                <th class="w-[18%] text-center">Estado Real</th>
                <th class="w-[37%]">Entregables y Evidencia Técnica</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="text-center font-bold text-slate-900">PB1</td>
                <td class="font-semibold text-slate-900">Rediseño Hero Section JTBD</td>
                <td class="text-center font-mono">3.0 h</td>
                <td class="text-center"><span class="badge-pill bg-emerald-100 text-emerald-800">100% Concluido</span></td>
                <td class="text-slate-600">Copys JTBD en <code class="tech-code">home.html</code>, trust banner con normativas (NOM-052, STPS) y paridad i18n.</td>
              </tr>
              <tr class="bg-slate-50/50">
                <td class="text-center font-bold text-slate-900">PB2</td>
                <td class="font-semibold text-slate-900">CTAs Estratégicos & Contacto</td>
                <td class="text-center font-mono">3.0 h</td>
                <td class="text-center"><span class="badge-pill bg-emerald-100 text-emerald-800">100% Concluido</span></td>
                <td class="text-slate-600">Botones "Cotizar", "WhatsApp" y "Ver Portafolio"; Sticky Bar + FAB WhatsApp en móvil.</td>
              </tr>
              <tr>
                <td class="text-center font-bold text-slate-900">PB3</td>
                <td class="font-semibold text-slate-900">Simplificación Formularios (6 Campos)</td>
                <td class="text-center font-mono">3.0 h</td>
                <td class="text-center"><span class="badge-pill bg-emerald-100 text-emerald-800">100% Concluido</span></td>
                <td class="text-slate-600">Formulario ultra-simplificado en <code class="tech-code">contact_faq.html</code>, Honeypot anti-spam y notificaciones Toast.</td>
              </tr>
              <tr class="bg-slate-50/50">
                <td class="text-center font-bold text-slate-900">PB4</td>
                <td class="font-semibold text-slate-900">Google Business Profile (SEO Local)</td>
                <td class="text-center font-mono">3.0 h</td>
                <td class="text-center"><span class="badge-pill bg-emerald-100 text-emerald-800">100% Concluido</span></td>
                <td class="text-slate-600">Ficha verificada con badge oficial, 11 imágenes HD (1200x896), video demo 3D y suite QR.</td>
              </tr>
              <tr>
                <td class="text-center font-bold text-slate-900">PB7</td>
                <td class="font-semibold text-slate-900">Optimización Portafolio PDF & QR</td>
                <td class="text-center font-mono">3.0 h</td>
                <td class="text-center"><span class="badge-pill bg-emerald-100 text-emerald-800">100% Concluido</span></td>
                <td class="text-slate-600">Portafolio integrado, suite QR en vector SVG y tarjeta de mostrador lista para recepción.</td>
              </tr>
              <tr class="bg-slate-50/50">
                <td class="text-center font-bold text-slate-900">PB12</td>
                <td class="font-semibold text-slate-900">Analíticas Digitales (GA4 & GTM)</td>
                <td class="text-center font-mono">3.0 h</td>
                <td class="text-center"><span class="badge-pill bg-emerald-100 text-emerald-800">100% Concluido</span></td>
                <td class="text-slate-600">Tag <code class="tech-code">G-1MLGHB4E6G</code> en 8 páginas, <code class="tech-code">analytics.js</code> con 8 eventos B2B, CSP y dataLayer activo.</td>
              </tr>
              <tr class="bg-amber-50/60">
                <td class="text-center font-bold text-amber-900">PB13</td>
                <td class="font-semibold text-amber-950">Google Ads Local (Pauta Pagada)</td>
                <td class="text-center font-mono">Post-Proj</td>
                <td class="text-center"><span class="badge-pill bg-amber-100 text-amber-800">Pospuesto</span></td>
                <td class="text-amber-900">Dictamen técnico emitido (<code class="tech-code">DOC-LA-MKT-2026-004</code>). Detenido para priorizar captación orgánica.</td>
              </tr>
              <tr>
                <td class="text-center font-bold text-slate-900">PB5</td>
                <td class="font-semibold text-slate-900">Landings de Servicios Específicos</td>
                <td class="text-center font-mono">6.0 h</td>
                <td class="text-center"><span class="badge-pill bg-blue-100 text-blue-800">En Curso</span></td>
                <td class="text-slate-600">Servicios concentrados y funcionales en <code class="tech-code">services.html</code> mediante pestañas adaptativas.</td>
              </tr>
              <tr class="bg-slate-50/50">
                <td class="text-center font-bold text-slate-900">PB6</td>
                <td class="font-semibold text-slate-900">Artículo Técnico Normativo</td>
                <td class="text-center font-mono">4.0 h</td>
                <td class="text-center"><span class="badge-pill bg-slate-100 text-slate-700">Sprint 2</span></td>
                <td class="text-slate-600">Normativas referenciadas en Hero; pendiente artículo editorial extendido para prospección.</td>
              </tr>
              <tr>
                <td class="text-center font-bold text-slate-900">PB8-10</td>
                <td class="font-semibold text-slate-900">Prospección Directa B2B & Alianzas</td>
                <td class="text-center font-mono">6.0 h</td>
                <td class="text-center"><span class="badge-pill bg-slate-100 text-slate-700">Próxima Fase</span></td>
                <td class="text-slate-600">Infraestructura 100% lista para recibir contactos comerciales y canalizarlos a WhatsApp/Form.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Síntesis de Eficiencia -->
        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2.5 flex items-center justify-between">
          <div class="text-[9px] text-slate-600">
            <strong class="text-slate-900">Balance de Capacidad:</strong> Los 6 hitos fundacionales (PB1, PB2, PB3, PB4, PB7, PB12) se ejecutaron con una eficiencia del 100% dentro del presupuesto horario planificado.
          </div>
          <span class="badge-pill bg-navy-900 text-white font-mono text-[9px]">21.0 hrs ejecutadas</span>
        </div>
      </div>
    </div>

    <!-- Footer Página 2 -->
    <footer class="border-t border-slate-200 pt-2 mt-2 flex items-center justify-between text-[8.5px] text-slate-400 shrink-0">
      <div class="flex items-center gap-2">
        <span class="font-bold text-slate-600 uppercase">Legado Ambiental S.A. de C.V.</span>
        <span>&bull;</span>
        <span>Evaluación de Cumplimiento &bull; Sprints Ágiles</span>
      </div>
      <div class="flex items-center gap-4">
        <span>Uso Interno</span>
        <span class="font-bold text-slate-700 bg-slate-100 px-2 py-0.5 rounded">Página 2 de 4</span>
      </div>
    </footer>
  </div>

  <!-- ========================================== -->
  <!-- PÁGINA 3: DETALLE DE HITOS CLAVE           -->
  <!-- ========================================== -->
  <div class="page-container">
    <div>
      <!-- Header Superior Compacto -->
      <header class="flex items-center justify-between border-b border-slate-200 pb-2.5 mb-3 shrink-0">
        <div class="flex items-center gap-2">
          <img src="{logo_b64}" alt="Legado Ambiental" class="h-8 w-auto object-contain">
          <span class="text-xs font-black uppercase text-navy-900 tracking-tight">Informe de Estado: Plan de Trabajo y Avances</span>
        </div>
        <span class="text-[9px] font-mono text-slate-400">SECCIÓN 3: DETALLE DE HITOS TÉCNICOS LOGRADOS</span>
      </header>

      <!-- Sección 3: Detalle de Hitos -->
      <div class="mb-3">
        <div class="flex items-center gap-2 mb-1.5">
          <div class="w-1.5 h-3.5 bg-brand-700 rounded-full"></div>
          <h3 class="text-xs font-black text-navy-900 uppercase tracking-wide">
            3. Radiografía de Logros: Plataforma Web, Google Business Profile y Analítica
          </h3>
        </div>

        <div class="space-y-2 text-[9.5px]">
          <!-- Hito 1: Web UI/UX -->
          <div class="bg-white border border-slate-200 rounded-lg p-2.5">
            <div class="flex items-center justify-between mb-1">
              <h4 class="font-black text-slate-900 text-[10px] flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-emerald-600"></span> Hito 1: Optimización Web, CRO e Internacionalización
              </h4>
              <span class="badge-pill bg-emerald-100 text-emerald-800">PRODUCCIÓN LISTA</span>
            </div>
            <p class="text-slate-600 text-[8.5px] leading-relaxed mb-1">
              Se superaron las 5 fases técnicas con cero desbordamiento horizontal en 320px. Se implementó el <strong>Patrón Híbrido B2B</strong> que combina una Sticky Mobile CTA Bar fija a pantalla completa (*"Cotizar Proyecto"*) con un botón flotante FAB para WhatsApp, reduciendo la fricción a solo 6 campos con Honeypot anti-spam. La plataforma cuenta con paridad estricta 1:1 en <code class="tech-code">i18n.js</code> entre Español e Inglés.
            </p>
            <div class="flex items-center gap-2 text-[8px] font-mono text-slate-500 bg-slate-50 p-1 rounded">
              <span>Touch Targets: &ge; 48px</span> &bull; 
              <span>Zero-FOUC Tema Oscuro</span> &bull; 
              <span>Schema.org: ConstructionBusiness</span> &bull; 
              <span>Redirect 301 Limpio</span>
            </div>
          </div>

          <!-- Hito 2: GBP SEO Local -->
          <div class="bg-white border border-slate-200 rounded-lg p-2.5">
            <div class="flex items-center justify-between mb-1">
              <h4 class="font-black text-slate-900 text-[10px] flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-emerald-600"></span> Hito 2: Google Business Profile (Pilar 5: SEO Local Concluido)
              </h4>
              <span class="badge-pill bg-emerald-100 text-emerald-800">FICHA VERIFICADA</span>
            </div>
            <p class="text-slate-600 text-[8.5px] leading-relaxed mb-1">
              La ficha de Legado Ambiental se encuentra formalmente verificada por Google, con el panel de administración operativo y <strong>más de 199 interacciones registradas</strong>. Se remasterizaron <strong>11 imágenes a 1200x896 px (proporción óptima 4:3)</strong> para Topografía, Construcción e Infraestructura Hidráulica, y se produjo la pieza de <strong>Modelado 3D / Volumetría</strong> con carátula HD y video demo remasterizado de 20 segundos.
            </p>
            <div class="grid grid-cols-3 gap-1.5 text-[8px] text-slate-600 bg-slate-50 p-1 rounded">
              <div>&bull; <strong>11 Fotos HD:</strong> Optimizadas a proporción 4:3</div>
              <div>&bull; <strong>Video Demo 3D:</strong> Curvas y volumetría</div>
              <div>&bull; <strong>Suite QR:</strong> Tarjeta de mostrador lista</div>
            </div>
          </div>

          <!-- Hito 3: GA4 y GTM -->
          <div class="bg-white border border-slate-200 rounded-lg p-2.5">
            <div class="flex items-center justify-between mb-1">
              <h4 class="font-black text-slate-900 text-[10px] flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-emerald-600"></span> Hito 3: Medición y Analítica Digital (GA4 y GTM Concluidos)
              </h4>
              <span class="badge-pill bg-emerald-100 text-emerald-800">TELEMETRÍA EN VIVO</span>
            </div>
            <p class="text-slate-600 text-[8.5px] leading-relaxed mb-1">
              Se implementó el contenedor Google Tag Manager y Google Analytics con ID <strong>G-1MLGHB4E6G</strong> en las 8 páginas HTML del sitio web. Se actualizaron los encabezados CSP para habilitar la telemetría sin advertencias de seguridad y se programaron 8 eventos de conversión en <code class="tech-code">assets/js/analytics.js</code> para registrar el embudo de ventas B2B.
            </p>
            <div class="flex items-center justify-between text-[8px] font-mono text-emerald-900 bg-emerald-50/70 p-1 rounded border border-emerald-200">
              <span>Eventos: form_start &bull; select_service &bull; generate_lead &bull; click_whatsapp &bull; click_phone &bull; scroll_depth</span>
            </div>
          </div>

          <!-- Módulo Adicional: Embudo de Conversión Activo -->
          <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
            <span class="text-[8.5px] font-extrabold uppercase text-slate-600 tracking-wider block mb-1">Flujo del Embudo B2B Activo en Producción</span>
            <div class="grid grid-cols-4 gap-1.5 text-center text-[8px]">
              <div class="bg-white p-1 rounded border border-slate-200">
                <span class="font-bold text-slate-800 block">1. Atracción Local</span>
                <span class="text-slate-500">Google Maps / SEO</span>
              </div>
              <div class="bg-white p-1 rounded border border-slate-200">
                <span class="font-bold text-slate-800 block">2. Interés JTBD</span>
                <span class="text-slate-500">Servicios / Normativas</span>
              </div>
              <div class="bg-white p-1 rounded border border-slate-200">
                <span class="font-bold text-slate-800 block">3. Conversión</span>
                <span class="text-slate-500">Form 6 / WhatsApp</span>
              </div>
              <div class="bg-emerald-50 p-1 rounded border border-emerald-300">
                <span class="font-bold text-emerald-900 block">4. Lead Calificado</span>
                <span class="text-emerald-700">Cotización B2B</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer Página 3 -->
    <footer class="border-t border-slate-200 pt-2 mt-2 flex items-center justify-between text-[8.5px] text-slate-400 shrink-0">
      <div class="flex items-center gap-2">
        <span class="font-bold text-slate-600 uppercase">Legado Ambiental S.A. de C.V.</span>
        <span>&bull;</span>
        <span>Evidencia de Entregables Técnicos &bull; Pilar 1 a 5</span>
      </div>
      <div class="flex items-center gap-4">
        <span>Uso Interno</span>
        <span class="font-bold text-slate-700 bg-slate-100 px-2 py-0.5 rounded">Página 3 de 4</span>
      </div>
    </footer>
  </div>

  <!-- ========================================== -->
  <!-- PÁGINA 4: DECISIÓN ADS & PRÓXIMOS PASOS    -->
  <!-- ========================================== -->
  <div class="page-container">
    <div>
      <!-- Header Superior Compacto -->
      <header class="flex items-center justify-between border-b border-slate-200 pb-2.5 mb-3 shrink-0">
        <div class="flex items-center gap-2">
          <img src="{logo_b64}" alt="Legado Ambiental" class="h-8 w-auto object-contain">
          <span class="text-xs font-black uppercase text-navy-900 tracking-tight">Informe de Estado: Plan de Trabajo y Avances</span>
        </div>
        <span class="text-[9px] font-mono text-slate-400">SECCIÓN 4 & 5: DECISIÓN ADS Y HOJA DE RUTA B2B</span>
      </header>

      <!-- Sección 4: Dictamen Google Ads -->
      <div class="mb-3">
        <div class="flex items-center gap-2 mb-1.5">
          <div class="w-1.5 h-3.5 bg-amber-600 rounded-full"></div>
          <h3 class="text-xs font-black text-amber-950 uppercase tracking-wide">
            4. Dictamen Financiero: Suspensión Temporal de Google Ads (Pilar 6)
          </h3>
        </div>

        <div class="bg-amber-50/70 border border-amber-300 rounded-lg p-2.5 text-[8.5px] text-amber-950 leading-relaxed">
          <div class="flex items-center justify-between mb-1">
            <span class="font-black text-[9.5px]">Decisión Corporativa: NO activar el cupón de $7,000 MXN en esta etapa</span>
            <span class="badge-pill bg-amber-200 text-amber-900 font-bold">Ahorro Inmediato: $8,120 MXN</span>
          </div>
          <p class="text-slate-700">
            <strong>Racionalidad Financiera y Eficiencia de Capital:</strong> La oferta requiere un gasto previo de $7,000 MXN + IVA en 60 días. Activar la pauta con una ficha de Maps recién creada reduciría la conversión por falta de reseñas previas y expondría a la empresa al riesgo de cobro automático recurrente al agotarse el crédito. Se aprueba reasignar los esfuerzos hacia la <strong>captación orgánica a costo $0</strong>.
          </p>
        </div>
      </div>

      <!-- Sección 5: Hoja de Ruta para los Primeros 100 Leads -->
      <div class="mb-3">
        <div class="flex items-center gap-2 mb-1.5">
          <div class="w-1.5 h-3.5 bg-brand-700 rounded-full"></div>
          <h3 class="text-xs font-black text-navy-900 uppercase tracking-wide">
            5. Hoja de Ruta Inmediata: Captación de los Primeros 100 Leads B2B
          </h3>
        </div>

        <div class="grid grid-cols-3 gap-2 text-[8.5px]">
          <div class="bg-white border border-slate-200 rounded-lg p-2 flex flex-col justify-between">
            <div>
              <span class="font-black text-slate-900 block text-[9.5px] mb-0.5">Paso 1: Reseñas en Maps</span>
              <p class="text-slate-600 leading-tight text-[8px] mb-1">
                Recolección de 5 a 10 reseñas verificadas de 5★ con clientes actuales usando la credencial QR para blindar prueba social.
              </p>
            </div>
            <span class="badge-pill bg-emerald-50 text-emerald-800 text-[7.5px] text-center block">Semana 1 &bull; Persona A</span>
          </div>

          <div class="bg-white border border-slate-200 rounded-lg p-2 flex flex-col justify-between">
            <div>
              <span class="font-black text-slate-900 block text-[9.5px] mb-0.5">Paso 2: Contenido Normativo</span>
              <p class="text-slate-600 leading-tight text-[8px] mb-1">
                Publicación del artículo técnico normativo (NOM-052 / STPS) para posicionar autoridad frente a constructoras del Bajío.
              </p>
            </div>
            <span class="badge-pill bg-slate-100 text-slate-800 text-[7.5px] text-center block">Semana 1 &bull; Persona A y B</span>
          </div>

          <div class="bg-white border border-slate-200 rounded-lg p-2 flex flex-col justify-between">
            <div>
              <span class="font-black text-slate-900 block text-[9.5px] mb-0.5">Paso 3: Prospección B2B</span>
              <p class="text-slate-600 leading-tight text-[8px] mb-1">
                Contacto directo en LinkedIn con directores de obra y contratistas dirigidos al nuevo formulario y WhatsApp institucional.
              </p>
            </div>
            <span class="badge-pill bg-slate-100 text-slate-800 text-[7.5px] text-center block">Semana 2 &bull; Persona B</span>
          </div>
        </div>
      </div>

      <!-- Sección 6: Cuadro de Firmas y Responsabilidades -->
      <div class="border-t-2 border-slate-200 pt-2 mb-2">
        <div class="flex items-center justify-between mb-1.5">
          <div>
            <h3 class="text-[10px] font-black text-navy-900 uppercase tracking-wide">
              6. Formalización y Aprobación del Informe de Estado
            </h3>
            <p class="text-[7.5px] text-slate-500">
              Enterados y de conformidad con el estado de avance técnico y la decisión presupuestal.
            </p>
          </div>
          <span class="text-[8px] font-mono font-bold text-slate-600">OCTUBRE 2026</span>
        </div>

        <div class="grid grid-cols-3 gap-3 pt-3">
          <div class="border-t border-slate-400 pt-1 text-center">
            <p class="text-[8px] font-bold text-slate-800 uppercase">Persona A</p>
            <p class="text-[7px] text-slate-500">Estratega Técnico / Dirección Comercial</p>
            <p class="text-[7px] font-mono text-slate-400 mt-3">FIRMA / FECHA</p>
          </div>

          <div class="border-t border-slate-400 pt-1 text-center">
            <p class="text-[8px] font-bold text-slate-800 uppercase">Persona B</p>
            <p class="text-[7px] text-slate-500">Desarrollador / Operador Digital</p>
            <p class="text-[7px] font-mono text-slate-400 mt-3">FIRMA / FECHA</p>
          </div>

          <div class="border-t border-slate-400 pt-1 text-center">
            <p class="text-[8px] font-bold text-emerald-900 uppercase">Dirección General</p>
            <p class="text-[7px] text-slate-500">Aprobación Final Vinculante</p>
            <p class="text-[7px] font-mono text-slate-400 mt-3">FIRMA / FECHA</p>
          </div>
        </div>
      </div>

      <!-- Tarjeta Institucional de Pie -->
      <div class="bg-navy-950 text-white rounded-lg p-2 flex items-center justify-between">
        <div class="flex items-center gap-2.5">
          <img src="{qr_b64}" alt="QR Web Legado" class="w-8 h-8 rounded bg-white p-0.5 object-contain shrink-0">
          <div>
            <p class="text-[8.5px] font-bold uppercase tracking-wide text-emerald-400">Legado Ambiental S.A. de C.V.</p>
            <p class="text-[7.5px] text-slate-300">San Juan del Río, Qro. &bull; Cobertura Bajío y Nacional &bull; https://legadoambiental.com.mx</p>
          </div>
        </div>
        <div class="text-right">
          <span class="text-[7.5px] font-bold uppercase text-slate-400 block">Certificación de Estado</span>
          <span class="text-[8px] font-extrabold text-white">Plan 100 Leads B2B &bull; 2026</span>
        </div>
      </div>
    </div>

    <!-- Footer Página 4 -->
    <footer class="border-t border-slate-200 pt-2 mt-2 flex items-center justify-between text-[8.5px] text-slate-400 shrink-0">
      <div class="flex items-center gap-2">
        <span class="font-bold text-slate-600 uppercase">Legado Ambiental S.A. de C.V.</span>
        <span>&bull;</span>
        <span>Documento Informativo Oficial del Proyecto</span>
      </div>
      <div class="flex items-center gap-4">
        <span>Uso Interno</span>
        <span class="font-bold text-slate-700 bg-slate-100 px-2 py-0.5 rounded">Página 4 de 4</span>
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

# Run headless Chrome to generate PDF
pdf_path = 'assets/docs/Informe_Ejecutivo_Plan_Trabajo_y_Avances_2026.pdf'
cmd = [
    'google-chrome',
    '--headless',
    '--disable-gpu',
    '--no-pdf-header-footer',
    '--virtual-time-budget=5000',
    '--run-all-compositor-stages-before-draw',
    f'--print-to-pdf={pdf_path}',
    html_path
]

print("Running command:", " ".join(cmd))
res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)

if os.path.exists(pdf_path):
    size_kb = os.path.getsize(pdf_path) / 1024
    print(f"SUCCESS: PDF created at {pdf_path} ({size_kb:.1f} KB)")
else:
    print("ERROR: PDF was not created!")
