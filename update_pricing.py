import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_idx = html.find('<!-- 9. Final CTA -->')
end_idx = html.find('<!-- 10. FAQ -->')

if start_idx == -1 or end_idx == -1:
    print("Section not found!")
    sys.exit(1)

new_section = """<!-- 9. Final CTA -->
<section class="py-24 bg-navy-900 text-white relative overflow-hidden" id="comprar">
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-blue-900/20 via-transparent to-transparent pointer-events-none"></div>

    <div class="container mx-auto px-6 max-w-4xl relative z-10">
        <div class="text-center mb-12">
            <h2 class="text-4xl md:text-5xl font-bold mb-4 leading-tight">Pare de publicar no escuro.</h2>
            <p class="text-gray-400 text-lg max-w-2xl mx-auto">
                Tenha o mapa exato do que escrever, como estruturar e onde focar para trazer tráfego qualificado que converte todos os dias.
            </p>
        </div>
        
        <div class="bg-white rounded-3xl p-8 md:p-12 shadow-2xl relative text-navy-900 max-w-2xl mx-auto border border-gray-100">
            <!-- Price Top -->
            <div class="text-center border-b border-gray-100 pb-8 mb-8">
                <div class="inline-block bg-red-50 text-red-500 text-xs font-black tracking-wide px-3 py-1.5 rounded-full mb-4 border border-red-100">HOJE COM DESCONTO</div>
                <div class="text-gray-400 line-through font-medium mb-1">De R$ 97,00</div>
                <div class="text-7xl font-black flex items-start justify-center gap-1 text-navy-900 tracking-tighter">
                    <span class="text-3xl mt-2 font-bold text-gray-500">R$</span>19,90
                </div>
                <p class="text-gray-500 text-sm mt-3 font-medium">Pagamento único. Acesso vitalício.</p>
            </div>
            
            <!-- Benefits -->
            <div class="space-y-5 mb-10">
                <div class="flex gap-4 items-center">
                    <div class="w-8 h-8 rounded-full bg-blue/10 text-blue flex items-center justify-center shrink-0"><svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg></div>
                    <span class="font-bold text-gray-800 text-lg">E-book: Dominando a Busca Orgânica</span>
                </div>
                <div class="flex gap-4 items-center">
                    <div class="w-8 h-8 rounded-full bg-blue/10 text-blue flex items-center justify-center shrink-0"><svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg></div>
                    <span class="font-bold text-gray-800 text-lg">Pack de Templates Prontos</span>
                </div>
                <div class="flex gap-4 items-center">
                    <div class="w-8 h-8 rounded-full bg-gold/20 text-gold flex items-center justify-center shrink-0"><svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg></div>
                    <span class="font-bold text-gray-800 text-lg">Bônus: Módulo SEO Local</span>
                </div>
            </div>
            
            <!-- Button -->
            <a href="https://pay.kiwify.com.br/4jxsMVp" target="_blank" class="block w-full bg-gold text-navy-900 text-center px-8 py-5 rounded-xl font-black text-xl hover:bg-yellow-400 transition-all shadow-[0_10px_40px_rgba(244,185,66,0.3)] hover:-translate-y-1">
                GARANTIR MEU ACESSO AGORA
            </a>
            
            <div class="flex justify-center items-center gap-6 mt-6 text-sm text-gray-400 font-medium">
                <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd"></path></svg> Compra Segura</div>
                <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> Garantia 7 dias</div>
            </div>
            
            <!-- Kiwify Info -->
            <div class="mt-8 bg-gray-50 p-4 rounded-xl flex items-center justify-center gap-4 border border-gray-200">
                <div class="text-blue bg-white p-2.5 rounded-full shadow-sm shrink-0">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                </div>
                <div class="text-left">
                    <div class="text-sm font-bold text-navy-900">Download imediato</div>
                    <div class="text-xs text-gray-500 mt-0.5">Baixe os materiais direto na plataforma da Kiwify.</div>
                </div>
            </div>
        </div>
    </div>
</section>

"""

html = html[:start_idx] + new_section + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
