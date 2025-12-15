# 📊 Dashboard de Análise de Mercado de Profissões

![Status](https://img.shields.io/badge/Status-Finalizado-green) ![Python](https://img.shields.io/badge/Python-3.13-blue) ![Flask](https://img.shields.io/badge/Flask-Framework-red) ![FrontEnd](https://img.shields.io/badge/FrontEnd-HTML%2FCSS%2FJS-orange)

## 📖 Sobre o Projeto

Este projeto é um **Dashboard Analítico** focado no mercado de trabalho brasileiro. O objetivo principal é fornecer uma interface visual e interativa para que estudantes e profissionais analisem a viabilidade de carreiras específicas para os próximos 10 anos.

O sistema utiliza uma lógica interna de **"Gap de Mercado"**, cruzando dados (simulados) de novos formandos anuais contra a demanda real de vagas, classificando automaticamente a carreira em:
* 🔵 **DÉFICIT:** Onde faltam profissionais (Alta empregabilidade).
* 🔴 **SATURADO:** Onde há excesso de mão de obra (Alta concorrência).
* ⚪ **EQUILIBRADO:** Onde a oferta atende a demanda.

## 🚀 Funcionalidades Principais

* **Interface Dark Mode:** Design moderno ("Cyberpunk Clean") focado na experiência do usuário (UX), com detalhes em Azul Neon para destacar informações críticas.
* **Cálculos em Tempo Real:** O Python processa os dados e o JavaScript atualiza a interface instantaneamente sem recarregar a página.
* **Projeção Salarial (Gráfico):** Utilização da biblioteca *Chart.js* para desenhar a curva de evolução salarial desde o nível Júnior até o Especialista.
* **Modal de Contexto:** Tela inicial que situa o usuário sobre a abrangência geográfica (Brasil) e o propósito da ferramenta.

## 🛠 Tecnologias Utilizadas

### Back-End (O Cérebro)
* **Python 3:** Linguagem base para a lógica de negócios.
* **Flask:** Micro-framework web utilizado para criar as rotas (`/`) e a API JSON (`/api/dados`) que alimenta o front-end.
* **Lógica de Dados:** Estruturação de dicionários complexos para simular um banco de dados de profissões (TI, Saúde, Engenharia, Direito, etc.).

### Front-End (O Visual)
* **HTML5:** Estrutura semântica organizada.
* **CSS3:**
    * Uso de **Flexbox** e **CSS Grid** para layout responsivo.
    * Variáveis CSS (`:root`) para fácil manutenção de cores.
    * Efeitos de *Hover* e *Glow* (Brilho Neon).
    * Fontes profissionais: *Poppins* (Títulos) e *Inter* (Leitura).
* **JavaScript (ES6+):**
    * **Fetch API:** Consumo assíncrono de dados do Python.
    * **DOM Manipulation:** Atualização dinâmica dos 8 cards de informação.
    * **Chart.js:** Renderização de gráficos de linha interativos.

## 📦 Como Rodar este Projeto

### Pré-requisitos
Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado em sua máquina.

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/viniols1/dashboard-analise-mercado.git](https://github.com/viniols1/dashboard-analise-mercado.git)
    ```

2.  **Entre na pasta do projeto:**
    ```bash
    cd dashboard-analise-mercado
    ```

3.  **Instale as dependências (Flask):**
    ```bash
    pip install flask
    ```

4.  **Execute o servidor:**
    ```bash
    python app.py
    ```

5.  **Acesse o Dashboard:**
    Abra seu navegador e digite: `http://127.0.0.1:5000`

---

## ⚠️ Nota Importante sobre os Dados
Embora a lógica de programação, o cálculo de déficit e a estrutura do software sejam funcionais e precisos, os **números estatísticos** (salários, quantidade de vagas e formandos) apresentados neste dashboard são **simulados** para fins didáticos e de demonstração de portfólio. Para uso comercial, recomenda-se a integração com APIs reais de dados públicos (IBGE/CAGED).

---

## 👨‍💻 Autor

**Vinicius Oliveira**
* Estudante de Análise e Desenvolvimento de Sistemas (Mackenzie)
* Foco em Desenvolvimento Full Stack e Python.

---
*Desenvolvido em 2025.*