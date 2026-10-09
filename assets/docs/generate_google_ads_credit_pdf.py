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
  <title>Dictamen Ejecutivo: Crédito Publicitario Google Ads MXN $7,000 - Legado Ambiental</title>
  
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
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 7px 10px;
    }}
    .table-custom td {{
      font-size: 10px;
      padding: 7px 10px;
      border-bottom: 1px solid #e2e8f0;
    }}
    .badge-pill {{
      display: inline-flex;
      align-items: center;
      padding: 2px 8px;
      border-radius: 9999px;
      font-size: 9px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
  </style>
</head>
<body class="text-charcoal font-sans antialiased">

  <!-- ========================================== -->
  <!-- PÁGINA 1: PORTADA & DICTAMEN EJECUTIVO     -->
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
          <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 bg-amber-50 border border-amber-300 rounded text-amber-900 text-[9.5px] font-bold">
            <span class="w-2 h-2 rounded-full bg-amber-500 animate-pulse"></span>
            DICTAMEN DIRECTIVO RESERVADO
          </div>
          <p class="text-[8.5px] font-mono text-slate-400 mt-0.5">CÓDIGO: DOC-LA-MKT-2026-004 | OCT 2026</p>
        </div>
      </header>

      <!-- Título Principal del Dictamen -->
      <div class="bg-gradient-to-r from-navy-950 via-navy-900 to-slate-900 rounded-xl p-3.5 text-white shadow-md mb-3 border-l-4 border-emerald-500">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[8.5px] font-extrabold tracking-widest text-emerald-400 uppercase bg-emerald-950/80 px-2 py-0.5 rounded border border-emerald-500/30">
              Estrategia Comercial B2B &bull; Pilar 5 & 6
            </span>
            <h2 class="text-lg font-black tracking-tight text-white mt-1 leading-tight">
              Dictamen de Viabilidad: Crédito Publicitario Google Ads ($7,000 MXN)
            </h2>
            <p class="text-[11px] text-slate-300 mt-1 max-w-xl font-normal leading-relaxed">
              Análisis técnico-financiero sobre la oferta de Google Business Profile: términos contractuales, riesgos de facturación oculta, retorno B2B proyectado y recomendación vinculante para la Junta Directiva.
            </p>
          </div>
          <div class="bg-emerald-500/10 border border-emerald-500/30 rounded-lg p-2 text-center shrink-0 ml-3">
            <span class="text-[8px] font-bold text-emerald-300 uppercase block">Subvención Oferta</span>
            <span class="text-lg font-black text-emerald-400 block">$7,000</span>
            <span class="text-[7.5px] text-slate-300 font-mono">MXN Bonificados</span>
          </div>
        </div>
      </div>

      <!-- Resumen Ejecutivo / Veredicto Visual -->
      <div class="bg-emerald-50 border-2 border-emerald-600 rounded-xl p-3 mb-3 shadow-sm">
        <div class="flex items-center justify-between mb-1">
          <div class="flex items-center gap-1.5">
            <span class="flex h-4 w-4 items-center justify-center rounded-full bg-emerald-600 text-white font-bold text-[10px]">✓</span>
            <h3 class="text-[11px] font-black uppercase tracking-wider text-emerald-950">
              Dictamen Ejecutivo Vinculante
            </h3>
          </div>
          <span class="badge-pill bg-emerald-700 text-white font-extrabold text-[8.5px]">
            RECOMENDACIÓN: ACTIVACIÓN DIFERIDA A FASE 6
          </span>
        </div>
        <p class="text-[10px] text-emerald-900 font-medium leading-relaxed">
          <strong class="font-black text-emerald-950">Resolución:</strong> La oferta representa un <strong>descuento comercial real del 50%</strong> en publicidad digital B2B (inversión de $14,000 MXN en clics calificados a un costo neto de $7,000 MXN). <strong>Se recomienda APROBAR el uso del crédito</strong>, pero <strong>NO activarlo de forma inmediata</strong>. Debe reservarse para el lanzamiento de la Fase 6 (Captación activa de los Primeros 100 Leads B2B) una vez recolectadas de 5 a 10 reseñas de 5 estrellas en Google Business Profile y con 4 escudos de frenado configurados.
        </p>
      </div>

      <!-- Métricas Clave de la Oferta (Grid 4 Tarjetas) -->
      <div class="grid grid-cols-4 gap-2 mb-3">
        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
          <span class="text-[8.5px] font-bold text-slate-500 uppercase tracking-wider block">Mecánica Real</span>
          <span class="text-[11px] font-black text-slate-900 block mt-0.5">Spend-Match 1:1</span>
          <p class="text-[8px] text-slate-600 mt-0.5 leading-snug">Gasta $7,000 propios en 60 días para liberar $7,000 de saldo.</p>
        </div>
        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
          <span class="text-[8.5px] font-bold text-slate-500 uppercase tracking-wider block">Plazo Calificación</span>
          <span class="text-[11px] font-black text-slate-900 block mt-0.5">60 Días Naturales</span>
          <p class="text-[8px] text-slate-600 mt-0.5 leading-snug">Plazo límite para completar el gasto de inversión desde el cupón.</p>
        </div>
        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
          <span class="text-[8.5px] font-bold text-slate-500 uppercase tracking-wider block">Vigencia Crédito</span>
          <span class="text-[11px] font-black text-slate-900 block mt-0.5">60 Días Posteriores</span>
          <p class="text-[8px] text-slate-600 mt-0.5 leading-snug">Vigencia del saldo promocional antes de expirar en cuenta.</p>
        </div>
        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
          <span class="text-[8.5px] font-bold text-slate-500 uppercase tracking-wider block">Retorno Efectivo</span>
          <span class="text-[11px] font-black text-emerald-700 block mt-0.5">Subsidio del 50%</span>
          <p class="text-[8px] text-slate-600 mt-0.5 leading-snug">$14,000 MXN de tráfico de ingeniería al 50% de costo.</p>
        </div>
      </div>

      <!-- Sección 1: Términos y Condiciones Esenciales (La Letra Chiquita) -->
      <div>
        <div class="flex items-center gap-2 mb-1.5">
          <div class="w-1.5 h-3.5 bg-brand-700 rounded-full"></div>
          <h3 class="text-[11px] font-black text-navy-900 uppercase tracking-wide">
            1. Desglose Contractual: Los 5 Términos y Condiciones Estrictos de Google
          </h3>
        </div>

        <div class="space-y-1.5 text-[9.5px]">
          <div class="bg-white border border-slate-200 rounded-lg p-2 flex items-start gap-2">
            <span class="w-4 h-4 rounded-full bg-slate-900 text-white font-bold text-[9px] flex items-center justify-center shrink-0 mt-0.5">1</span>
            <div>
              <h4 class="font-bold text-slate-900 text-[10px]">No es Dinero en Efectivo ni Descuento Anticipado</h4>
              <p class="text-slate-600 leading-snug text-[8.5px]">
                Google <strong>no deposita dinero en cuentas bancarias</strong> ni descuenta el crédito al inicio. Requiere facturar y cobrar primero $7,000 MXN netos a la tarjeta empresarial de Legado Ambiental mediante clics legítimos en un lapso máximo de 60 días naturales.
              </p>
            </div>
          </div>

          <div class="bg-white border border-slate-200 rounded-lg p-2 flex items-start gap-2">
            <span class="w-4 h-4 rounded-full bg-slate-900 text-white font-bold text-[9px] flex items-center justify-center shrink-0 mt-0.5">2</span>
            <div>
              <h4 class="font-bold text-slate-900 text-[10px]">Cuentas de Google Ads Nuevas Únicamente</h4>
              <p class="text-slate-600 leading-snug text-[8.5px]">
                El cupón promocional es válido exclusivamente para cuentas creadas hace <strong>menos de 14 a 21 días</strong> o que no hayan corrido campañas históricas previas. Dado que Legado Ambiental acaba de verificar su ficha GBP, se cumple al 100% el perfil de elegibilidad.
              </p>
            </div>
          </div>

          <div class="bg-white border border-slate-200 rounded-lg p-2 flex items-start gap-2">
            <span class="w-4 h-4 rounded-full bg-slate-900 text-white font-bold text-[9px] flex items-center justify-center shrink-0 mt-0.5">3</span>
            <div>
              <h4 class="font-bold text-slate-900 text-[10px]">Condición de "Todo o Nada" en el Umbral de Gasto</h4>
              <p class="text-slate-600 leading-snug text-[8.5px]">
                Si la empresa activa el cupón y gasta únicamente $6,500 MXN dentro de los 60 días, <strong>no se recibe crédito proporcional</strong>; el beneficio se pierde de manera irrevocable. El gasto debe llegar o superar exactamente los $7,000 MXN en el período establecido.
              </p>
            </div>
          </div>

          <div class="bg-white border border-slate-200 rounded-lg p-2 flex items-start gap-2">
            <span class="w-4 h-4 rounded-full bg-slate-900 text-white font-bold text-[9px] flex items-center justify-center shrink-0 mt-0.5">4</span>
            <div>
              <h4 class="font-bold text-slate-900 text-[10px]">Tratamiento Fiscal e IVA SAT (16%) en México</h4>
              <p class="text-slate-600 leading-snug text-[8.5px]">
                El crédito cubre el gasto neto de clics de Google. La facturación oficial es emitida por <em>Google Operaciones de México, S. de R.L. de C.V.</em> Por tanto, el cobro de los primeros $7,000 MXN causará 16% de IVA ($1,120 MXN), deducible al 100% con CFDI al registrar el RFC corporativo.
              </p>
            </div>
          </div>

          <div class="bg-white border border-slate-200 rounded-lg p-2 flex items-start gap-2">
            <span class="w-4 h-4 rounded-full bg-slate-900 text-white font-bold text-[9px] flex items-center justify-center shrink-0 mt-0.5">5</span>
            <div>
              <h4 class="font-bold text-slate-900 text-[10px]">Caducidad Fatal del Saldo Bonificado a los 60 Días</h4>
              <p class="text-slate-600 leading-snug text-[8.5px]">
                Una vez acreditados los $7,000 MXN en la sección de Facturación, Legado Ambiental dispone de una ventana fija de 60 días naturales para consumir el saldo en clics. Todo remanente no ejercido al concluir los 60 días vence y se cancela de forma irrevocable.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer Página 1 -->
    <footer class="border-t border-slate-200 pt-2 mt-2 flex items-center justify-between text-[8.5px] text-slate-400 shrink-0">
      <div class="flex items-center gap-2">
        <span class="font-bold text-slate-600 uppercase">Legado Ambiental S.A. de C.V.</span>
        <span>&bull;</span>
        <span>Comité de Dirección &bull; Dictamen de Decisión Google Ads</span>
      </div>
      <div class="flex items-center gap-4">
        <span>Confidencial</span>
        <span class="font-bold text-slate-700 bg-slate-100 px-2 py-0.5 rounded">Página 1 de 4</span>
      </div>
    </footer>
  </div>

  <!-- ========================================== -->
  <!-- PÁGINA 2: MECÁNICA Y RIESGOS DE FACTURACIÓN-->
  <!-- ========================================== -->
  <div class="page-container">
    <div>
      <!-- Header Superior Compacto -->
      <header class="flex items-center justify-between border-b border-slate-200 pb-2.5 mb-3 shrink-0">
        <div class="flex items-center gap-2">
          <img src="{logo_b64}" alt="Legado Ambiental" class="h-8 w-auto object-contain">
          <span class="text-xs font-black uppercase text-navy-900 tracking-tight">Dictamen Técnico Google Ads $7,000 MXN</span>
        </div>
        <span class="text-[9px] font-mono text-slate-400">SECCIÓN 2 & 3: MECÁNICA Y BLINDAJE DE RIESGOS</span>
      </header>

      <!-- Sección 2: ¿En Qué se Aplica y Cómo Opera? -->
      <div class="mb-3.5">
        <div class="flex items-center gap-2 mb-1.5">
          <div class="w-1.5 h-3.5 bg-brand-700 rounded-full"></div>
          <h3 class="text-xs font-black text-navy-900 uppercase tracking-wide">
            2. Mecánica de Aplicación: Destino del Saldo y Cronología Financiera
          </h3>
        </div>

        <div class="grid grid-cols-2 gap-2.5 mb-2.5">
          <div class="bg-emerald-50/60 border border-emerald-200 rounded-lg p-2.5">
            <h4 class="text-[10px] font-black uppercase text-emerald-950 flex items-center gap-1.5 mb-1">
              <span class="text-emerald-600 text-sm">✔</span> En Qué SÍ se Aplica el Crédito
            </h4>
            <ul class="text-[9px] text-emerald-900 space-y-1 leading-snug">
              <li>&bull; <strong>Google Search B2B:</strong> Clics de tomadores de decisión buscando <em>"estudios topográficos"</em>, <em>"supervisión de obra"</em> o <em>"modelado 3D curvas de nivel"</em>.</li>
              <li>&bull; <strong>Fichas Patrocinadas Google Maps:</strong> Aparecer en la 1.ª posición destacada cuando clientes corporativos busquen consultoría ambiental o topografía cercana.</li>
              <li>&bull; <strong>Campaña Local Inteligente:</strong> Llamadas directas y solicitudes de cotización al WhatsApp oficial de Legado Ambiental.</li>
            </ul>
          </div>

          <div class="bg-rose-50/60 border border-rose-200 rounded-lg p-2.5">
            <h4 class="text-[10px] font-black uppercase text-rose-950 flex items-center gap-1.5 mb-1">
              <span class="text-rose-600 text-sm">✕</span> En Qué NO se Aplica (Exclusiones)
            </h4>
            <ul class="text-[9px] text-rose-900 space-y-1 leading-snug">
              <li>&bull; <strong>No es transferible a efectivo:</strong> No puede retirarse a cuentas bancarias ni transferirse a otras razones sociales.</li>
              <li>&bull; <strong>No cubre impuestos (IVA):</strong> El 16% de IVA sobre el gasto inicial corre a cargo de la cuenta empresarial.</li>
              <li>&bull; <strong>No cubre honorarios externos:</strong> Solo amortiza costo directo por clic (CPC) o millar de impresiones (CPM) en la plataforma de Google.</li>
            </ul>
          </div>
        </div>

        <!-- Diagrama Cronológico en 3 Fases -->
        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2.5">
          <span class="text-[9px] font-extrabold uppercase text-slate-500 tracking-wider block mb-1.5">Cronología Operativa del Flujo Financiero</span>
          <div class="grid grid-cols-3 gap-2 text-[9.5px]">
            <div class="bg-white p-2 rounded border border-slate-200 relative">
              <div class="flex items-center justify-between mb-1">
                <span class="font-extrabold text-slate-900">Fase 1: Inversión Propia</span>
                <span class="badge-pill bg-slate-100 text-slate-700">Días 1 - 45</span>
              </div>
              <p class="text-slate-600 leading-tight text-[8.5px]">
                Legado Ambiental invierte a un ritmo de $150 MXN/día. Los cargos se cobran periódicamente a la tarjeta de crédito empresarial hasta sumar $7,000 MXN netos.
              </p>
              <div class="mt-2 text-right font-black text-slate-800 text-[10px]">Costo: $7,000 MXN</div>
            </div>

            <div class="bg-white p-2 rounded border border-emerald-300 relative">
              <div class="flex items-center justify-between mb-1">
                <span class="font-extrabold text-emerald-900">Fase 2: Acreditación</span>
                <span class="badge-pill bg-emerald-100 text-emerald-800">Días 46 - 47</span>
              </div>
              <p class="text-slate-600 leading-tight text-[8.5px]">
                El algoritmo de Google valida el umbral. En 35 horas hábiles se abona el cupón de $7,000 MXN en el apartado "Promociones" como saldo a favor activo.
              </p>
              <div class="mt-2 text-right font-black text-emerald-600 text-[10px]">+ $7,000 Bonificados</div>
            </div>

            <div class="bg-white p-2 rounded border border-slate-200 relative">
              <div class="flex items-center justify-between mb-1">
                <span class="font-extrabold text-slate-900">Fase 3: Consumo Crédito</span>
                <span class="badge-pill bg-slate-100 text-slate-700">Días 48 - 85</span>
              </div>
              <p class="text-slate-600 leading-tight text-[8.5px]">
                Google consume automáticamente el saldo promocional. <strong>Cero cargos a la tarjeta bancaria</strong> durante esta fase hasta agotar los $7,000 de crédito.
              </p>
              <div class="mt-2 text-right font-black text-brand-700 text-[10px]">Costo: $0 MXN</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Sección 3: ¿Qué Ocurre Cuando se Acaba el Crédito? (Riesgos y Blindaje) -->
      <div>
        <div class="flex items-center gap-2 mb-1.5">
          <div class="w-1.5 h-3.5 bg-rose-600 rounded-full"></div>
          <h3 class="text-xs font-black text-rose-950 uppercase tracking-wide">
            3. Alerta Crítica: ¿Qué Pasa Cuando se Agota el Crédito? (Riesgo de Cobro Oculto)
          </h3>
        </div>

        <!-- Alerta de Riesgo -->
        <div class="bg-rose-50 border-2 border-rose-500 rounded-lg p-2.5 mb-2.5">
          <div class="flex items-center gap-2 mb-1">
            <span class="text-rose-700 font-black text-xs">⚠️ RIESGO DIRECTO: GOOGLE NO PAUSA LAS CAMPAÑAS AL TERMINAR EL CRÉDITO</span>
          </div>
          <p class="text-[9.5px] text-rose-900 leading-snug">
            Por política operativa por defecto, en el instante en que el crédito promocional de $7,000 MXN llega a $0, <strong>las campañas publicitarias NO se detienen</strong>. Google continuará mostrando anuncios al ritmo del presupuesto diario y reanudará automáticamente los cargos a la tarjeta de crédito corporativa sin previo aviso si no se establecen controles técnicos previos.
          </p>
        </div>

        <!-- Los 4 Escudos Financieros de Blindaje Obligatorio -->
        <div class="grid grid-cols-2 gap-2.5">
          <div class="bg-white border border-slate-200 rounded-lg p-2.5">
            <div class="flex items-center gap-1.5 mb-1">
              <span class="w-4 h-4 rounded bg-slate-900 text-white font-bold text-[9px] flex items-center justify-center">1</span>
              <h4 class="font-bold text-slate-900 text-[10px]">Límite Mensual a Nivel de Cuenta</h4>
            </div>
            <p class="text-[8.5px] text-slate-600 leading-tight">
              Configurar un <em>Account Budget Cap</em> en Google Ads fijado exactamente en $13,900 MXN. De este modo, al superar dicha cifra, el sistema corta automáticamente cualquier gasto adicional.
            </p>
          </div>

          <div class="bg-white border border-slate-200 rounded-lg p-2.5">
            <div class="flex items-center gap-1.5 mb-1">
              <span class="w-4 h-4 rounded bg-slate-900 text-white font-bold text-[9px] flex items-center justify-center">2</span>
              <h4 class="font-bold text-slate-900 text-[10px]">Presupuesto Diario Estricto ($150 MXN)</h4>
            </div>
            <p class="text-[8.5px] text-slate-600 leading-tight">
              Tope diario de $150 MXN (~4 a 6 clics de alta intención B2B). Esto garantiza que el período de calificación de 60 días se cubra de forma armónica y predecible sin sorpresas en tarjeta.
            </p>
          </div>

          <div class="bg-white border border-slate-200 rounded-lg p-2.5">
            <div class="flex items-center gap-1.5 mb-1">
              <span class="w-4 h-4 rounded bg-slate-900 text-white font-bold text-[9px] flex items-center justify-center">3</span>
              <h4 class="font-bold text-slate-900 text-[10px]">Regla Algorítmica de Pausado Automático</h4>
            </div>
            <p class="text-[8.5px] text-slate-600 leading-tight">
              Creación de una regla automática en Google Ads con el disparador: <em>"Si el costo acumulado de la campaña alcanza $13,850 MXN, cambiar estado a PAUSADA y notificar por correo"</em>.
            </p>
          </div>

          <div class="bg-white border border-slate-200 rounded-lg p-2.5">
            <div class="flex items-center gap-1.5 mb-1">
              <span class="w-4 h-4 rounded bg-slate-900 text-white font-bold text-[9px] flex items-center justify-center">4</span>
              <h4 class="font-bold text-slate-900 text-[10px]">Alertas Preventivas de Consumo al 80%</h4>
            </div>
            <p class="text-[8.5px] text-slate-600 leading-tight">
              Activación de recordatorio al llegar a $11,500 MXN de gasto acumulado para evaluar el retorno en leads y decidir en Junta Directiva si la campaña continúa con inversión propia o concluye.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer Página 2 -->
    <footer class="border-t border-slate-200 pt-2.5 mt-2 flex items-center justify-between text-[9px] text-slate-400 shrink-0">
      <div class="flex items-center gap-2">
        <span class="font-bold text-slate-600 uppercase">Legado Ambiental S.A. de C.V.</span>
        <span>&bull;</span>
        <span>Control Presupuestario y Seguridad Financiera</span>
      </div>
      <div class="flex items-center gap-4">
        <span>Confidencial</span>
        <span class="font-bold text-slate-700 bg-slate-100 px-2 py-0.5 rounded">Página 2 de 4</span>
      </div>
    </footer>
  </div>

  <!-- ========================================== -->
  <!-- PÁGINA 3: UNIT ECONOMICS & RETORNO B2B     -->
  <!-- ========================================== -->
  <div class="page-container">
    <div>
      <!-- Header Superior Compacto -->
      <header class="flex items-center justify-between border-b border-slate-200 pb-2.5 mb-3 shrink-0">
        <div class="flex items-center gap-2">
          <img src="{logo_b64}" alt="Legado Ambiental" class="h-8 w-auto object-contain">
          <span class="text-xs font-black uppercase text-navy-900 tracking-tight">Dictamen Técnico Google Ads $7,000 MXN</span>
        </div>
        <span class="text-[9px] font-mono text-slate-400">SECCIÓN 4 & 5: RETORNO DE INVERSIÓN Y ESCENARIOS</span>
      </header>

      <!-- Sección 4: Unit Economics y Proyección de Retorno B2B -->
      <div class="mb-3.5">
        <div class="flex items-center gap-2 mb-1.5">
          <div class="w-1.5 h-3.5 bg-brand-700 rounded-full"></div>
          <h3 class="text-xs font-black text-navy-900 uppercase tracking-wide">
            4. Modelo de Unit Economics B2B: Proyección de Captación para Legado Ambiental
          </h3>
        </div>

        <p class="text-[9.5px] text-slate-600 mb-2 leading-relaxed">
          A diferencia del marketing de consumo masivo, los servicios de Legado Ambiental (Topografía con Dron, Georreferenciación GPS, Supervisión de Obra, PTAR) cuentan con tickets promedio elevados ($50,000 a $300,000+ MXN). Un solo cierre corporativo justifica con creces la inversión total.
        </p>

        <!-- Tabla de Escenarios Financieros -->
        <div class="overflow-hidden border border-slate-200 rounded-lg shadow-sm mb-2.5">
          <table class="w-full table-custom text-left border-collapse">
            <thead>
              <tr>
                <th class="w-1/4">Variable / Métrica Publicitaria</th>
                <th class="w-1/4 text-center">Escenario Prudente</th>
                <th class="w-1/4 text-center bg-emerald-900">Escenario Base (Esperado)</th>
                <th class="w-1/4 text-center">Escenario Alto</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="font-bold text-slate-900">Presupuesto Total Desplegado (50% Google)</td>
                <td class="text-center font-mono font-bold">$14,000 MXN</td>
                <td class="text-center font-mono font-bold text-emerald-700 bg-emerald-50/50">$14,000 MXN</td>
                <td class="text-center font-mono font-bold">$14,000 MXN</td>
              </tr>
              <tr class="bg-slate-50/50">
                <td>Costo por Clic Promedio (CPC B2B Especializado)</td>
                <td class="text-center font-mono">$42.00 MXN</td>
                <td class="text-center font-mono text-emerald-800 bg-emerald-50/50 font-semibold">$35.00 MXN</td>
                <td class="text-center font-mono">$28.00 MXN</td>
              </tr>
              <tr>
                <td>Visitas Calificadas al Sitio Web (Tomadores B2B)</td>
                <td class="text-center font-mono font-bold">333 clics</td>
                <td class="text-center font-mono font-bold text-emerald-700 bg-emerald-50/50">400 clics</td>
                <td class="text-center font-mono font-bold">500 clics</td>
              </tr>
              <tr class="bg-slate-50/50">
                <td>Tasa de Conversión a Lead (Formulario / WhatsApp)</td>
                <td class="text-center font-mono">3.0%</td>
                <td class="text-center font-mono text-emerald-800 bg-emerald-50/50 font-semibold">4.5%</td>
                <td class="text-center font-mono">6.0%</td>
              </tr>
              <tr>
                <td class="font-bold text-slate-900">Prospectos B2B Calificados Generados</td>
                <td class="text-center font-mono font-black text-slate-800">10 Leads</td>
                <td class="text-center font-mono font-black text-emerald-900 bg-emerald-50/50">18 Leads</td>
                <td class="text-center font-mono font-black text-slate-800">30 Leads</td>
              </tr>
              <tr class="bg-slate-50/50">
                <td>Costo Real por Lead B2B (Inversión neta $7,000 MXN)</td>
                <td class="text-center font-mono font-semibold">$700 MXN</td>
                <td class="text-center font-mono text-emerald-800 bg-emerald-50/50 font-bold">$388 MXN</td>
                <td class="text-center font-mono font-semibold">$233 MXN</td>
              </tr>
              <tr>
                <td class="font-bold text-slate-900">Contratos B2B Formalizados (Tasa Cierre ~10%)</td>
                <td class="text-center font-mono font-black text-slate-900">1 Contrato</td>
                <td class="text-center font-mono font-black text-emerald-950 bg-emerald-50/50">1 a 2 Contratos</td>
                <td class="text-center font-mono font-black text-slate-900">3 Contratos</td>
              </tr>
              <tr class="bg-emerald-100/60 font-black">
                <td class="text-emerald-950">Facturación Estimada Contratada (Ticket $95k)</td>
                <td class="text-center font-mono text-emerald-900">$95,000 MXN</td>
                <td class="text-center font-mono text-emerald-950 text-[11px] bg-emerald-200/50">$190,000 MXN</td>
                <td class="text-center font-mono text-emerald-900">$285,000 MXN</td>
              </tr>
              <tr class="bg-navy-900 text-white font-black">
                <td class="text-emerald-400">Retorno Neto sobre Inversión Propia (ROI)</td>
                <td class="text-center font-mono text-emerald-300">1,257%</td>
                <td class="text-center font-mono text-emerald-400 text-[11px] bg-navy-950">2,614%</td>
                <td class="text-center font-mono text-emerald-300">3,971%</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Sección 5: Matriz Comparativa de Decisiones para la Dirección -->
      <div>
        <div class="flex items-center gap-2 mb-1.5">
          <div class="w-1.5 h-3.5 bg-brand-700 rounded-full"></div>
          <h3 class="text-xs font-black text-navy-900 uppercase tracking-wide">
            5. Matriz de Decisión Estratégica: Tres Caminos para el Comité
          </h3>
        </div>

        <div class="space-y-2">
          <!-- Opción A -->
          <div class="bg-white border border-slate-200 rounded-lg p-2.5 flex items-start gap-2.5">
            <span class="w-5 h-5 rounded-full bg-slate-200 text-slate-700 font-bold text-[10px] flex items-center justify-center shrink-0 mt-0.5">A</span>
            <div class="w-full">
              <div class="flex items-center justify-between">
                <h4 class="font-bold text-slate-900 text-[10px]">Opción A: Reclamar y Activar de Inmediato (Esta Semana)</h4>
                <span class="badge-pill bg-rose-100 text-rose-800">NO RECOMENDADO</span>
              </div>
              <p class="text-slate-600 mt-0.5 text-[8.5px] leading-snug">
                <strong>Riesgo de Ineficiencia:</strong> La ficha de GBP recién verificada cuenta con 0 reseñas públicas. Los usuarios que lleguen por clics pagados verán un perfil sin prueba social, lo que reduce la tasa de conversión hasta en un 60%, desperdiciando parte del presupuesto inicial.
              </p>
            </div>
          </div>

          <!-- Opción B (Recomendada) -->
          <div class="bg-emerald-50/80 border-2 border-emerald-600 rounded-lg p-2.5 flex items-start gap-2.5 shadow-sm">
            <span class="w-5 h-5 rounded-full bg-emerald-600 text-white font-bold text-[10px] flex items-center justify-center shrink-0 mt-0.5">B</span>
            <div class="w-full">
              <div class="flex items-center justify-between">
                <h4 class="font-black text-emerald-950 text-[10.5px]">Opción B: Diferir Activación al Inicio de Fase 6 (Primeros 100 Leads)</h4>
                <span class="badge-pill bg-emerald-700 text-white font-black">ESTRATEGIA RECOMENDADA</span>
              </div>
              <p class="text-emerald-900 mt-0.5 text-[8.5px] leading-snug font-medium">
                <strong>Máxima Eficiencia y Conversión:</strong> Se concluye primero el Pilar 5 recolectando entre 5 y 10 reseñas de 5 estrellas con clientes vigentes y aliados de Legado Ambiental. Al tener una ficha blindada con reputación social y el sitio web con analítica GTM/GA4 activa, se activa el cupón para multiplicar la conversión por clic.
              </p>
            </div>
          </div>

          <!-- Opción C -->
          <div class="bg-white border border-slate-200 rounded-lg p-2.5 flex items-start gap-2.5">
            <span class="w-5 h-5 rounded-full bg-slate-200 text-slate-700 font-bold text-[10px] flex items-center justify-center shrink-0 mt-0.5">C</span>
            <div class="w-full">
              <div class="flex items-center justify-between">
                <h4 class="font-bold text-slate-900 text-[10px]">Opción C: Descartar u Omitir la Oferta</h4>
                <span class="badge-pill bg-slate-100 text-slate-600">DESACONSEJADO</span>
              </div>
              <p class="text-slate-600 mt-0.5 text-[8.5px] leading-snug">
                <strong>Costo de Oportunidad Comercial:</strong> Implica renunciar a $7,000 MXN de subvención directa en pauta digital que otorga Google. En un mercado competitivo de ingeniería, dejar de captar ~400 tomadores de decisión debilita el alcance frente a despachos competidores.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer Página 3 -->
    <footer class="border-t border-slate-200 pt-2.5 mt-2 flex items-center justify-between text-[9px] text-slate-400 shrink-0">
      <div class="flex items-center gap-2">
        <span class="font-bold text-slate-600 uppercase">Legado Ambiental S.A. de C.V.</span>
        <span>&bull;</span>
        <span>Evaluación Financiera y Rentabilidad B2B</span>
      </div>
      <div class="flex items-center gap-4">
        <span>Confidencial</span>
        <span class="font-bold text-slate-700 bg-slate-100 px-2 py-0.5 rounded">Página 3 de 4</span>
      </div>
    </footer>
  </div>

  <!-- ========================================== -->
  <!-- PÁGINA 4: RUTA CRÍTICA & APROBACIÓN        -->
  <!-- ========================================== -->
  <div class="page-container">
    <div>
      <!-- Header Superior Compacto -->
      <header class="flex items-center justify-between border-b border-slate-200 pb-2.5 mb-3 shrink-0">
        <div class="flex items-center gap-2">
          <img src="{logo_b64}" alt="Legado Ambiental" class="h-8 w-auto object-contain">
          <span class="text-xs font-black uppercase text-navy-900 tracking-tight">Dictamen Técnico Google Ads $7,000 MXN</span>
        </div>
        <span class="text-[9px] font-mono text-slate-400">SECCIÓN 6, 7 & 8: RUTA CRÍTICA, FAQ Y AUTORIZACIÓN</span>
      </header>

      <!-- Sección 6: Protocolo de Ejecución Técnica Paso a Paso -->
      <div class="mb-3">
        <div class="flex items-center gap-2 mb-1.5">
          <div class="w-1.5 h-3.5 bg-brand-700 rounded-full"></div>
          <h3 class="text-xs font-black text-navy-900 uppercase tracking-wide">
            6. Protocolo de Ejecución Táctica: Ruta de 5 Pasos para la Activación
          </h3>
        </div>

        <div class="grid grid-cols-5 gap-2 text-center text-[9px]">
          <div class="bg-white border border-slate-200 rounded-lg p-2 flex flex-col justify-between">
            <div>
              <span class="w-5 h-5 rounded-full bg-slate-900 text-white font-bold text-[9px] mx-auto flex items-center justify-center mb-1">1</span>
              <span class="font-black text-slate-900 block text-[9.5px]">Blindaje GBP</span>
              <p class="text-slate-500 mt-1 text-[8px] leading-tight">Completar 5 a 10 reseñas verificadas de 5★ en la ficha de Google.</p>
            </div>
            <span class="mt-2 text-[7.5px] font-bold text-emerald-700 bg-emerald-50 py-0.5 rounded">Requisito Previo</span>
          </div>

          <div class="bg-white border border-slate-200 rounded-lg p-2 flex flex-col justify-between">
            <div>
              <span class="w-5 h-5 rounded-full bg-slate-900 text-white font-bold text-[9px] mx-auto flex items-center justify-center mb-1">2</span>
              <span class="font-black text-slate-900 block text-[9.5px]">Alta Fiscal SAT</span>
              <p class="text-slate-500 mt-1 text-[8px] leading-tight">Vincular RFC de Legado Ambiental para recibir CFDI mensual deducible.</p>
            </div>
            <span class="mt-2 text-[7.5px] font-bold text-slate-700 bg-slate-100 py-0.5 rounded">Deducibilidad</span>
          </div>

          <div class="bg-white border border-slate-200 rounded-lg p-2 flex flex-col justify-between">
            <div>
              <span class="w-5 h-5 rounded-full bg-slate-900 text-white font-bold text-[9px] mx-auto flex items-center justify-center mb-1">3</span>
              <span class="font-black text-slate-900 block text-[9.5px]">Reclamo Cupón</span>
              <p class="text-slate-500 mt-1 text-[8px] leading-tight">Reclamar la oferta e iniciar el conteo oficial de 60 días naturales.</p>
            </div>
            <span class="mt-2 text-[7.5px] font-bold text-amber-700 bg-amber-50 py-0.5 rounded">Inicio Reloj</span>
          </div>

          <div class="bg-white border border-slate-200 rounded-lg p-2 flex flex-col justify-between">
            <div>
              <span class="w-5 h-5 rounded-full bg-slate-900 text-white font-bold text-[9px] mx-auto flex items-center justify-center mb-1">4</span>
              <span class="font-black text-slate-900 block text-[9.5px]">Campaña Search</span>
              <p class="text-slate-500 mt-1 text-[8px] leading-tight">Configurar keywords B2B exactas y negativas para filtrar curiosos.</p>
            </div>
            <span class="mt-2 text-[7.5px] font-bold text-slate-700 bg-slate-100 py-0.5 rounded">Filtro B2B</span>
          </div>

          <div class="bg-white border border-slate-200 rounded-lg p-2 flex flex-col justify-between">
            <div>
              <span class="w-5 h-5 rounded-full bg-emerald-700 text-white font-bold text-[9px] mx-auto flex items-center justify-center mb-1">5</span>
              <span class="font-black text-emerald-950 block text-[9.5px]">Frenado Auto</span>
              <p class="text-slate-500 mt-1 text-[8px] leading-tight">Activar regla de pausado al alcanzar $13,850 MXN de consumo.</p>
            </div>
            <span class="mt-2 text-[7.5px] font-bold text-emerald-800 bg-emerald-50 py-0.5 rounded">Blindaje $0</span>
          </div>
        </div>
      </div>

      <!-- Sección 7: FAQ y Contingencia Financiera para la Junta Directiva -->
      <div class="mb-3">
        <div class="flex items-center gap-2 mb-1.5">
          <div class="w-1.5 h-3.5 bg-brand-700 rounded-full"></div>
          <h3 class="text-xs font-black text-navy-900 uppercase tracking-wide">
            7. Preguntas Clave del Comité y Plan de Contingencia
          </h3>
        </div>

        <div class="grid grid-cols-2 gap-2 text-[9px]">
          <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
            <h4 class="font-black text-slate-900 text-[9.5px] flex items-center gap-1">
              <span class="text-brand-700 font-black">Q1:</span> ¿Qué pasa si una campaña consume más rápido de lo previsto?
            </h4>
            <p class="text-slate-600 mt-0.5 text-[8.5px] leading-snug">
              Google permite fluctuaciones diarias de hasta 2x sobre el presupuesto diario si detecta alta demanda, pero <strong>nunca cobra más del límite mensual</strong> (30.4 días x presupuesto diario). Con el límite de cuenta en $13,900 MXN, el desembolso total está matemáticamente topado.
            </p>
          </div>

          <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
            <h4 class="font-black text-slate-900 text-[9.5px] flex items-center gap-1">
              <span class="text-brand-700 font-black">Q2:</span> ¿El CFDI fiscal emitido por Google es 100% deducible en México?
            </h4>
            <p class="text-slate-600 mt-0.5 text-[8.5px] leading-snug">
              Sí. Al estar constituida <em>Google Operaciones de México, S. de R.L. de C.V.</em> en territorio nacional, emite factura con CFDI 4.0 con IVA desglosado deducible como gasto operativo comercial indispensable de la empresa bajo el régimen general de ley.
            </p>
          </div>

          <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
            <h4 class="font-black text-slate-900 text-[9.5px] flex items-center gap-1">
              <span class="text-brand-700 font-black">Q3:</span> ¿Podemos pausar la campaña antes de llegar a los $7,000 MXN?
            </h4>
            <p class="text-slate-600 mt-0.5 text-[8.5px] leading-snug">
              Se puede pausar en cualquier momento, pero si el gasto total no alcanza los $7,000 MXN antes de los 60 días, Google no bonificará ningún monto. Para maximizar el beneficio financiero, la inversión debe alcanzar el umbral completo de forma planificada.
            </p>
          </div>

          <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
            <h4 class="font-black text-slate-900 text-[9.5px] flex items-center gap-1">
              <span class="text-brand-700 font-black">Q4:</span> ¿Cómo garantizamos que los clics provengan de empresas (B2B)?
            </h4>
            <p class="text-slate-600 mt-0.5 text-[8.5px] leading-snug">
              Utilizando palabras clave de alta intención técnica (ej. <em>"despacho topografia obra bajio"</em>, <em>"estudio hidrogeologico constructora"</em>) y una robusta lista de palabras negativas (ej. <em>"gratis", "empleo", "pdf", "tesis", "curso"</em>) que bloquean clics no comerciales.
            </p>
          </div>
        </div>
      </div>

      <!-- Sección 8: Cuadro de Firmas y Autorización Corporativa -->
      <div class="border-t-2 border-slate-200 pt-2.5">
        <div class="flex items-center justify-between mb-2">
          <div>
            <h3 class="text-xs font-black text-navy-900 uppercase tracking-wide">
              8. Formalización y Aprobación de la Junta Directiva
            </h3>
            <p class="text-[8px] text-slate-500">
              La firma de este documento ratifica la adopción de la Opción B (Diferimiento a Fase 6) y autoriza la reserva presupuestal para el momento oportuno.
            </p>
          </div>
          <div class="text-right">
            <span class="text-[8px] font-bold text-slate-400 uppercase">Validez Ejecutiva</span>
            <span class="text-[9px] font-mono font-bold text-slate-700 block">Ejercicio Fiscal 2026</span>
          </div>
        </div>

        <div class="grid grid-cols-3 gap-3 pt-3 mb-2">
          <!-- Firma 1 -->
          <div class="border-t border-slate-400 pt-1.5 text-center">
            <p class="text-[8.5px] font-bold text-slate-800 uppercase">Coordinación de Marketing Digital</p>
            <p class="text-[7.5px] text-slate-500">Elaboración y Análisis Técnico</p>
            <p class="text-[7.5px] font-mono text-slate-400 mt-3">FIRMA / FECHA</p>
          </div>

          <!-- Firma 2 -->
          <div class="border-t border-slate-400 pt-1.5 text-center">
            <p class="text-[8.5px] font-bold text-slate-800 uppercase">Gerencia Administrativa y Finanzas</p>
            <p class="text-[7.5px] text-slate-500">Revisión Presupuestal y Fiscal</p>
            <p class="text-[7.5px] font-mono text-slate-400 mt-3">FIRMA / FECHA</p>
          </div>

          <!-- Firma 3 -->
          <div class="border-t border-slate-400 pt-1.5 text-center">
            <p class="text-[8.5px] font-bold text-emerald-900 uppercase">Dirección General</p>
            <p class="text-[7.5px] text-slate-500">Aprobación Final Vinculante</p>
            <p class="text-[7.5px] font-mono text-slate-400 mt-3">FIRMA / FECHA</p>
          </div>
        </div>
      </div>

      <!-- Tarjeta de Contacto / Identidad Institucional -->
      <div class="bg-navy-950 text-white rounded-lg p-2 flex items-center justify-between">
        <div class="flex items-center gap-2.5">
          <img src="{qr_b64}" alt="QR Web Legado" class="w-9 h-9 rounded bg-white p-0.5 object-contain shrink-0">
          <div>
            <p class="text-[9px] font-bold uppercase tracking-wide text-emerald-400">Legado Ambiental S.A. de C.V.</p>
            <p class="text-[7.5px] text-slate-300">San Juan del Río, Qro. &bull; Cobertura Bajío y Nacional</p>
            <p class="text-[7.5px] text-slate-400 font-mono">contacto@legadoambiental.com.mx &bull; https://legadoambiental.com.mx</p>
          </div>
        </div>
        <div class="text-right">
          <span class="text-[7.5px] font-bold uppercase text-slate-400 block">Certificación de Plan</span>
          <span class="text-[8.5px] font-extrabold text-white">Plan 100 Leads B2B &bull; 2026</span>
        </div>
      </div>
    </div>

    <!-- Footer Página 4 -->
    <footer class="border-t border-slate-200 pt-2 mt-2 flex items-center justify-between text-[8.5px] text-slate-400 shrink-0">
      <div class="flex items-center gap-2">
        <span class="font-bold text-slate-600 uppercase">Legado Ambiental S.A. de C.V.</span>
        <span>&bull;</span>
        <span>Documento de Decisión Corporativa</span>
      </div>
      <div class="flex items-center gap-4">
        <span>Confidencial</span>
        <span class="font-bold text-slate-700 bg-slate-100 px-2 py-0.5 rounded">Página 4 de 4</span>
      </div>
    </footer>
  </div>

</body>
</html>
"""

# Write HTML file
html_path = 'assets/docs/Dictamen_Credito_Google_Ads_7000_MXN.html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"HTML updated successfully: {html_path}")

# Run headless Chrome to generate PDF
pdf_path = 'assets/docs/Dictamen_Credito_Google_Ads_7000_MXN.pdf'
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
