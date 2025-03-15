import streamlit as st

# Configuração da página
st.set_page_config(page_title="Jorge Booz - Engenheiro de Software", layout="wide")

# Estilos CSS personalizados
st.markdown(
    """
    <style>
    .stApp {
        color: #0f1820; 

    }
    a {
        color: #d10f45; /* Cor terciária */
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    .section {
        margin-bottom: 30px;
        padding: 20px;
        background-color: #0f1820; 
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .header {
        background-color: #0f1820; 
        color: #fff; 
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 30px;
    }
    .footer {
        text-align: center;
        margin-top: 30px;
        font-size: 0.9em;
        color: #ffffff; /* Cor primária */
    }
    .hover-effect:hover {
        color: #d10f45; /* Cor terciária */
        cursor: pointer;
    }
    .col1 {
        padding-right: 20px; /* Espaço à direita da coluna 1 */
    }
    .col2 {
        padding-left: 20px; /* Espaço à esquerda da coluna 2 */
        text-align: right; /* Alinhar conteúdo à direita */
    }
    .separator {
        width: 2px;
        background-color: #d10f45; /* Cor terciária */
        margin: 0 20px; /* Espaço ao redor da coluna separadora */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Cabeçalho
st.markdown(
    """
    <div class="header">
        <h1 style="color: #fffff;">Jorge Henrique Freire Booz</h1>
        <h3 style="color: #d10f45;">Engenheiro de Software</h3>
        <p>
            <a href="https://github.com/jorgebooz" target="_blank">GitHub</a> | 
            <a href="https://linkedin.com/in/jorgebooz/" target="_blank">LinkedIn</a> | 
            <a mailto="https://linkedin.com/in/jorgebooz/" target="_blank">jorg.jhfb@gmail.com</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Layout de três colunas (esquerda, separador, direita)
col1, col_sep, col2 = st.columns([1.2, 0.05, 1])

# Coluna 1: Sobre, Experiência e Projetos
with col1:
    st.markdown('<div class="col1">', unsafe_allow_html=True)

    # Sobre
    st.markdown(
        '<h3 style="color: #d10f45;">Sobre</h3>', 
        unsafe_allow_html=True
    )
    st.write(
        """
        Engenheiro de Software com experiência em backend, frontend e análise de dados, utilizando tecnologias como Java, Spring Boot, React.js, Power BI e Python.
        Capacidade de desenvolver soluções inovadoras e transformar dados em insights, além de criar interfaces intuitivas e sustentáveis.
        """
    )

    # Experiência
    st.markdown(
        '<h3 style="color: #d10f45;">Experiência</h3>', 
        unsafe_allow_html=True
    )
    st.markdown("**Estágio Automações - Fluxee (Sodexo)**  \n*FEV 2024 - Presente*")
    st.write(
        """
        - Power Automate;
        - Desenvolvimento de Automações;
        - Desenvolvimento de Power Apps;
        - Atendimento de chamados;
        - Metodologias Ágeis;
        - Sustentação;
        - Documentação Técnica.
        """
    )

    st.markdown("**Estágio Data Analytics - Elife**  \n*NOV 2022 - JAN 2024*")
    st.write(
        """
        - Data Mining;
        - Social Listening;
        - Análise de sentimentos.
        """
    )

    # Projetos
    st.markdown(
        '<h3 style="color: #d10f45;">Projetos</h3>', 
        unsafe_allow_html=True
    )
    st.markdown("**Compasso - HCFMUSP**")
    st.write(
        """
        Desenvolvimento de uma ferramenta para orientar visitantes dentro do hospital, mostrando o caminho mais rápido até o destino.
        **Tecnologias:** Python, React.js, MySQL, Arduino.
        """
    )

    st.markdown("**GameList**")
    st.write(
        """
        Sistema backend para gerenciar lista de jogos, com funcionalidades para listar, adicionar, editar e organizar descrições.
        **Tecnologias:** Java, Spring Boot, React.js, Docker.
        """
    )

    st.markdown("**Maré Cheia**")
    st.write(
        """
        Projeto voltado à conscientização ambiental de comunidades costeiras, monitorando indicadores oceânicos.
        **Tecnologias:** Python (Pandas, Matplotlib, Seaborn), React.js, Arduino/Sensores.
        """
    )

    st.markdown('</div>', unsafe_allow_html=True)

# Coluna Separadora
with col_sep:
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

# Coluna 2: Tecnologias, Educação, Cursos, Habilidades, Idiomas
with col2:
    st.markdown('<div class="col2">', unsafe_allow_html=True)

    # Tecnologias
    st.markdown(
        '<h3 style="color: #d10f45;">Tecnologias</h3>', 
        unsafe_allow_html=True
    )
    st.markdown("**Backend**")
    st.write("- Java\n- Spring Framework\n- SQL")
    st.markdown("**Frontend**")
    st.write("- React.js\n- JavaScript\n- HTML/CSS\n- Figma")
    st.markdown("**Data Science**")
    st.write("- Python (Pandas, Numpy, Matplotlib, Seaborn)\n- Power BI\n- Excel")

    # Educação
    st.markdown(
        '<h3 style="color: #d10f45;">Educação</h3>', 
        unsafe_allow_html=True
    )
    st.markdown("**Engenharia de Software - FIAP**  \n*2023-2027*")
    st.write("Linguagens de programação: Java (POO), Python, HTML, CSS, React.js.")

    st.markdown("**Comunicação Visual - ETEC Carlos de Campos**  \n*2019-2021*")

    # Cursos Complementares
    st.markdown(
        '<h3 style="color: #d10f45;">Cursos Complementares</h3>', 
        unsafe_allow_html=True
    )
    st.write(
        """
        - Formação Power BI (Alura)
        - Formação Excel (Alura)
        - Spring Boot (Alura)
        - Pandas para Data Science (Alura)
        - Oracle Database (Alura)
        - Algoritmo e Lógica de Programação (Curso em Vídeo)
        """
    )

    # Habilidades
    st.markdown(
        '<h3 style="color: #d10f45;">Habilidades</h3>', 
        unsafe_allow_html=True
    )
    st.write(
        """
        - Criatividade;
        - Comunicação Assertiva;
        - Resolução de problemas;
        - Pensamento Analítico;
        - Trabalho em equipe.
        """
    )

    # Idiomas
    st.markdown(
        '<h3 style="color: #d10f45;">Idiomas</h3>', 
        unsafe_allow_html=True
    )
    st.write("- Inglês - Intermediário")

    st.markdown('</div>', unsafe_allow_html=True)

# Rodapé
st.markdown(
    """
    <div class="footer">
        Desenvolvido com Streamlit por Jorge Booz.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="footer">
        Desenvolvido com Streamlit por Jorge Booz.
    </div>
    """,
    unsafe_allow_html=True,
)