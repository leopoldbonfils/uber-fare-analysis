🚖 Uber Fare Analysis Project

 
🎓 Student and ID: *Mugisha Leopold - 26636* 

📂 Tools Used: Python, Power BI, Pandas  
📊 Dataset: [Uber Fares Dataset on Kaggle](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset)

🎯 Project Objective

Conduct end-to-end analysis of Uber ride fare data to:
 Explore ride and fare trends across time intervals  
 Clean, transform, and visualize the dataset  
 Build an interactive Power BI dashboard  
 Generate meaningful business insights

🧹 Step 1: Data Cleaning

✔️ Loaded `uber.csv` using Python  
✔️ Removed 1 row with null coordinates  
✔️ Removed entries with:
    Negative fares
    Passenger count ≤ 0 or > 6

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
<img width="776" height="388" alt="Screenshot 2025-07-25 102656" src="https://github.com/user-attachments/assets/8a8e2c60-0e61-4f9d-a780-eb8edf68686a" />
<img width="1920" height="1080" alt="Screenshot 2025-07-23 201328" src="https://github.com/user-attachments/assets/d88837bf-8b17-4ef2-8402-7982603e50fb" />
<img width="1920" height="1080" alt="Screenshot 2025-07-23 091033" src="https://github.com/user-attachments/assets/9c3504bf-4d7b-4657-98af-ff8947ebd53f" />
<img width="1910" height="1007" alt="Screenshot 2025-07-23 091820" src="https://github.com/user-attachments/assets/d877152d-2c82-4201-9275-8ddbb874d504" />
<img width="1920" height="1080" alt="Screenshot 2025-07-23 091902" src="https://github.com/user-attachments/assets/3b5e2c8b-20e8-4aae-ad04-f9cdccf45c78" />
<img width="1920" height="1080" alt="Screenshot 2025-07-23 092222" src="https://github.com/user-attachments/assets/dc283fec-071c-480e-a63f-a5adff05cc25" />



🔗 References

- 📁 [Dataset on Kaggle](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset)  
- 🐍 [Pandas Documentation](https://pandas.pydata.org/docs/)  
- 📊 [Power BI Guides](https://learn.microsoft.com/en-us/power-bi/)

