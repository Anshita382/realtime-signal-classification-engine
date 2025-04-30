import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

messages = []

def accumulate_data(message):
    messages.append(message)
    if len(messages) >= 5:
        df = pd.DataFrame(messages)
        df["time"] = pd.to_datetime(df["time"], unit="s")
        os.makedirs("output", exist_ok=True)

        # 1. Map of sighting locations
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=df, x="lon", y="lat", hue="label")
        plt.title("Sighting Locations")
        plt.savefig("output/report1.pdf")
        plt.clf()

        # 2. Shape frequency over time
        sns.lineplot(data=df, x="time", y="frequency", hue="shape", marker="o")
        plt.title("Shape Frequency Over Time")
        plt.savefig("output/report2.pdf")
        plt.clf()

        # 3. Shape distribution
        sns.countplot(data=df, x="shape")
        plt.title("Shape Distribution")
        plt.savefig("output/report3.pdf")
        plt.clf()

        # 4. Message type distribution
        sns.countplot(data=df, x="label")
        plt.title("Alien vs Human Message Count")
        plt.savefig("output/report4.pdf")
        plt.clf()
