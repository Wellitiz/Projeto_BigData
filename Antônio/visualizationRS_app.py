import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os arquivos CSV para os DataFrames correspondentes
customers = pd.read_csv('csv_olist_customers_dataset.csv')
orders = pd.read_csv('t_olist_orders_dataset.csv')

# Unir os DataFrames usando a coluna 'customer_id' como chave de junção
merged_data = pd.merge(orders, customers, on='customer_id')

# Filtrar para incluir apenas clientes da região Sudeste (SP, RJ, MG, ES)
southeast_customers = merged_data[merged_data['customer_state'].isin(['SP', 'RJ', 'MG', 'ES'])]

# Converter a coluna 'order_purchase_timestamp' para o tipo de data
southeast_customers['order_purchase_timestamp_date'] = pd.to_datetime(southeast_customers['order_purchase_timestamp_date'])

# Extrair o trimestre a partir da coluna 'order_purchase_timestamp'
southeast_customers['order_trimester'] = southeast_customers['order_purchase_timestamp_date'].dt.to_period('Q')

# Agrupar as vendas por trimestre e calcular a média
trimester_sales = southeast_customers.groupby('order_trimester').size()

# Configuração da página Streamlit
st.title('Sazonalidade de Vendas por Trimestre na Região Sudeste')
st.write('Visualização da sazonalidade das vendas por trimestre')

# Criar o gráfico de barras usando Matplotlib
fig, ax = plt.subplots(figsize=(12, 6))  # Definindo o tamanho do gráfico
trimester_sales.plot(kind='bar', ax=ax)
plt.xlabel('Trimestre')
plt.ylabel('Número de Vendas')
plt.title('Vendas por Trimestre na Região Sudeste')

# Exibir o gráfico no Streamlit
st.pyplot(fig)
