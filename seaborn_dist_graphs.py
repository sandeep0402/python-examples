#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 18:19:29 2021

@author: sandeep
"""

import seaborn as sns
import matplotlib.pyplot as plt

print("In built example datasets in seaborn are: ", sns.get_dataset_names())
tips = sns.load_dataset("tips")

sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)

dots = sns.load_dataset("dots")
print(dots.head())
sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate", col="align",
    hue="choice", size="coherence", style="choice",
    facet_kws=dict(sharex=False),
)


sns.displot(data=tips, kind="ecdf", x="total_bill", col="time", hue="smoker", rug=True)

sns.catplot(data=tips, kind="swarm", x="day", y="total_bill", hue="smoker")

penguins = sns.load_dataset("penguins")
sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species")

sns.pairplot(data=penguins, hue="species")

# heatmap
# Load the example flights dataset and convert to long-form
flights_long = sns.load_dataset("flights")
flights = flights_long.pivot("month", "year", "passengers")

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax,  cmap="cool")

sns.clustermap(flights, annot=True, fmt="d", linewidths=.5,   cmap="cool")
