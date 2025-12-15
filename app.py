from flask import Flask, render_template, jsonify

app = Flask(__name__)

dados_profissoes = [
    {
        "id": 1,
        "nome": "Dev. Python (Back-End)",
        "salario_medio": "R$ 9.200",
        "crescimento": "+30%",
        "profissionais_ativos": "350.000",
        "nivel_estresse": "Médio",
        "descricao": "Cria a lógica por trás dos sites, APIs e inteligência de dados.",
        "perspectiva_10_anos": "+150% (Explosivo)",
        "formados_ano": 15000,
        "demanda_anual": 24000
    },
    {
        "id": 2,
        "nome": "Dev. Front-End (React/Vue)",
        "salario_medio": "R$ 7.800",
        "crescimento": "+22%",
        "profissionais_ativos": "200.000",
        "nivel_estresse": "Médio",
        "descricao": "Responsável pelo visual e interatividade de sites e aplicativos.",
        "perspectiva_10_anos": "+80% (Alta)",
        "formados_ano": 25000,
        "demanda_anual": 28000
    },
    {
        "id": 3,
        "nome": "Especialista em Cibersegurança",
        "salario_medio": "R$ 13.000",
        "crescimento": "+40%",
        "profissionais_ativos": "80.000",
        "nivel_estresse": "Muito Alto",
        "descricao": "Protege empresas contra ataques hackers e vazamento de dados.",
        "perspectiva_10_anos": "+200% (Crítico)",
        "formados_ano": 4000,
        "demanda_anual": 18000
    },
    {
        "id": 4,
        "nome": "Cientista de Dados",
        "salario_medio": "R$ 12.200",
        "crescimento": "+35%",
        "profissionais_ativos": "120.000",
        "nivel_estresse": "Alto",
        "descricao": "Analisa estatísticas complexas para guiar decisões de negócios.",
        "perspectiva_10_anos": "+120% (Muito Alta)",
        "formados_ano": 8000,
        "demanda_anual": 15000
    },
    {
        "id": 5,
        "nome": "Engenheiro de IA",
        "salario_medio": "R$ 16.000",
        "crescimento": "+55%",
        "profissionais_ativos": "40.000",
        "nivel_estresse": "Alto",
        "descricao": "Treina modelos de Inteligência Artificial e Machine Learning.",
        "perspectiva_10_anos": "+300% (Revolucionário)",
        "formados_ano": 2000,
        "demanda_anual": 10000
    },
    {
        "id": 6,
        "nome": "Product Owner (PO)",
        "salario_medio": "R$ 11.000",
        "crescimento": "+20%",
        "profissionais_ativos": "90.000",
        "nivel_estresse": "Alto",
        "descricao": "Define as prioridades do produto e faz a ponte entre TI e Negócios.",
        "perspectiva_10_anos": "+40% (Estável)",
        "formados_ano": 12000,
        "demanda_anual": 14000
    },

    {
        "id": 7,
        "nome": "Médico Cirurgião",
        "salario_medio": "R$ 18.500",
        "crescimento": "+15%",
        "profissionais_ativos": "350.000",
        "nivel_estresse": "Extremo",
        "descricao": "Realiza procedimentos invasivos para tratamento de doenças.",
        "perspectiva_10_anos": "+30% (Sempre Alta)",
        "formados_ano": 25000,
        "demanda_anual": 35000
    },
    {
        "id": 8,
        "nome": "Enfermeiro Chefe",
        "salario_medio": "R$ 6.500",
        "crescimento": "+25%",
        "profissionais_ativos": "600.000",
        "nivel_estresse": "Muito Alto",
        "descricao": "Gerencia equipes de enfermagem e cuidados intensivos.",
        "perspectiva_10_anos": "+60% (Envelhecimento Pop.)",
        "formados_ano": 40000,
        "demanda_anual": 55000
    },
    {
        "id": 9,
        "nome": "Psicólogo Clínico",
        "salario_medio": "R$ 4.200",
        "crescimento": "+35%",
        "profissionais_ativos": "450.000",
        "nivel_estresse": "Alto",
        "descricao": "Trata da saúde mental e comportamental dos pacientes.",
        "perspectiva_10_anos": "+80% (Alta Demanda)",
        "formados_ano": 60000,
        "demanda_anual": 62000
    },
    {
        "id": 10,
        "nome": "Nutricionista",
        "salario_medio": "R$ 3.800",
        "crescimento": "+10%",
        "profissionais_ativos": "180.000",
        "nivel_estresse": "Baixo",
        "descricao": "Planeja dietas e promove reeducação alimentar.",
        "perspectiva_10_anos": "+20% (Moderada)",
        "formados_ano": 25000,
        "demanda_anual": 20000
    },

    {
        "id": 11,
        "nome": "Engenheiro Civil",
        "salario_medio": "R$ 8.500",
        "crescimento": "+5%",
        "profissionais_ativos": "300.000",
        "nivel_estresse": "Alto",
        "descricao": "Projeta e gerencia obras de infraestrutura e edifícios.",
        "perspectiva_10_anos": "+10% (Depende da Economia)",
        "formados_ano": 40000,
        "demanda_anual": 30000
    },
    {
        "id": 12,
        "nome": "Engenheiro de Energias",
        "salario_medio": "R$ 10.500",
        "crescimento": "+60%",
        "profissionais_ativos": "15.000",
        "nivel_estresse": "Médio",
        "descricao": "Foca em fontes renováveis: Solar, Eólica e Hidrogênio.",
        "perspectiva_10_anos": "+200% (Transição Verde)",
        "formados_ano": 2000,
        "demanda_anual": 8000
    },
    {
        "id": 13,
        "nome": "Engenheiro Agrônomo",
        "salario_medio": "R$ 9.000",
        "crescimento": "+28%",
        "profissionais_ativos": "100.000",
        "nivel_estresse": "Médio",
        "descricao": "Otimiza a produção agrícola e gestão do agronegócio.",
        "perspectiva_10_anos": "+50% (Agro Tech)",
        "formados_ano": 12000,
        "demanda_anual": 18000
    },

    {
        "id": 14,
        "nome": "Gerente de Projetos",
        "salario_medio": "R$ 10.000",
        "crescimento": "+15%",
        "profissionais_ativos": "300.000",
        "nivel_estresse": "Alto",
        "descricao": "Liderança de equipes e gestão de prazos/custos corporativos.",
        "perspectiva_10_anos": "+45% (Estável)",
        "formados_ano": 50000,
        "demanda_anual": 48000
    },
    {
        "id": 15,
        "nome": "Analista de Investimentos",
        "salario_medio": "R$ 14.000",
        "crescimento": "+18%",
        "profissionais_ativos": "40.000",
        "nivel_estresse": "Muito Alto",
        "descricao": "Recomenda onde aplicar dinheiro na bolsa e fundos.",
        "perspectiva_10_anos": "+35% (Alta)",
        "formados_ano": 5000,
        "demanda_anual": 7000
    },
    {
        "id": 16,
        "nome": "Contador",
        "salario_medio": "R$ 5.500",
        "crescimento": "+5%",
        "profissionais_ativos": "520.000",
        "nivel_estresse": "Médio",
        "descricao": "Gestão tributária, balanços e conformidade fiscal.",
        "perspectiva_10_anos": "-10% (Automação)",
        "formados_ano": 70000,
        "demanda_anual": 65000
    },
    {
        "id": 17,
        "nome": "Especialista em Marketing Digital",
        "salario_medio": "R$ 6.800",
        "crescimento": "+45%",
        "profissionais_ativos": "250.000",
        "nivel_estresse": "Alto",
        "descricao": "Gerencia tráfego pago, redes sociais e branding.",
        "perspectiva_10_anos": "+100% (Essencial)",
        "formados_ano": 40000,
        "demanda_anual": 60000
    },

    {
        "id": 18,
        "nome": "Advogado Júnior",
        "salario_medio": "R$ 3.500",
        "crescimento": "+2%",
        "profissionais_ativos": "1.300.000",
        "nivel_estresse": "Alto",
        "descricao": "Atuação em processos civis, trabalhistas ou criminais.",
        "perspectiva_10_anos": "+5% (Concorrência Alta)",
        "formados_ano": 120000,
        "demanda_anual": 80000
    },

    {
        "id": 19,
        "nome": "UX/UI Designer",
        "salario_medio": "R$ 7.500",
        "crescimento": "+30%",
        "profissionais_ativos": "80.000",
        "nivel_estresse": "Médio",
        "descricao": "Desenha a experiência do usuário em aplicativos e sistemas.",
        "perspectiva_10_anos": "+60% (Alta)",
        "formados_ano": 10000,
        "demanda_anual": 15000
    },
    {
        "id": 20,
        "nome": "Editor de Vídeo",
        "salario_medio": "R$ 4.000",
        "crescimento": "+50%",
        "profissionais_ativos": "100.000",
        "nivel_estresse": "Médio",
        "descricao": "Edição para YouTube, Cinema e Publicidade.",
        "perspectiva_10_anos": "+90% (Creator Economy)",
        "formados_ano": 15000,
        "demanda_anual": 22000
    }
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/dados')
def obter_dados():
    return jsonify(dados_profissoes)


if __name__ == '__main__':
    app.run(debug=True)
