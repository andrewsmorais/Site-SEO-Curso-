import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Templates images CSS
html = html.replace('h-48 w-full object-cover object-top rounded-lg mb-6 border border-gray-200 shadow-sm',
                    'w-full h-auto object-contain rounded-lg mb-6 border border-gray-100 shadow-md')

# 2. FAQ section replacement
faq_new = """        <div class="space-y-4" id="duvidas">
            <details class="bg-white border border-gray-200 rounded-lg group cursor-pointer" open>
                <summary class="w-full px-6 py-5 font-bold text-navy-900 flex justify-between items-center focus:outline-none list-none marker:hidden">
                    Como aparecer no Google e como fazer SEO?
                    <span class="transition group-open:rotate-180 text-gold">
                        <svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </span>
                </summary>
                <div class="px-6 pb-5 text-gray-600 text-sm">
                    O e-book mostra como fazer SEO com pesquisa de intenção, páginas úteis, conteúdo rastreável, links internos, autoridade e medição no Search Console. Nenhuma posição é garantida, porque o resultado depende do mercado, do site e da execução.
                </div>
            </details>
            
            <details class="bg-white border border-gray-200 rounded-lg group cursor-pointer">
                <summary class="w-full px-6 py-5 font-bold text-navy-900 flex justify-between items-center focus:outline-none list-none marker:hidden">
                    Como atrair clientes pelo Google e colocar minha empresa no Google?
                    <span class="transition group-open:rotate-180 text-gold">
                        <svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </span>
                </summary>
                <div class="px-6 pb-5 text-gray-600 text-sm">
                    Você aprende a organizar páginas de serviço, oferta, prova e chamada para ação, além de entender como conectar busca orgânica, Perfil da Empresa no Google e conversões.
                </div>
            </details>
            
            <details class="bg-white border border-gray-200 rounded-lg group cursor-pointer">
                <summary class="w-full px-6 py-5 font-bold text-navy-900 flex justify-between items-center focus:outline-none list-none marker:hidden">
                    Como colocar minha loja no Google Maps?
                    <span class="transition group-open:rotate-180 text-gold">
                        <svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </span>
                </summary>
                <div class="px-6 pb-5 text-gray-600 text-sm">
                    O módulo de SEO local explica como trabalhar informações reais, categoria, serviços, área atendida, horários, fotos próprias, avaliações honestas e consistência no Perfil da Empresa no Google.
                </div>
            </details>
            
            <details class="bg-white border border-gray-200 rounded-lg group cursor-pointer">
                <summary class="w-full px-6 py-5 font-bold text-navy-900 flex justify-between items-center focus:outline-none list-none marker:hidden">
                    Como aparecer na primeira página do Google?
                    <span class="transition group-open:rotate-180 text-gold">
                        <svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </span>
                </summary>
                <div class="px-6 pb-5 text-gray-600 text-sm">
                    O método ensina diagnóstico, intenção, qualidade de conteúdo, SEO técnico, autoridade e ciclos de melhoria. A primeira página não pode ser prometida, mas o processo para melhorar a relevância fica claro.
                </div>
            </details>
            
            <details class="bg-white border border-gray-200 rounded-lg group cursor-pointer">
                <summary class="w-full px-6 py-5 font-bold text-navy-900 flex justify-between items-center focus:outline-none list-none marker:hidden">
                    Como aparecer no ChatGPT e usar o ChatGPT para empresas?
                    <span class="transition group-open:rotate-180 text-gold">
                        <svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </span>
                </summary>
                <div class="px-6 pb-5 text-gray-600 text-sm">
                    O conteúdo explica como produzir informação clara, útil, verificável e bem contextualizada para diferentes experiências de busca e resposta por IA. Não há técnica garantida para forçar uma citação.
                </div>
            </details>
            
            <details class="bg-white border border-gray-200 rounded-lg group cursor-pointer">
                <summary class="w-full px-6 py-5 font-bold text-navy-900 flex justify-between items-center focus:outline-none list-none marker:hidden">
                    Como otimizar site para o Google?
                    <span class="transition group-open:rotate-180 text-gold">
                        <svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </span>
                </summary>
                <div class="px-6 pb-5 text-gray-600 text-sm">
                    Você encontra orientações sobre indexação, arquitetura, dados estruturados coerentes, Core Web Vitals, conteúdo, acessibilidade, links e medição. O site deve ser bom para pessoas antes de ser otimizado para robôs.
                </div>
            </details>
            
            <details class="bg-white border border-gray-200 rounded-lg group cursor-pointer">
                <summary class="w-full px-6 py-5 font-bold text-navy-900 flex justify-between items-center focus:outline-none list-none marker:hidden">
                    O que é SEO na era da inteligência artificial, AEO e GEO?
                    <span class="transition group-open:rotate-180 text-gold">
                        <svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </span>
                </summary>
                <div class="px-6 pb-5 text-gray-600 text-sm">
                    SEO ajuda páginas a serem encontradas; AEO organiza respostas para perguntas; GEO, ou Generative Engine Optimization, trabalha clareza, contexto, evidência e reputação em mecanismos generativos. O e-book funciona como um método GEO IA prático, não como promessa de resultado.
                </div>
            </details>

            <details class="bg-white border border-gray-200 rounded-lg group cursor-pointer">
                <summary class="w-full px-6 py-5 font-bold text-navy-900 flex justify-between items-center focus:outline-none list-none marker:hidden">
                    Isso é um curso de GEO IA ou um guia de SEO para iniciantes?
                    <span class="transition group-open:rotate-180 text-gold">
                        <svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </span>
                </summary>
                <div class="px-6 pb-5 text-gray-600 text-sm">
                    É um e-book digital que serve como guia de SEO para iniciantes e também avança para SEO e GEO, conteúdo, autoridade, SEO local, e-commerce, medição e canais fora do Google.
                </div>
            </details>

            <details class="bg-white border border-gray-200 rounded-lg group cursor-pointer">
                <summary class="w-full px-6 py-5 font-bold text-navy-900 flex justify-between items-center focus:outline-none list-none marker:hidden">
                    O que recebo por R$ 19,90?
                    <span class="transition group-open:rotate-180 text-gold">
                        <svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </span>
                </summary>
                <div class="px-6 pb-5 text-gray-600 text-sm">
                    Você recebe o e-book digital completo, 14 infográficos, plano de 90 dias, checklists, templates, prompts e o módulo de bônus sobre SEO local.
                </div>
            </details>

            <details class="bg-white border border-gray-200 rounded-lg group cursor-pointer">
                <summary class="w-full px-6 py-5 font-bold text-navy-900 flex justify-between items-center focus:outline-none list-none marker:hidden">
                    O checkout já está funcionando?
                    <span class="transition group-open:rotate-180 text-gold">
                        <svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </span>
                </summary>
                <div class="px-6 pb-5 text-gray-600 text-sm">
                    A página está pronta para receber o link real de checkout. Neste momento, o botão sinaliza a etapa de compra, mas não simula um pagamento integrado.
                </div>
            </details>
        </div>"""

