import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("Afficionado Coffee Roasters.xlsx")

print(df.head())
print(df.shape)

df["Revenue"]=df["transaction_qty"]*df["unit_price"]

print("Total Revenue: ", df["Revenue"].sum())

category_revenue=df.groupby("product_category")["Revenue"].sum()
print("Revenue by Category:")
print(category_revenue) 

#Store -wise revenue

store_revenue=df.groupby("store_location")["Revenue"].sum()
print("\nRevenue by Store:")
print(store_revenue)

top_products=df.groupby("product_detail")["Revenue"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Revenue:")
print(top_products)

top_products.plot(kind="bar", figsize=(12,6))

plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
    
    
category_revenue.plot(kind="pie", autopct="%1.1f%%", figsize=(8,8))

plt.title("Revenue Share by Category")
plt.ylabel("")

plt.show()    


store_revenue.plot(kind="bar", figsize=(8,5))
plt.title("store-wise Revenue")
plt.xlabel("Store")
plt.ylabel("Revenue($)")

plt.tight_layout()
plt.show()

#revenue share by category

category_revenue.plot(kind="pie", autopct="%1.1f%%", figsize=(8,8))

plt.title("Revenue Share by Category")
plt.ylabel("")
plt.show()

#store-wise revenue

store_revenue.plot(kind="bar", figsize=(8,5))

plt.title("Store-wise Revenue")
plt.xlabel("Store")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()

#top 10 products by revenue

top_qty=df.groupby("product_detail")["transaction_qty"].sum()

top_qty =top_qty.sort_values(ascending=False).head(10)

print(top_qty)

top_qty.plot(kind="bar", figsize=(10,5))

plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")

plt.tight_layout()
plt.show()