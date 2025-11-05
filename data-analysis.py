# ===================================================
# Data Analysis and Visualization - With Error Handling
# ===================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------
# Task 1: Load and Explore the Dataset
# --------------------------------------------

print("🔹 Starting Data Analysis...\n")

# Prompt user for dataset path or URL
dataset_path = input("Enter the CSV file path or URL (press Enter to use the Iris dataset): ").strip()

# Default to Iris dataset if no input is provided
if dataset_path == "":
    dataset_path = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

try:
    # Attempt to load the dataset
    df = pd.read_csv(dataset_path)
    print("\n✅ Dataset loaded successfully!")
except FileNotFoundError:
    print("\n❌ Error: File not found. Please check your file path or URL.")
    exit()
except pd.errors.EmptyDataError:
    print("\n❌ Error: The file is empty. Please provide a valid dataset.")
    exit()
except pd.errors.ParserError:
    print("\n❌ Error: The file could not be parsed. Ensure it’s a valid CSV file.")
    exit()
except Exception as e:
    print(f"\n❌ Unexpected error while reading the file: {e}")
    exit()

# Display the first few rows
print("\n🔹 First 5 rows of the dataset:")
print(df.head())

# Check structure and missing values
print("\n🔹 Dataset Info:")
print(df.info())

print("\n🔹 Missing Values:")
print(df.isnull().sum())

# Handle missing values safely
try:
    if df.isnull().sum().sum() > 0:
        # Drop or fill missing values
        df = df.dropna()
        print("\n⚠️ Missing values detected and dropped.")
    else:
        print("\n✅ No missing values found.")
except Exception as e:
    print(f"\n❌ Error while handling missing values: {e}")

# --------------------------------------------
# Task 2: Basic Data Analysis
# --------------------------------------------

try:
    print("\n🔹 Basic Statistics:")
    print(df.describe())
except Exception as e:
    print(f"\n❌ Error while computing statistics: {e}")

# Choose a categorical column if available
categorical_columns = df.select_dtypes(include=["object", "category"]).columns
numerical_columns = df.select_dtypes(include=["number"]).columns

if len(categorical_columns) == 0 or len(numerical_columns) == 0:
    print("\n⚠️ Dataset doesn’t have both categorical and numerical columns for grouping.")
else:
    try:
        cat_col = categorical_columns[0]
        print(f"\n🔹 Grouping by '{cat_col}' and computing mean of numerical columns:")
        grouped_means = df.groupby(cat_col).mean(numeric_only=True)
        print(grouped_means)
    except Exception as e:
        print(f"\n❌ Error during grouping and aggregation: {e}")

# --------------------------------------------
# Task 3: Data Visualization
# --------------------------------------------

sns.set(style="whitegrid")

try:
    # 1. Line Chart
    plt.figure(figsize=(8, 5))
    plt.plot(df.index, df[numerical_columns[0]], color="teal", label=numerical_columns[0])
    plt.title(f"Line Chart: {numerical_columns[0]} Trend over Index")
    plt.xlabel("Index")
    plt.ylabel(numerical_columns[0])
    plt.legend()
    plt.show()

    # 2. Bar Chart
    if len(categorical_columns) > 0:
        plt.figure(figsize=(8, 5))
        sns.barplot(x=cat_col, y=numerical_columns[0], data=df, ci=None, palette="viridis")
        plt.title(f"Bar Chart: Average {numerical_columns[0]} per {cat_col}")
        plt.xlabel(cat_col.capitalize())
        plt.ylabel(f"Average {numerical_columns[0]}")
        plt.show()

    # 3. Histogram
    plt.figure(figsize=(8, 5))
    plt.hist(df[numerical_columns[0]], bins=15, color="skyblue", edgecolor="black")
    plt.title(f"Histogram: {numerical_columns[0]} Distribution")
    plt.xlabel(numerical_columns[0])
    plt.ylabel("Frequency")
    plt.show()

    # 4. Scatter Plot
    if len(numerical_columns) >= 2:
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=numerical_columns[0], y=numerical_columns[1], hue=cat_col if len(categorical_columns) > 0 else None, data=df, palette="deep")
        plt.title(f"Scatter Plot: {numerical_columns[0]} vs {numerical_columns[1]}")
        plt.xlabel(numerical_columns[0])
        plt.ylabel(numerical_columns[1])
        plt.legend(title=cat_col.capitalize() if len(categorical_columns) > 0 else "")
        plt.show()

    print("\n✅ All visualizations generated successfully!")
except Exception as e:
    print(f"\n❌ Error during visualization: {e}")

print("\n🎯 Program completed successfully.")