faq_pattern = re.compile(r'<div class="space-y-4">.*?</section>', re.DOTALL)
html = faq_pattern.sub(faq_new + '\\n    </div>\\n</section>', html)

# 3. Footer replacement
footer_new = """<!-- Footer -->
<footer class="bg-navy-900 border-t border-gray-800 text-gray-400 py-12">
    <div class="container mx-auto px-6 flex flex-col items-center text-center space-y-6">
        <div>
            <a href="#top" class="text-white font-bold text-xl flex items-center gap-2 justify-center hover:text-gold transition">
                DOMINANDO GOOGLE SEARCH 2026
            </a>
            <p class="text-sm mt-2 text-gray-500">Um guia prático para busca, IA e conversão.</p>
        </div>
        
        <div class="flex gap-6 text-sm font-medium">
            <a href="#conteudo" class="hover:text-white transition">Conteúdo</a>
            <a href="#duvidas" class="hover:text-white transition">Dúvidas</a>
            <a href="#comprar" class="hover:text-white transition">Comprar</a>
        </div>
        
        <div class="text-xs text-gray-600 pt-6 border-t border-gray-800 w-full max-w-sm">
            &copy; 2026 · Conteúdo digital<br>SEO · AEO · GEO
        </div>
    </div>
</footer>"""

footer_pattern = re.compile(r'<!-- Footer -->.*?</footer>', re.DOTALL)
html = footer_pattern.sub(footer_new, html)

# 4. Add ID to body for #top
html = html.replace('<body class="antialiased text-gray-800 bg-white">', '<body class="antialiased text-gray-800 bg-white" id="top">')

# 5. Add IDs for anchor links
html = html.replace('<section class="py-24 bg-white">', '<section class="py-24 bg-white" id="conteudo">', 1)
html = html.replace('<section class="py-24 bg-navy-900 text-white relative overflow-hidden">', '<section class="py-24 bg-navy-900 text-white relative overflow-hidden" id="comprar">', 1)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
