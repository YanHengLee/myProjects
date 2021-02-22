import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = (df["weight"] / df['height'] ** 2) * 10000
df["overweight"] = df["overweight"].apply(lambda x: 1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df["cholesterol"] == 1, "cholesterol"] = 0
df.loc[df["cholesterol"] > 1, "cholesterol"] = 1

df["gluc"] = df["gluc"].apply(lambda x: 0 if x == 1 else 1)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for catplot using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'
    df_cat = pd.melt(df, id_vars="cardio", value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])

    # Draw the catplot
    g = sns.catplot(x="variable", hue="value", col="cardio", data=df_cat, kind="count")
    g.set_ylabels("total")
    g.set_xlabels("variable")
    fig = g.fig

    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[~(df['ap_lo'] > df['ap_hi']) &
                 ~(df["height"] < df["height"].quantile(0.025)) &
                 ~(df["height"] > df["height"].quantile(0.975)) &
                 ~(df["weight"] < df["weight"].quantile(0.025)) &
                 ~(df["weight"] > df["weight"].quantile(0.975))
                 ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(9, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, linewidths=1, mask=mask, vmax=.8, center=0.09, annot=True, square=True, fmt=".1f", cbar_kws={"shrink": 0.5})

    fig.savefig('heatmap.png')
    return fig
