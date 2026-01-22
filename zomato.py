import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import warnings

# Suppress warnings for a cleaner output
warnings.filterwarnings('ignore')

#Step 1: Load and Clean the Data 
try:
    print("Loading the dataset...")
    df = pd.read_csv('zomato_dataset.csv')
    df.columns = df.columns.str.strip()
    print("Columns found:", df.columns.tolist())
    print("-" * 50)
    print("Cleaning the data...")
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
    df['Average Price'] = df['Average Price'].str.extract('(\d+)').astype(float)
    df.dropna(subset=['Rating', 'Average Price', 'Cuisine', 'Location'], inplace=True)
    print("Data cleaning complete.")
    print("-" * 50)
except FileNotFoundError:
    print("Error: 'zomato_dataset.csv' not found. Please make sure it's in the same directory.")
    exit()


#Task 1: Location-wise Restaurant Ratings (Lollipop Chart)
print("Task 1: Analyzing Location-wise Restaurant Ratings...")
city_ratings = df.groupby('Location')['Rating'].mean().reset_index()
city_ratings_sorted = city_ratings.sort_values(by='Rating', ascending=False).head(10)
print("\nTop 10 Locations with the Highest Average Ratings:")
print(city_ratings_sorted)
city_ratings_plot_data = city_ratings_sorted.sort_values(by='Rating', ascending=True)
plt.figure(figsize=(12, 8))
plt.hlines(y=city_ratings_plot_data['Location'], xmin=0, xmax=city_ratings_plot_data['Rating'], color='skyblue', alpha=0.7, linewidth=3)
plt.scatter(city_ratings_plot_data['Rating'], city_ratings_plot_data['Location'], color='dodgerblue', s=100, alpha=1)
plt.title('Top 10 Locations by Average Restaurant Rating (Lollipop Chart)')
plt.xlabel('Average Rating')
plt.ylabel('Location')
plt.xlim(city_ratings_plot_data['Rating'].min() - 0.1, city_ratings_plot_data['Rating'].max() + 0.1)
plt.grid(True, axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
print("\nChart displayed. Close the chart window to continue.")
print("-" * 50, "\n")



#Task 2: Most Popular Cuisines
print("Task 2: Finding the Most Popular Cuisines...")
cuisines_list = df['Cuisine'].str.split(', ').sum()
cuisine_counts = Counter(cuisines_list)
top_10_cuisines = pd.DataFrame(cuisine_counts.most_common(10), columns=['Cuisine', 'Count'])
print("\nTop 10 Most Popular Cuisines:")
print(top_10_cuisines)
plt.figure(figsize=(12, 6))
sns.barplot(x='Count', y='Cuisine', data=top_10_cuisines)
plt.title('Top 10 Most Popular Cuisines')
plt.xlabel('Number of Restaurants')
plt.ylabel('Cuisine')
plt.tight_layout()
plt.show()
print("\nChart displayed. Close the chart window to continue.")
print("-" * 50, "\n")



#Task 3: Relationship Between Cost and Rating (Binned Line Plot)
print("Task 3: Analyzing the Relationship Between Cost and Rating...")
df['Price Bin'] = pd.qcut(df['Average Price'], q=5, labels=False, duplicates='drop')
bin_ratings = df.groupby('Price Bin')['Rating'].mean().reset_index()
bin_labels = df.groupby('Price Bin')['Average Price'].mean().round(0)
bin_ratings['Average Price in Bin'] = bin_labels
print("\nAverage rating per price bin:")
print(bin_ratings)
print("\nDisplaying Binned Line Plot...")
plt.figure(figsize=(10, 6))
sns.lineplot(x='Average Price in Bin', y='Rating', data=bin_ratings, marker='o', color='crimson')
plt.title('Average Rating by Price Range')
plt.xlabel('Average Price in Bin (₹)')
plt.ylabel('Average Rating')
plt.grid(True)
plt.tight_layout()
plt.show()
print("\nChart displayed. Close the chart window to continue.")
print("-" * 50, "\n")


#Task 4: Price Contribution by Top 5 Locations
print("Task 4: Calculating Price Contribution by Top 5 Locations...")
city_cost = df.groupby('Location')['Average Price'].sum().reset_index()
top_5_cities = city_cost.sort_values(by='Average Price', ascending=False).head(5)
total_cost = df['Average Price'].sum()
top_5_cities['Contribution (%)'] = (top_5_cities['Average Price'] / total_cost) * 100
print("\nPrice Contribution by Top 5 Locations:")
print(top_5_cities)
plt.figure(figsize=(10, 8))
plt.pie(top_5_cities['Average Price'], labels=top_5_cities['Location'], autopct='%1.1f%%', startangle=140)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Price Contribution by Top 5 Locations (Donut Chart)')
plt.axis('equal')
plt.show()
print("\nChart displayed. Close the chart window to continue.")
print("-" * 50, "\n")
print("Project script finished!")