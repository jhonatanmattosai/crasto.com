import base64
import re
import json

html_path = r'c:\Users\jm881\OneDrive\CRASTO.COM\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find the script tag with the base64 string
match = re.search(r'<script defer="" src="data:text/javascript;base64,([^"]+)"></script>', html)
if not match:
    print("Script not found in index.html!")
    exit(1)

b64_str = match.group(1)
try:
    decoded = base64.b64decode(b64_str).decode('utf-8')
except Exception as e:
    print("Error decoding:", e)
    exit(1)

# Now define the full i18n mapping
# We want to use `.elementor-heading-title` or `p` when we don't want to destroy the elementor tags, OR
# we can just use the provided selectors and append `.elementor-heading-title` or `.elementor-widget-container` where relevant.

i18n_obj = {
    "pt": {
        ".hero-overline .elementor-heading-title": "Comportamento · Estratégia · Tecnologia",
        ".hero-title .elementor-heading-title": "Três problemas que parecem diferentes.<br><em>Uma raiz que ninguém vê.</em>",
        ".hero-sub p": "Comportamento frágil, estratégia confusa e tecnologia atrasada são sintomas do mesmo sistema. A CRASTO é a única que resolve os três.",
        ".hero-scroll .elementor-heading-title": "↓ Conheça a lógica",
        ".pain-question .elementor-heading-title": "Você se reconhece em algum desses cenários?",
        ".pain-cards > .e-con:nth-child(1) .pain-card-label .elementor-heading-title": "Cenário 01",
        ".pain-cards > .e-con:nth-child(2) .pain-card-label .elementor-heading-title": "Cenário 02",
        ".pain-cards > .e-con:nth-child(3) .pain-card-label .elementor-heading-title": "Cenário 03",
        ".pain-cards > .e-con:nth-child(1) .pain-card-text p": "O empresário que acha que precisa de <em>tecnologia</em> — mas o problema real é <span class=\"hl-gold\">liderança</span>.",
        ".pain-cards > .e-con:nth-child(2) .pain-card-text p": "A empresa que acha que precisa de <em>consultoria</em> — mas o problema real é <span class=\"hl-blue\">automação</span>.",
        ".pain-cards > .e-con:nth-child(3) .pain-card-text p": "O líder que acha que precisa de <em>terapia</em> — mas o problema real é <span class=\"hl-green\">estratégia</span>.",
        ".pain-cards > .e-con:nth-child(1) .pain-card-reveal p": "O problema não é a ferramenta. É quem decide como usá-la.",
        ".pain-cards > .e-con:nth-child(2) .pain-card-reveal p": "Processos manuais não sobrevivem ao crescimento. IA escala o que gestão apenas estabiliza.",
        ".pain-cards > .e-con:nth-child(3) .pain-card-reveal p": "Não é burnout. É um negócio sem direção consumindo a pessoa.",
        ".philosophy-text p": "Pode ser comportamento. Pode ser estratégia. Pode ser tecnologia.<br>Na maioria das vezes, <strong>são os três</strong> — e é exatamente por isso que a CRASTO existe.",
        ".philosophy-sub p": "A maioria das empresas trata cada problema isoladamente. A CRASTO é a única que integra os três — porque o que parece separado, na raiz, é uma coisa só.",
        ".solutions-overline .elementor-heading-title": "Ecossistema Integrado",
        ".solutions-title .elementor-heading-title": "Três dimensões. <em>Um sistema.</em>",
        ".card-dev .solution-name .elementor-heading-title": "Desenvolvimento Comportamental",
        ".card-tech .solution-name .elementor-heading-title": "Agentes de IA & Automação",
        ".card-consult .solution-name .elementor-heading-title": "Consultoria Estratégica",
        ".card-dev .solution-desc p": "Crescer sem método é desperdiçar potencial. A comunicação é o veículo — o comportamento é o destino.",
        ".card-tech .solution-desc p": "Escalar exige inteligência artificial — não mais gente. Tecnologia que pensa, decide e executa com a inteligência do seu negócio.",
        ".card-consult .solution-desc p": "Empresa que cresce sem estrutura, quebra com estrutura. Estratégia clara. Processos reais. Execução que sustenta.",
        ".pessoal-label .elementor-heading-title": "Evolução Pessoal",
        ".pessoal-title .elementor-heading-title": "Nem todo problema é empresarial.<br><em>Alguns são seus.</em>",
        ".pessoal-desc p": "Você pode estar aqui como empresário, como líder ou como profissional. Mas por trás de todo cargo, existe uma pessoa. E algumas dores não se resolvem com estratégia ou tecnologia — se resolvem com profundidade, método e acompanhamento real.",
        ".logic-bottom p": "Essa é a lógica central da CRASTO. Nenhuma parte funciona sozinha. É por isso que não oferecemos soluções isoladas — oferecemos evolução integrada.",
        ".method-label .elementor-heading-title": "O Sistema por Trás da Transformação",
        ".method-title .elementor-heading-title": "O Método Evolution não trata partes isoladas.<br><em>Ele reorganiza o sistema inteiro.</em>",
        ".method-desc p": "Desenvolvido ao longo de mais de duas décadas de prática clínica e empresarial, o Método Evolution by Crasto é um framework integrado de diagnóstico, decisão e evolução.",
        ".method-bottom p": "A CRASTO é a única que integra essas três camadas em um único sistema — porque evolução real nunca é parcial.",
        ".casos-label .elementor-heading-title": "Resultados Reais",
        ".casos-title .elementor-heading-title": "Histórias de quem passou <em>pelo processo.</em>",
        ".cta-overline .elementor-heading-title": "Próximo Passo",
        ".cta-title .elementor-heading-title": "Seja lá qual for o seu problema.<br>Sabemos que <em>ele não é isolado.</em>",
        ".cta-sub p": "Agende uma reunião de diagnóstico gratuita de 30 minutos. Vamos identificar juntos onde está a raiz — e qual evolução faz sentido agora.",
        ".cta-detail .elementor-heading-title": "30 minutos · Sem custo · Sem compromisso",
        ".c-nav-link[href=\"#solucoes\"]": "Soluções",
        ".c-nav-link[href=\"#metodo\"]": "Método",
        "#cNavBtn": "Agendar",
        
        ".crasto-hero .btn-primary .elementor-button-text": "Descubra qual evolução você precisa",
        ".solution-link .elementor-button-text": "Acessar →",
        ".crasto-pessoal .btn-primary .elementor-button-text": "Agendar conversa sobre evolução pessoal",
        ".crasto-cta .btn-primary .elementor-button-text": "Agendar Diagnóstico Gratuito",
        ".c-mob-cta": "Agendar Diagnóstico",
        ".c-mob-link[href=\"#solucoes\"]": "Soluções",
        ".c-mob-link[href=\"#metodo\"]": "Método",
        
        ".caso-card:nth-child(1) .caso-tag .elementor-heading-title": "Caso 1 · Empresária, 30 anos · Setor Alimentício",
        ".caso-card:nth-child(2) .caso-tag .elementor-heading-title": "Caso 2 · Profissional, 56 anos · Setor Público",
        ".caso-card:nth-child(3) .caso-tag .elementor-heading-title": "Caso 3 · Empresário · Tecnologia",

        ".caso-card:nth-child(1) .caso-headline .elementor-heading-title": "De emagrecimento a sucessão empresarial.",
        ".caso-card:nth-child(2) .caso-headline .elementor-heading-title": "Do zero à empresa funcionando. Aos 56 anos.",
        ".caso-card:nth-child(3) .caso-headline .elementor-heading-title": "De caos operacional a empresa escalável.",

        ".caso-card:nth-child(1) .caso-text p": "Entrou no processo focada apenas em emagrecimento. Nove meses depois: 35 quilos eliminados de forma sustentável, desmame de medicação conduzido. Mas o que realmente mudou foi invisível — conflitos familiares profundos resolvidos, maturidade executiva desenvolvida, sucessão empresarial estruturada.",
        ".caso-card:nth-child(2) .caso-text p": "Carregava luto materno recente, traumas antigos, fobias, autossabotagem. Seis meses de mentoria terapêutica intensiva: luto resolvido, traumas tratados, relações parentais restauradas. Renovação por mais um ano para construir do zero: método próprio, empresa profissionalizada, estrutura completa.",
        ".caso-card:nth-child(3) .caso-text p": "Empresa em crescimento acelerado sem estrutura. Processos manuais, equipe sobrecarregada, fundador operacional. Diagnóstico empresarial, automação de processos críticos com IA e reestruturação de liderança. Resultado: 40% de redução de horas operacionais, escala sem contratações adicionais.",

        ".caso-card:nth-child(1) .caso-result-text p": "<strong style=\"color:#c9a84c;\">Renovação para programa anual. Resultados muito além do contratado.</strong>",
        ".caso-card:nth-child(2) .caso-result-text p": "<strong style=\"color:#c9a84c;\">Empresa estruturada do zero. Renovação anual consecutiva.</strong>",
        ".caso-card:nth-child(3) .caso-result-text p": "<strong style=\"color:#c9a84c;\">Operação automatizada. Fundador voltou a ser estratégico.</strong>",
        
        ".sobre-label .elementor-heading-title": "Quem Conduz o Processo",
        ".sobre-name .elementor-heading-title": "Carlos Crasto",
        ".method-step:nth-child(1) .method-step-label .elementor-heading-title": "Comportamento<br>corrige liderança",
        ".method-step:nth-child(2) .method-step-label .elementor-heading-title": "Estratégia<br>organiza direção",
        ".method-step:nth-child(3) .method-step-label .elementor-heading-title": "Tecnologia<br>escala execução",
        ".method-step:nth-child(1) .method-step-desc p": "Diagnóstico comportamental profundo. Reorganização dos padrões que sabotam decisões e relações.",
        ".method-step:nth-child(2) .method-step-desc p": "Clareza de modelo, processos e governança. Estrutura que sustenta o crescimento.",
        ".method-step:nth-child(3) .method-step-desc p": "IA, automação e sistemas inteligentes. Infraestrutura que multiplica sem depender de mais gente.",
        
        ".proof-stat:nth-child(1) .proof-label .elementor-heading-title": "anos de experiência",
        ".proof-stat:nth-child(2) .proof-label .elementor-heading-title": "sessões realizadas",
        ".proof-stat:nth-child(3) .proof-label .elementor-heading-title": "abordagens integradas",
        ".proof-stat:nth-child(4) .proof-label .elementor-heading-title": "dimensões de evolução",
        
        ".logic-chain .logic-item:nth-child(1) p": "<em>Comportamento</em> melhora liderança",
        ".logic-chain .logic-item:nth-child(3) p": "<em>Liderança</em> melhora <span class=\"hl-green\">gestão</span>",
        ".logic-chain .logic-item:nth-child(5) p": "<span class=\"hl-blue\">Tecnologia</span> escala <span class=\"hl-green\">gestão</span>"
    },
    "en": {
        ".hero-overline .elementor-heading-title": "Behavior · Strategy · Technology",
        ".hero-title .elementor-heading-title": "Three problems that seem different.<br><em>One root nobody sees.</em>",
        ".hero-sub p": "Fragile behavior, confused strategy and outdated technology are symptoms of the same system. CRASTO is the only one that solves all three.",
        ".hero-scroll .elementor-heading-title": "↓ Discover the logic",
        ".pain-question .elementor-heading-title": "Do you recognize yourself in any of these scenarios?",
        ".pain-cards > .e-con:nth-child(1) .pain-card-label .elementor-heading-title": "Scenario 01",
        ".pain-cards > .e-con:nth-child(2) .pain-card-label .elementor-heading-title": "Scenario 02",
        ".pain-cards > .e-con:nth-child(3) .pain-card-label .elementor-heading-title": "Scenario 03",
        ".pain-cards > .e-con:nth-child(1) .pain-card-text p": "The entrepreneur who thinks they need <em>technology</em> — but the real problem is <span class=\"hl-gold\">leadership</span>.",
        ".pain-cards > .e-con:nth-child(2) .pain-card-text p": "The company that thinks it needs <em>consulting</em> — but the real problem is <span class=\"hl-blue\">automation</span>.",
        ".pain-cards > .e-con:nth-child(3) .pain-card-text p": "The leader who thinks they need <em>therapy</em> — but the real problem is <span class=\"hl-green\">strategy</span>.",
        ".pain-cards > .e-con:nth-child(1) .pain-card-reveal p": "The problem isn't the tool. It's who decides how to use it.",
        ".pain-cards > .e-con:nth-child(2) .pain-card-reveal p": "Manual processes don't survive growth. AI scales what management only stabilizes.",
        ".pain-cards > .e-con:nth-child(3) .pain-card-reveal p": "It's not burnout. It's a business without direction consuming the person.",
        ".philosophy-text p": "It could be behavior. It could be strategy. It could be technology.<br>Most of the time, <strong>it's all three</strong> — and that's exactly why CRASTO exists.",
        ".philosophy-sub p": "Most companies treat each problem in isolation. CRASTO is the only one that integrates all three — because what seems separate, at its root, is one thing.",
        ".solutions-overline .elementor-heading-title": "Integrated Ecosystem",
        ".solutions-title .elementor-heading-title": "Three dimensions. <em>One system.</em>",
        ".card-dev .solution-name .elementor-heading-title": "Behavioral Development",
        ".card-tech .solution-name .elementor-heading-title": "AI Agents & Automation",
        ".card-consult .solution-name .elementor-heading-title": "Strategic Consulting",
        ".card-dev .solution-desc p": "Growing without method is wasting potential. Communication is the vehicle — behavior is the destination.",
        ".card-tech .solution-desc p": "Scaling requires artificial intelligence — not more people. Technology that thinks, decides and executes with your business intelligence.",
        ".card-consult .solution-desc p": "A company that grows without structure breaks with structure. Clear strategy. Real processes. Sustainable execution.",
        ".pessoal-label .elementor-heading-title": "Personal Evolution",
        ".pessoal-title .elementor-heading-title": "Not every problem is business.<br><em>Some are yours.</em>",
        ".pessoal-desc p": "You may be here as an entrepreneur, a leader or a professional. But behind every title, there's a person. And some pains can't be solved with strategy or technology — they're solved with depth, method and real support.",
        ".logic-bottom p": "This is CRASTO's core logic. No part works alone. That's why we don't offer isolated solutions — we offer integrated evolution.",
        ".method-label .elementor-heading-title": "The System Behind the Transformation",
        ".method-title .elementor-heading-title": "The Evolution Method doesn't treat isolated parts.<br><em>It reorganizes the entire system.</em>",
        ".method-desc p": "Developed over more than two decades of clinical and business practice, the Evolution Method by Crasto is an integrated framework for diagnosis, decision and evolution.",
        ".method-bottom p": "CRASTO is the only one that integrates these three layers into a single system — because real evolution is never partial.",
        ".casos-label .elementor-heading-title": "Real Results",
        ".casos-title .elementor-heading-title": "Stories from those who went through <em>the process.</em>",
        ".cta-overline .elementor-heading-title": "Next Step",
        ".cta-title .elementor-heading-title": "Whatever your problem is.<br>We know <em>it's not isolated.</em>",
        ".cta-sub p": "Schedule a free 30-minute diagnostic meeting. Together we'll identify the root — and which evolution makes sense now.",
        ".cta-detail .elementor-heading-title": "30 minutes · No cost · No commitment",
        ".c-nav-link[href=\"#solucoes\"]": "Solutions",
        ".c-nav-link[href=\"#metodo\"]": "Method",
        "#cNavBtn": "Schedule",
        
        ".crasto-hero .btn-primary .elementor-button-text": "Discover which evolution you need",
        ".solution-link .elementor-button-text": "Access →",
        ".crasto-pessoal .btn-primary .elementor-button-text": "Schedule chat about personal evolution",
        ".crasto-cta .btn-primary .elementor-button-text": "Schedule Free Diagnosis",
        ".c-mob-cta": "Schedule Diagnosis",
        ".c-mob-link[href=\"#solucoes\"]": "Solutions",
        ".c-mob-link[href=\"#metodo\"]": "Method",
        
        ".caso-card:nth-child(1) .caso-tag .elementor-heading-title": "Case 1 · Businesswoman, 30 years old · Food Sector",
        ".caso-card:nth-child(2) .caso-tag .elementor-heading-title": "Case 2 · Professional, 56 years old · Public Sector",
        ".caso-card:nth-child(3) .caso-tag .elementor-heading-title": "Case 3 · Businessman · Technology",

        ".caso-card:nth-child(1) .caso-headline .elementor-heading-title": "From weight loss to business succession.",
        ".caso-card:nth-child(2) .caso-headline .elementor-heading-title": "From scratch to running business. At 56 years old.",
        ".caso-card:nth-child(3) .caso-headline .elementor-heading-title": "From operational chaos to scalable company.",

        ".caso-card:nth-child(1) .caso-text p": "Entered the process focused only on weight loss. Nine months later: 35 kilos eliminated sustainably, medication weaning conducted. But what really changed was invisible — deep family conflicts resolved, executive maturity developed, structured business succession.",
        ".caso-card:nth-child(2) .caso-text p": "Carried recent maternal grief, old traumas, phobias, self-sabotage. Six months of intensive therapeutic mentoring: grief resolved, traumas treated, parental relationships restored. Renewal for another year to build from scratch: own method, professionalized company, complete structure.",
        ".caso-card:nth-child(3) .caso-text p": "Rapidly growing company without structure. Manual processes, overloaded team, operational founder. Business diagnosis, automation of critical processes with AI and leadership restructuring. Result: 40% reduction in operational hours, scaling without additional hires.",

        ".caso-card:nth-child(1) .caso-result-text p": "<strong style=\"color:#c9a84c;\">Renewal for annual program. Results far beyond expectations.</strong>",
        ".caso-card:nth-child(2) .caso-result-text p": "<strong style=\"color:#c9a84c;\">Company structured from scratch. Consecutive annual renewal.</strong>",
        ".caso-card:nth-child(3) .caso-result-text p": "<strong style=\"color:#c9a84c;\">Automated operation. Founder returned to being strategic.</strong>",
        
        ".sobre-label .elementor-heading-title": "Who Leads the Process",
        ".sobre-name .elementor-heading-title": "Carlos Crasto",
        ".method-step:nth-child(1) .method-step-label .elementor-heading-title": "Behavior<br>fixes leadership",
        ".method-step:nth-child(2) .method-step-label .elementor-heading-title": "Strategy<br>organizes direction",
        ".method-step:nth-child(3) .method-step-label .elementor-heading-title": "Technology<br>scales execution",
        ".method-step:nth-child(1) .method-step-desc p": "Deep behavioral diagnosis. Reorganization of patterns that sabotage decisions and relationships.",
        ".method-step:nth-child(2) .method-step-desc p": "Clarity of model, processes and governance. Structure that sustains growth.",
        ".method-step:nth-child(3) .method-step-desc p": "AI, automation and intelligent systems. Infrastructure that multiplies without depending on more people.",
        
        ".proof-stat:nth-child(1) .proof-label .elementor-heading-title": "years of experience",
        ".proof-stat:nth-child(2) .proof-label .elementor-heading-title": "sessions completed",
        ".proof-stat:nth-child(3) .proof-label .elementor-heading-title": "integrated approaches",
        ".proof-stat:nth-child(4) .proof-label .elementor-heading-title": "dimensions of evolution",
        
        ".logic-chain .logic-item:nth-child(1) p": "<em>Behavior</em> improves leadership",
        ".logic-chain .logic-item:nth-child(3) p": "<em>Leadership</em> improves <span class=\"hl-green\">management</span>",
        ".logic-chain .logic-item:nth-child(5) p": "<span class=\"hl-blue\">Technology</span> scales <span class=\"hl-green\">management</span>"
    },
    "es": {
        ".hero-overline .elementor-heading-title": "Comportamiento · Estrategia · Tecnología",
        ".hero-title .elementor-heading-title": "Tres problemas que parecen diferentes.<br><em>Una raíz que nadie ve.</em>",
        ".hero-sub p": "Comportamiento frágil, estrategia confusa y tecnología atrasada son síntomas del mismo sistema. CRASTO es la única que resuelve los tres.",
        ".hero-scroll .elementor-heading-title": "↓ Conoce la lógica",
        ".pain-question .elementor-heading-title": "¿Te reconoces en alguno de estos escenarios?",
        ".pain-cards > .e-con:nth-child(1) .pain-card-label .elementor-heading-title": "Escenario 01",
        ".pain-cards > .e-con:nth-child(2) .pain-card-label .elementor-heading-title": "Escenario 02",
        ".pain-cards > .e-con:nth-child(3) .pain-card-label .elementor-heading-title": "Escenario 03",
        ".pain-cards > .e-con:nth-child(1) .pain-card-text p": "El empresario que cree que necesita <em>tecnología</em> — pero el problema real es <span class=\"hl-gold\">liderazgo</span>.",
        ".pain-cards > .e-con:nth-child(2) .pain-card-text p": "La empresa que cree que necesita <em>consultoría</em> — pero el problema real es <span class=\"hl-blue\">automatización</span>.",
        ".pain-cards > .e-con:nth-child(3) .pain-card-text p": "El líder que cree que necesita <em>terapia</em> — pero el problema real es <span class=\"hl-green\">estrategia</span>.",
        ".pain-cards > .e-con:nth-child(1) .pain-card-reveal p": "El problema no es la herramienta. Es quién decide cómo usarla.",
        ".pain-cards > .e-con:nth-child(2) .pain-card-reveal p": "Los procesos manuales no sobreviven al crecimiento. La IA escala lo que la gestión solo estabiliza.",
        ".pain-cards > .e-con:nth-child(3) .pain-card-reveal p": "No es burnout. Es un negocio sin dirección consumiendo a la persona.",
        ".philosophy-text p": "Puede ser comportamiento. Puede ser estrategia. Puede ser tecnología.<br>La mayoría de las veces, <strong>son los tres</strong> — y es exactamente por eso que CRASTO existe.",
        ".philosophy-sub p": "La mayoría de las empresas trata cada problema de forma aislada. CRASTO es la única que integra los tres — porque lo que parece separado, en la raíz, es una sola cosa.",
        ".solutions-overline .elementor-heading-title": "Ecosistema Integrado",
        ".solutions-title .elementor-heading-title": "Tres dimensiones. <em>Un sistema.</em>",
        ".card-dev .solution-name .elementor-heading-title": "Desarrollo Comportamental",
        ".card-tech .solution-name .elementor-heading-title": "Agentes de IA y Automatización",
        ".card-consult .solution-name .elementor-heading-title": "Consultoría Estratégica",
        ".card-dev .solution-desc p": "Crecer sin método es desperdiciar potencial. La comunicación es el vehículo — el comportamiento es el destino.",
        ".card-tech .solution-desc p": "Escalar exige inteligencia artificial — no más gente. Tecnología que piensa, decide y ejecuta con la inteligencia de tu negocio.",
        ".card-consult .solution-desc p": "Empresa que crece sin estructura, quiebra con estructura. Estrategia clara. Procesos reales. Ejecución sostenible.",
        ".pessoal-label .elementor-heading-title": "Evolución Personal",
        ".pessoal-title .elementor-heading-title": "No todo problema es empresarial.<br><em>Algunos son tuyos.</em>",
        ".pessoal-desc p": "Puedes estar aquí como empresario, como líder o como profesional. Pero detrás de todo cargo, existe una persona. Y algunos dolores no se resuelven con estrategia o tecnología — se resuelven con profundidad, método y acompañamiento real.",
        ".logic-bottom p": "Esta es la lógica central de CRASTO. Ninguna parte funciona sola. Por eso no ofrecemos soluciones aisladas — ofrecemos evolución integrada.",
        ".method-label .elementor-heading-title": "El Sistema Detrás de la Transformación",
        ".method-title .elementor-heading-title": "El Método Evolution no trata partes aisladas.<br><em>Reorganiza el sistema entero.</em>",
        ".method-desc p": "Desarrollado a lo largo de más de dos décadas de práctica clínica y empresarial, el Método Evolution by Crasto es un framework integrado de diagnóstico, decisión y evolución.",
        ".method-bottom p": "CRASTO es la única que integra estas tres capas en un único sistema — porque la evolución real nunca es parcial.",
        ".casos-label .elementor-heading-title": "Resultados Reales",
        ".casos-title .elementor-heading-title": "Historias de quienes pasaron <em>por el proceso.</em>",
        ".cta-overline .elementor-heading-title": "Próximo Paso",
        ".cta-title .elementor-heading-title": "Sea cual sea tu problema.<br>Sabemos que <em>no es aislado.</em>",
        ".cta-sub p": "Agenda una reunión de diagnóstico gratuita de 30 minutos. Juntos identificaremos la raíz — y qué evolución tiene sentido ahora.",
        ".cta-detail .elementor-heading-title": "30 minutos · Sin costo · Sin compromiso",
        ".c-nav-link[href=\"#solucoes\"]": "Soluciones",
        ".c-nav-link[href=\"#metodo\"]": "Método",
        "#cNavBtn": "Agendar",
        
        ".crasto-hero .btn-primary .elementor-button-text": "Descubre qué evolución necesitas",
        ".solution-link .elementor-button-text": "Acceder →",
        ".crasto-pessoal .btn-primary .elementor-button-text": "Agendar charla sobre evolución personal",
        ".crasto-cta .btn-primary .elementor-button-text": "Agendar Diagnóstico Gratuito",
        ".c-mob-cta": "Agendar Diagnóstico",
        ".c-mob-link[href=\"#solucoes\"]": "Soluciones",
        ".c-mob-link[href=\"#metodo\"]": "Método",
        
        ".caso-card:nth-child(1) .caso-tag .elementor-heading-title": "Caso 1 · Empresaria, 30 años · Sector Alimenticio",
        ".caso-card:nth-child(2) .caso-tag .elementor-heading-title": "Caso 2 · Profesional, 56 años · Sector Público",
        ".caso-card:nth-child(3) .caso-tag .elementor-heading-title": "Caso 3 · Empresario · Tecnología",

        ".caso-card:nth-child(1) .caso-headline .elementor-heading-title": "De adelgazamiento a sucesión empresarial.",
        ".caso-card:nth-child(2) .caso-headline .elementor-heading-title": "De cero a empresa funcionando. A los 56 años.",
        ".caso-card:nth-child(3) .caso-headline .elementor-heading-title": "De caos operativo a empresa escalable.",

        ".caso-card:nth-child(1) .caso-text p": "Entró en el proceso enfocada solo en adelgazar. Nueve meses después: 35 kilos eliminados de forma sostenible, destete de medicación conducido. Pero lo que realmente cambió fue invisible: profundos conflictos familiares resueltos, madurez ejecutiva desarrollada, sucesión empresarial estructurada.",
        ".caso-card:nth-child(2) .caso-text p": "Cargaba dolor materno reciente, viejos traumas, fobias, autosabotaje. Seis meses de mentoría terapéutica intensiva: duelo resuelto, traumas tratados, relaciones parentales restauradas. Renovación por otro año para construir desde cero: método propio, empresa profesionalizada, estructura completa.",
        ".caso-card:nth-child(3) .caso-text p": "Empresa en rápido crecimiento sin estructura. Procesos manuales, equipo sobrecargado, fundador operativo. Diagnóstico empresarial, automatización de procesos críticos con IA y reestructuración de liderazgo. Resultado: reducción del 40% de horas operativas, escalabilidad sin contrataciones adicionales.",

        ".caso-card:nth-child(1) .caso-result-text p": "<strong style=\"color:#c9a84c;\">Renovación para el programa anual. Resultados mucho más allá de lo esperado.</strong>",
        ".caso-card:nth-child(2) .caso-result-text p": "<strong style=\"color:#c9a84c;\">Empresa estructurada desde cero. Renovación anual consecutiva.</strong>",
        ".caso-card:nth-child(3) .caso-result-text p": "<strong style=\"color:#c9a84c;\">Operación automatizada. El fundador volvió a ser estratégico.</strong>",
        
        ".sobre-label .elementor-heading-title": "Quién Conduce el Proceso",
        ".sobre-name .elementor-heading-title": "Carlos Crasto",
        ".method-step:nth-child(1) .method-step-label .elementor-heading-title": "Comportamiento<br>corrige liderazgo",
        ".method-step:nth-child(2) .method-step-label .elementor-heading-title": "Estrategia<br>organiza dirección",
        ".method-step:nth-child(3) .method-step-label .elementor-heading-title": "Tecnología<br>escala ejecución",
        ".method-step:nth-child(1) .method-step-desc p": "Diagnóstico comportamental profundo. Reorganización de los patrones que sabotean decisiones y relaciones.",
        ".method-step:nth-child(2) .method-step-desc p": "Claridad de modelo, procesos y gobernanza. Estructura que sustenta el crecimiento.",
        ".method-step:nth-child(3) .method-step-desc p": "IA, automatización y sistemas inteligentes. Infraestructura que multiplica sin depender de más personas.",
        
        ".proof-stat:nth-child(1) .proof-label .elementor-heading-title": "años de experiencia",
        ".proof-stat:nth-child(2) .proof-label .elementor-heading-title": "sesiones realizadas",
        ".proof-stat:nth-child(3) .proof-label .elementor-heading-title": "enfoques integrados",
        ".proof-stat:nth-child(4) .proof-label .elementor-heading-title": "dimensiones de evolución",
        
        ".logic-chain .logic-item:nth-child(1) p": "<em>Comportamiento</em> mejora liderazgo",
        ".logic-chain .logic-item:nth-child(3) p": "<em>Liderazgo</em> mejora <span class=\"hl-green\">gestión</span>",
        ".logic-chain .logic-item:nth-child(5) p": "<span class=\"hl-blue\">Tecnología</span> escala <span class=\"hl-green\">gestión</span>"
    }
}

# The JS expects `var i18n={...}`. Replace in the decoded JS.
# I'll just find the start of `var i18n={` and replace it.
i18n_str = 'var i18n=' + json.dumps(i18n_obj, ensure_ascii=False, separators=(',', ':')) + ';'

# The decoded js has `var i18n={pt:{...};window.cSetLang=`
js_match = re.search(r'(var i18n=\{.*?\};)window\.cSetLang', decoded)
if not js_match:
    print("Could not find i18n definition in JS")
    exit(1)

new_decoded = decoded.replace(js_match.group(1), i18n_str)

# Now encode back to base64
new_b64 = base64.b64encode(new_decoded.encode('utf-8')).decode('utf-8')

# Now replace in html
new_html = html.replace(b64_str, new_b64)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Translation updated successfully!")
