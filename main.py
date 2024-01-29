import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import cycle

# Load the dataset
file_path = '/home/ghassanbaltaji/Desktop/CountryGDP.csv'
df = pd.read_csv(file_path)

# List of unique countries and corresponding unique colors
countries = df['Country'].unique()
colors = dict(zip(countries, cycle(plt.cm.tab10.colors)))  # Using tab10 colormap

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))


def update(frame):
    ax.clear()

    # Filter data for the current year
    data_year = df[df['Year'] == frame]

    # Plot a bar for each country with a unique color
    bars = ax.bar(data_year['Country'], data_year['GDP'], color=[colors[c] for c in data_year['Country']])

    ax.set_title(f'GDP Comparison - Year {frame}')
    ax.set_xlabel('Country')
    ax.set_ylabel('GDP (in Trillions USD)')
    ax.set_xticklabels(data_year['Country'], rotation=45, ha='right')

    return bars


# Set the years for the animation
years = df['Year'].unique()

# Create the animation
animation = FuncAnimation(fig, update, frames=years, interval=1500, repeat=False)

# Display the animation
plt.show()
