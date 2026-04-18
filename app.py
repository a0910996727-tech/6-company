
# ACC102 Track4 - US Sportswear Brands Financial Analysis (Streamlit Interactive Tool)
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter

# 页面配置
st.set_page_config(
    page_title="US Sportswear Financial Analysis",
    page_icon="📊",
    layout="wide"
)

# 全局样式
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette(['#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd','#8c564b'])
st.title("📊 US Sportswear Brands Financial Analysis (2015-2024)")
st.subheader("ACC102 Track4 | Interactive Data Tool | DuPont Analysis + YoY Growth")

# ----------------------
# 1. 数据加载（本地Excel，无WRDS依赖）
# ----------------------
@st.cache_data
def load_data():
    df = pd.read_excel("full_financial_analysis_2015_2024.xlsx")
    return df

df = load_data()
company_dict = {
    'NKE': 'Nike, Inc.',
    'DECK': 'Deckers Brands',
    'COLM': 'Columbia Sportswear',
    'DKS': "Dick's Sporting Goods",
    'WWW': 'Wolverine World Wide',
    'SKX': 'Skechers U.S.A., Inc.'
}

# ----------------------
# 2. 侧边栏交互控件
# ----------------------
st.sidebar.header("⚙️ Control Panel")
selected_companies = st.sidebar.multiselect(
    "Select Companies",
    options=list(company_dict.keys()),
    default=['NKE','DECK','SKX']
)
selected_indicator = st.sidebar.selectbox(
    "Select Financial Indicator",
    options=['Revenue','ROE','Gross_Margin','Net_Margin','Asset_Turnover','Leverage','Revenue_Growth']
)
year_range = st.sidebar.slider("Year Range", 2015, 2024, (2015, 2024))

# 数据筛选
filtered_df = df[
    (df['Ticker'].isin(selected_companies)) &
    (df['Year'] >= year_range[0]) &
    (df['Year'] <= year_range[1])
]

# ----------------------
# 3. 数据概览面板
# ----------------------
st.divider()
st.header("1. Data Overview")
st.dataframe(filtered_df, use_container_width=True)

# ----------------------
# 4. 趋势分析（交互式）
# ----------------------
st.divider()
st.header(f"2. Trend Analysis: {selected_indicator}")
fig, ax = plt.subplots(figsize=(12, 5))
for ticker in selected_companies:
    data = filtered_df[filtered_df['Ticker'] == ticker]
    ax.plot(data['Year'], data[selected_indicator], marker='o', linewidth=2, label=company_dict[ticker])

ax.set_title(f"{selected_indicator} Trend ({year_range[0]}-{year_range[1]})", fontsize=14)
ax.legend()
ax.grid(True)
if '%' in selected_indicator or selected_indicator in ['Gross_Margin','Net_Margin','ROE','Revenue_Growth']:
    ax.yaxis.set_major_formatter(PercentFormatter())
st.pyplot(fig)

# ----------------------
# 5. 2024 年对比柱状图
# ----------------------
st.divider()
st.header("3. 2024 Key Indicators Comparison")
df_2024 = df[df['Year'] == 2024].copy()
fig2, axes = plt.subplots(2, 2, figsize=(16, 10))

# 营收
axes[0,0].bar(df_2024['Ticker'], df_2024['Revenue']/1e9, color='#1f77b4')
axes[0,0].set_title('Total Revenue (Billion USD)')
# ROE
axes[0,1].bar(df_2024['Ticker'], df_2024['ROE'], color='#ff7f0e')
axes[0,1].set_title('ROE (%)')
# 资产周转率
axes[1,0].bar(df_2024['Ticker'], df_2024['Asset_Turnover'], color='#2ca02c')
axes[1,0].set_title('Asset Turnover')
# 财务杠杆
axes[1,1].bar(df_2024['Ticker'], df_2024['Leverage'], color='#d62728')
axes[1,1].set_title('Financial Leverage')

plt.tight_layout()
st.pyplot(fig2)

# ----------------------
# 6. 杜邦分析核心结论
# ----------------------
st.divider()
st.header("4. DuPont Analysis Key Insights")
st.markdown("""
1. **Nike (NKE)**: Largest revenue scale with conservative leverage
2. **Deckers (DECK)**: Highest gross margin & stable profitability
3. **Dick's (DKS)**: Best operational efficiency (highest asset turnover)
4. **Skechers (SKX)**: Consistent growth & balanced financial ratios
5. **DuPont Formula**: ROE = Net Margin × Asset Turnover × Leverage
""")

# ----------------------
# 7. 相关性热力图
# ----------------------
st.divider()
st.header("5. Financial Indicators Correlation Heatmap")
corr_df = df[['Gross_Margin','Net_Margin','ROE','Asset_Turnover','Leverage','Revenue_Growth']].corr()
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.heatmap(corr_df, annot=True, cmap='RdBu_r', linewidths=0.5, fmt='.2f', ax=ax3)
st.pyplot(fig3)

st.success("✅ Tool Running Successfully | ACC102 Track4 Completed")
