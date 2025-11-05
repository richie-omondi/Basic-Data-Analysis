📊 Data Analysis and Visualization Project
------------------------------------------

### 📝 Overview

This project demonstrates **data loading, cleaning, analysis, and visualization** using Python.It performs basic **exploratory data analysis (EDA)** on a CSV dataset (default: the Iris dataset) and handles potential data issues through exception handling.

The script guides you through:

1.  Loading and exploring data using **pandas**
    
2.  Performing **basic statistical analysis and grouping**
    
3.  Creating **various types of visualizations** with **matplotlib** and **seaborn**
    

### 🚀 Features

✅ Load dataset from a local file or URL✅ Handle missing or incorrect data safely✅ Compute descriptive statistics✅ Group and summarize data by categories✅ Create and customize multiple plot types:

*   Line chart
    
*   Bar chart
    
*   Histogram
    
*   Scatter plot✅ Exception handling for:
    
    *   File not found
        
    *   Empty or invalid CSV
        
    *   Data type mismatches
        
    *   Missing values
        

### 🧠 Tasks Breakdown

#### **Task 1: Load and Explore the Dataset**

*   Prompts user for a CSV file path or URL (defaults to the Iris dataset)
    
*   Displays the first few rows using .head()
    
*   Checks data types and missing values
    
*   Cleans the dataset by filling or dropping missing entries
    

#### **Task 2: Basic Data Analysis**

*   Computes basic statistics (mean, median, std, etc.)
    
*   Groups data by a categorical column (e.g., _species_) and calculates the mean for each group
    
*   Identifies interesting patterns in the dataset
    

#### **Task 3: Data Visualization**

*   Creates four types of visualizations:
    
    1.  **Line chart** – Trends over time or index
        
    2.  **Bar chart** – Comparison across categories
        
    3.  **Histogram** – Data distribution
        
    4.  **Scatter plot** – Relationship between two numerical variables
        
*   Adds titles, axis labels, and legends for clarity
    

### ⚙️ Technologies Used

*   **Python 3.x**
    
*   **pandas** – for data handling and analysis
    
*   **matplotlib** – for plotting and visualization
    
*   **seaborn** – for advanced and aesthetic charts
    

### 📂 Project Structure
```bash
Basic_Data_Analysis/
│
├── data_analysis.py     # Main Python script
├── README.md                    # Project documentation (this file)
└── (optional) dataset.csv       # Custom dataset (if not using the default)
```

▶️ How to Run

1. **Clone or download** the project files

```bash
git clone https://github.com/yourusername/data-analysis-project.git
cd data-analysis-project
```

2. **Install dependencies**

```bash
pip install pandas matplotlib seaborn
```

3. **Run the script**

```bash
python data_analysis_project.py
```

4. Provide a dataset path or press Enter to use the default Iris dataset.

🧩 **Example Output**

When using the Iris dataset:

* Displays first 5 rows of the data

* Shows summary statistics

* Groups data by species

* Generates four plots:

   * Petal length trend

   * Average petal length per species

   * Sepal length distribution

   * Sepal length vs. petal length scatter plot

🧰 Error Handling

This program includes robust exception handling for:

* `FileNotFoundError` – if the provided file path is invalid

* `EmptyDataError` – if the dataset file is empty

* `ParserError` – if the file is not a valid CSV

* `TypeError / ValueError` – for invalid data types or operations

* General exceptions – to catch and log unexpected errors

🧪 Example Usage

```bash
Enter the CSV file path or URL (press Enter to use the Iris dataset): 
```

Output:

```bash
✅ Dataset loaded successfully!
🔹 First 5 rows of the dataset:
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
...
✅ All visualizations generated successfully!
```

📈 Possible Enhancements

* Save visualizations as PNG files

* Add logging to store errors in a log file

* Automate dataset profiling using `pandas-profiling`

* Allow the user to choose which plots to generate

👨‍💻 Author

Richard Orido

