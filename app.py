# ==========================================================
# ACC102 Mini Assignment - US Sportswear Brands Financial Analysis
# Streamlit Dashboard | WRDS Data | DuPont Analysis | Visualization | Excel Export
# 6 Companies: NKE, DECK, COLM, DKS, WWW, SKX | 2015-2024
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
from matplotlib.ticker import PercentFormatter

# ------------------------------
# Global Matplotlib Settings
# ------------------------------
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette(['#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd','#8c564b'])

# ------------------------------
# Streamlit Page Configuration
# ------------------------------
st.set_page_config(page_title="US Sportswear Financial Analysis", layout="wide")
st.title("🏃 US Sportswear Brands Financial Analysis (2015-2024)")
st.subheader("DuPont Analysis | YoY Growth | Correlation Heatmap | Statistical Analysis")

# ------------------------------
# Helper Function: Excel Export
# ------------------------------
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    return output.getvalue()

# ------------------------------
# WRDS Login Input Form
# ------------------------------
st.divider()
st.markdown("### 🔑 WRDS Login")
wrds_username = st.text_input("WRDS Username")
wrds_password = st.text_input("WRDS Password", type="password")

# Fixed Ticker List for Sportswear Brands
sport_brands = {
    'NKE': 'Nike, Inc.',
    'DECK': 'Deckers Brands',
    'COLM': 'Columbia Sportswear',
    'DKS': "Dick's Sporting Goods",
    'WWW': 'Wolverine World Wide',
    'SKX': 'Skechers U.S.A., Inc.'
}
tickers = list(sport_brands.keys())

