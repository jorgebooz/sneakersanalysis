import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotnine import *
import seaborn as sns
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Dashboard de Distribuições Probabilísticas", layout="wide")

# Adicionando o logo
st.logo("logo.png")

# Adicionando o logo
st.image("logo.png", width=150)

def load_data():
    df = pd.read_csv("StockX-Data-Contest-2019-3.csv")
    df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%y")
    df["Release Date"] = pd.to_datetime(df["Release Date"], format="%m/%d/%y")
    df["Sale Price"] = df["Sale Price"].replace({'\\$': '', ',': ''}, regex=True).astype(float)
    df["Retail Price"] = df["Retail Price"].replace({'\\$': '', ',': ''}, regex=True).astype(float)
    df["Shoe Size"] = df["Shoe Size"].astype(float)
    df["Days to Sell"] = (df["Order Date"] - df["Release Date"]).dt.days
    df["Price Difference"] = df["Sale Price"] - df["Retail Price"]
    df['Month'] = df["Order Date"].dt.to_period('M')
    return df

df = load_data()

# Seção de Introdução do Conjunto de Dados
st.markdown(
    """
    <div class="section">
        <h2 style="color: #d10f45;">Introdução ao Conjunto de Dados</h2>
        <p>
            O mercado de sneakers é extremamente grande e dinâmico. <strong>O sistema de retail de sneakers</strong> envolve lançamentos limitados, estratégias de marketing exclusivas e uma forte cultura de revenda. Nesse modelo, as vendas de varejo são marcadas pela alta demanda e pela especulação, onde edições limitadas muitas vezes se transformam em itens de colecionador e são revendidas por preços significativamente maiores que o preço original.
            Neste projeto iremos analisar as vendas de duas marcas concorrentes a Off-White x Yeezy.
        </p>
        <p>
            Para entender as particularidades dessa disputa, busquei uma base de dados do maior marketplace do setor, abrangendo o período de 2017 a 2019. Com esses dados, podemos explorar aspectos mais profundos, como:
            <ul>
                <li>Qual foi o tênis mais vendido entre 2017-2019?</li>
                <li>Em média qual a margem de lucro que se tem ao revender um modelo das duas marcas?</li>
                <li>Qual a probabilidade de se ter lucro ao revender um dos modelos?</li>
                <li>A cada 20 tenis quantos serão tenis Off-White e qauntos Adidas?</li>
            </ul>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="background-color: #0f1820; padding: 10px; border-radius: 10px;">
        <h3 style="color: #d10f45;">Resumo do Conjunto de Dados</h3>
        <p>Este conjunto de dados contém informações sobre as vendas dos concorrentes entre 2017 e 2019 no maior marketplace do setor. As variáveis incluem identificador, datas, marca, modelo, preços de venda e varejo, tamanho do sneaker e região do comprador.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Converter a coluna 'Order Date' para datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Filtrar os dados para os anos de 2017 a 2019
df_filtrado = df[df['Order Date'].dt.year.between(2017, 2019)]

# Contar as vendas por 'Sneaker Name'
vendas = df_filtrado['Sneaker Name'].value_counts()

# Obter o tênis mais vendido
tenis_mais_vendido = vendas.idxmax()

# Exibir o nome do tênis em um H1
st.markdown(f'<h2 style="color: #fff;">Qual foi o tênis mais vendido entre 2017-2019?</h2>', unsafe_allow_html=True)

st.markdown(f'<h3 style="color: #d10f45;">{tenis_mais_vendido}</h3>', unsafe_allow_html=True)
st.image("yeezy350.jpg", width=300)

# Tabela de Identificação do Tipo das Variáveis
dados = {
    "Variável": [
        "id", 
        "Order Date", 
        "Brand", 
        "Sneaker Name", 
        "Sale Price", 
        "Retail Price", 
        "Release Date", 
        "Shoe Size", 
        "Buyer Region"
    ],
    "Descrição": [
        "Identificador único de cada venda",
        "Data em que o pedido foi realizado",
        "Marca do tênis",
        "Nome/modelo do tênis",
        "Preço de venda do tênis (valor pago pelo comprador)",
        "Preço de varejo sugerido do tênis",
        "Data de lançamento do tênis",
        "Tamanho do tênis vendido",
        "Região do comprador"
    ],
    "Tipo": [
        "Numérica (Inteiro)",
        "Data",
        "Categórica (String)",
        "Texto",
        "Numérica (Float)",
        "Numérica (Float)",
        "Data",
        "Numérica (Float)",
        "Categórica (String)"
    ]
}
df_variaveis = pd.DataFrame(dados)
st.markdown("""
<h2 style="color: #d10f45;">Identificação do Tipo das Variáveis</h2>
""", unsafe_allow_html=True)
st.table(df_variaveis)

col1, col2 = st.columns(2)

# Tópico 1: Preços de Venda (Sale Price) - Coluna 1
with col1:
    st.markdown("""
    <h3 style="color: #d10f45;">Margem de Lucro (%)</h3>
    <p> A margem de lucro representa o percentual de acréscimo entre o preço de venda e o preço de varejo, refletindo o potencial de rentabilidade dos pares.</p>
    """, unsafe_allow_html=True)
    
    # Calculando a margem de lucro percentual para cada sneaker
    df['Profit Margin (%)'] = ((df['Sale Price'] - df['Retail Price']) / df['Retail Price']) * 100
    
    mean_margin = df['Profit Margin (%)'].mean()
    median_margin = df['Profit Margin (%)'].median()
    mode_margin = df['Profit Margin (%)'].mode().iloc[0] if not df['Profit Margin (%)'].mode().empty else np.nan
    
    st.write(f"Média: **{mean_margin:.2f}%**")
    st.write(f"Mediana: **{median_margin:.2f}%**")
    st.write(f"Moda: **{mode_margin:.2f}%**")

# Tópico 2: Diferença entre Sale Price e Retail Price - Coluna 1
with col1:
    st.markdown("""
    <h3 style="color: #d10f45;">2. Diferença entre Sale Price e Retail Price</h3>
                <p> Embora a média de $208,61 seja ligeiramente inferior à mediana e à moda de $220,00, isso indica que alguns pares são vendidos por valores menores em seus lançamentos, enquanto muitos pares na revenda estão superinflacionados, sugerindo raridade ou alta demanda pelo par. </p>
    """, unsafe_allow_html=True)
    mean_retail = df["Retail Price"].mean()
    median_retail = df["Retail Price"].median()
    mode_retail = df["Retail Price"].mode().iloc[0] if not df["Retail Price"].mode().empty else np.nan

    st.write(f"Média: ${mean_retail:.2f}")
    st.write(f"Mediana: ${median_retail:.2f}")
    st.write(f"Moda: ${mode_retail:.2f}")   


# Tópico 3: Tamanhos Vendidos (Shoe Size) - Coluna 2
with col2:
    st.markdown("""
    <h3 style="color: #d10f45;">3. Tamanhos Vendidos (Shoe Size)</h3>
    
    <p> As três medidas de tendência central são próximas, indicando um alvo de tamanhos para comprar e revender.</p>
    """, unsafe_allow_html=True)
    mean_size = df["Shoe Size"].mean()
    median_size = df["Shoe Size"].median()
    mode_size = df["Shoe Size"].mode().iloc[0] if not df["Shoe Size"].mode().empty else np.nan
    st.write(f"Média do Tamanho: **{mean_size:.2f}**")
    st.write(f"Mediana do Tamanho: **{median_size:.2f}**")
    st.write(f"Moda do Tamanho: **{mode_size:.2f}**")

# Tópico 4: Tempo de Espera entre Lançamento e Venda - Coluna 2
with col2:
    st.markdown("""
    <h3 style="color: #d10f45;">4. Tempo de Espera (Data da compra - Data do lançamento)</h3>
    <p> Se consideramos a de esgotamento da loja como cerca de um mês, metade das vendas podem ser consideradas rápidas(26 dias), porém a baixa procura por alguns pares ou o tempo maior de disponibilidade nas lojas eleva muito o tempo médio de vendas. </p>
    """, unsafe_allow_html=True)
    mean_days = df["Days to Sell"].mean()
    median_days = df["Days to Sell"].median()
    mode_days = df["Days to Sell"].mode().iloc[0] if not df["Days to Sell"].mode().empty else np.nan
    st.write(f"Média de Dias para Venda: **{mean_days:.2f} dias**")
    st.write(f"Mediana de Dias para Venda: **{median_days:.2f} dias**")

st.markdown(f"""<h3 'color: #d10f45;'>Em média qual a margem de lucro que se tem ao revender um modelo das duas marcas?</h3>
            <p>Embora a média de 124.82% sugira que, em média, os sneakers são revendidos a mais do que o dobro do preço de lançamento, a moda de 22.73% indica que a maioria dos pares é negociada com um acréscimo de cerca de 22%, demonstrando que alguns outliers elevam significativamente a média.</p>""", unsafe_allow_html=True)


df_numeric = df.select_dtypes(include=['number'])

        # Calcula a matriz de correlação completa (com ID)
corr_matrix = df_numeric.corr()

# Remove a coluna "ID" do heatmap, se existir
if "id" in df_numeric.columns:
    df_numeric = df_numeric.drop(columns=["id"])

# Recalcula a matriz de correlação sem ID para o heatmap
corr_matrix_heatmap = df_numeric.corr()

# Exibe um heatmap da matriz de correlação sem ID
st.markdown('<h1 style="color: #d10f45;">Heatmap da Matriz de Correlação</h1>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix_heatmap, annot=True, cmap="coolwarm", ax=ax, fmt=".2f")
st.pyplot(fig)
st.markdown('''
<ul>
     <li>A correlação entre o preço de revenda e o dias para revenda é alta, indicando que quanto menor mais rápida a venda.</li>
     <li>A correlação entre o preço de revenda e a diferença de preço é tem um valor negativo expressivo, poode representar que alguns tênis podem ser revendidos com margens altíssimas, enquanto outros têm preços mais estáveis, criando uma relação não linear.</li>
    <li>O preço de revenda sempre é diferente do preço de lançamento.</li>            
</ul>
''', unsafe_allow_html=True)

st.markdown(
    """
    <div class="footer">
        Desenvolvido com Streamlit por Jorge Booz.
    </div>
    """,
    unsafe_allow_html=True,
)