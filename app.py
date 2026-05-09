import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Configuração da página
st.set_page_config(
    page_title="Passos Mágicos - Risco de Defasagem",
    page_icon="🎓",
    layout="centered"
)

# Carregando o modelo
@st.cache_resource
def load_model():
    # Carrega o modelo salvo na Fase 3
    return joblib.load('models/modelo_risco_rf.pkl')

modelo = load_model()

# Título e descrição
st.title("🎓 Predição de Risco de Defasagem Escolar")
st.markdown("""
Esta aplicação utiliza um modelo de Machine Learning (Random Forest) para prever o risco de um aluno entrar em defasagem escolar (Adequação ao Nível Crítico).
Preencha os dados do aluno no menu lateral para visualizar a probabilidade de risco e tomar medidas pedagógicas preventivas.
""")

st.divider()

# Menu lateral para input de dados
st.sidebar.header("📊 Dados do Aluno")
st.sidebar.markdown("Insira os indicadores de desempenho e sociais:")

fase = st.sidebar.selectbox("Fase de Aprendizado (FASE)", options=[0, 1, 2, 3, 4, 5, 6, 7, 8], index=3)
idade = st.sidebar.number_input("Idade do Aluno", min_value=7, max_value=25, value=14, step=1)
iaa = st.sidebar.slider("Autoavaliação (IAA)", min_value=0.0, max_value=10.0, value=7.0, step=0.1)
ieg = st.sidebar.slider("Engajamento (IEG)", min_value=0.0, max_value=10.0, value=7.0, step=0.1)
ips = st.sidebar.slider("Aspectos Psicossociais (IPS)", min_value=0.0, max_value=10.0, value=7.0, step=0.1)
qtd_avaliacoes = st.sidebar.number_input("Quantidade de Avaliações", min_value=1, max_value=10, value=4, step=1)
defasagem = st.sidebar.number_input("Defasagem (Distorção Idade-Série)", min_value=-5, max_value=5, value=0, step=1)

# Organizando os dados de input no mesmo formato que o modelo espera
input_data = pd.DataFrame({
    'FASE': [fase],
    'IDADE_2022': [idade],
    'IAA_2022': [iaa],
    'IEG_2022': [ieg],
    'IPS_2022': [ips],
    'QTD_AVALIACOES_2022': [qtd_avaliacoes],
    'DEFASAGEM_2022': [defasagem]
})

# Botão de predição
if st.button("🔮 Prever Risco de Defasagem", type="primary"):
    
    # Realiza a predição e probabilidade
    predicao = modelo.predict(input_data)[0]
    probabilidade = modelo.predict_proba(input_data)[0]
    
    st.subheader("Resultado da Previsão")
    
    # Risco Alto = classe 1
    if predicao == 1:
        st.error(f"⚠️ **ALTO RISCO DE DEFASAGEM**")
        st.markdown(f"**Probabilidade de Risco:** {probabilidade[1]*100:.1f}%")
        st.markdown("Recomenda-se acompanhamento pedagógico e psicossocial de perto para este aluno, focando no aumento do engajamento (IEG).")
    else:
        st.success(f"✅ **BAIXO RISCO DE DEFASAGEM**")
        st.markdown(f"**Probabilidade de Risco:** {probabilidade[1]*100:.1f}%")
        st.markdown("O aluno apresenta bons indicadores para seguir na sua evolução padrão.")
    
    # Exibir resumo dos dados
    st.write("---")
    st.write("Resumo dos indicadores fornecidos:")
    st.dataframe(input_data)
