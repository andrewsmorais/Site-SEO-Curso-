with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove Kiwify Info box
kiwify_box = """            <!-- Kiwify Info -->
            <div class="mt-8 bg-gray-50 p-4 rounded-xl flex items-center justify-center gap-4 border border-gray-200">
                <div class="text-blue bg-white p-2.5 rounded-full shadow-sm shrink-0">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                </div>
                <div class="text-left">
                    <div class="text-sm font-bold text-navy-900">Download imediato</div>
                    <div class="text-xs text-gray-500 mt-0.5">Baixe os materiais direto na plataforma da Kiwify.</div>
                </div>
            </div>"""

html = html.replace(kiwify_box, "")


# Highlight the discount badge
old_badge = """<div class="inline-block bg-red-50 text-red-500 text-xs font-black tracking-wide px-3 py-1.5 rounded-full mb-4 border border-red-100">HOJE COM DESCONTO</div>
                <div class="text-gray-400 line-through font-medium mb-1">De R$ 97,00</div>"""

new_badge = """<div class="inline-block bg-red-600 text-white text-sm font-black tracking-widest px-5 py-2 rounded-full mb-4 shadow-lg shadow-red-600/30 animate-pulse">HOJE COM DESCONTO</div>
                <div class="text-gray-500 line-through font-bold text-lg mb-1">De R$ 97,00</div>"""

html = html.replace(old_badge, new_badge)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
