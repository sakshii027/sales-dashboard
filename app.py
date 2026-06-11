import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

# 🔥 CUSTOM CSS (UI design)
st.markdown("""
<style>
.metric-card {
    background: linear-gradient(135deg, #667eea, #764ba2);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 4px 4px 15px rgba(0,0,0,0.3);
    text-align: center;
    color: white;   /* 🔥 visible text */
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Advanced Sales Dashboard 🚀")

# Load data
df = pd.read_csv("sales.csv")
df.columns = df.columns.str.strip()

df["Order Date"] = pd.to_datetime(df["Order Date"], errors='coerce')
df["Month"] = df["Order Date"].dt.month

# Sidebar
st.sidebar.header("🎛 Filter")
category = st.sidebar.selectbox("Select Category", df["Category"].unique())
filtered_df = df[df["Category"] == category]

# 🔥 KPI CARDS
col1, col2, col3 = st.columns(3)

col1.markdown(f"""
<div class="metric-card">
<h3>Total Sales</h3>
<h2>{filtered_df["Sales"].sum()}</h2>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div class="metric-card">
<h3>Total Orders</h3>
<h2>{len(filtered_df)}</h2>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div class="metric-card">
<h3>Avg Sales</h3>
<h2>{round(filtered_df["Sales"].mean(),2)}</h2>
</div>
""", unsafe_allow_html=True)

# Charts layout
col4, col5 = st.columns(2)

# Line chart
monthly_sales = filtered_df.groupby("Month")["Sales"].sum().reset_index()
fig1 = px.line(monthly_sales, x="Month", y="Sales", markers=True, title="📈 Monthly Sales Trend")
col4.plotly_chart(fig1, use_container_width=True)

# Pie chart
fig2 = px.pie(filtered_df, names="Category", values="Sales", title="🥧 Sales Distribution", hole=0.4)
col5.plotly_chart(fig2, use_container_width=True)

# Bar chart
fig3 = px.bar(filtered_df, x="Category", y="Sales", color="Category", title="📊 Category Sales")
st.plotly_chart(fig3, use_container_width=True)

# Table
st.subheader("📋 Data Table")
st.dataframe(filtered_df)
