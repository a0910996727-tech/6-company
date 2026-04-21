# US Sportswear Brands Financial Analysis (2015-2024)
## ACC102 Mini Assignment - Track 4: Interactive Data Tool

### 1. Project Overview
This project presents an interactive financial dashboard analyzing six major US sportswear companies: **Nike (NKE), Deckers (DECK), Columbia (COLM), Dick's (DKS), Wolverine (WWW), and Skechers (SKX)**. 

Using the **DuPont Analysis** framework, this tool visualizes how these industry leaders drive their Return on Equity (ROE) through profit margins, asset efficiency, and financial leverage over a 10-year period (2015-2024).

### 2. Core Chain: From Problem to Insights
* **The Problem:** In the highly competitive sportswear industry, which financial levers (profitability, efficiency, or leverage) differentiate top-tier brands from their competitors?
* **The Data:** Ten years of annual financial records (2015-2024) processed into a structured dataset (`full_financial_analysis_2015_2024.xlsx`).
* **The Methods:** * **Data Processing:** Cleaned and calculated DuPont components using `Pandas`.
    * **Analysis:** Calculated Year-over-Year (YoY) growth rates and correlation matrices.
    * **Visualization:** Developed an interactive interface using `Streamlit` with dynamic `Matplotlib` and `Seaborn` charts.
* **Key Findings:** * **Deckers (DECK)** maintains a premium position with high net margins.
    * **Dick's Sporting Goods (DKS)** excels in operational efficiency (Asset Turnover).
    * **Nike (NKE)** shows stable performance but employs a more conservative financial structure compared to smaller peers.

### 3. File Structure
* `app.py`: The interactive Streamlit web application.
* `6_company.ipynb`: Research notebook containing the original data cleaning and analysis logic.
* `full_financial_analysis_2015_2024.xlsx`: The core financial dataset.
* `requirements.txt`: Environment dependencies.

### 4. How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Launch the app: `streamlit run app.py`

### 5. Professional Practice & AI Disclosure
* **AI Usage:** I utilized **Doubao (ByteDance AI)** to assist in generating the core logic for the Streamlit dashboard and to debug the data visualization code (specifically the multi-subplot layouts in Matplotlib).
* **Human Contribution:** I designed the research scope, selected the peer group companies, verified the financial formulas for DuPont Analysis, and provided the final interpretation of the trends.
* **Limitations:** The dataset is limited to annual public filings and does not account for intra-year seasonal volatility or non-public marketing expenditures.

### 6. Author Information
* **Name:** Guifen Lai
* **Major:** Economic and Finance
* **University:** Xi'an Jiaotong-Liverpool University (XJTLU)
