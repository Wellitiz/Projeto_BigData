import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o DataFrame 'customers_compras_products.csv'
df = pd.read_csv('c_customers_compras_products.csv')

# Converter a coluna 'order_purchase_timestamp_date' para o tipo datetime
df['order_purchase_timestamp_date'] = pd.to_datetime(df['order_purchase_timestamp_date'])

# Filtrar os dados para o último semestre do último ano
last_year = df['order_purchase_timestamp_date'].dt.year.max()
last_semester_start = df[(df['order_purchase_timestamp_date'].dt.year == last_year) & 
                         (df['order_purchase_timestamp_date'].dt.month > 6)]

# Agrupar por região ('customer_state') e 'product_category_name', contando as vendas
grouped = last_semester_start.groupby(['customer_state', 'product_category_name']).size().reset_index(name='count')

# Encontrar as cem principais categorias de produtos vendidos em cada região
top_categories = grouped.groupby('customer_state').apply(lambda x: x.nlargest(10, 'count')).reset_index(drop=True)

# Mapeamento de cores para cada estado
color_map_states = {
    'AC': '#FF0000', 'AL': '#00FF00', 'AP': '#0000FF', 'AM': '#FFFF00', 'BA': '#FF00FF', 'CE': '#000000',
    'DF': '#800000', 'ES': '#808000', 'GO': '#008080', 'MA': '#800080', 'MT': '#FF8500', 'MS': '#FF69B4',
    'MG': '#B8860B', 'PA': '#9ACD32', 'PB': '#483D8B', 'PR': '#2E8B57', 'PE': '#20B2AA', 'PI': '#5F9EA0',
    'RJ': '#9FFF80', 'RN': '#D2691E', 'RS': '#6495ED', 'RO': '#DC143C', 'RR': '#00FFFF', 'SC': '#1E90FF',
    'SP': '#8A2BE2', 'SE': '#7FFFD4', 'TO': '#FFD700'
}

# Atribuir cores aos estados
top_categories['color'] = top_categories['customer_state'].map(color_map_states)

# Configuração da página Streamlit
st.title('As 10 principais categorias de produtos vendidos em cada estado do Brasil')
st.write('Último semestre do ano - 2017')

# Criar o gráfico de barras com cores específicas para cada estado
fig = px.bar(top_categories, x='count', y='product_category_name', color='customer_state', 
             title='As 10 principais categorias de produtos vendidas em cada estado do Brasil último semestre do ano - 2017',
             labels={'count': 'Número de Vendas', 'product_category_name': 'Categoria do Produto'},
             color_discrete_map=color_map_states)  # Usar o mapeamento de cores

fig.update_layout(xaxis_title='Número de Vendas', yaxis_title='Categoria do Produto', height=700, width=900)

# Mostrar o gráfico no Streamlit
st.plotly_chart(fig)
