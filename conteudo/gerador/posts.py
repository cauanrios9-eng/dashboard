"""Conteúdo das 2 primeiras semanas da CR Automações (Instagram + TikTok).

Fonte única: o renderizador de carrosséis, o de vídeos e o plano em Markdown
leem tudo daqui. Para criar novos posts, copie um bloco e edite.

Regra da casa (vinda das skills ig-*): nada de número, resultado ou cliente
inventado. Se um dia tiver um caso real com número, ele entra aqui.
"""

MARCA = "CR Automações"
FUSO = "America/Sao_Paulo"

# ---------------------------------------------------------------- carrosséis
# tipos de slide: capa | item | lista | antesdepois | cta
CARROSSEIS = [
    {
        "id": "c01",
        "data": "2026-11-16T12:00:00",
        "formula": "IG5 Listicle (saves)",
        "slides": [
            {"tipo": "capa", "kicker": "WHATSAPP DA SUA EMPRESA",
             "titulo": "5 sinais de que você está perdendo cliente no WhatsApp",
             "sub": "o 4º acontece todo fim de semana"},
            {"tipo": "item", "n": "1", "titulo": "Cliente pergunta o preço e some",
             "corpo": "Ele perguntou pra você e pra mais três. Quem respondeu primeiro levou a conversa."},
            {"tipo": "item", "n": "2", "titulo": "Você responde \"bom dia\" às 15h",
             "corpo": "Resposta atrasada passa a mensagem de que a empresa não está ali. O cliente sente."},
            {"tipo": "item", "n": "3", "titulo": "Ninguém sabe quantos contatos chegaram ontem",
             "corpo": "Sem número, não dá pra saber se o marketing funcionou ou se o atendimento travou."},
            {"tipo": "item", "n": "4", "titulo": "Mensagem de sábado só é vista na segunda",
             "corpo": "O cliente decide no fim de semana. Na segunda ele já comprou de outro."},
            {"tipo": "item", "n": "5", "titulo": "O follow-up depende da sua memória",
             "corpo": "\"Vou pensar e te falo\" vira silêncio porque ninguém voltou a chamar."},
            {"tipo": "cta", "titulo": "Marcou 2 ou mais?",
             "corpo": "Seu WhatsApp está deixando venda na mesa. Dá pra resolver com automação + um painel que mostra tudo.",
             "acao": "Salva este post e comenta AUTOMAÇÃO"},
        ],
        "legenda": (
            "você não perde cliente só por preço. muitas vezes perde por demora.\n\n"
            "passa o carrossel e conta quantos desses sinais acontecem aí na sua empresa. "
            "o 4º é o mais comum e quase ninguém percebe.\n\n"
            "se marcou 2 ou mais, comenta AUTOMAÇÃO que eu te explico como resolver sem contratar mais gente."
        ),
        "hashtags": ["#automacaowhatsapp", "#atendimentoaocliente", "#pequenasempresas", "#vendaspelowhatsapp"],
    },
    {
        "id": "c02",
        "data": "2026-11-18T12:00:00",
        "formula": "IG8 Steal-This Framework (saves)",
        "slides": [
            {"tipo": "capa", "kicker": "SEM ENROLAÇÃO",
             "titulo": "Como funciona uma automação de WhatsApp de verdade",
             "sub": "4 etapas. a 3ª é a que separa curioso de cliente"},
            {"tipo": "item", "n": "1", "titulo": "Recebe",
             "corpo": "Toda mensagem é respondida na hora, 24h por dia, inclusive feriado e madrugada."},
            {"tipo": "item", "n": "2", "titulo": "Entende",
             "corpo": "O fluxo identifica o que a pessoa quer: preço, horário, agendamento, suporte."},
            {"tipo": "item", "n": "3", "titulo": "Qualifica",
             "corpo": "Faz as perguntas certas e separa quem está pronto pra comprar de quem só está pesquisando."},
            {"tipo": "item", "n": "4", "titulo": "Agenda ou encaminha",
             "corpo": "Marca o horário sozinho ou passa a conversa pra sua equipe, já com o contexto todo."},
            {"tipo": "item", "n": "+", "titulo": "E tudo cai num painel",
             "corpo": "Mensagens por dia, horário de pico e cada contato num CRM: novo, interessado, agendado, concluído."},
            {"tipo": "cta", "titulo": "Recebe → Entende → Qualifica → Agenda",
             "corpo": "Salva esse esquema. É a base de qualquer atendimento automático que funciona.",
             "acao": "Quer o seu? Comenta AUTOMAÇÃO"},
        ],
        "legenda": (
            "automação de WhatsApp não é um robô mandando \"digite 1\".\n\n"
            "é um processo de 4 etapas, e a etapa 3 é a que faz diferença no caixa: "
            "qualificar antes de passar pra equipe.\n\n"
            "salva pra consultar depois e manda pra quem cuida do atendimento aí."
        ),
        "hashtags": ["#automacaowhatsapp", "#chatbot", "#atendimentoaocliente", "#empreendedorismo"],
    },
    {
        "id": "c03",
        "data": "2026-11-20T12:00:00",
        "formula": "IG7 Myth-Buster (shares)",
        "slides": [
            {"tipo": "capa", "kicker": "MITOS",
             "titulo": "4 mentiras que te contaram sobre automação de atendimento",
             "sub": "a última é a que mais trava empresário"},
            {"tipo": "antesdepois", "n": "1", "mito": "\"Robô espanta cliente\"",
             "verdade": "O que espanta é robô mal feito. Fluxo bem escrito parece conversa e resolve rápido."},
            {"tipo": "antesdepois", "n": "2", "mito": "\"É coisa de empresa grande\"",
             "verdade": "Quem mais ganha é a pequena: é quem tem menos gente pra responder tudo."},
            {"tipo": "antesdepois", "n": "3", "mito": "\"Vou perder o toque humano\"",
             "verdade": "A automação cuida do repetitivo. Sua equipe fica livre pra conversa que fecha venda."},
            {"tipo": "antesdepois", "n": "4", "mito": "\"Depois eu vejo isso\"",
             "verdade": "Cada semana sem resposta rápida é cliente indo pro concorrente que responde."},
            {"tipo": "cta", "titulo": "Automação boa não substitui gente.",
             "corpo": "Ela garante que nenhum cliente fique sem resposta enquanto sua equipe faz o que importa.",
             "acao": "Manda pra um empresário que precisa ver isso"},
        ],
        "legenda": (
            "\"robô espanta cliente\" é o mito que mais escuto. e faz sentido: todo mundo já caiu num menu de \"digite 1\" infinito.\n\n"
            "mas o problema nunca foi a automação. é automação mal feita.\n\n"
            "qual desses você já pensou? me conta nos comentários."
        ),
        "hashtags": ["#automacao", "#atendimentoaocliente", "#pequenasempresas", "#gestaodeempresas"],
    },
    {
        "id": "c04",
        "data": "2026-11-23T12:00:00",
        "formula": "IG6 Before/After (saves, follows)",
        "slides": [
            {"tipo": "capa", "kicker": "ANTES x DEPOIS",
             "titulo": "O mesmo cliente, a mesma mensagem. Dois finais diferentes.",
             "sub": "arrasta e vê o que muda"},
            {"tipo": "item", "n": "22h", "titulo": "Chega: \"oi, quanto custa?\"",
             "corpo": "Sua empresa já fechou. O celular está carregando na gaveta."},
            {"tipo": "antesdepois", "n": "SEM", "mito": "Ninguém responde",
             "verdade": "Às 9h você manda \"bom dia, tudo bem?\". Ele já resolveu com outra empresa ontem à noite.", "cor": "vermelho"},
            {"tipo": "antesdepois", "n": "COM", "mito": "Resposta em segundos",
             "verdade": "A automação responde, tira a dúvida do preço e oferece horários livres.", "cor": "verde"},
            {"tipo": "item", "n": "9h", "titulo": "Você chega e encontra:",
             "corpo": "Um horário agendado e o contato já na coluna \"Agendado\" do seu CRM."},
            {"tipo": "cta", "titulo": "A diferença não foi o preço.",
             "corpo": "Foi quem estava lá na hora que o cliente quis comprar.",
             "acao": "Segue pra mais conteúdo assim"},
        ],
        "legenda": (
            "mesma pergunta, mesmo cliente, mesma hora. a diferença foi só quem respondeu.\n\n"
            "a maior parte das vendas perdidas no WhatsApp não aparece em lugar nenhum. "
            "a pessoa só some.\n\n"
            "segue a CR Automações pra ver como montar isso na sua empresa."
        ),
        "hashtags": ["#vendaspelowhatsapp", "#automacaowhatsapp", "#empreendedor", "#atendimento"],
    },
    {
        "id": "c05",
        "data": "2026-11-25T12:00:00",
        "formula": "IG8 Steal-This Framework (saves)",
        "slides": [
            {"tipo": "capa", "kicker": "FUNIL DO WHATSAPP",
             "titulo": "As 4 colunas que organizam todo cliente que te chama",
             "sub": "copia esse funil hoje, mesmo sem automação"},
            {"tipo": "item", "n": "1", "titulo": "Novo contato",
             "corpo": "Chegou agora. Meta: responder rápido e descobrir o que a pessoa precisa."},
            {"tipo": "item", "n": "2", "titulo": "Interessado",
             "corpo": "Pediu preço ou detalhes. Meta: tirar a objeção e propor o próximo passo."},
            {"tipo": "item", "n": "3", "titulo": "Agendado",
             "corpo": "Marcou horário ou visita. Meta: lembrete antes pra ele não faltar."},
            {"tipo": "item", "n": "4", "titulo": "Concluído",
             "corpo": "Comprou ou foi atendido. Meta: pedir avaliação e chamar de novo no futuro."},
            {"tipo": "lista", "titulo": "Regra de ouro",
             "itens": ["Todo contato está em uma coluna", "Ninguém fica parado mais de 1 dia", "Você olha o quadro todo dia"]},
            {"tipo": "cta", "titulo": "No nosso painel isso é arrastar e soltar.",
             "corpo": "Cada conversa do WhatsApp vira um cartão no CRM, com anotações.",
             "acao": "Salva e comenta FUNIL"},
        ],
        "legenda": (
            "se você não sabe em que etapa está cada cliente que te chamou essa semana, você está vendendo no escuro.\n\n"
            "4 colunas resolvem: novo contato, interessado, agendado, concluído.\n\n"
            "dá pra fazer até numa planilha. no painel da CR é arrastar o cartão. "
            "comenta FUNIL que eu te mostro funcionando."
        ),
        "hashtags": ["#crm", "#funildevendas", "#vendaspelowhatsapp", "#pequenasempresas"],
    },
    {
        "id": "c06",
        "data": "2026-11-27T10:00:00",
        "formula": "IG5 Listicle (saves, shares) — Black Friday",
        "slides": [
            {"tipo": "capa", "kicker": "BLACK FRIDAY",
             "titulo": "Checklist pra não perder venda no WhatsApp hoje",
             "sub": "ainda dá tempo de fazer o 1 e o 2"},
            {"tipo": "item", "n": "1", "titulo": "Mensagem de boas-vindas com a oferta",
             "corpo": "Quem chamar já recebe o que está em promoção, sem esperar alguém digitar."},
            {"tipo": "item", "n": "2", "titulo": "Respostas prontas pras 5 perguntas de sempre",
             "corpo": "Preço, prazo, frete, forma de pagamento, troca. Escreve uma vez, usa o dia todo."},
            {"tipo": "item", "n": "3", "titulo": "Etiqueta em cada conversa",
             "corpo": "Separa quem já comprou de quem está negociando. Ninguém fica esquecido."},
            {"tipo": "item", "n": "4", "titulo": "Atendimento depois do horário",
             "corpo": "Muita gente compra à noite. Se ninguém responde, a venda vai pro concorrente."},
            {"tipo": "item", "n": "5", "titulo": "Follow-up no dia seguinte",
             "corpo": "\"Vi que você se interessou...\" recupera quem ficou na dúvida."},
            {"tipo": "cta", "titulo": "Fez os 5?",
             "corpo": "Agora imagina isso rodando sozinho o ano inteiro, não só na Black Friday.",
             "acao": "Salva e manda pro seu sócio"},
        ],
        "legenda": (
            "hoje seu WhatsApp vai receber mais mensagem que o normal. a pergunta é quantas vão ficar sem resposta.\n\n"
            "checklist rápido no carrossel. o 1 e o 2 dá pra fazer em menos de uma hora.\n\n"
            "salva e manda pra quem cuida do atendimento aí."
        ),
        "hashtags": ["#blackfriday", "#vendaspelowhatsapp", "#automacaowhatsapp", "#lojistas"],
    },
]

