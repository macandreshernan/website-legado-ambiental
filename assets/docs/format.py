import re

with open('Curricula_Legado_Ambiental_2026.html', 'r', encoding='utf-8') as f:
    html = f.read()

def get_footer(num):
    return f"""    </section>

    <!-- Page {num} Footer -->
    <div class="absolute bottom-[15mm] left-[15mm] right-[15mm]">
      <footer class="pt-5 border-t border-gray-200 text-center relative">
        <p class="text-xs text-gray-500">Legado Ambiental, S.A. de C.V. &bull; Derechos Reservados</p>
        <div class="absolute right-0 bottom-0 pt-5">
          <span class="text-xs font-bold text-gray-400 tracking-widest">PÁGINA {num} DE 6</span>
        </div>
      </footer>
    </div>
  </div> <!-- FIN PÁGINA {num} -->

  <!-- PÁGINA {num+1} -->
  <div class="page-container">
    <section class="pt-4">
"""

# Strip all existing page breaks/footers/headers
# The easiest way is to just do targeted replaces.

# 1. Update all existing footers to DE 6 temporarily
html = re.sub(r'PÁGINA (\d) DE 5', r'PÁGINA \1 DE 6', html)

# 2. Page 1 -> Page 2 break (Before Saneamiento)
html = html.replace('    <!-- EXPERIENCE SECTION START -->\n    <section>', get_footer(1) + '    <!-- EXPERIENCE SECTION START -->')
# Note: we need to remove the old Page 1 footer
html = re.sub(r'    </section>\n\n    <!-- Page 1 Footer -->.*?</div> <!-- FIN PÁGINA 1 -->\n\n  <!-- PÁGINA 2 -->\n  <div class="page-container">\n    <section class="pt-4">', '', html, flags=re.DOTALL)

# Now Saneamiento is on P2. Nogver is also on P2.
# We need to break BEFORE Corporativos to make P3.
html = html.replace('      <!-- XEROX & TELCEL & TEPJF -->', get_footer(2) + '      <!-- XEROX & TELCEL & TEPJF -->')
# Note: we need to remove the old Page 2 footer
html = re.sub(r'    </section>\n\n    <div class="absolute bottom-\[15mm\] left-\[15mm\] right-\[15mm\]">\n      <footer class="pt-5 border-t border-gray-200 text-center relative">\n        <p class="text-xs text-gray-500">Legado Ambiental, S.A. de C.V. &bull; Derechos Reservados</p>\n        <div class="absolute right-0 bottom-0 pt-5">\n          <span class="text-xs font-bold text-gray-400 tracking-widest">PÁGINA 2 DE 6</span>\n        </div>\n      </footer>\n    </div>\n  </div> <!-- FIN PÁGINA 2 -->\n\n  <!-- PÁGINA 3 -->\n  <div class="page-container">\n    <section class="pt-4">', '', html, flags=re.DOTALL)

# Now Corporativos and Industriales are on P3.
# We need to break BEFORE Diag1 to make P4.
html = html.replace('      <h2 class="text-lg font-bold text-navy mb-3 flex items-center gap-2">\n        <span class="w-6 h-1 bg-primary rounded-full"></span> Medio Ambiente e Ingeniería Ambiental\n      </h2>', get_footer(3) + '      <h2 class="text-lg font-bold text-navy mb-3 flex items-center gap-2">\n        <span class="w-6 h-1 bg-primary rounded-full"></span> Medio Ambiente e Ingeniería Ambiental\n      </h2>')
# Remove old Page 3 footer
html = re.sub(r'    </section>\n\n    <div class="absolute bottom-\[15mm\] left-\[15mm\] right-\[15mm\]">\n      <footer class="pt-5 border-t border-gray-200 text-center relative">\n        <p class="text-xs text-gray-500">Legado Ambiental, S.A. de C.V. &bull; Derechos Reservados</p>\n        <div class="absolute right-0 bottom-0 pt-5">\n          <span class="text-xs font-bold text-gray-400 tracking-widest">PÁGINA 3 DE 6</span>\n        </div>\n      </footer>\n    </div>\n  </div> <!-- FIN PÁGINA 3 -->\n\n  <!-- PÁGINA 4 -->\n  <div class="page-container">\n    <section class="pt-4">', '', html, flags=re.DOTALL)

# Now Diag1 and Diag2 are on P4.
# We need to break BEFORE Agua to make P5.
html = html.replace('      <!-- COINPRO & VASCONIA (Agua) -->', get_footer(4) + '      <!-- COINPRO & VASCONIA (Agua) -->')
# Remove old Page 4 footer
html = re.sub(r'    </section>\n\n    <div class="absolute bottom-\[15mm\] left-\[15mm\] right-\[15mm\]">\n      <footer class="pt-5 border-t border-gray-200 text-center relative">\n        <p class="text-xs text-gray-500">Legado Ambiental, S.A. de C.V. &bull; Derechos Reservados</p>\n        <div class="absolute right-0 bottom-0 pt-5">\n          <span class="text-xs font-bold text-gray-400 tracking-widest">PÁGINA 4 DE 6</span>\n        </div>\n      </footer>\n    </div>\n  </div> <!-- FIN PÁGINA 4 -->\n\n  <!-- PÁGINA 5 -->\n  <div class="page-container">\n    <section class="pt-4">', '', html, flags=re.DOTALL)

# Now Agua and Institucional are on P5.
# The split for P6 (Proteccion Civil) was already there as old Page 5!
# But old Page 5 footer says "5 DE 6", which we need to change to "6 DE 6", and the old split needs to be replaced.
# Wait, let's just replace the old page 5 split.
html = re.sub(r'    </section>\n\n    <!-- Page 5 Footer -->.*?<!-- PÁGINA 6 -->', get_footer(5), html, flags=re.DOTALL)
# Actually, the old split was from Page 4 to Page 5, which we removed? No, the last split we handled was old P4 footer.
# Let's just fix the very last footer to PÁGINA 6 DE 6 manually.
html = html.replace('PÁGINA 5 DE 6', 'PÁGINA 6 DE 6')

with open('Curricula_Legado_Ambiental_2026.html', 'w', encoding='utf-8') as f:
    f.write(html)
