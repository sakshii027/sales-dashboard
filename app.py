import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Sales Analytics Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("sales.csv")

df = load_data()

# Title
st.title("📊 Sales Analytics Dashboard")
st.markdown("Real-time insights into sales performance and trends")

# Sidebar filters
st.sidebar.header("Filters")

if "Region" in df.columns:
    region = st.sidebar.selectbox("Select Region", df["Region"].unique())
    df = df[df["Region"] == region]

# Key Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"{df['Sales'].sum():,.0f}")
col2.metric("Total Orders", len(df))
col3.metric("Average Sales", f"{df['Sales'].mean():,.0f}")

st.markdown("---")

# Sales by Category
if "Category" in df.columns:
    fig1 = px.bar(df, x="Category", y="Sales", color="Category",
                  title="Sales by Category")
    st.plotly_chart(fig1, use_container_width=True)

# Sales Trend (if Date exists)
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    trend = df.groupby("Date")["Sales"].sum().reset_index()

    fig2 = px.line(trend, x="Date", y="Sales",
                   title="Sales Trend Over Time")
    st.plotly_chart(fig2, use_container_width=True)

# Data table
st.subheader("📄 Raw Data")
st.dataframe(df)
