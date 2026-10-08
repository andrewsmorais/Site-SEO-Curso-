with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

header_old = """<div class="w-6 h-6 bg-gold rounded-sm"></div>"""
header_new = """<div class="w-8 h-8 rounded-full bg-white flex items-center justify-center shadow-lg"><img src="./assets/google-logo.png" alt="Google Logo" class="w-6 h-6 object-contain"></div>"""
html = html.replace(header_old, header_new)

footer_old = """            <a href="#top" class="text-white font-bold text-xl flex items-center gap-2 justify-center hover:text-gold transition">
                DOMINANDO GOOGLE SEARCH 2026
            </a>"""
footer_new = """            <a href="#top" class="text-white font-bold text-xl flex items-center gap-2 justify-center hover:text-gold transition">
                <div class="w-6 h-6 rounded-full bg-white flex items-center justify-center opacity-90"><img src="./assets/google-logo.png" alt="Google Logo" class="w-4 h-4 object-contain"></div>
                DOMINANDO GOOGLE SEARCH 2026
            </a>"""
html = html.replace(footer_old, footer_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
