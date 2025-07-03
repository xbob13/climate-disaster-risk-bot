def assess_risk(df):
    df["CompositeRisk"] = (df["FireRisk"] + df["FloodRisk"] + df["DisplacementRisk"]) / 3
    df = df.sort_values("CompositeRisk", ascending=False)
    msg = "**🚨 Top Climate Risk Zones:**\n"
    for _, row in df.iterrows():
        msg += f"- {row['Region']}: {row['CompositeRisk']:.2f} risk\n"
    return msg