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


# Read Unit of Measure Conversions data
df_uom = pd.read_csv('Data/uom_conversions.csv', index_col=0)
print("{:,} Unit of Measure Conversions".format(len(df_uom))

# Create a copy of df_lines to join with uom data
df_join = df_lines.copy()

# Define columns for joining records
COLS_JOIN = ['Item Code']

# Merge df_join with df_uom
df_join = df_join.merge(df_uom, on=COLS_JOIN, how='left')

# Drop any redundant columns
df_join.drop(df_join.filter(regex='_y$').columns.tolist(), axis=1, inplace=True)
print("{:,} records".format(len(df_join))
df_join.head()


# Calculate Weight (KG)
df_join['KG'] = df_join['Units'] * df_join['Conversion Ratio']

# Define columns to group by for aggregation
GPBY_ORDER = ['Date', 'Month-Year', 
    'Warehouse Code', 'Warehouse Name', 'Warehouse Country', 'Warehouse City',
    'Customer Code', 'Customer Country', 'Customer City', 'Location', 'GPS 1', 'GPS 2', 
    'Road', 'Rail', 'Sea', 'Air',
    'Order Number']

# Aggregate data
df_agg = df_join.groupby(GPBY_ORDER)[['Units', 'KG']].sum().reset_index()

# CO2 Emissions Calculation
dict_co2e = {'Air': 2.1, 'Sea': 0.01, 'Road': 0.096, 'Rail': 0.028}
MODES = ['Road', 'Rail', 'Sea', 'Air']

for mode in MODES:
    df_agg['CO2 ' + mode] = df_agg['KG'] / 1000 * df_agg[mode] * dict_co2e[mode]

df_agg['CO2 Total'] = df_agg[['CO2 ' + mode for mode in MODES]].sum(axis=1)

# Mapping the delivery Mode
df_agg['Delivery Mode'] = df_agg[MODES].apply(
    lambda t: [mode if t[mode] > 0 else '-' for mode in MODES], axis=1)

dict_map = dict(zip(df_agg['Delivery Mode'].astype(str).unique(), 
    [i.replace(", '-'", '').replace("'-'", '').replace("'", '') for i in df_agg['Delivery Mode'].astype(str).unique()]))

df_agg['Delivery Mode'] = df_agg['Delivery Mode'].astype(str).map(dict_map)

