# US Sportswear Brands Financial Analysis (2015-2024)
## ACC102 Mini Assignment - Track 4: Interactive Data Tool

### 1. Problem & User
This project was created for the ACC102 mini assignment and is designed for instructors, classmates, and other readers who want a quick financial comparison of major US sportswear brands. It asks which firms outperform their peers from 2015 to 2024 and whether ROE is mainly driven by profitability, operating efficiency, or financial leverage.

### 2. Data
Source: WRDS comp.funda annual financial statement data, extracted in the notebook and exported to full_financial_analysis_2015_2024.xlsx.
Access date: The original WRDS pull date is not recorded in the notebook; this project file was reviewed on April 22, 2026.
Companies covered: Nike (NKE), Deckers (DECK), Columbia Sportswear (COLM), Dick's Sporting Goods (DKS), Wolverine World Wide (WWW), and Skechers (SKX).
Time period: 2015-2024.
Key fields: Revenue, COGS, Net_Income, Total_Equity, Total_Assets, Gross_Margin, Net_Margin, ROE, Asset_Turnover, Leverage, Revenue_Growth, and NetIncome_Growth.

### 3. Methods
Pulled annual company financial data from WRDS for six selected sportswear companies.
Cleaned the data by removing duplicates, sorting by ticker and year, and filtering out invalid values.
Renamed raw variables into readable financial fields and calculated core ratios including gross margin, net margin, ROE, asset turnover, and leverage.
Applied DuPont analysis using ROE = Net Margin x Asset Turnover x Leverage.
Calculated year-over-year revenue and net income growth.
Exported the final analysis table to Excel and built an interactive Streamlit dashboard with line charts, bar charts, and a correlation heatmap.

### 4. Key Findings
Nike (NKE) remains the largest company by revenue in 2024 at about USD 46.3 billion, but its 2024 revenue growth turned negative and its leverage stayed more conservative than some peers.
Deckers (DECK) is the strongest overall profitability leader in the latest year, with the highest 2024 gross margin, ROE, and revenue growth among the six companies.
Dick's Sporting Goods (DKS) shows strong operating efficiency and consistently high asset turnover, making it one of the most efficient firms in the sample.
Wolverine World Wide (WWW) carries the highest leverage, which can support ROE but also suggests greater financial risk and more volatile performance.
Skechers (SKX) stands out for relatively balanced ratios and strong long-run growth, while Columbia (COLM) shows steadier but less aggressive performance.

### 5. How to Run
1. Install dependencies: pip install -r requirements.txt
2. Make sure full_financial_analysis_2015_2024.xlsx is in the same folder as app.py.
3. Launch the Streamlit app: streamlit run app.py
   
### 6. Product Link / Demo
This project includes a local interactive demo built with Streamlit in app.py. No public deployment link is included in the current project files.https://github.com/a0910996727-tech/6-company/blob/main/README.md

### 7. Limitations & Next Steps
The analysis uses annual accounting data only, so it does not capture quarterly seasonality, short-term shocks, or intra-year strategy changes.
The source notebook does not record the original WRDS extraction date, which weakens the metadata quality of the dataset documentation.
The current dashboard relies on a local Excel file rather than an automated live data pipeline.
A useful next step would be adding more brands, quarterly data, and stronger company-level narrative interpretation for each chart.
