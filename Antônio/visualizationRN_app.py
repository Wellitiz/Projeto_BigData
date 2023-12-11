import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o DataFrame 'customers_compras_products.csv'
df = pd.read_csv('c_customers_compras_products.csv')

# Lista de estados da região Nordeste
northeastern_states = ['MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA']

# Configuração da página Streamlit
st.title('Sazonalidade de Vendas Nordeste do Segundo Semestre do Ano - 2017 As 10 principais categorias de produtos vendidos')
st.write('Visualização da sazonalidade das vendas por cada estado, em toda região Nordeste e as vendas no dia 20, 21, 22, 23, 24 e 25 de Dezembro de 2017.')

# As 10 principais categorias de produtos vendidas na região do Nordeste
st.write('### Vendas na região do Nordeste')
northeast_df = df[df['customer_state'].isin(northeastern_states)]
northeast_df['order_purchase_timestamp_date'] = pd.to_datetime(northeast_df['order_purchase_timestamp_date'])
last_semester_start = northeast_df[(northeast_df['order_purchase_timestamp_date'].dt.year == 2017) &
                                   (northeast_df['order_purchase_timestamp_date'].dt.month > 6)]
grouped = last_semester_start.groupby('product_category_name').size().reset_index(name='count')
top_categories = grouped.nlargest(10, 'count')
color_map_states = {'MA': '#800080', 'PI': '#5F9EA0', 'CE': '#000000', 'RN': '#D2691E', 'PB': '#483D8B',
                    'PE': '#20B2AA', 'AL': '#00FF00', 'SE': '#7FFFD4', 'BA': '#FF00FF'}
fig1 = px.bar(top_categories, x='count', y='product_category_name',
              title='Segundo semestre do ano - 2017',
              labels={'count': 'Contagem de Vendas', 'product_category_name': 'Categoria de Produto'},
              color='product_category_name', color_discrete_map=color_map_states)
fig1.update_layout(xaxis_title='Contagem de Vendas', yaxis_title='Categoria de Produto', height=600, width=800)
st.plotly_chart(fig1)

# As 10 principais categorias de produtos vendidas em cada estado do Nordeste
st.write('### Vendas em cada estado do Nordeste')
northeast_df = df[df['customer_state'].isin(northeastern_states)]
northeast_df['order_purchase_timestamp_date'] = pd.to_datetime(northeast_df['order_purchase_timestamp_date'])
last_year = northeast_df['order_purchase_timestamp_date'].dt.year.max()
last_semester_start = northeast_df[(northeast_df['order_purchase_timestamp_date'].dt.year == last_year) & 
                                   (northeast_df['order_purchase_timestamp_date'].dt.month > 6)]
grouped = last_semester_start.groupby(['customer_state', 'product_category_name']).size().reset_index(name='count')
top_categories = grouped.groupby('customer_state').apply(lambda x: x.nlargest(10, 'count')).reset_index(drop=True)
color_map_states = {'MA': '#800080', 'PI': '#5F9EA0', 'CE': '#FFBF00', 'RN': '#D2691E', 'PB': '#483D8B',
                    'PE': '#20B2AA', 'AL': '#00FF00', 'SE': '#7FFFD4', 'BA': '#FF00FF'}
top_categories['color'] = top_categories['customer_state'].map(color_map_states)
fig2 = px.bar(top_categories, x='count', y='product_category_name', color='customer_state',
              title='Segundo semestre do ano - 2017',
              labels={'count': 'Número de Vendas', 'product_category_name': 'Categoria do Produto'},
              color_discrete_map=color_map_states)
fig2.update_layout(xaxis_title='Número de Vendas', yaxis_title='Categoria do Produto', height=600, width=800)
st.plotly_chart(fig2)

# As 10 principais categorias de produtos vendidas na região do Nordeste
st.write('### Vendidas na região do Nordeste no dia...')
northeast_df = df[df['customer_state'].isin(northeastern_states)]
northeast_df['order_purchase_timestamp_date'] = pd.to_datetime(northeast_df['order_purchase_timestamp_date'])
specific_dates = ['2017-12-20', '2017-12-21', '2017-12-22', '2017-12-23', '2017-12-24', '2017-12-25']
filtered_dates = northeast_df[northeast_df['order_purchase_timestamp_date'].isin(specific_dates)]
grouped = filtered_dates.groupby('product_category_name').size().reset_index(name='count')
top_categories = grouped.nlargest(10, 'count')
color_map_states = {'MA': '#800080', 'PI': '#5F9EA0', 'CE': '#000000', 'RN': '#D2691E', 'PB': '#483D8B',
                    'PE': '#20B2AA', 'AL': '#00FF00', 'SE': '#7FFFD4', 'BA': '#FF00FF'}
fig3 = px.bar(top_categories, x='count', y='product_category_name',
              title='20, 21, 22, 23, 24 e 25 de dezembro de 2017',
              labels={'count': 'Contagem de Vendas', 'product_category_name': 'Categoria de Produto'},
              color='product_category_name', color_discrete_map=color_map_states)
fig3.update_layout(xaxis_title='Contagem de Vendas', yaxis_title='Categoria de Produto', height=600, width=1000)
st.plotly_chart(fig3)
