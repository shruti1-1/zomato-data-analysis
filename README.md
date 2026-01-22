### 🍽️ Zomato Data Analysis Project
  ## 📌 Project Overview

This project performs Exploratory Data Analysis (EDA) on a Zomato restaurant dataset to uncover meaningful insights related to restaurant ratings, pricing patterns, cuisines, and city-wise trends.
The goal is to transform raw food-service data into actionable insights that could help platforms like Zomato, restaurant owners, or customers make informed decisions.

  ## 🎯 Objectives
  - Analyze restaurant ratings across different cities
  - Identify the most popular cuisines
  - Study the relationship between average price and customer ratings
  - Understand city-wise pricing patterns
  - Present insights using clear and effective visualizations

  ## 🗂️ Dataset Information
  - File: zomato_dataset.csv
  - Source: Publicly available Zomato dataset
  - Key Columns Used:
      - Restaurant Name
      - City
      - Cuisine
      - Rating
      - Average Price

  ## 🛠️ Technologies Used
  - Python
  - Pandas – data cleaning and manipulation
  - NumPy – numerical operations
  - Matplotlib & Seaborn – data visualization

  ## 📊 Analysis Performed
  - Data cleaning and preprocessing
  - Handling missing and inconsistent values
  - Conversion of ratings and prices into numeric formats
  - Aggregation and grouping by city and cuisine
  - Visual analysis using:
      - Bar charts
      - Lollipop charts
      - Line plots
      - Donut charts
        
---

### 📈 Key Insights


  ## ⭐ Ratings by City
  - Certain cities consistently show higher average ratings, indicating better customer satisfaction.
  - Urban areas tend to have a wider spread of ratings due to more restaurant variety.

  ## 🍕 Most Popular Cuisines
  - A small number of cuisines dominate restaurant listings.
  - These cuisines appear frequently across multiple cities, suggesting strong customer demand.

  ## 💰 Price vs Rating Relationship
  - Restaurants with moderate pricing often receive higher ratings.
  - Extremely high-priced restaurants do not always guarantee better customer satisfaction.

  ## 🏙️ City-wise Average Pricing
  - Metro cities generally show higher average prices.
  - Smaller cities offer more affordable dining options with competitive ratings.

---

## ▶️ How to Run the Project
1. Clone the repository
```bash
git clone https://github.com/shruti1-1/zomato-data-analysis.git
cd zomato-data-analysis
```

2. Install dependencies
```bash
pip install pandas numpy matplotlib seaborn
```

3. Run the analysis script
```bash
python zomato.py
```

## 📁 Project Structure
```bash
zomato-data-analysis/
│
├── zomato.py                 # Main analysis script
├── zomato_dataset.csv        # Dataset
├── README.md                 # Project documentation
├── LICENSE                   # MIT License
├── Lollipop_chart.png
├── Popular_Cuisines.png
├── Price_vs_Rating.png
└── City_wise_price.png
```

## 🚀 Future Enhancements
- Convert analysis into a Jupyter Notebook with markdown explanations
- Build an interactive dashboard using Streamlit
- Add geographical maps for city-wise restaurant density
- Apply machine learning models to predict restaurant ratings

## 📄 License
- This project is licensed under the MIT License.
- You are free to use, modify, and distribute it with attribution.

## 🙌 Acknowledgement
- Thanks to Zomato and open data contributors for providing datasets that enable learning and exploration in data analytics.
