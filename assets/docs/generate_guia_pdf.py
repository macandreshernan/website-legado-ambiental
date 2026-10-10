import subprocess
import os

with open('assets/docs/logo_base64.txt', 'r', encoding='utf-8') as f:
    logo_b64 = f.read().strip()

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Guía Estratégica: Google Business Profile y Google Ads Local - Legado Ambiental</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&family=Merriweather:ital,wght@0,300;0,400;0,700;1,400&display=swap" rel="stylesheet">
  
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
            primary: '#22c55e',
            secondary: '#3b82f6',
            navy: '#0f172a',
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
      background-color: #f1f5f9;
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
      padding: 11mm 14mm;
      box-sizing: border-box;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
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
        padding: 11mm 14mm;
        box-shadow: none;
        page-break-after: always;
        overflow: hidden;
      }}
      .no-print {{
        display: none !important;
      }}
    }}
  </style>
</head>
<body class="text-charcoal font-sans antialiased">

  <!-- ========================================== -->
  <!-- PÁGINA 1: PORTADA EJECUTIVA Y RESUMEN     -->
  <!-- ========================================== -->
  <div class="page-container flex flex-col justify-between">
    <div>
      <!-- Header Superior con Logo y Slogan -->
      <header class="flex items-center justify-between border-b-2 border-slate-200 pb-4 mb-5 shrink-0">
        <div class="flex items-center gap-4">
          <img src="{logo_b64}" alt="Legado Ambiental" class="h-14 w-auto object-contain">
          <div>
            <h1 class="text-navy font-black text-xl tracking-tight leading-none uppercase">Legado Ambiental</h1>
            <p class="text-[11px] font-semibold text-emerald-700 tracking-wide mt-1">Consultoría Integral &bull; Topografía &bull; Obra Civil</p>
          </div>
        </div>
        <div class="text-right">
          <span class="inline-block px-3 py-1 bg-emerald-50 text-emerald-800 border border-emerald-300 rounded-full text-[10px] font-extrabold uppercase tracking-wider">
            Documento Técnico Estratégico
          </span>
          <p class="text-[10px] text-gray-500 font-bold mt-1">Versión 1.0 &bull; Ciclo 2026</p>
        </div>
      </header>

      <!-- Barra Acento Bicolor -->
      <div class="flex h-1.5 w-full rounded-full overflow-hidden mb-6">
        <div class="w-1/2 bg-primary"></div>
        <div class="w-1/2 bg-secondary"></div>
      </div>

      <!-- Título Principal y Subtítulo Editorial -->
      <div class="mb-6">
        <span class="text-xs font-bold uppercase tracking-widest text-secondary block mb-1">Plan de Trabajo UI/UX &bull; Pilares 5 y 6</span>
        <h2 class="text-2xl font-extrabold text-navy leading-tight tracking-tight mb-2">
          Guía de Configuración e Implementación: <br>
          <span class="text-emerald-600">Google Business Profile (Pilar 5)</span> &amp; 
          <span class="text-blue-600">Google Ads Local (Pilar 6)</span>
        </h2>
        <p class="font-serif text-xs text-slate-600 italic leading-relaxed border-l-2 border-primary pl-3 py-1">
          Manual operativo y técnico para la activación de presencia local orgánica en Google Maps y captación publicitaria de alta intención B2B en el Valle de México.
        </p>
      </div>

      <!-- Ficha Técnica Institucional (Grid 2 columnas) -->
      <div class="bg-slate-50 border border-slate-200 rounded-xl p-4 mb-5">
        <h3 class="text-xs font-extrabold uppercase tracking-wider text-navy mb-3 flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-primary inline-block"></span> Ficha Técnica de la Organización
        </h3>
        <div class="grid grid-cols-2 gap-x-6 gap-y-2 text-xs">
          <div>
            <span class="text-gray-500 block font-semibold text-[10px] uppercase">Razón Social:</span>
            <strong class="text-navy">Legado Ambiental S.A. de C.V.</strong>
          </div>
          <div>
            <span class="text-gray-500 block font-semibold text-[10px] uppercase">Sede y Ubicación Oficial:</span>
            <span class="text-charcoal font-medium">U.H. Valle de Ecatepec, C.P. 55119, Edo. Méx.</span>
          </div>
          <div>
            <span class="text-gray-500 block font-semibold text-[10px] uppercase">Canales de Contacto:</span>
            <span class="text-charcoal font-medium">+52 55 8367 1036 &bull; +52 72 2672 7212</span>
          </div>
          <div>
            <span class="text-gray-500 block font-semibold text-[10px] uppercase">Portal Web &amp; Dominio:</span>
            <span class="text-emerald-700 font-bold">https://www.legadoambiental.com.mx</span>
          </div>
          <div class="col-span-2 pt-1 border-t border-slate-200">
            <span class="text-gray-500 block font-semibold text-[10px] uppercase">Meta del Proyecto:</span>
            <span class="text-charcoal font-medium">Embudo de conversión CRO para captar los primeros <strong>100 prospectos B2B cualificados</strong> (empresas constructoras, desarrolladores y dependencias públicas).</span>
          </div>
        </div>
      </div>

      <!-- Resumen Ejecutivo y Alcance -->
      <div class="mb-5">
        <h3 class="text-xs font-extrabold uppercase tracking-wider text-navy mb-2 flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-secondary inline-block"></span> Resumen Ejecutivo y Marco Estratégico
        </h3>
        <p class="text-xs text-charcoal leading-relaxed text-justify mb-2">
          El presente documento complementa el <em>Plan Estratégico de Trabajo y Arquitectura UI/UX</em>. En una capacidad de 40 horas efectivas de desarrollo, la plataforma web evoluciona de un catálogo estático a un embudo de conversión B2B. Dentro de este sistema, el <strong>Pilar 5 (SEO Local)</strong> garantiza la indexación territorial y autoridad mediante opiniones verificadas, mientras que el <strong>Pilar 6 (Google Ads Local)</strong> canaliza la demanda activa con presupuesto controlado hacia páginas de aterrizaje específicas.
        </p>
      </div>

      <!-- Tabla de Contenido Sintética -->
      <div class="border border-slate-200 rounded-xl overflow-hidden">
        <div class="bg-navy text-white text-[10px] font-bold uppercase tracking-wider px-3 py-1.5">
          Estructura del Manual Técnico
        </div>
        <div class="grid grid-cols-2 divide-x divide-slate-200 text-xs">
          <div class="p-3 bg-white">
            <strong class="text-emerald-700 block text-[11px] font-bold mb-1">PARTE 1: Google Business Profile (Pilar 5)</strong>
            <ul class="space-y-1 text-[11px] text-slate-600">
              <li>&bull; 1.1 Verificación de ficha en México (video/código)</li>
              <li>&bull; 1.2 Estandarización NAP 1:1 con sitio web</li>
              <li>&bull; 1.3 Categorías primarias y secundarias clave</li>
              <li>&bull; 1.4 Áreas de servicio (Edomex, CDMX y Nacional)</li>
              <li>&bull; 1.5 Catálogo de servicios B2B y enlaces profundos</li>
              <li>&bull; 1.6 Protocolo y plantillas de gestión de reseñas</li>
            </ul>
          </div>
          <div class="p-3 bg-white">
            <strong class="text-blue-700 block text-[11px] font-bold mb-1">PARTE 2: Google Ads Local (Pilar 6)</strong>
            <ul class="space-y-1 text-[11px] text-slate-600">
              <li>&bull; 2.1 Vinculación GBP y recursos de ubicación</li>
              <li>&bull; 2.2 Segmentación geográfica estricta (CDMX/Edomex)</li>
              <li>&bull; 2.3 Arquitectura de 4 grupos de anuncios por servicio</li>
              <li>&bull; 2.4 Matriz de palabras clave (Frase y Exacta)</li>
              <li>&bull; 2.5 Lista maestra de palabras clave negativas</li>
              <li>&bull; 2.6 Medición de conversiones, pujas y checklist</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer Página 1 -->
    <footer class="pt-3 border-t border-slate-200 flex justify-between items-center text-[10px] text-gray-500 shrink-0">
      <span>Legado Ambiental S.A. de C.V. &bull; Plan de Trabajo UI/UX 2026</span>
      <span class="font-extrabold text-navy tracking-widest uppercase">PÁGINA 1 DE 5</span>
    </footer>
  </div>

  <!-- ========================================== -->
  <!-- PÁGINA 2: PARTE 1 - GOOGLE BUSINESS PROFILE -->
  <!-- ========================================== -->
  <div class="page-container flex flex-col justify-between">
    <div>
      <!-- Header Superior -->
      <div class="flex items-center justify-between border-b border-slate-200 pb-2 mb-4 shrink-0">
        <div class="flex items-center gap-2">
          <span class="h-3 w-3 rounded-full bg-primary inline-block"></span>
          <span class="text-xs font-black text-navy uppercase tracking-wider">Parte 1: Google Business Profile (Pilar 5: SEO Local)</span>
        </div>
        <span class="text-[10px] font-bold text-gray-400 uppercase">Fundamentos &bull; Verificación &bull; NAP</span>
      </div>

      <!-- Título de Sección -->
      <h2 class="text-lg font-black text-navy mb-1 tracking-tight">1. Alta, Verificación y Datos Fundamentales de la Ficha Local</h2>
      <p class="text-xs text-slate-600 mb-4">
        Google Business Profile es el núcleo del posicionamiento en el <strong>Local 3-Pack</strong> y <strong>Google Maps</strong>. Permite captar clientes en los corredores industriales y de construcción del Valle de México.
      </p>

      <!-- 1.1 Verificación en México -->
      <div class="bg-slate-50 border border-slate-200 rounded-lg p-3 mb-4">
        <h3 class="text-xs font-bold text-navy uppercase mb-1.5 flex items-center gap-1.5">
          <span class="text-emerald-600 font-extrabold">&bull;</span> 1.1 Proceso de Creación y Verificación de Ficha
        </h3>
        <p class="text-[11px] text-charcoal leading-relaxed mb-2 text-justify">
          <strong>Acceso oficial:</strong> Iniciar sesión en <code>google.com/business</code> con <code>legado.ambiental.mx@gmail.com</code>. Registrar el nombre comercial: <strong>Legado Ambiental</strong> bajo la modalidad <em>"Empresa de servicios y oficina comercial"</em>.
        </p>
        <div class="bg-white border-l-2 border-emerald-500 p-2 rounded text-[11px] text-slate-700">
          <strong class="text-emerald-800 block mb-0.5 font-bold">Protocolo de Verificación por Video en México:</strong>
          Para empresas de servicios técnicos en el Estado de México, Google exige una grabación continua sin cortes mostrando:
          <ol class="list-decimal pl-4 space-y-0.5 mt-1">
            <li>Nomenclatura exterior de la calle y número oficial en Valle de Ecatepec.</li>
            <li>Acceso a la oficina e instalaciones interiores.</li>
            <li>Herramientas de trabajo e instrumental de campo (estación total topográfica, niveles, drones y planos con membrete oficial) junto con cédula de identificación fiscal SAT.</li>
          </ol>
        </div>
      </div>

      <!-- 1.2 Estandarización NAP -->
      <div class="mb-4">
        <h3 class="text-xs font-bold text-navy uppercase mb-1.5 flex items-center gap-1.5">
          <span class="text-emerald-600 font-extrabold">&bull;</span> 1.2 Estandarización NAP (Name, Address, Phone) 1:1
        </h3>
        <p class="text-[11px] text-charcoal mb-2">
          La coherencia exacta entre la ficha de Google y los datos del sitio web evita penalizaciones y eleva la confianza del algoritmo:
        </p>
        <div class="border border-slate-200 rounded-lg overflow-hidden text-xs">
          <table class="w-full text-left">
            <thead class="bg-navy text-white text-[10px] uppercase font-bold">
              <tr>
                <th class="p-1.5 pl-3">Parámetro</th>
                <th class="p-1.5">Configuración Oficial en GBP</th>
                <th class="p-1.5">Coincidencia en Sitio Web</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-200 text-[11px]">
              <tr class="bg-white">
                <td class="p-1.5 pl-3 font-bold text-navy">Nombre (Name)</td>
                <td class="p-1.5">Legado Ambiental</td>
                <td class="p-1.5 text-slate-600">Logo, H1 y Schema <code>legalName</code></td>
              </tr>
              <tr class="bg-slate-50">
                <td class="p-1.5 pl-3 font-bold text-navy">Dirección (Address)</td>
                <td class="p-1.5">U.H. Valle de Ecatepec, C.P. 55119, Ecatepec, Méx.</td>
                <td class="p-1.5 text-slate-600">Footer, Contacto y Schema PostalAddress</td>
              </tr>
              <tr class="bg-white">
                <td class="p-1.5 pl-3 font-bold text-navy">Teléfono Principal</td>
                <td class="p-1.5 font-mono text-emerald-700">+52 55 8367 1036 (Atención General)</td>
                <td class="p-1.5 text-slate-600">Enlace interactivo <code>tel:+525583671036</code></td>
              </tr>
              <tr class="bg-slate-50">
                <td class="p-1.5 pl-3 font-bold text-navy">Teléfono Móvil/WA</td>
                <td class="p-1.5 font-mono text-emerald-700">+52 72 2672 7212 (Ingeniería/WhatsApp)</td>
                <td class="p-1.5 text-slate-600">Enlace FAB y <code>tel:+527226727212</code></td>
              </tr>
              <tr class="bg-white">
                <td class="p-1.5 pl-3 font-bold text-navy">Sitio Web &bull; URL Citas</td>
                <td class="p-1.5 font-mono text-blue-700">https://www.legadoambiental.com.mx</td>
                <td class="p-1.5 text-slate-600">Enlace directo a <code>contact_faq.html</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- 1.3 Selección de Categorías -->
      <div class="mb-4">
        <h3 class="text-xs font-bold text-navy uppercase mb-1.5 flex items-center gap-1.5">
          <span class="text-emerald-600 font-extrabold">&bull;</span> 1.3 Selección Estratégica de Categorías en Google
        </h3>
        <div class="grid grid-cols-2 gap-3 text-[11px]">
          <div class="bg-emerald-50/70 border border-emerald-200 rounded-lg p-2.5">
            <strong class="text-emerald-800 text-xs block mb-1 font-bold">Categoría Primaria (Mayor Peso SEO):</strong>
            <span class="text-navy font-extrabold text-sm block mb-1">Consultor ambiental</span>
            <p class="text-slate-600 text-[10px] leading-tight">
              Alinea el negocio a búsquedas de Manifestación de Impacto Ambiental (MIA), autorizaciones SEMARNAT, licencias y normativas hídricas.
            </p>
          </div>
          <div class="bg-slate-50 border border-slate-200 rounded-lg p-2.5">
            <strong class="text-navy text-xs block mb-1 font-bold">Categorías Secundarias (4 Especialidades):</strong>
            <ul class="space-y-0.5 text-[10px] text-slate-700">
              <li><strong>1. Ingeniero consultor:</strong> Proyectos ejecutivos e ingeniería.</li>
              <li><strong>2. Empresa constructora:</strong> Obra civil, vivienda y saneamiento.</li>
              <li><strong>3. Agrimensor (Topógrafo):</strong> Levantamientos y fotogrametría.</li>
              <li><strong>4. Control de seguridad laboral:</strong> Capacitación STPS / DC-3.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- 1.4 Delimitación de Áreas de Servicio -->
      <div>
        <h3 class="text-xs font-bold text-navy uppercase mb-1.5 flex items-center gap-1.5">
          <span class="text-emerald-600 font-extrabold">&bull;</span> 1.4 Definición de Áreas de Servicio (Service Area Business)
        </h3>
        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2.5 text-[11px] leading-relaxed">
          <p class="mb-1 text-slate-700">
            <strong>Estado de México (Corredores prioritarios):</strong> Ecatepec de Morelos, Tlalnepantla de Baz, Naucalpan de Juárez, Cuautitlán Izcalli, Tultitlán, Tecámac, Coacalco, Toluca, Lerma, Texcoco, Nezahualcóyotl.
          </p>
          <p class="mb-1 text-slate-700">
            <strong>Ciudad de México (Alcaldías clave):</strong> Gustavo A. Madero, Azcapotzalco, Cuauhtémoc, Miguel Hidalgo, Álvaro Obregón, Benito Juárez, Venustiano Carranza, Iztapalapa.
          </p>
          <p class="text-slate-700">
            <strong>Cobertura Nacional:</strong> Registrar <em>México</em> para respaldar licitaciones y obras federales fuera de la zona metropolitana.
          </p>
        </div>
      </div>
    </div>

    <!-- Footer Página 2 -->
    <footer class="pt-3 border-t border-slate-200 flex justify-between items-center text-[10px] text-gray-500 shrink-0">
      <span>Legado Ambiental S.A. de C.V. &bull; Plan de Trabajo UI/UX 2026</span>
      <span class="font-extrabold text-navy tracking-widest uppercase">PÁGINA 2 DE 5</span>
    </footer>
  </div>

  <!-- ========================================== -->
  <!-- PÁGINA 3: PARTE 1 - SERVICIOS Y RESEÑAS    -->
  <!-- ========================================== -->
  <div class="page-container flex flex-col justify-between">
    <div>
      <!-- Header Superior -->
      <div class="flex items-center justify-between border-b border-slate-200 pb-2 mb-4 shrink-0">
        <div class="flex items-center gap-2">
          <span class="h-3 w-3 rounded-full bg-primary inline-block"></span>
          <span class="text-xs font-black text-navy uppercase tracking-wider">Parte 1: Google Business Profile (Pilar 5: SEO Local)</span>
        </div>
        <span class="text-[10px] font-bold text-gray-400 uppercase">Servicios &bull; Multimedia &bull; Reseñas</span>
      </div>

      <h2 class="text-lg font-black text-navy mb-1 tracking-tight">2. Catálogo de Servicios, Activos Visuales y Gestión de Reseñas</h2>
      <p class="text-xs text-slate-600 mb-4">
        Estructuración del inventario técnico y protocolo de captación de prueba social para maximizar la tasa de conversión B2B.
      </p>

      <!-- 1.5 Catálogo de Servicios en GBP -->
      <div class="mb-4">
        <h3 class="text-xs font-bold text-navy uppercase mb-1.5 flex items-center gap-1.5">
          <span class="text-emerald-600 font-extrabold">&bull;</span> 1.5 Catálogo de Servicios y Productos B2B en GBP
        </h3>
        <div class="grid grid-cols-2 gap-2 text-[11px]">
          <div class="border border-slate-200 rounded-lg p-2.5 bg-white">
            <span class="font-bold text-navy block text-xs mb-0.5">1. Impacto Ambiental (MIA)</span>
            <p class="text-[10px] text-slate-600 leading-tight mb-1.5">
              Estudios técnicos justificativos, diagnósticos de daño y cumplimiento NOM-052-SEMARNAT / NOM-001.
            </p>
            <span class="text-[9px] font-mono text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200">
              services.html#tab-1
            </span>
          </div>
          <div class="border border-slate-200 rounded-lg p-2.5 bg-white">
            <span class="font-bold text-navy block text-xs mb-0.5">2. Topografía de Precisión</span>
            <p class="text-[10px] text-slate-600 leading-tight mb-1.5">
              Levantamientos con dron, fotogrametría, curvas de nivel, deslindes catastrales y GPS geodésico.
            </p>
            <span class="text-[9px] font-mono text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200">
              services.html#tab-3
            </span>
          </div>
          <div class="border border-slate-200 rounded-lg p-2.5 bg-white">
            <span class="font-bold text-navy block text-xs mb-0.5">3. Saneamiento &amp; Plantas PTAR</span>
            <p class="text-[10px] text-slate-600 leading-tight mb-1.5">
              Diseño, construcción y rehabilitación de plantas de tratamiento de agua residual y redes de drenaje.
            </p>
            <span class="text-[9px] font-mono text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200">
              services.html#tab-2
            </span>
          </div>
          <div class="border border-slate-200 rounded-lg p-2.5 bg-white">
            <span class="font-bold text-navy block text-xs mb-0.5">4. Seguridad STPS / DC-3</span>
            <p class="text-[10px] text-slate-600 leading-tight mb-1.5">
              Capacitación por Agente Capacitador Externo (ACE), constancias DC-3 y planes de seguridad en obra.
            </p>
            <span class="text-[9px] font-mono text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200">
              services.html#tab-4
            </span>
          </div>
        </div>
      </div>

      <!-- 1.6 Activos Multimedia y SEO de Fotos -->
      <div class="bg-slate-50 border border-slate-200 rounded-lg p-3 mb-4 text-[11px]">
        <h3 class="text-xs font-bold text-navy uppercase mb-1.5 flex items-center gap-1.5">
          <span class="text-emerald-600 font-extrabold">&bull;</span> 1.6 Activos Multimedia y Nomenclatura SEO de Fotografías
        </h3>
        <p class="text-slate-700 leading-relaxed mb-2">
          Subir fotografías reales de alta resolución optimizadas: logotipo oficial (<code>logo_final_v2.webp</code>), portada (<code>servicios-legado-ambiental-2026-og.png</code>), ingenieros en campo con Equipo de Protección Personal (EPP: chaleco y casco) e instrumental técnico (estación total y dron).
        </p>
        <div class="bg-white p-2 rounded border border-slate-200 text-[10px] font-mono text-slate-600">
          <strong>Nombres semánticos requeridos:</strong><br>
          &bull; <code>levantamiento-topografico-estado-de-mexico-legado-ambiental.jpg</code><br>
          &bull; <code>estudio-impacto-ambiental-semarnat-ecatepec.jpg</code><br>
          &bull; <code>supervision-obra-civil-capacitacion-stps.jpg</code>
        </div>
      </div>

      <!-- 1.7 Protocolo de Reseñas -->
      <div class="border border-slate-200 rounded-lg p-3 bg-white mb-4">
        <h3 class="text-xs font-bold text-navy uppercase mb-1 flex items-center justify-between">
          <span class="flex items-center gap-1.5"><span class="text-emerald-600 font-extrabold">&bull;</span> 1.7 Protocolo Sistemático de Gestión de Reseñas</span>
          <span class="text-[10px] font-extrabold text-amber-600 bg-amber-50 px-2 py-0.5 rounded border border-amber-200">5.0 ESTRELLAS</span>
        </h3>
        <p class="text-[11px] text-charcoal mb-2">
          <strong>Obtención del enlace corto:</strong> En el panel de GBP, copiar el enlace único: <code>https://g.page/r/[CODIGO]/review</code>.
        </p>

        <!-- Plantilla WhatsApp -->
        <div class="bg-slate-50 border-l-2 border-primary p-2.5 rounded mb-2 text-[10px]">
          <strong class="text-navy block font-bold mb-1">Plantilla de Solicitud (WhatsApp / Email post-entrega de proyecto):</strong>
          <p class="italic text-slate-700 leading-relaxed">
            "Estimado/a [Nombre]: Ha sido un gusto colaborar con [Empresa] en [servicio, ej. el levantamiento topográfico para su obra en Ecatepec]. Para nuestro equipo técnico es muy valioso conocer su experiencia. ¿Podría apoyarnos con una breve reseña de 1 minuto en Google? Su opinión ayuda a que otras constructoras conozcan nuestro rigor técnico: [ENLACE CORTO DE RESEÑAS]. ¡Agradecemos su confianza!"
          </p>
        </div>

        <!-- Protocolo de Respuesta -->
        <div class="bg-slate-50 border-l-2 border-secondary p-2.5 rounded text-[10px]">
          <strong class="text-navy block font-bold mb-1">Protocolo de Respuesta Profesional (con Keywords Locales &bull; &lt; 24h):</strong>
          <p class="italic text-slate-700 leading-relaxed">
            "Muchas gracias por su confianza, Ing. [Apellido]. En Legado Ambiental nos comprometemos con la máxima exactitud en cada levantamiento topográfico y trámite normativo en el Estado de México. Quedamos a su disposición para las siguientes etapas constructivas de su proyecto."
          </p>
        </div>
      </div>

      <!-- 1.8 Publicaciones Periódicas -->
      <div class="bg-emerald-50/60 border border-emerald-200 rounded-lg p-2.5 text-[11px]">
        <h3 class="text-xs font-bold text-emerald-900 uppercase mb-1 flex items-center gap-1.5">
          <span class="text-emerald-600 font-extrabold">&bull;</span> 1.8 Publicaciones Semanales (Google Updates)
        </h3>
        <p class="text-slate-700 leading-tight">
          Publicar 1 actualización semanal con casos de éxito o síntesis normativas (NOM-001, NOM-052 o inspecciones STPS) integrando botones de acción: <em>"Más información"</em> dirigiendo a <code>services.html</code> o <em>"Llamar ahora"</em>.
        </p>
      </div>
    </div>

    <!-- Footer Página 3 -->
    <footer class="pt-3 border-t border-slate-200 flex justify-between items-center text-[10px] text-gray-500 shrink-0">
      <span>Legado Ambiental S.A. de C.V. &bull; Plan de Trabajo UI/UX 2026</span>
      <span class="font-extrabold text-navy tracking-widest uppercase">PÁGINA 3 DE 5</span>
    </footer>
  </div>

  <!-- ========================================== -->
  <!-- PÁGINA 4: PARTE 2 - GOOGLE ADS LOCAL       -->
  <!-- ========================================== -->
  <div class="page-container flex flex-col justify-between">
    <div>
      <!-- Header Superior -->
      <div class="flex items-center justify-between border-b border-slate-200 pb-2 mb-4 shrink-0">
        <div class="flex items-center gap-2">
          <span class="h-3 w-3 rounded-full bg-secondary inline-block"></span>
          <span class="text-xs font-black text-navy uppercase tracking-wider">Parte 2: Google Ads Local (Pilar 6: Adquisición Pagada)</span>
        </div>
        <span class="text-[10px] font-bold text-gray-400 uppercase">Campaña &bull; Segmentación &bull; Keywords</span>
      </div>

      <h2 class="text-lg font-black text-navy mb-1 tracking-tight">3. Arquitectura de Campaña, Segmentación y Matriz de Palabras Clave</h2>
      <p class="text-xs text-slate-600 mb-4">
        Campaña diferida para la fase post-proyecto (Semana 3), diseñada para capturar demanda transaccional de alta intención en CDMX y Edomex.
      </p>

      <!-- 2.1 y 2.2 Vinculación y Segmentación -->
      <div class="grid grid-cols-2 gap-3 mb-4 text-[11px]">
        <div class="bg-slate-50 border border-slate-200 rounded-lg p-3">
          <strong class="text-navy text-xs block mb-1 font-bold">2.1 Vinculación Google Ads + GBP:</strong>
          <p class="text-slate-600 leading-relaxed">
            Vincular la cuenta en <em>Cuentas Vinculadas &gt; Google Business Profile</em> para habilitar los <strong>Recursos de Ubicación</strong> (Location Assets). Permite que los anuncios muestren la dirección física y aparezcan en Google Maps.
          </p>
        </div>
        <div class="bg-slate-50 border border-slate-200 rounded-lg p-3">
          <strong class="text-navy text-xs block mb-1 font-bold">2.2 Segmentación Geográfica Estricta:</strong>
          <p class="text-slate-600 leading-relaxed">
            Red de Búsqueda (Search) &bull; Objetivo: Clientes potenciales. Ubicaciones: <strong>Estado de México y Ciudad de México</strong>. Seleccionar estrictamente: <em>"Presencia: Personas que se encuentran en tus ubicaciones incluidas"</em>.
          </p>
        </div>
      </div>

      <!-- 2.3 Estructura de Grupos de Anuncios -->
      <div class="mb-4">
        <h3 class="text-xs font-bold text-navy uppercase mb-1.5 flex items-center gap-1.5">
          <span class="text-blue-600 font-extrabold">&bull;</span> 2.3 Estructura de 4 Grupos de Anuncios por Intención B2B
        </h3>
        <div class="grid grid-cols-4 gap-2 text-center text-[10px]">
          <div class="bg-white border border-slate-200 rounded-lg p-2 shadow-sm">
            <span class="font-extrabold text-navy block text-[11px] mb-1">G1: Impacto Ambiental</span>
            <span class="text-gray-500 block text-[9px] mb-1">MIA, SEMARNAT, NOM</span>
            <span class="font-mono text-emerald-700 bg-slate-50 px-1 py-0.5 rounded text-[8px] border border-slate-200 block">
              services.html#tab-1
            </span>
          </div>
          <div class="bg-white border border-slate-200 rounded-lg p-2 shadow-sm">
            <span class="font-extrabold text-navy block text-[11px] mb-1">G2: Topografía de Obra</span>
            <span class="text-gray-500 block text-[9px] mb-1">Levantamientos, Dron, Curvas</span>
            <span class="font-mono text-emerald-700 bg-slate-50 px-1 py-0.5 rounded text-[8px] border border-slate-200 block">
              services.html#tab-3
            </span>
          </div>
          <div class="bg-white border border-slate-200 rounded-lg p-2 shadow-sm">
            <span class="font-extrabold text-navy block text-[11px] mb-1">G3: Saneamiento y PTAR</span>
            <span class="text-gray-500 block text-[9px] mb-1">Plantas Tratamiento, Agua</span>
            <span class="font-mono text-emerald-700 bg-slate-50 px-1 py-0.5 rounded text-[8px] border border-slate-200 block">
              services.html#tab-2
            </span>
          </div>
          <div class="bg-white border border-slate-200 rounded-lg p-2 shadow-sm">
            <span class="font-extrabold text-navy block text-[11px] mb-1">G4: Seguridad STPS</span>
            <span class="text-gray-500 block text-[9px] mb-1">Cursos ACE, Constancias DC-3</span>
            <span class="font-mono text-emerald-700 bg-slate-50 px-1 py-0.5 rounded text-[8px] border border-slate-200 block">
              services.html#tab-4
            </span>
          </div>
        </div>
      </div>

      <!-- 2.4 Matriz de Palabras Clave Positivas -->
      <div class="mb-4">
        <h3 class="text-xs font-bold text-navy uppercase mb-1.5 flex items-center gap-1.5">
          <span class="text-blue-600 font-extrabold">&bull;</span> 2.4 Matriz de Palabras Clave Positivas (Concordancia Frase y Exacta)
        </h3>
        <div class="grid grid-cols-2 gap-2 text-[10px]">
          <div class="bg-slate-50 border border-slate-200 rounded-lg p-2.5">
            <strong class="text-navy block font-bold mb-1">G1: Impacto Ambiental (Búsquedas Transaccionales)</strong>
            <ul class="font-mono text-slate-700 space-y-0.5 text-[9.5px]">
              <li>&bull; "estudio de impacto ambiental estado de mexico"</li>
              <li>&bull; "manifestacion de impacto ambiental semarnat cdmx"</li>
              <li>&bull; "consultoria ambiental para empresas"</li>
              <li>&bull; [estudio de impacto ambiental costo]</li>
            </ul>
          </div>
          <div class="bg-slate-50 border border-slate-200 rounded-lg p-2.5">
            <strong class="text-navy block font-bold mb-1">G2: Topografía y Fotogrametría</strong>
            <ul class="font-mono text-slate-700 space-y-0.5 text-[9.5px]">
              <li>&bull; "levantamiento topografico para obra"</li>
              <li>&bull; "topografia con dron estado de mexico"</li>
              <li>&bull; "servicios de topografia cdmx"</li>
              <li>&bull; [brigada de topografia cotizacion]</li>
            </ul>
          </div>
          <div class="bg-slate-50 border border-slate-200 rounded-lg p-2.5">
            <strong class="text-navy block font-bold mb-1">G3: Saneamiento y Plantas PTAR</strong>
            <ul class="font-mono text-slate-700 space-y-0.5 text-[9.5px]">
              <li>&bull; "construccion de plantas de tratamiento de aguas"</li>
              <li>&bull; "diseno de ptar industrial"</li>
              <li>&bull; "obras de saneamiento y drenaje"</li>
              <li>&bull; [mantenimiento de plantas de aguas residuales]</li>
            </ul>
          </div>
          <div class="bg-slate-50 border border-slate-200 rounded-lg p-2.5">
            <strong class="text-navy block font-bold mb-1">G4: Seguridad e Higiene STPS</strong>
            <ul class="font-mono text-slate-700 space-y-0.5 text-[9.5px]">
              <li>&bull; "cursos stps constancia dc3"</li>
              <li>&bull; "capacitacion en seguridad e higiene para obra"</li>
              <li>&bull; "asesoria en seguridad y salud en el trabajo"</li>
              <li>&bull; [agente capacitador externo stps]</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- 2.5 Palabras Clave Negativas -->
      <div class="border border-red-200 bg-red-50/50 rounded-lg p-2.5 text-[11px]">
        <h3 class="text-xs font-bold text-red-900 uppercase mb-1 flex items-center justify-between">
          <span>&bull; 2.5 Lista Maestra de Palabras Clave Negativas (Blindaje de Pauta)</span>
          <span class="text-[9px] font-mono text-red-700 uppercase font-bold">Nivel de Campaña</span>
        </h3>
        <p class="text-[10px] text-red-800 mb-1.5">
          Excluir de inmediato para evitar clics de estudiantes, postulantes de empleo o usuarios sin presupuesto comercial:
        </p>
        <p class="font-mono text-[9px] text-red-700 leading-relaxed bg-white p-2 rounded border border-red-200">
          -gratis, -empleo, -vacantes, -bolsa de trabajo, -sueldo, -salario, -que es, -definicion, -wikipedia, -tarea, -universidad, -carrera, -tesis, -pdf libro, -descargar gratis, -curso gratis, -practicas profesionales, -servicio social, -diplomado gratis
        </p>
      </div>
    </div>

    <!-- Footer Página 4 -->
    <footer class="pt-3 border-t border-slate-200 flex justify-between items-center text-[10px] text-gray-500 shrink-0">
      <span>Legado Ambiental S.A. de C.V. &bull; Plan de Trabajo UI/UX 2026</span>
      <span class="font-extrabold text-navy tracking-widest uppercase">PÁGINA 4 DE 5</span>
    </footer>
  </div>

  <!-- ========================================== -->
  <!-- PÁGINA 5: PARTE 2 - ANUNCIOS Y CIERRE       -->
  <!-- ========================================== -->
  <div class="page-container flex flex-col justify-between">
    <div>
      <!-- Header Superior -->
      <div class="flex items-center justify-between border-b border-slate-200 pb-2 mb-4 shrink-0">
        <div class="flex items-center gap-2">
          <span class="h-3 w-3 rounded-full bg-secondary inline-block"></span>
          <span class="text-xs font-black text-navy uppercase tracking-wider">Parte 2: Google Ads Local (Pilar 6: Adquisición Pagada)</span>
        </div>
        <span class="text-[10px] font-bold text-gray-400 uppercase">Anuncios &bull; Conversiones &bull; Pujas</span>
      </div>

      <h2 class="text-lg font-black text-navy mb-1 tracking-tight">4. Anuncios Responsivos, Trazabilidad, Puja y Checklist</h2>
      <p class="text-xs text-slate-600 mb-3">
        Configuración de anuncios con enfoque Jobs-to-be-Done (JTBD), medición de conversiones y presupuesto de lanzamiento.
      </p>

      <!-- 2.6 y 2.7 Anuncios RSAs y Extensiones -->
      <div class="grid grid-cols-2 gap-3 mb-3 text-[11px]">
        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2.5">
          <strong class="text-navy text-xs block mb-1 font-bold">2.6 Anuncios de Búsqueda Responsivos (RSAs):</strong>
          <span class="text-[10px] text-gray-500 font-semibold block mb-1">Títulos (30 caracteres máx. c/u):</span>
          <ul class="text-[9.5px] text-slate-700 space-y-0.5 mb-1.5 font-medium">
            <li>&bull; Estudios de Impacto Ambiental &bull; Consultoría Ambiental B2B</li>
            <li>&bull; Cumplimiento NOM y SEMARNAT &bull; Legado Ambiental S.A.</li>
            <li>&bull; Dictámenes y Trámites MIA &bull; Cotiza tu Estudio Ambiental</li>
          </ul>
          <span class="text-[10px] text-gray-500 font-semibold block mb-0.5">Descripciones (90 caracteres máx. c/u):</span>
          <p class="text-[9px] italic text-slate-600 leading-tight">
            "Soluciones integrales en estudios ambientales y trámites normativos. Cotiza tu proyecto."<br>
            "Más de 20 años respaldando a constructoras e industrias en CDMX y Edomex. Atención técnica."
          </p>
        </div>

        <div class="bg-slate-50 border border-slate-200 rounded-lg p-2.5">
          <strong class="text-navy text-xs block mb-1 font-bold">2.7 Recursos / Extensiones Obligatorios:</strong>
          <ul class="text-[10px] text-slate-700 space-y-1">
            <li><strong>&bull; Recurso de Ubicación:</strong> Conectado a la ficha de GBP.</li>
            <li><strong>&bull; Recurso de Llamada:</strong> Teléfono directo <code>+52 55 8367 1036</code>.</li>
            <li><strong>&bull; Enlaces de Sitio (Sitelinks):</strong> Cotizar Proyecto, Topografía de Obra, Portafolio PDF, Quiénes Somos.</li>
            <li><strong>&bull; Textos Destacados:</strong> +20 Años Experiencia, Agente STPS, Cobertura CDMX/Edomex, Respuesta 24h.</li>
          </ul>
        </div>
      </div>

      <!-- 2.8 Medición y Atribución -->
      <div class="mb-3">
        <h3 class="text-xs font-bold text-navy uppercase mb-1.5 flex items-center gap-1.5">
          <span class="text-blue-600 font-extrabold">&bull;</span> 2.8 Medición y Atribución de Conversiones (Integradas al Sitio Web)
        </h3>
        <div class="border border-slate-200 rounded-lg overflow-hidden text-xs">
          <table class="w-full text-left">
            <thead class="bg-navy text-white text-[9.5px] uppercase font-bold">
              <tr>
                <th class="p-1 pl-2.5">Acción de Conversión</th>
                <th class="p-1">Evento en Código Web</th>
                <th class="p-1">Trazabilidad Técnica</th>
                <th class="p-1">Valor Asignado</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-200 text-[10px]">
              <tr class="bg-white">
                <td class="p-1 pl-2.5 font-bold text-navy">Envío Formulario de Cotización</td>
                <td class="p-1 font-mono text-emerald-700">generate_lead</td>
                <td class="p-1 text-slate-600">Captura gclid y envía a formsubmit.co</td>
                <td class="p-1 font-bold text-slate-800">$500 MXN</td>
              </tr>
              <tr class="bg-slate-50">
                <td class="p-1 pl-2.5 font-bold text-navy">Llamada Telefónica Directa</td>
                <td class="p-1 font-mono text-blue-700">click_phone</td>
                <td class="p-1 text-slate-600">Auto-tracking en enlaces tel:+52...</td>
                <td class="p-1 font-bold text-slate-800">$300 MXN</td>
              </tr>
              <tr class="bg-white">
                <td class="p-1 pl-2.5 font-bold text-navy">Clic Inicio Chat WhatsApp</td>
                <td class="p-1 font-mono text-emerald-700">click_whatsapp</td>
                <td class="p-1 text-slate-600">Tracking enlaces wa.me con mensaje</td>
                <td class="p-1 font-bold text-slate-800">$250 MXN</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- 2.9 Estrategia de Puja y Presupuesto -->
      <div class="bg-blue-50/60 border border-blue-200 rounded-lg p-2.5 mb-3 text-[11px]">
        <h3 class="text-xs font-bold text-blue-900 uppercase mb-1 flex items-center justify-between">
          <span>&bull; 2.9 Estrategia de Puja y Presupuesto Recomendado</span>
          <span class="text-[9px] font-bold text-blue-700 bg-white px-2 py-0.5 rounded border border-blue-200">Fase Post-Proyecto (Semana 3)</span>
        </h3>
        <div class="grid grid-cols-2 gap-2 text-[10px] text-slate-700 mt-1">
          <div>
            <strong>Fase 1 (Semanas 3 a 5 &bull; Aprendizaje):</strong>
            <p class="leading-tight text-slate-600">
              Estrategia <em>Maximizar Clics</em> con límite de CPC máximo de <strong>$18.00 a $25.00 MXN</strong>.<br>
              Presupuesto sugerido: <strong>$150 a $250 MXN/día</strong> ($4,500 a $7,500 MXN/mes).
            </p>
          </div>
          <div>
            <strong>Fase 2 (Optimizada &bull; &gt; 30 Conversiones):</strong>
            <p class="leading-tight text-slate-600">
              Migración a <em>Maximizar Conversiones</em> con CPA objetivo (~$120.00 MXN por lead cualificado).
            </p>
          </div>
        </div>
      </div>

      <!-- 2.10 Checklist de Ejecución -->
      <div class="border border-slate-200 rounded-lg p-2.5 bg-slate-50 text-[10px]">
        <h3 class="text-[11px] font-extrabold uppercase tracking-wider text-navy mb-1.5">
          Checklist Ejecutivo de Activación (Pilares 5 y 6)
        </h3>
        <div class="grid grid-cols-2 gap-2 text-slate-700">
          <div>
            <strong class="text-emerald-800 block text-[10px] mb-0.5">&bull; Inmediato (Google Business Profile):</strong>
            <ul class="space-y-0.5 text-[9px]">
              <li>[X] Schema.org LocalBusiness enriquecido en 6 páginas web.</li>
              <li>[X] Componente de Reseñas de Google integrado en contacto.</li>
              <li>[ ] Grabar video de verificación en oficinas de Ecatepec.</li>
              <li>[ ] Cargar fotos técnicas con EPP y solicitar 5 primeras reseñas.</li>
            </ul>
          </div>
          <div>
            <strong class="text-blue-800 block text-[10px] mb-0.5">&bull; Semana 3 (Google Ads Local):</strong>
            <ul class="space-y-0.5 text-[9px]">
              <li>[X] Captura de gclid y UTMs en formulario lista en código web.</li>
              <li>[X] Auto-tracking de llamadas telefónicas activo en analytics.js.</li>
              <li>[ ] Vincular cuenta de Google Ads con GBP verificada.</li>
              <li>[ ] Cargar 4 grupos de anuncios con lista de palabras negativas.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer Página 5 -->
    <footer class="pt-3 border-t border-slate-200 flex justify-between items-center text-[10px] text-gray-500 shrink-0">
      <span>Legado Ambiental S.A. de C.V. &bull; Plan de Trabajo UI/UX 2026</span>
      <span class="font-extrabold text-navy tracking-widest uppercase">PÁGINA 5 DE 5</span>
    </footer>
  </div>

</body>
</html>
"""

with open('assets/docs/Guia_Estrategica_Google_Business_Profile_y_Ads_Local.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML generated successfully: assets/docs/Guia_Estrategica_Google_Business_Profile_y_Ads_Local.html")

# Render to PDF using Chrome headless
cmd = [
    'google-chrome',
    '--headless',
    '--disable-gpu',
    '--no-pdf-header-footer',
    '--virtual-time-budget=5000',
    '--run-all-compositor-stages-before-draw',
    '--print-to-pdf=assets/docs/Guia_Estrategica_Google_Business_Profile_y_Ads_Local.pdf',
    'assets/docs/Guia_Estrategica_Google_Business_Profile_y_Ads_Local.html'
]

print("Running command:", " ".join(cmd))
res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)
print("Stdout:", res.stdout)
print("Stderr:", res.stderr)

pdf_path = 'assets/docs/Guia_Estrategica_Google_Business_Profile_y_Ads_Local.pdf'
if os.path.exists(pdf_path):
    size_kb = os.path.getsize(pdf_path) / 1024
    print(f"SUCCESS: PDF created at {pdf_path} ({size_kb:.1f} KB)")
else:
    print("ERROR: PDF was not created!")
