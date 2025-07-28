import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("/workspace/boilerplate-sea-level-predictor/epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    first_line_of_best_fit = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    year_range = pd.Series(range(1880, 2051))
    y_pred = first_line_of_best_fit.slope * year_range + first_line_of_best_fit.intercept
    plt.plot(year_range, y_pred, label="Best Fit Line (1880 to 2050)")

    # Create second line of best fit
    df_culled = df[df['Year'] >= 2000]
    second_line_of_best_fit = linregress(x=df_culled['Year'], y=df_culled['CSIRO Adjusted Sea Level'])
    second_year_range = pd.Series(range(2000, 2051))
    y_pred_2 = second_line_of_best_fit.slope * second_year_range + second_line_of_best_fit.intercept
    plt.plot(second_year_range, y_pred_2, label='Best Fit Line (2000 to 2050)')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
