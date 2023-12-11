import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV de vendas por trimestre
orders_trimester = pd.read_csv('t_olist_orders_dataset.csv')
orders_trimester['order_purchase_timestamp_date'] = pd.to_datetime(orders_trimester['order_purchase_timestamp_date'])
orders_trimester['order_trimester'] = orders_trimester['order_purchase_timestamp_date'].dt.to_period('Q')
trimester_sales = orders_trimester.groupby('order_trimester').size()

# Carregar o arquivo CSV de vendas por mês
orders_month = pd.read_csv('t_olist_orders_dataset.csv')
orders_month['order_purchase_timestamp_date'] = pd.to_datetime(orders_month['order_purchase_timestamp_date'])
orders_month['order_month'] = orders_month['order_purchase_timestamp_date'].dt.to_period('M')
monthly_sales = orders_month.groupby('order_month').size()

# Carregar o arquivo CSV de vendas por hora
orders_hour = pd.read_csv('t_olist_orders_dataset.csv')
order_payments = pd.read_csv('t_olist_order_payments_dataset.csv')
merged_df = pd.merge(orders_hour, order_payments, on='order_id')
merged_df['order_purchase_timestamp_hour'] = pd.to_datetime(merged_df['order_purchase_timestamp_hour'])
merged_df['order_purchase_hour'] = merged_df['order_purchase_timestamp_hour'].dt.hour
hourly_sales = merged_df.groupby('order_purchase_hour').size()

# Configuração da página Streamlit
st.title('Sazonalidade de Vendas; Ano - 2017 e 1º Trimestre 2018')
st.write('Visualização da sazonalidade das vendas por trimestre, mês e hora.')

# Gráficos em duas colunas
col1, col2 = st.columns(2)

# Gráfico de sazonalidade por trimestre
with col1:
    st.write("### Sazonalidade de Vendas por Trimestre")
    fig_trimester, ax_trimester = plt.subplots(figsize=(8, 5))
    trimester_sales.plot(kind='line', marker='o', color='blue', ax=ax_trimester)
    plt.xlabel('Trimestre')
    plt.ylabel('Número de Vendas')
    plt.grid(True)
    st.pyplot(fig_trimester)

# Gráfico de sazonalidade por mês
with col2:
    st.write("### Sazonalidade de Vendas por Mês")
    fig_month, ax_month = plt.subplots(figsize=(8, 5))
    monthly_sales.plot(kind='line', marker='o', color='green', ax=ax_month)
    plt.xlabel('Mês')
    plt.ylabel('Número de Vendas')
    plt.grid(True)
    st.pyplot(fig_month)

# Gráfico de sazonalidade por hora
st.write("### Sazonalidade de Vendas por Hora")
fig_hour, ax_hour = plt.subplots(figsize=(16, 5))
hourly_sales.plot(kind='line', marker='o', color='orange', ax=ax_hour)
plt.xlabel('Hora do Dia')
plt.ylabel('Número de Vendas')
plt.grid(True)
st.pyplot(fig_hour)