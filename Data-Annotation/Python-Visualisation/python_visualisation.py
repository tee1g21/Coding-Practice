import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv("6XWX_bike_rides.csv")

# Display the first 5 rows
#print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
#print(df.info())

# Convert `date` to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter data by year 2022
df_2022 = df[df['date'].dt.year == 2022]
print(df_2022.head().to_markdown(index=False, numalign="left", stralign="left"))

print(df_2022.size)

# Compute and print average `group_size` in 2022
avg_group_size_2022 = df_2022['group_size'].mean()
print(
    f"The average group size for rides in 2022 was: {avg_group_size_2022:.2f}"
)