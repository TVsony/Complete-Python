import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv(r"data\food_data.csv", parse_dates=['Date'])

st.set_page_config(page_title="Food Hotel Dashboard", layout="wide")
st.title("🍽️ Food Hotel Performance Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")
date_range = st.sidebar.date_input("Select Date Range", [df['Date'].min(), df['Date'].max()])
order_type = st.sidebar.multiselect("Order Type", options=df['Order_Type'].unique(), default=df['Order_Type'].unique())

# Filtered Data
mask = (
    (df['Date'] >= pd.to_datetime(date_range[0])) &
    (df['Date'] <= pd.to_datetime(date_range[1])) &
    (df['Order_Type'].isin(order_type))
)
df_filtered = df[mask]

# KPI Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"₹{df_filtered['Revenue'].sum():,.0f}")
col2.metric("Total Orders", int(df_filtered['Quantity'].sum()))
col3.metric("Avg. Rating", f"{df_filtered['Customer_Rating'].mean():.2f}")
col4.metric("Food Wasted (g)", f"{df_filtered['Wastage_g'].sum():,.0f}")

st.markdown("---")

# Sales by Dish
st.subheader("🍲 Top-Selling Dishes")
dish_sales = df_filtered.groupby('Dish')['Quantity'].sum().sort_values(ascending=False).head(10)
fig1 = px.bar(dish_sales, x=dish_sales.values, y=dish_sales.index, orientation='h', title="Top 10 Dishes by Quantity")
st.plotly_chart(fig1, use_container_width=True)

# Revenue Trend
st.subheader("📈 Daily Revenue Trend")
daily_rev = df_filtered.groupby('Date')['Revenue'].sum().reset_index()
fig2 = px.line(daily_rev, x='Date', y='Revenue', markers=True)
st.plotly_chart(fig2, use_container_width=True)

# Category Pie Chart
st.subheader("📊 Revenue by Category")
cat_rev = df_filtered.groupby('Category')['Revenue'].sum().reset_index()
fig3 = px.pie(cat_rev, values='Revenue', names='Category', hole=0.4)
st.plotly_chart(fig3, use_container_width=True)

# Sentiment Word Cloud (placeholder text summary)
st.subheader("💬 Feedback Summary")
st.write("Most common feedback:")
st.write(df_filtered['Feedback'].value_counts().head(5))
