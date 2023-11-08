import pandas as pd

# Read distances data
df_dist = pd.read_csv('Data/distances.csv', index_col=0)

# Create 'Location' column
df_dist['Location'] = df_dist['Customer Country'].astype(str) + ', ' + df_dist['Customer City'].astype(str)

# Read GPS locations data
df_gps = pd.read_csv('Data/gps_locations.csv', index_col=0)
print("{:,} Locations".format(len(df_gps))

# Merge GPS data with distances data
df_dist = df_dist.merge(df_gps, on='Location', how='left')

# Define columns for joining records
COLS_JOIN = ['Warehouse Code', 'Customer Code']

# Merge 'df_dist' with another DataFrame (assuming 'df_join' is defined elsewhere)
df_join = df_join.merge(df_dist, on=COLS_JOIN, how='left')

print("{:,} records".format(len(df_join)))
