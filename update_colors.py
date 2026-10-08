import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract Section 2
start_idx = html.find('<!-- 2. Section: SEO in 2026 -->')
end_idx = html.find('</section>', start_idx) + 10

if start_idx != -1:
    section_html = html[start_idx:end_idx]
    
    # Replace teal with gold/blue
    section_html = section_html.replace('text-teal', 'text-gold')
    
    # Custom bg-teal replacements
    section_html = section_html.replace('bg-teal text-white', 'bg-gold text-navy-900')
    section_html = section_html.replace('bg-teal shrink-0', 'bg-gold shrink-0')
    section_html = section_html.replace('bg-teal/10', 'bg-gold/10')
    
    # Button at the bottom
    section_html = section_html.replace('bg-[#E8F5E9]', 'bg-gold/10')
    section_html = section_html.replace('border-teal', 'border-gold')
    
    # Re-insert
    html = html[:start_idx] + section_html + html[end_idx:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Sucesso!")
else:
    print("Section 2 not found.")
