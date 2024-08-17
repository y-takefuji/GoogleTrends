import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Load the dataset
df = pd.read_csv('govesg.csv')

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], format='%m-%y')

# Filter data from 2004 to 2023
df = df[(df['date'].dt.year >= 2004) & (df['date'].dt.year <= 2023)]

# Plotting
plt.figure(figsize=(10,6))

# Plot each line with black color
plt.plot(df['date'],df['corporate governance'], label='Corporate Governance',linewidth=1.5,linestyle='solid', color='black')
plt.plot(df['date'],df['ESG'], label='ESG', linestyle='dotted',color='black')

plt.xlabel('Date')
plt.ylabel('Popularity')

# Rotate x-axis labels and limit number of ticks on x-axis
plt.xticks(rotation=90)
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=10))

# Add legend to distinguish lines
plt.legend()

# Show the plot
plt.tight_layout()
plt.savefig('govesg.png')
plt.show()
