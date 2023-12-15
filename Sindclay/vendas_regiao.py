import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

df_orders = pd.read_csv("https://raw.githubusercontent.com/Wellitiz/Projeto_BigData/main/CSV%20Tratados/t_olist_orders_dataset.csv")
df_customers = pd.read_csv("https://raw.githubusercontent.com/Wellitiz/Projeto_BigData/main/CSV%20Tratados/csv_olist_customers_dataset.csv")

order_customer = pd.merge(df_orders, df_customers, how="inner", on="customer_id")

estados = order_customer['customer_state'].value_counts()

# Dicionário que mapeia cada estado para sua respectiva região
estado_regiao = {
    'AC': 'Norte', 'AL': 'Nordeste', 'AP': 'Norte', 'AM': 'Norte',
    'BA': 'Nordeste', 'CE': 'Nordeste', 'DF': 'Centro-Oeste', 'ES': 'Sudeste',
    'GO': 'Centro-Oeste', 'MA': 'Nordeste', 'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste',
    'MG': 'Sudeste', 'PA': 'Norte', 'PB': 'Nordeste', 'PR': 'Sul', 'PE': 'Nordeste',
    'PI': 'Nordeste', 'RJ': 'Sudeste', 'RN': 'Nordeste', 'RS': 'Sul', 'RO': 'Norte',
    'RR': 'Norte', 'SC': 'Sul', 'SP': 'Sudeste', 'SE': 'Nordeste', 'TO': 'Norte'
}

# Adiciona uma nova coluna 'regiao' ao DataFrame com base no mapeamento
order_customer['regiao'] = order_customer['customer_state'].map(estado_regiao)

vendas_regiao = order_customer['regiao'].value_counts()

st.set_page_config(page_title="Vendas por Região")

with st.container():    
    st.header("Análise das Vendas por estado e por região do Brasil")
    st.write("---")

    st.subheader("Vendas por estado brasileiro")
    st.write("O sucesso de uma operação comercial muitas vezes está intrinsecamente ligado à compreensão detalhada do desempenho de vendas em diferentes regiões geográficas. No contexto do mercado brasileiro, a análise da distribuição das vendas por estado é essencial para identificar padrões, oportunidades e desafios específicos em cada localidade.")
    
    st.write("A visualização a seguir apresenta de forma clara e concisa a distribuição de vendas por estado brasileiro. Cada linha do gráfico representa um estado específico, oferecendo uma representação visual dinâmica da contribuição relativa de cada região para o total de vendas. Analisar esses dados de maneira visual facilita a identificação de padrões sazonais, discrepâncias significativas e áreas de oportunidade que podem orientar estratégias futuras.")

    st.line_chart(estados)

    st.write("---")

    st.subheader("Vendas por região do Brasil")

    st.write("Os dados revelam que a Região Sudeste lidera significativamente em termos de número de vendas, consolidando-se como a força motriz do mercado nacional. Em um sólido segundo lugar, a Região Sul também desempenha um papel crucial, seguida pelo Nordeste, Centro-Oeste e, por fim, a Região Norte.")

    st.bar_chart(vendas_regiao)

    st.write("Esta análise proporciona uma visão estratégica das oportunidades e desafios específicos em cada região, permitindo ajustes precisos nas abordagens de marketing e nas operações logísticas. Para uma compreensão mais aprofundada dessas dinâmicas, o gráfico abaixo oferece uma representação visual clara da distribuição proporcional de vendas em todo o território nacional.")

    st.write("Este panorama regional não apenas evidencia as disparidades geográficas, mas também serve como um guia fundamental para a formulação de estratégias comerciais mais direcionadas e eficazes, alinhadas às nuances peculiares de cada localidade.")