import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import bernoulli, poisson

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

# Criando variável binária: 1 se o sneaker foi vendido acima do preço de varejo, 0 caso contrário
df["AboveRetail"] = (df["Sale Price"] > df["Retail Price"]).astype(int)

# Calculando a probabilidade de sucesso (venda acima do preço de varejo)
p_success = df["AboveRetail"].mean()

st.markdown("## Análise de Bernoulli para Vendas de Sneakers")
st.write("Probabilidade de um sneaker ser vendido acima do preço de varejo:")
st.write(f"p = {p_success:.2f}")

# Gráfico interativo da distribuição de Bernoulli
fig_bernoulli = go.Figure()
fig_bernoulli.add_trace(go.Bar(
    x=['Venda ≤ Retail', 'Venda > Retail'], 
    y=[1 - p_success, p_success],
    marker=dict(color=['#d10f45', '#0f1820']),
    text=[f"{(1 - p_success) * 100:.2f}%", f"{p_success * 100:.2f}%"],
    textposition='auto'
))
fig_bernoulli.update_layout(
    title="Distribuição de Bernoulli - Vendas acima do preço de varejo",
    xaxis_title="Resultado",
    yaxis_title="Probabilidade"
)
st.plotly_chart(fig_bernoulli)

# Simulação de 1000 eventos usando a distribuição de Bernoulli
n_sim = 1000
simulated = bernoulli.rvs(p_success, size=n_sim)
st.write("Simulação de 1000 vendas (0: não acima do retail, 1: acima do retail):")
st.write(np.bincount(simulated))

st.markdown(f"""<h3 style='color: #d10f45;'>Qual a probabilidade de se ter lucro ao revender um dos modelos?</h3>
            <p>De acordo com a distribuição de Bernoulli é muito provável que um tênis seja revendido por um preço superior ao de seu lançamento. 
            A cada 1000 vendas, apenas {np.bincount(simulated)[0]} foram revendidos por um valor menor que o de lançamento.</p>""", unsafe_allow_html=True)

st.markdown(f"""
            <p>A distribuição de Bernoulli foi escolhida para analisar a probabilidade de um tênis ser vendido por um preço superior ao de varejo, pois trata-se de um evento binário:"Sucesso" (1) → quando o tênis é vendido acima do preço de varejo."Fracasso" (0) → quando o tênis é vendido pelo mesmo preço ou abaixo do varejo. Como cada venda é um evento independente e só pode ter dois resultados possíveis, a distribuição de Bernoulli é a melhor escolha para modelar esse comportamento. Além disso, ao simular 1000 vendas com base na proporção de tênis revendidos acima do preço de varejo, conseguimos entender melhor a tendência do mercado de revenda.
""", unsafe_allow_html=True)


# Seleção de marca
brands = df["Brand"].unique()
selected_brand = st.selectbox("Selecione a marca para análise:", brands)

# Calculando a proporção de vendas para a marca selecionada
p_brand = (df["Brand"] == selected_brand).mean()

# Parâmetro lambda para a distribuição de Poisson
lambda_val = 20 * p_brand

st.markdown(f"""
<h3 style="color: #d10f45;">Análise de Vendas - Distribuição de Poisson para {selected_brand}</h3>
<p>Considerando 20 vendas, o parâmetro <em>λ</em> é calculado como 20 * (proporção de vendas da marca).<br>
Proporção de vendas da marca {selected_brand}: <strong>{p_brand:.2%}</strong><br>
λ (para 20 vendas): <strong>{lambda_val:.2f}</strong></p>
""", unsafe_allow_html=True)

# Cálculo da distribuição de Poisson
k_values = np.arange(0, 21)
poisson_probs = poisson.pmf(k_values, lambda_val)

# Criando gráfico interativo para distribuição de Poisson
fig_poisson = go.Figure()
fig_poisson.add_trace(go.Bar(
    x=k_values, 
    y=poisson_probs,
    marker=dict(color="#d10f45"),
    text=[f"{p*100:.2f}%" for p in poisson_probs],
    textposition='auto'
))
fig_poisson.update_layout(
    title=f"Distribuição de Poisson para {selected_brand} (λ = {lambda_val:.2f})",
    xaxis_title="Número de Vendas da Marca",
    yaxis_title="Probabilidade"
)
st.plotly_chart(fig_poisson)

st.markdown(f"""<h3 style='color: #d10f45;'>A cada 20 tênis quantos serão da marca Off-White e quantos Adidas?</h3>
            <p>A cada 20 tênis, cerca de 14 serão Yeezy e 6 serão Off-White.
            </p>
            <p>A distribuição de Poisson foi aplicada para modelar o número esperado de vendas de uma determinada marca dentro de um grupo de 20 vendas. Isso faz sentido porque:
            Queremos prever a frequência de um evento raro (vendas de uma marca específica) dentro de um número fixo de tentativas.
            Assumimos que as vendas acontecem de maneira independente e com uma taxa média constante para cada marca, o que é um dos pressupostos da distribuição de Poisson.
            O parâmetro λ (lambda), calculado como a taxa de vendas da marca multiplicada por 20, reflete a expectativa de quantos pares dessa marca serão vendidos no conjunto analisado.</p
            """, unsafe_allow_html=True)

st.markdown(
    """
    <div class="footer">
        Desenvolvido com Streamlit por Jorge Booz.
    </div>
    """,
    unsafe_allow_html=True,
)
