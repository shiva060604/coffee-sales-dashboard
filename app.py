import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# load data
df=pd.read_excel("Afficionado Coffee Roasters.xlsx")

# Revenue calculation
df["Revenue"]=df["transaction_qty"]*df["unit_price"]

st.title("coffee sale dashboard")

#KPL
st.metric(label="Total Revenue", value=f"${df['Revenue'].sum():,.2f}")

#Revenue by category
st.subheader("Revenue by Category")

category_revenue=df.groupby("product_category")["Revenue"].sum()

fig, ax = plt.subplots(figsize=(6, 6))
category_revenue.plot(kind="pie", autopct="%1.1f%%", ax=ax)
ax.set_ylabel("")

st.pyplot(fig)

#Revenue by store
st.subheader("Revenue by Store")

store_revenue=df.groupby("store_location")["Revenue"].sum()

fig2, ax2 = plt.subplots(figsize=(8, 5))
store_revenue.plot(kind="bar", ax=ax2)

ax2.set_title("Revenue")
ax2.set_xlabel("Store")

st.pyplot(fig2)

#Top 10 products by revenue

st.subheader("Top 10 Products by Revenue")

top_products=df.groupby("product_detail")["Revenue"].sum().sort_values(ascending=False).head(10)

fig3, ax3 = plt.subplots(figsize=(10, 5))
top_products.plot(kind="bar", ax=ax3)

ax3.set_ylabel("Revenue($)")

st.pyplot(fig3)



