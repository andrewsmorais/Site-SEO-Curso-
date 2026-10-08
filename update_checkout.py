with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

kiwify_link = 'https://pay.kiwify.com.br/4jxsMVp'

# 1. Header button
html = html.replace(
    '<a href="#" class="bg-white text-navy-900 px-5 py-2.5 rounded font-bold text-sm hover:bg-gray-100 transition">Comprar e-book</a>',
    f'<a href="{kiwify_link}" target="_blank" class="bg-white text-navy-900 px-5 py-2.5 rounded font-bold text-sm hover:bg-gray-100 transition">Comprar e-book</a>'
)

# 2. Hero button
html = html.replace(
    '<button class="bg-gold text-navy-900 px-8 py-4 rounded font-bold text-lg w-full sm:w-auto hover:bg-yellow-400 transition shadow-[0_0_20px_rgba(244,185,66,0.3)]">\n                    COMPRAR POR R$ 19,90\n                </button>',
    f'<a href="{kiwify_link}" target="_blank" class="bg-gold text-navy-900 px-8 py-4 rounded font-bold text-lg w-full sm:w-auto hover:bg-yellow-400 transition shadow-[0_0_20px_rgba(244,185,66,0.3)] text-center inline-block">\n                    COMPRAR POR R$ 19,90\n                </a>'
)

# 3. Buy Section Button
html = html.replace(
    '<a href="#" class="inline-block bg-gold text-navy-900 px-8 py-4 rounded font-bold text-lg hover:bg-yellow-400 transition shadow-[0_0_20px_rgba(244,185,66,0.2)] w-full text-center">',
    f'<a href="{kiwify_link}" target="_blank" class="inline-block bg-gold text-navy-900 px-8 py-4 rounded font-bold text-lg hover:bg-yellow-400 transition shadow-[0_0_20px_rgba(244,185,66,0.2)] w-full text-center">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
