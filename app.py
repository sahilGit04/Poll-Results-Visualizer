import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.analysis import *

st.set_page_config(page_title="Poll Visualizer", layout="wide")

st.title("📊 Poll Results Visualizer")



df = load_data("data/poll_data.csv")
df = clean_data(df)

# Sidebar filters (PRO FEATURE)
st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Select Region",
    df['region'].unique(),
    default=df['region'].unique()
)

age = st.sidebar.multiselect(
    "Select Age Group",
    df['age_group'].unique(),
    default=df['age_group'].unique()
)

filtered_df = df[
    (df['region'].isin(region)) &
    (df['age_group'].isin(age))
]

st.subheader("Key Metrics")

col1, col2 = st.columns(2)

col1.metric("Total Responses", len(filtered_df))
col2.metric("Unique Options", filtered_df['choice'].nunique())

# Dataset preview
st.subheader("Dataset")
st.dataframe(filtered_df)

# Vote %
st.subheader("Vote Share (%)")
vote = vote_percentage(filtered_df)
st.bar_chart(vote)

# Pie Chart
fig, ax = plt.subplots()
ax.pie(vote, labels=vote.index, autopct='%1.1f%%')
st.pyplot(fig)

from src.analysis import trend_analysis

st.subheader("Trend Over Time")

trend = trend_analysis(filtered_df)
st.line_chart(trend)

# Region Heatmap (ADVANCED FEATURE)
st.subheader("Region-wise Analysis")
heatmap_data = region_analysis(filtered_df)

fig2, ax2 = plt.subplots()
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='coolwarm', ax=ax2)
st.pyplot(fig2)

# Insight generation (PRO FEATURE)
st.subheader("Insights")

top_choice = vote.idxmax()
st.success(f"Top choice is {top_choice} with {vote.max():.2f}% votes")

st.subheader("Download Results")

csv = filtered_df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download Data as CSV",
    data=csv,
    file_name='filtered_poll_data.csv',
    mime='text/csv'
)