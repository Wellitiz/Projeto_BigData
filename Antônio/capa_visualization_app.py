import streamlit as st

texto = """
# <div style='text-align: center; font-size: 44px;'>Sazonalidade</div>

<p style='text-align: justify; font-size: 22px; line-height: 1.5em;'>
A análise de sazonalidade refere-se à identificação, compreensão e avaliação de padrões recorrentes e previsíveis em dados ao longo de períodos específicos de tempo, geralmente em ciclos, como diário, semanal, mensal ou sazonal. Ela permite compreender variações regulares ou previsíveis em um conjunto de dados ao longo do tempo, identificando padrões que se repetem em intervalos regulares.
</p>

<p style='text-align: justify; font-size: 22px; line-height: 1.5em;'>
Em resumo, a análise de sazonalidade é essencial para entender e antecipar variações temporais nos dados, fornecendo informações valiosas para planejamento estratégico, previsões precisas e tomada de decisões informadas ao longo do tempo.
</p>
"""

st.markdown(texto, unsafe_allow_html=True)
