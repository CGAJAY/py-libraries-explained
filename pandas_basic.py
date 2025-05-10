# This is a simple script to demonstrate the use of pandas

# Importing the pandas library
import pandas as pd

# Creating a simple DataFrame (Table with data)
data = {
    "Name": ["Alice", "Bob", "Charlie", "Alice", "Bob"],
    "Age": [25, 30, 35, 28, 32],
    "City": ["Nairobi", "Kampala", "Lagos", "Nairobi", "Kampala"],
    "Score": [85, 90, 95, 80, 88]
}
df = pd.DataFrame(data) # Creating a DataFrame from the dictionary
print("DataFrame:")
# Displaying the DataFrame
print(df)

print('\n')

print('Names: ')
#Accessing a specific column
print(df['Name']) # Accessing the 'Name' column

print('\n')
#Filtering rows based on a condition
print('People older than 28:')
print(df[df['Age'] > 28]) # Filtering rows where Age is greater than 28
#df is a DataFrame object
#df['Age'] is a way to access the 'Age' column
#df[df['Age'] > 28] filters the DataFrame to include only rows where the 'Age' column is greater than 28
print('\n')
print(df['Age'] > 28)
print('\n')

print(df)

print('\n')
#Sorting the DataFrame by columnn(ascending order)
print('Sorted by Age:')
print(df.sort_values(by='Age', ascending=True)) # Sorting the DataFrame by the 'Age' column
print('\n')

#Sorting by multiple columns
print('Sorted by City and Age:')
print(df.sort_values(by=['City', 'Age'], ascending=[True, False])) # Sorting by 'City' and then by 'Age' in descending order
print('\n')

#Grouping Data and Aggregating
print('Average Score by City:')
print(df.groupby('City')['Score'].mean()) # Grouping by 'City' and calculating the mean of 'Score'
print('\n')

#Adding or Modifying Columns
#Adding a new column based on condition
df['Passed'] = df['Score'] >= 87 # Adding a new column 'Passed' based on the condition
print('DataFrame with Passed column:')
print(df) # Displaying the DataFrame with the new column
print('\n')

#modifying an existing column
df['Age'] = df['Age'] + 1 # Incrementing the 'Age' column by 1
print('DataFrame with incremented Age:')
print(df) # Displaying the DataFrame with the modified column
print('\n')

#Dropping a column
df = df.drop(columns=['Passed']) # Dropping the 'Passed' column
print('DataFrame after dropping Passed column:')
print(df) # Displaying the DataFrame after dropping the column
print('\n')

#Saving to CSV
df.to_csv('people.csv', index=False) # Saving the DataFrame to a CSV file without the index
print('DataFrame saved to people.csv') # Confirmation message
print('\n')

#Reading from CSV
df_from_csv = pd.read_csv('people.csv') # Reading the DataFrame from the CSV file
print('DataFrame read from people.csv:')
print(df_from_csv) # Displaying the DataFrame read from the CSV file
print('\n')

#Concatenating DataFrames
data2 = {
    "Name": ["David", "Eve"],
    "Age": [40, 45],
    "City": ["Accra", "Abuja"],
    "Score": [92, 89]
}

df2 = pd.DataFrame(data2) # Creating another DataFrame
print('Second DataFrame:')
print(df2) # Displaying the second DataFrame
print('\n')

#Concatenating the two DataFrames
df_combined = pd.concat([df, df2], ignore_index=True) # Concatenating the two DataFrames
print('Combined DataFrame:')
print(df_combined) # Displaying the combined DataFrame
print('\n')

#Merging DataFrames on a common column like SQL JOIN
data3 = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Country": ["Kenya", "Uganda", "Nigeria"]
}
df3 = pd.DataFrame(data3) # Creating another DataFrame
print('Third DataFrame:')
print(df3) # Displaying the third DataFrame
print('\n')

#Merging the DataFrames on 'Name'
df_merged = pd.merge(df, df3, on='Name', how='inner') # Merging the DataFrames on 'Name'
print('Merged DataFrame:')
print(df_merged) # Displaying the merged DataFrame
print('\n')

#Pivoting Data
print('Pivot Table:')
pivot_table = df.pivot_table(values='Score', index='City', columns='Name', aggfunc='mean') # Creating a pivot table
print(pivot_table) # Displaying the pivot table
print('\n')

#Additional useful pandas methods
df.head() # Display the first 5 rows of the DataFrame
df.tail() # Display the last 5 rows of the DataFrame
df.sample(3) # Display a random sample of 3 rows from the DataFrame
df.shape # Get the shape of the DataFrame (rows, columns)
df.columns # Get the column names of the DataFrame
df.index # Get the index of the DataFrame
df.dtypes # Get the data types of each column
df['Age'].mean() # Calculate the mean of the 'Age' column
df['Age'].median() # Calculate the median of the 'Age' column
df['Age'].mode() # Calculate the mode of the 'Age' column
df['Age'].min() # Get the minimum value of the 'Age' column
df['Age'].max() # Get the maximum value of the 'Age' column
df['Age'].std() # Get the standard deviation of the 'Age' column
df['Age'].var() # Get the variance of the 'Age' column
df['Age'].sum() # Get the sum of the 'Age' column
df['Age'].count() # Get the count of non-null values in the 'Age' column
df['Age'].quantile(0.5) # Get the 50th percentile (median) of the 'Age' column
df['Age'].quantile([0.25, 0.5, 0.75]) # Get the 25th, 50th, and 75th percentiles of the 'Age' column
df.describe() # Get a statistical summary of the numeric columns
df.info() # Get a concise summary of the DataFrame
df.isnull().sum() # Check for missing values in each column
df.fillna(0) # Fill missing values with 0
df.dropna() # Drop rows with missing values
df['Name'].unique() # Get unique values in the 'Name' column
df['Name'].value_counts() # Count occurrences of each unique value in the 'Name' column
df['Name'].str.contains('A') # Check if 'A' is in the 'Name' column
df['Name'].str.replace('A', 'X') # Replace 'A' with 'X' in the 'Name' column
df['Name'].str.split(' ') # Split the 'Name' column by space
df['Name'].str.upper() # Convert the 'Name' column to uppercase
df['Name'].str.lower() # Convert the 'Name' column to lowercase
df['Name'].str.title() # Convert the 'Name' column to title case
df['Name'].str.len() # Get the length of each name in the 'Name' column
df['Name'].str.slice(0, 3) # Get the first 3 characters of each name in the 'Name' column
df['Name'].str.cat(sep=', ') # Concatenate all names in the 'Name' column with a comma separator
df['Name'].str.extract(r'(\w+)') # Extract the first word from each name in the 'Name' column
df['Name'].str.findall(r'(\w+)') # Find all words in each name in the 'Name' column
df['Name'].str.get_dummies() # Get dummy variables for each unique value in the 'Name' column
df['Name'].str.get(0) # Get the first character of each name in the 'Name' column
df['Name'].str.get(-1) # Get the last character of each name in the 'Name' column
df['Name'].str.get(-2) # Get the second to last character of each name in the 'Name' column             
