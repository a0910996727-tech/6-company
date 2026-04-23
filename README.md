# US Sportswear Brands Financial Analysis (2015-2024)
## ACC102 Mini Assignment - Track 4: Interactive Data Tool

### 1. Problem & User
This project was created for the ACC102 mini assignment and is designed for instructors, classmates, and other readers who want a quick financial comparison of major US sportswear brands. It asks which firms outperform their peers from 2015 to 2024 and whether ROE is mainly driven by profitability, operating efficiency, or financial leverage.

### 2. Data
Source: WRDS Compustat (comp.funda) annual financial statement data, retrieved directly through the Streamlit interface upon user login.
Access date: Data extraction occurs dynamically at runtime; the project structure and code were finalized on April 22, 2026.
Companies covered: Nike (NKE), Deckers (DECK), Columbia Sportswear (COLM), Dick's Sporting Goods (DKS), Wolverine World Wide (WWW), and Skechers (SKX).
Time period: 2015–2024 (10 full fiscal years).
Key fields: Revenue, COGS, Net Income, Total Equity, Total Assets, Gross Margin, Net Margin, ROE, Asset Turnover, Financial Leverage, Revenue Growth, and Net Income Growth.


### 3. Methods
Pulled annual corporate financial data directly from WRDS for six selected sportswear firms using valid user credentials.
Cleaned the dataset by removing duplicates, sorting observations by ticker and fiscal year, and excluding records with non-positive or missing values for core financial items.
Renamed raw accounting variables into interpretable financial metrics and computed key ratios including gross margin, net margin, ROE, asset turnover, and financial leverage.
Conducted DuPont analysis by decomposing ROE into the product of net margin, asset turnover, and financial leverage.
Calculated year-over-year growth rates for revenue and net income within each company.
Developed an interactive Streamlit dashboard with multi-perspective visualizations including line charts, bar charts, boxplots, scatter plots, and a correlation heatmap. The dashboard supports automated Excel export of cleaned and analyzed data for further review.

### 4. Key Findings
Nike (NKE) maintained the largest revenue scale in 2024 at approximately USD 46.3 billion, but experienced negative revenue growth in the latest year while maintaining a relatively conservative capital structure compared to some peers.
Deckers (DECK) led the group in overall profitability in 2024, achieving the highest gross margin, ROE, and revenue growth among the six companies.
Dick's Sporting Goods (DKS) demonstrated strong operational efficiency through consistently high asset turnover, positioning it as one of the most operationally efficient firms in the sample.
Wolverine World Wide (WWW) employed the highest financial leverage, which may boost ROE during favorable periods but also introduces higher financial risk and greater performance volatility.
Skechers (SKX) exhibited well-balanced financial ratios and solid long-term growth momentum, whereas Columbia (COLM) delivered stable but comparatively modest performance across most metrics.

### 5. How to Run
1. Install dependencies: pip install -r requirements.txt
2. Make sure full_financial_analysis_2015_2024.xlsx is in the same folder as app.py.
3. Launch the Streamlit app: streamlit run app.py
   
### 6. Limitations & Next Steps
The analysis relies solely on annual accounting data, therefore it does not reflect quarterly seasonality, short-term market shocks, or within-year strategic adjustments.
Data access requires manual user input of WRDS credentials at runtime, as the dashboard does not support automated or persistent authentication.
The current version pulls data only at execution time and does not store a fixed historical snapshot locally, which limits reproducibility under unchanged data environments.
Future improvements could include expanding the sample to include more sportswear and apparel brands, incorporating quarterly financial data, adding peer group benchmarking, and enhancing chart explanations with company-specific strategic context.
