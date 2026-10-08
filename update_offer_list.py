with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_benefits = """            <!-- Benefits -->
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
            </div>"""

new_benefits = """            <!-- Benefits -->
            <div class="grid md:grid-cols-2 gap-x-6 gap-y-5 mb-10">
                <div class="flex gap-4 items-center">
                    <div class="w-8 h-8 rounded-full bg-blue/10 text-blue flex items-center justify-center shrink-0"><svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg></div>
                    <span class="font-bold text-gray-800 text-base">E-book: Dominando a Busca Orgânica</span>
                </div>
                <div class="flex gap-4 items-center">
                    <div class="w-8 h-8 rounded-full bg-blue/10 text-blue flex items-center justify-center shrink-0"><svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg></div>
                    <span class="font-bold text-gray-800 text-base">Plano de Execução de 90 Dias</span>
                </div>
                <div class="flex gap-4 items-center">
                    <div class="w-8 h-8 rounded-full bg-blue/10 text-blue flex items-center justify-center shrink-0"><svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg></div>
                    <span class="font-bold text-gray-800 text-base">Pack de Templates Prontos</span>
                </div>
                <div class="flex gap-4 items-center">
                    <div class="w-8 h-8 rounded-full bg-blue/10 text-blue flex items-center justify-center shrink-0"><svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg></div>
                    <span class="font-bold text-gray-800 text-base">Biblioteca de Prompts para IA</span>
                </div>
                <div class="flex gap-4 items-center">
                    <div class="w-8 h-8 rounded-full bg-blue/10 text-blue flex items-center justify-center shrink-0"><svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg></div>
                    <span class="font-bold text-gray-800 text-base">Checklist de Auditoria Completo</span>
                </div>
                <div class="flex gap-4 items-center">
                    <div class="w-8 h-8 rounded-full bg-gold/20 text-gold flex items-center justify-center shrink-0"><svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg></div>
                    <span class="font-bold text-gray-800 text-base text-gold">Bônus: Módulo SEO Local</span>
                </div>
            </div>"""

if old_benefits in html:
    html = html.replace(old_benefits, new_benefits)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Success")
else:
    print("Old string not found. Please verify.")
