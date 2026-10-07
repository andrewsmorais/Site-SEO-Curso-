import os

def get_template(title, content):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Escola de SEO</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                    }},
                    colors: {{
                        navy: {{
                            900: '#0B132B',
                        }},
                        gold: '#F4B942',
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="antialiased text-gray-800 bg-white flex flex-col min-h-screen">
    
    <header class="bg-navy-900 text-white py-6 border-b border-gray-800">
        <div class="container mx-auto px-6 flex justify-between items-center">
            <a href="index.html" class="font-bold text-xl hover:text-gold transition">Escola de SEO</a>
            <a href="index.html" class="text-sm font-medium hover:text-gold transition">&larr; Voltar para a página inicial</a>
        </div>
    </header>

    <main class="flex-grow container mx-auto px-6 py-16 max-w-3xl">
        <h1 class="text-3xl md:text-4xl font-bold text-navy-900 mb-8">{title}</h1>
        <div class="prose prose-gray max-w-none text-gray-600 space-y-6">
            {content}
        </div>
    </main>

    <footer class="bg-navy-900 border-t border-gray-800 text-gray-400 py-8">
        <div class="container mx-auto px-6 text-center text-sm">
            &copy; 2026 Escola de SEO. Todos os direitos reservados.
        </div>
    </footer>
</body>
</html>"""

pages = {
    'reembolso.html': ('Política de Reembolso de 7 Dias', '''
        <p>A Escola de SEO garante a sua total satisfação. Se por qualquer motivo você não ficar satisfeito com o nosso material, oferecemos uma política de reembolso incondicional de 7 dias.</p>
        <h3 class="text-xl font-bold text-gray-800 mt-6 mb-2">Como solicitar o reembolso</h3>
        <p>Para solicitar o reembolso, basta enviar um e-mail para o nosso suporte oficial dentro do prazo de 7 dias contados a partir da data e hora da aprovação do pagamento.</p>
        <p>Não faremos perguntas e não tentaremos convencer você do contrário. O reembolso será processado imediatamente pelo nosso gateway de pagamento e devolvido na mesma forma de pagamento original (PIX ou estorno no cartão de crédito).</p>
    '''),
    
    'cookies.html': ('Política de Cookies', '''
        <p>Utilizamos cookies e tecnologias semelhantes para melhorar a sua experiência em nosso site, personalizar conteúdo e anúncios, e analisar nosso tráfego.</p>
        <h3 class="text-xl font-bold text-gray-800 mt-6 mb-2">O que são cookies?</h3>
        <p>Cookies são pequenos arquivos de texto armazenados no seu navegador ou dispositivo que nos permitem reconhecê-lo em visitas futuras e lembrar das suas preferências.</p>
        <h3 class="text-xl font-bold text-gray-800 mt-6 mb-2">Como usamos</h3>
        <p>Usamos cookies essenciais para o funcionamento do site (como o carrinho de compras e checkout) e cookies analíticos para entender como os visitantes interagem com nossas páginas, ajudando a melhorar nossos produtos.</p>
        <p>Você pode configurar seu navegador para bloquear cookies, porém algumas áreas do site poderão não funcionar corretamente.</p>
    '''),
    
    'privacidade.html': ('Política de Privacidade', '''
        <p>A sua privacidade é fundamental para nós. É política da Escola de SEO respeitar a sua privacidade em relação a qualquer informação sua que possamos coletar no site.</p>
        <h3 class="text-xl font-bold text-gray-800 mt-6 mb-2">Coleta de Dados</h3>
        <p>Solicitamos informações pessoais, como nome, e-mail e dados de pagamento, apenas quando você efetua uma compra ou se cadastra em nossas comunicações. Esta coleta é feita por meios justos e legais, com o seu conhecimento e consentimento.</p>
        <h3 class="text-xl font-bold text-gray-800 mt-6 mb-2">Segurança e Compartilhamento</h3>
        <p>Os seus dados de pagamento são processados através de gateways seguros e encriptados. Não armazenamos os dados do seu cartão de crédito nos nossos servidores.</p>
        <p>Não compartilhamos informações de identificação pessoal publicamente ou com terceiros, exceto quando exigido por lei ou estritamente necessário para processar o pagamento ou entrega do material digital.</p>
    '''),
    
    'termos.html': ('Termos de Uso', '''
        <p>Ao acessar e utilizar os materiais da Escola de SEO, você concorda em cumprir estes termos de serviço, todas as leis e regulamentos aplicáveis.</p>
        <h3 class="text-xl font-bold text-gray-800 mt-6 mb-2">Uso da Licença</h3>
        <p>É concedida permissão para baixar uma cópia do e-book e dos materiais complementares para visualização e estudo pessoal e não comercial.</p>
        <p>Esta é a concessão de uma licença, não uma transferência de título e, sob esta licença, <strong>você não pode:</strong></p>
        <ul class="list-disc pl-5 mt-2 space-y-2">
            <li>modificar ou copiar os materiais para redistribuição comercial;</li>
            <li>vender, revender, piratear ou distribuir o material publicamente;</li>
            <li>remover quaisquer direitos autorais ou outras notações de propriedade dos materiais.</li>
        </ul>
        <h3 class="text-xl font-bold text-gray-800 mt-6 mb-2">Violação</h3>
        <p>Esta licença será automaticamente rescindida se você violar alguma dessas restrições e poderá ser rescindida pela Escola de SEO a qualquer momento. Em caso de pirataria, medidas legais severas poderão ser aplicadas.</p>
    ''')
}

for filename, (title, content) in pages.items():
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(get_template(title, content))

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Footer with new links
footer_start_pattern = '<div class="flex gap-6 text-sm font-medium">'
legal_links = """
        <div class="flex flex-wrap justify-center gap-4 md:gap-6 text-xs text-gray-500 mt-6">
            <a href="reembolso.html" class="hover:text-white transition">Reembolso 7 Dias</a>
            <a href="cookies.html" class="hover:text-white transition">Política de Cookies</a>
            <a href="privacidade.html" class="hover:text-white transition">Política de Privacidade</a>
            <a href="termos.html" class="hover:text-white transition">Termos de Uso</a>
        </div>
"""

copyright_pattern = '<div class="text-xs text-gray-600 pt-6 border-t border-gray-800 w-full max-w-sm">'

html = html.replace(copyright_pattern, legal_links + '        ' + copyright_pattern)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
