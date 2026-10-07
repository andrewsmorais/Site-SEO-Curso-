import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate section 6
start_str = '<!-- 6. Section: Mockups Image area -->'
end_str = '</section>'
start_idx = html.find(start_str)

if start_idx != -1:
    end_idx = html.find(end_str, start_idx) + len(end_str)
    
    new_section = """<!-- 6. Section: Para Quem É -->
<section class="py-24 bg-gray-50 border-b border-gray-200">
    <div class="container mx-auto px-6 max-w-6xl">
        <div class="text-center mb-16">
            <span class="text-xs font-bold text-teal tracking-widest uppercase mb-3 block">Público-Alvo</span>
            <h2 class="text-3xl md:text-5xl font-black text-navy-900 mb-4 tracking-tight">Para quem é este guia?</h2>
            <p class="text-gray-500 text-lg max-w-2xl mx-auto">Se você precisa de mais clientes chegando até você de forma orgânica e qualificada, a resposta está na busca.</p>
        </div>
        
        <div class="grid md:grid-cols-3 gap-8">
            <!-- Card 1: Empresários -->
            <div class="group rounded-3xl overflow-hidden bg-white shadow-xl shadow-gray-200/50 border border-gray-100 hover:-translate-y-2 transition-transform duration-300">
                <div class="h-56 overflow-hidden relative">
                    <img src="https://images.unsplash.com/photo-1556761175-5973dc0f32d7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Empresários" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-navy-900/90 via-navy-900/30 to-transparent"></div>
                    <div class="absolute bottom-6 left-6 flex items-center gap-3">
                        <div class="w-12 h-12 rounded-full bg-blue flex items-center justify-center text-white shadow-lg">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                        </div>
                        <h3 class="text-2xl font-bold text-white">Empresários</h3>
                    </div>
                </div>
                <div class="p-8">
                    <p class="text-gray-600 leading-relaxed font-medium">Donos de negócios físicos ou digitais que não querem mais depender exclusivamente de tráfego pago (anúncios caros) para vender todos os dias.</p>
                </div>
            </div>

            <!-- Card 2: Nova Profissão -->
            <div class="group rounded-3xl overflow-hidden bg-white shadow-xl shadow-gray-200/50 border border-gray-100 hover:-translate-y-2 transition-transform duration-300 md:-translate-y-4">
                <div class="h-56 overflow-hidden relative">
                    <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Nova Profissão" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-navy-900/90 via-navy-900/30 to-transparent"></div>
                    <div class="absolute bottom-6 left-6 flex items-center gap-3">
                        <div class="w-12 h-12 rounded-full bg-gold flex items-center justify-center text-white shadow-lg">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
                        </div>
                        <h3 class="text-2xl font-bold text-white">Nova Profissão</h3>
                    </div>
                </div>
                <div class="p-8">
                    <p class="text-gray-600 leading-relaxed font-medium">Para quem está procurando se preparar e faturar dominando uma das habilidades mais valiosas do mercado: prestando consultoria em SEO e IA para empresas.</p>
                </div>
            </div>

            <!-- Card 3: Autônomos -->
            <div class="group rounded-3xl overflow-hidden bg-white shadow-xl shadow-gray-200/50 border border-gray-100 hover:-translate-y-2 transition-transform duration-300">
                <div class="h-56 overflow-hidden relative">
                    <img src="https://images.unsplash.com/photo-1629909613654-28e377c37b09?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Profissionais Autônomos" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-navy-900/90 via-navy-900/30 to-transparent"></div>
                    <div class="absolute bottom-6 left-6 flex items-center gap-3">
                        <div class="w-12 h-12 rounded-full bg-teal flex items-center justify-center text-white shadow-lg">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                        </div>
                        <h3 class="text-2xl font-bold text-white">Autônomos</h3>
                    </div>
                </div>
                <div class="p-8">
                    <p class="text-gray-600 leading-relaxed font-medium">Dentistas, advogados, nutricionistas e especialistas que precisam ser o <strong>primeiro resultado</strong> no Google e na IA quando o cliente busca perto de casa.</p>
                </div>
            </div>
        </div>
    </div>
</section>"""
    
    html = html[:start_idx] + new_section + html[end_idx:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Sucesso!")
else:
    print("Section not found.")
