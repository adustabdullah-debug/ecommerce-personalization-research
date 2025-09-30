# Data Cleaning Process
1. Removed transactions with missing CustomerID (135,080 records)
2. Excluded negative quantities and zero-priced items (returns and corrections)
3. Converted CustomerID to integer format for consistent identification
4. Created calculated fields: TotalAmount = Quantity × UnitPrice
5. Final cleaned dataset: 406,829 transactions across 4,338 customers