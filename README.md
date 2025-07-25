🚖 Uber Fare Analysis Project
 
🎓 Student: *Mugisha Leopold*  
🏫 Institution: AUCA  
👨‍🏫 Instructor: Eric Maniraguha  
📂 Tools Used: Python, Power BI, Pandas  
📊 Dataset: [Uber Fares Dataset on Kaggle](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset)

🎯 Project Objective

Conduct end-to-end analysis of Uber ride fare data to:
- Explore ride and fare trends across time intervals  
- Clean, transform, and visualize the dataset  
- Build an **interactive Power BI dashboard**  
- Generate meaningful **business insights**

🧹 Step 1: Data Cleaning

✔️ Loaded `uber.csv` using Python  
✔️ Removed 1 row with null coordinates  
✔️ Removed entries with:
❌ Negative fares
❌ Passenger count ≤ 0 or > 6

✅ Final dataset size: `199,269 rows`


## 🛠️ Step 2: Feature Engineering

🔄 Extracted from `pickup_datetime`:
 🕐 `hour`
 📅 `day`, `month`
 📆 `day_of_week`

⚡ Added custom column:
 🟡 `is_peak` → `"Peak"` or `"Off-Peak"` hours

📤 Saved as: `uber_enhanced.csv`

📈 Step 3–5: Visual Analytics (Power BI)

📌 Key Dashboards Created:

- ⏰ Fare Patterns by Hour → Line + Bar Charts  
- 🧭 Ride Counts by:
  - Hour
  - Day
  - Month
- 📅 Seasonal Trends using `day_of_week`  
- 🔄 Peak vs Off-Peak rides (Pie + Area chart)  
- 🗺️ (Optional): Spatial Distribution using Maps
- 
 🧩 Interactivity:
- ✅ Slicers, filters, and tooltips enabled
- ✅ Drill-down from month → day → hour

🔍 Step 6: Key Insights

📊 Peak Ride Hours:  
- 🕗 8 AM  
- 🕕 6 PM  

📅 Most Active Days: 
- Weekdays > Weekends

🧾 Fare Trends:  
- Fares peak during rush hours
- Off-peak rides dominate (~65%)

📤 Deliverables

| File | Description |
|------|-------------|
| `uber.csv` | Original dataset |
| `uber_cleaned.csv` | After cleaning |
| `uber_enhanced.csv` | With new time columns |
| `DataFrame.py` | Python EDA script |
| `uber_analysis.pbix` | Power BI dashboard |
| `README.md` | This project report |
| `/screenshots` | Power BI visuals |


## 📌 Screenshots

![Dashboard Overview](screenshots/dashboard_full.png)  
_Add more screenshots as needed_

💡 Future Recommendations

- 📡 Integrate **weather data** to examine its effect  
- 🚦 Use **geolocation clustering** for hotspot zones  
- 🧠 Predictive modeling to forecast fare surges

---

## 🔗 References

- 📁 [Dataset on Kaggle](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset)  
- 🐍 [Pandas Documentation](https://pandas.pydata.org/docs/)  
- 📊 [Power BI Guides](https://learn.microsoft.com/en-us/power-bi/)

