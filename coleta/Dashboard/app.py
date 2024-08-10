import streamlit as st
import pandas as pd
import sqlite3

# Conectar ao banco de dados SQLite (ou criar um novo)
conn = sqlite3.connect('C:\\Users\\lurch\\Documents\\projetowebscrapping\\coleta\\data\\quotes.db')


#query
df = pd.read_sql_query("SELECT * FROM mercadolivre_items" , conn)

#fechar conexão
conn.close()


#titulo do grafico
st.title('Pesquisa de mercado - Tenis esportivos do mercado livre')
st.subheader('Kpis principais do sistema')
col1,col2,col3 = st.columns(3)

#kpi1 n total de itens

total_items = df.shape[0]
col1.metric(label="Numero total de Items" , value= total_items)

#kpi2 numero de marcas unicas

unique_brands = df['brand'].nunique()  #distinct
col2.metric(label="Numero de Marcas Unicas" , value= unique_brands)


#kpi3 preco medio (reais)

avg_new_price = df['new_price'].mean()  #preço medio
col3.metric(label= "Preço Medio Novo" , value= f"{avg_new_price : .2f}")


# Quais marcas são mais encontradas até a 10ª página
st.subheader('Marcas mais encontradas até a 10ª página')
col1, col2 = st.columns([4, 2])
top_10_pages_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands)


# Qual o preço médio por marca
st.subheader('Preço médio por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_prices = df[df['new_price'] > 0]
average_price_by_brand = df_non_zero_prices.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

# Qual a satisfação por marca
st.subheader('Satisfação por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)