# ------------------------------
# Run Analysis Button
# ------------------------------
st.divider()
if st.button("🚀 Run Full Financial Analysis"):
    # Validate WRDS Credentials
    if not wrds_username or not wrds_password:
        st.error("Please enter your WRDS username and password!")
    else:
        with st.spinner("Connecting to WRDS & Fetching Data..."):
            try:
                # 1. Connect to WRDS Database
                import wrds
                conn = wrds.Connection(wrds_username=wrds_username, wrds_password=wrds_password)

                # 2. Pull Financial Data from Compustat
                query = """
                SELECT tic, conm, fyear, sale, cogs, ni, seq, at
                FROM comp.funda
                WHERE tic IN ('NKE','DECK','COLM','DKS','WWW','SKX')
                  AND indfmt='INDL' AND datafmt='STD' AND consol='C'
                  AND fyear BETWEEN 2015 AND 2024
                ORDER BY tic, fyear;
                """
                df = conn.raw_sql(query)
                conn.close()

                # ------------------------------
                # 3. Data Cleaning & Quality Control
                # ------------------------------
                st.success("✅ Data Fetching Completed!")
                st.divider()
                st.subheader("📊 Data Quality Control Report")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Raw Data Rows", len(df))
                with col2:
                    st.metric("Missing Values", df.isnull().sum().sum())

                # Remove duplicates, filter invalid values
                df = df.drop_duplicates(subset=['tic','fyear']).sort_values(['tic','fyear'])
                df = df[(df['sale']>0) & (df['seq']>0) & (df['at']>0)].reset_index(drop=True)
                st.metric("Cleaned Data Rows", len(df))

                # Rename Columns for Readability
                df.rename(columns={
                    'tic':'Ticker','conm':'Company','fyear':'Year',
                    'sale':'Revenue','cogs':'COGS','ni':'Net_Income',
                    'seq':'Total_Equity','at':'Total_Assets'
                }, inplace=True)

                # ------------------------------
                # 4. Financial Metrics Calculation
                # ------------------------------
                df['Gross_Margin'] = (df['Revenue']-df['COGS'])/df['Revenue']*100
                df['Net_Margin'] = df['Net_Income']/df['Revenue']*100
                df['ROE'] = df['Net_Income']/df['Total_Equity']*100
                df['Asset_Turnover'] = df['Revenue'] / df['Total_Assets']
                df['Leverage'] = df['Total_Assets'] / df['Total_Equity']
                df['DuPont_Check'] = df['Net_Margin'] * df['Asset_Turnover'] * df['Leverage']

                # Calculate Year-over-Year Growth Rates
                df = df.sort_values(['Ticker','Year'])
                df['Revenue_Growth'] = df.groupby('Ticker')['Revenue'].pct_change() * 100
                df['NetIncome_Growth'] = df.groupby('Ticker')['Net_Income'].pct_change() * 100

                # Final Analysis DataFrame
                analysis_df = df[[
                    'Ticker','Company','Year','Revenue','Revenue_Growth',
                    'Net_Income','NetIncome_Growth','Gross_Margin','Net_Margin',
                    'ROE','DuPont_Check','Asset_Turnover','Leverage'
                ]].copy()

                # Display Full Financial Dataset
                st.divider()
                st.subheader("📈 Full Financial Analysis Data")
                st.dataframe(analysis_df, use_container_width=True)

                # ------------------------------
                # 5. Descriptive Statistics
                # ------------------------------
                st.divider()
                st.subheader("📊 Descriptive Statistics (2015-2024)")
                desc_stats = analysis_df.groupby('Ticker')[['Revenue','ROE','Asset_Turnover','Leverage']].agg([
                    'mean','median','std','min','max'
                ])
                st.dataframe(desc_stats, use_container_width=True)

                # ------------------------------
                # 6. 2024 Key Indicators
                # ------------------------------
                st.divider()
                st.subheader("🏢 2024 Company-Specific Key Indicators")
                df_2024 = analysis_df[analysis_df['Year']==2024].sort_values('Revenue', ascending=False)
                st.dataframe(df_2024, use_container_width=True)

                # ------------------------------
                # 7. Data Visualizations
                # ------------------------------
                st.divider()
                st.subheader("📊 Data Visualization")

                # Chart 1: Correlation Heatmap
                with st.expander("Correlation Heatmap", expanded=True):
                    fig, ax = plt.subplots(figsize=(12,8))
                    corr_matrix = analysis_df[['Gross_Margin','Net_Margin','ROE','Asset_Turnover','Leverage','Revenue_Growth']].corr()
                    sns.heatmap(corr_matrix, annot=True, cmap='RdBu_r', linewidths=0.5, fmt='.2f', ax=ax)
                    ax.set_title('Financial Indicators Correlation Matrix', fontsize=14)
                    st.pyplot(fig)

                # Chart 2: 10-Year Financial Trends
                with st.expander("Full Financial Trends (2015-2024)", expanded=True):
                    fig, axes = plt.subplots(3, 3, figsize=(27, 15))
                    fig.suptitle('Full Financial Trends (2015-2024)', fontsize=20)
                    indicators = [
                        ('Revenue', 'Revenue (Billion USD)', lambda x: x/1e9),
                        ('Revenue_Growth', 'Revenue Growth (%)', None),
                        ('Gross_Margin', 'Gross Margin (%)', None),
                        ('Net_Margin', 'Net Margin (%)', None),
                        ('ROE', 'ROE (%)', None),
                        ('Asset_Turnover', 'Asset Turnover', None),
                        ('Leverage', 'Financial Leverage', None),
                        ('NetIncome_Growth', 'Net Income Growth (%)', None),
                        ('DuPont_Check', 'DuPont ROE (%)', None)
                    ]
                    ax_flat = axes.flatten()
                    for i, (col, title, func) in enumerate(indicators):
                        ax = ax_flat[i]
                        for t in tickers:
                            sub = analysis_df[analysis_df['Ticker']==t]
                            y = func(sub[col]) if func else sub[col]
                            ax.plot(sub['Year'], y, marker='o', linewidth=2, label=sport_brands[t])
                        ax.set_title(title, fontsize=12)
                        ax.legend(fontsize=8)
                        ax.grid(True)
                        if '%' in title:
                            ax.yaxis.set_major_formatter(PercentFormatter())
                    plt.tight_layout()
                    st.pyplot(fig)

                # Chart 3: ROE Box Plot
                with st.expander("ROE Distribution Box Plot"):
                    fig, ax = plt.subplots(figsize=(14, 8))
                    sns.boxplot(x='Ticker', y='ROE', data=analysis_df, palette='Set2', linewidth=2, ax=ax)
                    sns.stripplot(x='Ticker', y='ROE', data=analysis_df, color='black', size=4, alpha=0.6, ax=ax)
                    ax.set_title('ROE Distribution by Company (2015-2024)', fontsize=16, weight='bold')
                    st.pyplot(fig)

                # Chart 4: Revenue vs ROE Scatter Plot
                with st.expander("Revenue vs ROE Scatter Plot"):
                    fig, ax = plt.subplots(figsize=(14, 8))
                    sns.scatterplot(data=analysis_df, x='Revenue', y='ROE', hue='Ticker', s=120, alpha=0.8, palette='tab10', ax=ax)
                    sns.regplot(data=analysis_df, x='Revenue', y='ROE', scatter=False, color='red', line_kws={'linewidth':2}, ax=ax)
                    ax.set_title('Revenue vs Return on Equity (ROE)', fontsize=16, weight='bold')
                    st.pyplot(fig)

                # Chart 5: 2024 Multi-Indicator Bar Chart
                with st.expander("2024 Key Indicators Comparison"):
                    fig, axes = plt.subplots(2, 2, figsize=(16,10))
                    fig.suptitle('2024 Key Financial Indicators Comparison', fontsize=16)
                    axes[0,0].bar(df_2024['Ticker'], df_2024['Revenue']/1e9)
                    axes[0,0].set_title('Total Revenue (Billion USD)')
                    axes[0,1].bar(df_2024['Ticker'], df_2024['ROE'])
                    axes[0,1].set_title('ROE (%)')
                    axes[1,0].bar(df_2024['Ticker'], df_2024['Asset_Turnover'])
                    axes[1,0].set_title('Asset Turnover')
                    axes[1,1].bar(df_2024['Ticker'], df_2024['Leverage'])
                    axes[1,1].set_title('Financial Leverage')
                    plt.tight_layout()
                    st.pyplot(fig)

                # Chart 6: 2024 Revenue Comparison
                with st.expander("2024 Revenue Comparison"):
                    fig, ax = plt.subplots(figsize=(12,6))
                    bars = ax.bar(df_2024['Ticker'], df_2024['Revenue']/1e9)
                    ax.set_title('2024 Total Revenue (Billion USD)', fontsize=14)
                    ax.bar_label(bars, fmt='%.2fB')
                    st.pyplot(fig)

                # Chart 7: 2024 Revenue Market Share Pie Chart
                with st.expander("2024 Revenue Market Share"):
                    fig, ax = plt.subplots(figsize=(10,10))
                    ax.pie(df_2024['Revenue'], labels=df_2024['Ticker'], autopct='%1.1f%%', startangle=90, textprops={'fontsize':12})
                    ax.set_title('2024 Revenue Market Share (%)', fontsize=14)
                    st.pyplot(fig)

                # ------------------------------
                # 8. Final Comprehensive Conclusion
                # ------------------------------
                st.divider()
                st.subheader("📌 Final Comprehensive Conclusion")
                conclusion = """
                1. NIKE (NKE) is the BEST in REVENUE: It outperforms DECK, COLM, DKS, WWW and SKX by a huge margin, ranking 1st in market scale.
                2. DECKERS (DECK) is the BEST in PROFITABILITY: It has higher ROE and gross margin than NKE, DKS and all other peers.
                3. DICK'S (DKS) is the BEST in OPERATIONAL EFFICIENCY: Its asset turnover is higher than every other company in the group.
                4. SKECHERS (SKX) is the MOST BALANCED: It performs better than WWW and COLM in growth, profitability and stability.
                5. COLUMBIA (COLM) is stable but weaker than NKE, DECK and SKX in most financial indicators.
                6. WOLVERINE (WWW) is the WEAKEST: It has the worst profitability stability and highest financial risk among all 6 companies.
                """
                st.text(conclusion)

                # ------------------------------
                # 9. Excel Export Buttons
                # ------------------------------
                st.divider()
                st.subheader("📥 Excel Export")
                col1, col2 = st.columns(2)
                with col1:
                    st.download_button(
                        label="Download Full Financial Data",
                        data=to_excel(analysis_df),
                        file_name="sportswear_financial_analysis_2015_2024.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                with col2:
                    st.download_button(
                        label="Download 2024 Summary Report",
                        data=to_excel(df_2024),
                        file_name="sportswear_2024_summary.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")