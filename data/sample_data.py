"""
OmniSight Enterprise Analytics - Sample Data Generator and Loader
Author: Mauricio Arian Choqueña Choque
Repo: Visualization-Reports-or-Dashboard---MCC
"""

import os
import numpy as np
import pandas as pd

CSV_PATH = os.path.join(os.path.dirname(__file__), "sales_and_metrics.csv")

def generate_enterprise_data(records=2500, random_seed=42):
    np.random.seed(random_seed)
    
    dates = pd.date_range(start="2025-01-01", periods=records, freq="h")
    
    regions_countries = {
        "North America": ["USA", "Canada"],
        "Europe (EMEA)": ["Germany", "UK", "France", "Spain"],
        "Asia-Pacific (APAC)": ["Japan", "Singapore", "Australia", "India"],
        "Latin America (LATAM)": ["Peru", "Brazil", "Mexico", "Colombia", "Chile"]
    }
    
    regions = list(regions_countries.keys())
    categories = ["Cloud Infrastructure", "Enterprise AI & LLM", "Cybersecurity", "Data Analytics & BI", "Edge IoT"]
    
    chosen_regions = np.random.choice(regions, size=records, p=[0.38, 0.28, 0.22, 0.12])
    chosen_countries = [np.random.choice(regions_countries[r]) for r in chosen_regions]
    chosen_categories = np.random.choice(categories, size=records, p=[0.30, 0.35, 0.15, 0.12, 0.08])
    
    base_revenue = {
        "Cloud Infrastructure": 4800,
        "Enterprise AI & LLM": 7500,
        "Cybersecurity": 5200,
        "Data Analytics & BI": 3900,
        "Edge IoT": 3100
    }
    
    revenues = [
        round(float(base_revenue[cat] * np.random.uniform(0.75, 1.65) * (1.2 if reg == "North America" else 1.0)), 2)
        for cat, reg in zip(chosen_categories, chosen_regions)
    ]
    
    margins = np.random.uniform(0.25, 0.65, size=records)
    profits = [round(float(rev * margin), 2) for rev, margin in zip(revenues, margins)]
    costs = [round(rev - prof, 2) for rev, prof in zip(revenues, profits)]
    
    active_users = [int(np.random.poisson(lam=120) * (rev / 4000)) for rev in revenues]
    csat = np.clip(np.random.normal(loc=4.65, scale=0.35, size=records), 1.0, 5.0).round(2)
    latency_ms = np.clip(np.random.normal(loc=135, scale=35, size=records), 45, 450).round(1)
    uptime_pct = np.clip(np.random.normal(loc=99.92, scale=0.08, size=records), 98.5, 100.0).round(3)
    
    churn_risks = np.random.choice(["Bajo", "Medio", "Alto"], size=records, p=[0.72, 0.21, 0.07])
    
    df = pd.DataFrame({
        "timestamp": dates,
        "region": chosen_regions,
        "country": chosen_countries,
        "category": chosen_categories,
        "revenue_usd": revenues,
        "cost_usd": costs,
        "profit_usd": profits,
        "active_users": active_users,
        "csat_score": csat,
        "latency_ms": latency_ms,
        "uptime_percent": uptime_pct,
        "churn_risk": churn_risks
    })
    
    # Save CSV for instant offline access
    df.to_csv(CSV_PATH, index=False)
    return df

def load_data():
    if os.path.exists(CSV_PATH):
        try:
            df = pd.read_csv(CSV_PATH)
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            return df
        except Exception:
            return generate_enterprise_data()
    else:
        return generate_enterprise_data()

if __name__ == "__main__":
    df = generate_enterprise_data()
    print(f"Generated {len(df)} rows successfully. Saved to {CSV_PATH}")
