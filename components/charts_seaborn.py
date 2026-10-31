"""
Statistical Seaborn and Matplotlib Visualizations Component
Author: Mauricio Arian Choqueña Choque
"""

import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def set_dark_seaborn_style():
    plt.style.use("dark_background")
    sns.set_theme(style="darkgrid", rc={
        "axes.facecolor": "#131B2E",
        "figure.facecolor": "#0A0E17",
        "grid.color": "#1F293D",
        "text.color": "#E2E8F0",
        "axes.labelcolor": "#CBD5E1",
        "xtick.color": "#94A3B8",
        "ytick.color": "#94A3B8"
    })

def render_seaborn_distribution(df):
    set_dark_seaborn_style()
    fig, ax = plt.subplots(figsize=(10, 4.5))
    
    palette = sns.color_palette(["#00D2FF", "#7928CA", "#FF0080", "#10B981", "#F59E0B"])
    sns.kdeplot(
        data=df,
        x="revenue_usd",
        hue="category",
        common_norm=False,
        fill=True,
        alpha=0.35,
        palette=palette,
        linewidth=2,
        ax=ax
    )
    
    ax.set_title("Distribución de Densidad de Probabilidad (KDE) por Categoría", fontsize=13, weight="bold", pad=12, color="#FFFFFF")
    ax.set_xlabel("Facturación Unitaria (USD)", fontsize=10)
    ax.set_ylabel("Densidad Estimada", fontsize=10)
    plt.tight_layout()
    return fig

def render_seaborn_violin(df):
    set_dark_seaborn_style()
    fig, ax = plt.subplots(figsize=(10, 4.5))
    
    palette = sns.color_palette(["#00D2FF", "#7928CA", "#FF0080", "#10B981"])
    sns.violinplot(
        data=df,
        x="region",
        y="profit_usd",
        palette=palette,
        inner="quartile",
        linewidth=1.2,
        ax=ax
    )
    
    ax.set_title("Distribución y Cuartiles de Beneficio Operativo por Región (Violin Plot)", fontsize=13, weight="bold", pad=12, color="#FFFFFF")
    ax.set_xlabel("Región Geográfica", fontsize=10)
    ax.set_ylabel("Margen de Beneficio (USD)", fontsize=10)
    plt.xticks(rotation=12)
    plt.tight_layout()
    return fig

def render_seaborn_heatmap(df):
    set_dark_seaborn_style()
    fig, ax = plt.subplots(figsize=(7.5, 5))
    
    numeric_cols = ["revenue_usd", "cost_usd", "profit_usd", "active_users", "csat_score", "latency_ms", "uptime_percent"]
    corr = df[numeric_cols].corr()
    
    cmap = sns.diverging_palette(220, 20, as_cmap=True)
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap=cmap,
        linewidths=0.75,
        linecolor="#0A0E17",
        square=True,
        cbar_kws={"shrink": 0.8},
        ax=ax
    )
    
    ax.set_title("Matriz de Correlación Estadística Paramétrica (Pearson)", fontsize=12, weight="bold", pad=12, color="#FFFFFF")
    plt.tight_layout()
    return fig

def render_seaborn_regression(df):
    set_dark_seaborn_style()
    sample = df.sample(min(len(df), 350), random_state=42)
    
    fig, ax = plt.subplots(figsize=(10, 4.5))
    sns.regplot(
        data=sample,
        x="latency_ms",
        y="csat_score",
        scatter_kws={"alpha": 0.45, "color": "#00D2FF", "s": 35},
        line_kws={"color": "#FF0080", "linewidth": 2.5},
        ax=ax
    )
    
    ax.set_title("Regresión Lineal: Impacto de la Latencia del Sistema en el CSAT", fontsize=13, weight="bold", pad=12, color="#FFFFFF")
    ax.set_xlabel("Latencia Promedio de Servicio (ms)", fontsize=10)
    ax.set_ylabel("Puntuación de Satisfacción (CSAT)", fontsize=10)
    plt.tight_layout()
    return fig
