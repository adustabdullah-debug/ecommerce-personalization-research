"""
Complete Data Analysis for Personalization-Loyalty Research
Author: [Your Name]
Date: [Current Date]
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

def load_and_clean_data():
    """Load and clean the Online Retail dataset"""
    print("Loading dataset from UCI Machine Learning Repository...")
    
    # Load the dataset
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
    df = pd.read_excel(url)
    
    print(f"Original dataset: {df.shape[0]:,} rows, {df.shape[1]} columns")
    
    # Data cleaning steps
    df_clean = df.copy()
    
    # Remove missing CustomerIDs
    initial_rows = len(df_clean)
    df_clean = df_clean[df_clean['CustomerID'].notnull()]
    print(f"Removed {initial_rows - len(df_clean):,} rows with missing CustomerID")
    
    # Remove negative quantities and zero prices
    df_clean = df_clean[df_clean['Quantity'] > 0]
    df_clean = df_clean[df_clean['UnitPrice'] > 0]
    
    # Convert CustomerID to integer
    df_clean['CustomerID'] = df_clean['CustomerID'].astype(int)
    
    # Create total amount column
    df_clean['TotalAmount'] = df_clean['Quantity'] * df_clean['UnitPrice']
    
    print(f"Final cleaned dataset: {len(df_clean):,} rows")
    return df_clean

# ... [Include all the analysis functions we created]