# ---------------------------------------------------------------- vídeos
# cenas: gancho | chat | lista | painel | texto | cta   (dur em segundos)
VIDEOS = [
    {
        "id": "v01",
        "data": "2026-11-17T19:00:00",
        "formula": "IG9 Pattern-Interrupt",
        "cenas": [
            {"tipo": "gancho", "dur": 3.0, "kicker": "23:47", "texto": "Um cliente te chamou agora."},
            {"tipo": "chat", "dur": 4.5, "msgs": [("in", "oi, vocês têm horário amanhã?"), ("in", "quanto fica?")]},
            {"tipo": "texto", "dur": 2.8, "texto": "Você está dormindo.", "sub": "e o concorrente também."},
            {"tipo": "texto", "dur": 2.8, "texto": "Quem responde primeiro, leva.", "destaque": True},
            {"tipo": "chat", "dur": 5.5, "msgs": [("in", "oi, vocês têm horário amanhã?"),
                                                  ("out", "Oi! Temos sim 😊 Prefere manhã ou tarde?"),
                                                  ("in", "manhã"),
                                                  ("out", "Fechado: amanhã 9h. Te mando lembrete!")]},
            {"tipo": "cta", "dur": 3.5, "texto": "Automação de WhatsApp", "sub": "comenta AUTOMAÇÃO"},
        ],
        "roteiro_fala": "São quase meia-noite e um cliente te chamou. Você tá dormindo. Quem responde primeiro, leva. Com automação, ele recebe resposta na hora e já sai com horário marcado. Comenta AUTOMAÇÃO.",
        "legenda": (
            "o cliente não espera o horário comercial pra decidir.\n\n"
            "com automação, a resposta sai na hora e o horário já fica marcado. você acorda com a agenda preenchida.\n\n"
            "comenta AUTOMAÇÃO que eu te mostro como fica na sua empresa."
        ),
        "hashtags": ["#automacaowhatsapp", "#atendimento24h", "#pequenasempresas", "#empreendedorismo"],
    },
    {
        "id": "v02",
        "data": "2026-11-19T19:00:00",
        "formula": "IG10 How-I",
        "cenas": [
            {"tipo": "gancho", "dur": 3.0, "kicker": "TODO SANTO DIA", "texto": "As 3 perguntas que roubam seu tempo"},
            {"tipo": "lista", "dur": 5.0, "titulo": "Você responde isso o dia inteiro:",
             "itens": ["\"Quanto custa?\"", "\"Qual o horário?\"", "\"Onde fica?\""]},
            {"tipo": "texto", "dur": 3.0, "texto": "Uma vez, tudo bem.", "sub": "Cem vezes por mês, é um funcionário."},
            {"tipo": "chat", "dur": 5.0, "msgs": [("in", "qual o horário de vocês?"),
                                                  ("out", "Seg a sex 8h–18h, sáb 8h–12h. Quer agendar?")]},
            {"tipo": "texto", "dur": 2.8, "texto": "Escreve uma vez.", "sub": "A automação responde pra sempre.", "destaque": True},
            {"tipo": "cta", "dur": 3.5, "texto": "Segue a CR Automações", "sub": "pra mais atalhos assim"},
        ],
        "roteiro_fala": "Quanto custa, qual o horário, onde fica. Você responde isso o dia inteiro. Uma vez tudo bem, mas todo dia vira o trabalho de uma pessoa. Escreve a resposta uma vez e deixa a automação responder pra sempre.",
        "legenda": (
            "preço, horário e endereço. se você somar o tempo que gasta respondendo isso, vai se assustar.\n\n"
            "escreve uma vez e deixa a automação responder. sua equipe fica pra conversa que fecha venda.\n\n"
            "qual é a pergunta que você mais responde? me fala aqui."
        ),
        "hashtags": ["#produtividade", "#automacaowhatsapp", "#atendimentoaocliente", "#dicasdenegocio"],
    },
    {
        "id": "v03",
        "data": "2026-11-21T11:00:00",
        "formula": "IG10 How-I (bastidores do painel)",
        "cenas": [
            {"tipo": "gancho", "dur": 3.0, "kicker": "BASTIDORES", "texto": "O painel que mostra o que seu WhatsApp esconde"},
            {"tipo": "painel", "dur": 5.0, "foco": "dias", "legenda": "Mensagens por dia"},
            {"tipo": "painel", "dur": 4.5, "foco": "horas", "legenda": "Horário de pico"},
            {"tipo": "painel", "dur": 4.5, "foco": "crm", "legenda": "Cada contato numa coluna"},
            {"tipo": "texto", "dur": 3.0, "texto": "Sem achismo.", "sub": "Você vê onde o cliente trava.", "destaque": True},
            {"tipo": "cta", "dur": 3.5, "texto": "Quer ver o seu?", "sub": "comenta PAINEL"},
        ],
        "roteiro_fala": "Esse é o painel que eu entrego junto com a automação. Mensagens por dia, horário de pico, e cada contato numa coluna do CRM. Sem achismo: você vê exatamente onde o cliente trava. Comenta PAINEL.",
        "legenda": (
            "a maioria das empresas não sabe quantas pessoas chamaram no WhatsApp ontem.\n\n"
            "no painel da CR você vê mensagens por dia, horário de pico e cada contato num CRM de arrastar. "
            "(dados ilustrativos no vídeo)\n\n"
            "comenta PAINEL que eu te mostro ao vivo."
        ),
        "hashtags": ["#dashboard", "#crm", "#automacaowhatsapp", "#gestaodeempresas"],
    },
    {
        "id": "v04",
        "data": "2026-11-24T19:00:00",
        "formula": "IG2 Contrarian (reel)",
        "cenas": [
            {"tipo": "gancho", "dur": 3.0, "kicker": "VERDADE INCÔMODA", "texto": "Seu horário de pico não é o que você acha"},
            {"tipo": "texto", "dur": 3.2, "texto": "Você coloca gente no balcão às 10h.", "sub": "o cliente chama às 21h."},
            {"tipo": "painel", "dur": 4.5, "foco": "horas", "legenda": "o painel mostra a hora real"},
            {"tipo": "lista", "dur": 5.0, "titulo": "Com esse dado você:",
             "itens": ["Ajusta a escala da equipe", "Liga a automação no horário vazio", "Agenda posts na hora certa"]},
            {"tipo": "cta", "dur": 3.5, "texto": "Para de chutar.", "sub": "comenta PAINEL"},
        ],
        "roteiro_fala": "Seu horário de pico provavelmente não é o que você acha. Muita empresa coloca gente pra atender de manhã enquanto o cliente chama à noite. O painel mostra a hora real, e com isso você ajusta equipe, automação e até a hora de postar.",
        "legenda": (
            "você escala a equipe pelo horário comercial. o seu cliente não segue horário comercial.\n\n"
            "quando você vê a hora real em que as mensagens chegam, muda a escala, liga a automação no horário vazio e até posta na hora certa.\n\n"
            "comenta PAINEL pra ver o seu."
        ),
        "hashtags": ["#gestaodeempresas", "#dadosparadecisao", "#automacaowhatsapp", "#empreendedor"],
    },
    {
        "id": "v05",
        "data": "2026-11-26T19:00:00",
        "formula": "IG3 Relatable (qualificação)",
        "cenas": [
            {"tipo": "gancho", "dur": 3.0, "kicker": "SEM ENROLAR", "texto": "Automação de WhatsApp NÃO é pra todo mundo"},
            {"tipo": "lista", "dur": 5.5, "titulo": "É pra você se:",
             "itens": ["Recebe muita mensagem repetida", "Perde cliente fora do horário", "Não sabe quantos leads chegam"]},
            {"tipo": "lista", "dur": 5.0, "titulo": "Não é pra você se:", "negativo": True,
             "itens": ["Recebe 2 mensagens por semana", "Não quer olhar pra números"]},
            {"tipo": "texto", "dur": 3.0, "texto": "Se marcou a primeira lista...", "sub": "a gente precisa conversar.", "destaque": True},
            {"tipo": "cta", "dur": 3.5, "texto": "Comenta AUTOMAÇÃO", "sub": "te chamo no direct"},
        ],
        "roteiro_fala": "Automação de WhatsApp não é pra todo mundo. É pra quem recebe muita mensagem repetida, perde cliente fora do horário e não sabe quantos leads chegam. Se você recebe duas mensagens por semana, não precisa. Se marcou a primeira lista, comenta AUTOMAÇÃO.",
        "legenda": (
            "não vou te vender automação se você não precisa.\n\n"
            "se você recebe mensagem repetida o dia todo, perde gente fora do horário e não sabe quantos contatos chegam, aí sim faz sentido.\n\n"
            "se encaixou, comenta AUTOMAÇÃO que eu te chamo."
        ),
        "hashtags": ["#automacaowhatsapp", "#pequenasempresas", "#vendas", "#empreendedorismo"],
    },
    {
        "id": "v06",
        "data": "2026-11-28T11:00:00",
        "formula": "IG10 How-I (oferta)",
        "cenas": [
            {"tipo": "gancho", "dur": 3.0, "kicker": "COMO FUNCIONA", "texto": "Como eu monto a automação do seu WhatsApp"},
            {"tipo": "lista", "dur": 6.0, "titulo": "4 passos:",
             "itens": ["Diagnóstico do seu atendimento", "Fluxo escrito com a sua cara", "Testes antes de ligar", "Painel + CRM pra acompanhar"]},
            {"tipo": "chat", "dur": 4.5, "msgs": [("in", "quero entender como funciona"),
                                                  ("out", "Bora! Me conta: qual é o seu negócio?")]},
            {"tipo": "texto", "dur": 3.0, "texto": "Você não precisa entender de tecnologia.", "sub": "isso é comigo.", "destaque": True},
            {"tipo": "cta", "dur": 3.5, "texto": "Comenta AUTOMAÇÃO", "sub": "ou chama no link da bio"},
        ],
        "roteiro_fala": "É assim que eu monto a automação do seu WhatsApp: diagnóstico do seu atendimento, fluxo escrito com a sua cara, testes antes de ligar, e um painel com CRM pra você acompanhar tudo. Você não precisa entender de tecnologia. Comenta AUTOMAÇÃO.",
        "legenda": (
            "você não precisa entender de tecnologia pra ter um atendimento que responde sozinho.\n\n"
            "diagnóstico, fluxo com a cara da sua empresa, testes e um painel pra acompanhar. é assim que funciona.\n\n"
            "comenta AUTOMAÇÃO ou chama no link da bio."
        ),
        "hashtags": ["#automacaowhatsapp", "#chatbot", "#pequenasempresas", "#transformacaodigital"],
    },
]
