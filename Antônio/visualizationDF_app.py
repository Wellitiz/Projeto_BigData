import streamlit as st
import pandas as pd

# Carregar o DataFrame do arquivo 'customers_compras_products.csv'
merged_df = pd.read_csv('c_customers_compras_products.csv')

# Configuração da página Streamlit
st.title('Visualização do DataFrame')
st.write('c_customers_compras_products')

# Exibir a tabela no Streamlit com estilo e cores
st.write(merged_df.head(22).style.set_table_styles([
    {
        'selector': 'th',
        'props': [
            ('font-size', '14px'),
            ('text-align', 'center'),
            ('color', 'black'),
            ('background-color', '#f2f2f2'),
            ('border-style', 'solid'),
            ('border-width', '1px'),
            ('border-color', 'black')
        ]
    },
    {
        'selector': 'td',
        'props': [
            ('font-size', '14px'),
            ('text-align', 'center'),
            ('color', 'black'),
            ('border-style', 'solid'),
            ('border-width', '1px'),
            ('border-color', 'black')
        ]
    },
    {
        'selector': 'tr:nth-child(even)',
        'props': [('background-color', '#f7f7f7')]
    },
    {
        'selector': 'tr:nth-child(odd)',
        'props': [('background-color', '#ffffff')]
    }
]))