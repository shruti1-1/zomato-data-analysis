# Zomato Data Analysis Project

## Project Overview
This project performs **Exploratory Data Analysis (EDA)** on the Zomato restaurant dataset using Python.  
The aim is to analyze restaurant ratings, pricing trends, cuisines, and locations to gain meaningful insights into customer preferences and restaurant performance.

This project is created for academic learning and portfolio demonstration purposes.

---

## Objectives
- Clean and preprocess real-world restaurant data  
- Analyze ratings and pricing patterns  
- Identify popular cuisines and locations  
- Study the relationship between ratings and customer votes  
- Visualize data to extract insights  

---

## Project Structure
zomato-data-analysis/
│
├── zomato.py # Main Python script for analysis
├── zomato_dataset.csv # Dataset used for analysis
├── README.md # Project documentation
├── .gitignore # Ignored system/cache files
└── LICENSE # MIT License

---

## Dataset Information
- **Dataset Name:** Zomato Restaurant Dataset  
- **File Format:** CSV  
- **Description:** Contains information about restaurants including ratings, cuisines, location, cost, and customer votes.

### Key Columns
- Restaurant Name  
- Location  
- Cuisines  
- Average Cost for Two  
- Aggregate Rating  
- Votes  
- Online Delivery  
- Table Booking  

---

## Technologies Used
- **Language:** Python 3  
- **Libraries:**
  - pandas  
  - numpy  
  - matplotlib  
  - seaborn  

---

## Installation

### Install Required Libraries
```bash
pip install pandas numpy matplotlib seaborn
```

## Run the Project
```bash
python zomato.py
```
## Analysis Performed
- Data loading and inspection
- Handling missing and duplicate values
- Rating distribution analysis
- Cost vs rating analysis
- Location-wise restaurant analysis
- Cuisine popularity analysis

## Key Insights
- Restaurants with moderate pricing often receive higher ratings
- Popular cuisines vary by location
- Restaurants with higher votes generally have better ratings

## Future Enhancements
- Build an interactive dashboard using Streamlit
- Add more advanced visualizations
- Perform predictive analysis on ratings
- Include geographical maps

## Learning Outcomes
- Practical experience with real-world datasets
- Strong understanding of EDA workflow
- Improved data visualization skills
- Better project documentation practices

## License
- This project is licensed under the MIT License.
- The dataset is used strictly for educational purposes.
