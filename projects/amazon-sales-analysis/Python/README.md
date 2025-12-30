# Amazon Sales Analysis  
**Impact of Pricing, Coupons, and Sponsored Placement on Monthly Sales**

## Project Overview
This project analyzes Amazon product listings to understand **how pricing strategies, coupons, and sponsored placement influence monthly sales performance**.

Using a real-world scraped dataset, the analysis focuses on identifying which levers (discounts vs visibility) most strongly drive sales volume.

The project demonstrates end-to-end data analysis skills:
- Data cleaning & feature engineering (SQL)
- Exploratory data analysis (EDA)
- Aggregation & statistical comparison
- Visualization in Python
- Business-oriented insights

---

## Business Question
**How do pricing and discounts influence monthly sales performance on Amazon products, and how does their impact compare to sponsored placement?**

---

## Data Source
- Amazon product listings (scraped dataset)
- Stored and processed in **SQLite**
- Exported to CSV for Python analysis

Key raw fields include:
- Ratings and reviews
- Monthly purchase indicators
- Listed price vs discounted price
- Coupon information
- Sponsored status
- Buy Box availability

---

## Data Cleaning & Feature Engineering (SQL)
A SQL view (`amazon_products_analysis`) was created to standardize and engineer analytical fields:

### Key engineered features:
- `units_bought_last_month` (numeric)
- `current_price` (what the customer actually pays)
- `original_price` (pre-discount price, when available)
- `discount_pct`
- `has_coupon` (binary)
- `coupon_type` (percent vs fixed amount)
- `is_sponsored_flag`
- `has_buy_box`

All cleaning logic is performed **inside SQL** to ensure reproducibility.

---

## Exploratory Data Analysis (EDA)
EDA was conducted using SQL to:
- Examine distributions of monthly sales
- Compare average and median sales across groups
- Control for sponsored vs organic placement
- Analyze coupon effectiveness

---

## Visualization
A Python visualization was created to compare **average monthly units sold** across four groups:

| Coupon | Sponsored | Avg Units Sold |
|------|----------|----------------|
| No   | Organic  | Low |
| No   | Sponsored | **Highest** |
| Yes  | Organic  | Moderate |
| Yes  | Sponsored | Medium |

**Visualization:**  
`figures/coupon_vs_sponsored.png`

This heatmap highlights the interaction between coupon usage and sponsored placement.

---

## Key Insights
- **Sponsored placement is the strongest driver of sales volume**
- Products that are **Sponsored without coupons outperform all other groups**
- Coupons increase sales for **organic listings**, but the effect is much smaller than sponsored visibility
- Coupons act best as a **secondary optimization**, not a primary growth lever

**Conclusion:**  
Paid visibility (Sponsored placement) has a significantly larger impact on sales than price discounts alone.

---

## Tools & Technologies
- **SQLite** (data storage, cleaning, feature engineering)
- **DBeaver** (SQL development)
- **Python 3.12**
  - pandas
  - matplotlib
  - seaborn
- **PyCharm** (project environment)

---

## Project Structure

```text
Amazon-Sales/
├── Data/
│   └── amazon_products_analysis.csv
├── SQL/
│   └── analysis_view.sql
├── Python/
│   ├── scripts/
│   │   └── coupon_vs_sponsored.py
│   ├── figures/
│          └── coupon_vs_sponsored.png
│   
├── Notes/
│   └── insights.md
└── README.md
```
- **Data/**: Cleaned dataset exported from SQLite
- **SQL/**: Analytical views and feature engineering
- **Python/**: Visualization scripts and figures
- **Notes/**: Business insights and conclusions


---

## Next Steps (Optional Extensions)
- Regression analysis to quantify effect sizes
- Price elasticity modeling
- Category-level analysis
- Time-series tracking with repeated scrapes

---

## Author
**Alejandro**  
Data Analyst | SQL • Python • Analytics



