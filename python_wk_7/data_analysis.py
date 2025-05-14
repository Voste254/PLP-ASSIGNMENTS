
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore
from sklearn.datasets import load_iris # type: ignore


# Task 1: Load and Explore the Dataset


try:
    # Load Iris dataset from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame

    # Display the first few rows
    print("First five rows of the dataset:")
    print(df.head())

    # Check data types and missing values
    print("\nDataset info:")
    print(df.info())

    print("\nMissing values in each column:")
    print(df.isnull().sum())


except Exception as e:
    print(f"An error occurred while loading or exploring the dataset: {e}")

# Task 2: Basic Data Analysis


try:
    # Descriptive statistics
    print("\nDescriptive statistics:")
    print(df.describe())

    # Group by target (species) and compute mean of features
    df['species'] = df['target'].map(dict(zip(range(3), iris.target_names)))
    grouped = df.groupby('species').mean()
    print("\nMean values by species:")
    print(grouped)

    # Example finding
    print("\nObservation: Setosa species has significantly shorter petal lengths on average.")

except Exception as e:
    print(f"An error occurred during basic data analysis: {e}")

# Task 3: Data Visualization


try:
    # Line plot: Mean petal length by species
    plt.figure(figsize=(8, 5))
    grouped['petal length (cm)'].plot(kind='line', marker='o')
    plt.title("Average Petal Length by Species")
    plt.xlabel("Species")
    plt.ylabel("Petal Length (cm)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("line_plot.png")
    plt.show()

    # Bar chart: Average sepal width by species
    plt.figure(figsize=(8, 5))
    sns.barplot(x=grouped.index, y=grouped['sepal width (cm)'])
    plt.title("Average Sepal Width by Species")
    plt.xlabel("Species")
    plt.ylabel("Sepal Width (cm)")
    plt.tight_layout()
    plt.savefig("bar_chart.png")
    plt.show()

    # Histogram: Distribution of petal lengths
    plt.figure(figsize=(8, 5))
    plt.hist(df['petal length (cm)'], bins=15, color='skyblue', edgecolor='black')
    plt.title("Distribution of Petal Length")
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("histogram.png")
    plt.show()

    # Scatter plot: Sepal length vs Petal length
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
    plt.title("Sepal Length vs Petal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend(title="Species")
    plt.tight_layout()
    plt.savefig("scatter_plot.png")
    plt.show()

except Exception as e:
    print(f"An error occurred while creating visualizations: {e}")
