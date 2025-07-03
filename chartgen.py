import matplotlib.pyplot as plt

def generate_disaster_charts(df):
    # Heatmap
    plt.figure(figsize=(10, 5))
    df.set_index("Region")[["FireRisk", "FloodRisk", "DisplacementRisk"]].plot(kind="bar", stacked=True)
    plt.title("Disaster Risk Heatmap by Region")
    plt.ylabel("Risk Level")
    plt.tight_layout()
    plt.savefig("disaster_risk_heatmap.png")
    plt.close()

    # Trendline placeholder (not time-based yet)
    plt.figure(figsize=(10, 5))
    df["CompositeRisk"] = (df["FireRisk"] + df["FloodRisk"] + df["DisplacementRisk"]) / 3
    df.plot(x="Region", y="CompositeRisk", kind="line", marker="o", title="Composite Disaster Trend")
    plt.ylabel("Risk")
    plt.savefig("disaster_trendline.png")
    plt.close()