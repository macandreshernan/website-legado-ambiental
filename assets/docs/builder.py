import re

with open('Curricula_Legado_Ambiental_2026.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract blocks precisely by finding their known HTML strings
def extract(start_str, end_str):
    idx1 = html.find(start_str)
    if idx1 == -1: print(f"Could not find start: {start_str[:30]}"); return ""
    idx2 = html.find(end_str, idx1)
    if idx2 == -1: print(f"Could not find end: {end_str[:30]}"); return ""
    return html[idx1:idx2 + len(end_str)]

header = extract('<header class="flex', '</header>')
datos_generales = extract('<!-- Empresa y Registros -->', '</div>\n      </div>')
# Rebuild the Datos Generales full block (header to end)
datos_generales_full = f"""    <section class="mb-4 shrink-0">
      <h2 class="text-lg font-bold text-navy mb-2 flex items-center gap-2">
        <span class="w-6 h-1 bg-secondary rounded-full"></span> Datos Generales
      </h2>
      
      <div class="bg-slate-50 rounded-lg p-3 border border-slate-200 mb-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          
{datos_generales.split('<!-- Especialidad -->')[0]}        </div>
      </div>
"""

especialidad = extract('<!-- Especialidad -->', '</div>\n\n        </div>')
especialidad_full = f"""      <!-- Giro / Especialidad (Full width) -->
      <div class="bg-slate-50 rounded-lg p-4 border border-slate-200">
        <p class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-2">Giro / Especialidad</p>
        <p class="text-sm text-charcoal leading-relaxed">
          <strong class="text-primary">INGENIERÍA AMBIENTAL:</strong> Estudios y proyectos en materia de agua potable, agua residual y manejo integral de residuos.<br>
          <span class="block h-2"></span>
          <strong class="text-secondary">INGENIERÍA CIVIL:</strong> Estudios, proyectos, supervisión, rehabilitación y construcción de obras hidráulicas y de tratamiento de agua residual.
        </p>
      </div>
    </section>"""

saneamiento = extract('<!-- SANEAMIENTO AMBIENTAL -->', '</div>\n      </div>')
nogver_elogim = extract('<!-- NOGVER & GRUPO ELOGIM -->', '</div>\n      </div>')
corporativos = extract('<!-- XEROX & TELCEL & TEPJF -->', '</div>\n      </div>')
industriales = extract('<!-- FIBRAND\'S', '</div>\n      </div>')
diag1 = extract('<!-- DIAGNOSTICOS AMBIENTALES Y PTAR -->', '</div>\n      </div>')
diag2 = extract('<!-- DIAGNOSTICOS AMBIENTALES Y PTAR PARTE 2 -->', '</div>\n      </div>')
agua = extract('<!-- COINPRO & VASCONIA (Agua) -->', '</div>\n      </div>')
institucional = extract('<!-- INSTITUCIONES, IPN, IMMSA -->', '</div>\n      </div>')
proteccion = extract('<!-- ESTUDIOS HIDROMETEOROLOGICOS -->', '</div>\n      </div>')

def page_wrap(num, content, include_title_civil=False, include_title_medio=False):
    title_civil = """      <h2 class="text-lg font-bold text-navy mb-3 flex items-center gap-2">
        <span class="w-6 h-1 bg-primary rounded-full"></span> Trabajos Relacionados con Ingeniería Civil y Construcción
      </h2>
""" if include_title_civil else ""
    title_medio = """      <h2 class="text-lg font-bold text-navy mb-3 flex items-center gap-2">
        <span class="w-6 h-1 bg-primary rounded-full"></span> Medio Ambiente e Ingeniería Ambiental
      </h2>
""" if include_title_medio else ""
    title_proteccion = """      <h2 class="text-lg font-bold text-navy mb-3 flex items-center gap-2">
        <span class="w-6 h-1 bg-primary rounded-full"></span> Protección Civil (Prevención de Inundaciones)
      </h2>
""" if "ESTUDIOS HIDROMETEOROLOGICOS" in content else ""

    footer_text = ""
    if num > 1:
        footer_text = f"""      <footer class="pt-5 border-t border-gray-200 text-center relative">
        <p class="text-xs text-gray-500">Legado Ambiental, S.A. de C.V. &bull; Derechos Reservados</p>
        <div class="absolute right-0 bottom-0 pt-5">
          <span class="text-xs font-bold text-gray-400 tracking-widest">PÁGINA {num} DE 6</span>
        </div>
      </footer>"""
    else:
        footer_text = f"""      <div class="absolute right-0 bottom-0">
        <span class="text-xs font-bold text-gray-400 tracking-widest">PÁGINA {num} DE 6</span>
      </div>"""

    return f"""  <!-- PÁGINA {num} -->
  <div class="page-container">
{content if num == 1 else '    <section class="pt-4">\n' + title_civil + title_medio + title_proteccion + content + '\n    </section>'}
    <!-- Page {num} Footer -->
    <div class="absolute bottom-[15mm] left-[15mm] right-[15mm]">
{footer_text}
    </div>
  </div> <!-- FIN PÁGINA {num} -->

"""

html_top = html[:html.find('  <!-- PÁGINA 1 -->')]
html_bottom = """</body>
</html>
"""

page1_content = f"    {header}\n\n{datos_generales_full}\n{especialidad_full}"
page2_content = f"      {saneamiento}\n\n      {nogver_elogim}"
page3_content = f"      {corporativos}\n\n      {industriales}"
page4_content = f"      {diag1}\n\n      {diag2}"
page5_content = f"      {agua}\n\n      {institucional}"
page6_content = f"      {proteccion}"

new_html = html_top + \
           page_wrap(1, page1_content) + \
           page_wrap(2, page2_content, include_title_civil=True) + \
           page_wrap(3, page3_content) + \
           page_wrap(4, page4_content, include_title_medio=True) + \
           page_wrap(5, page5_content) + \
           page_wrap(6, page6_content) + \
           html_bottom

with open('Curricula_Legado_Ambiental_2026.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("6 Pages rebuilt successfully!")
