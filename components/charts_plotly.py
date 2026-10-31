"""
Interactive Plotly Visualizations Component (Dash Engine)
Author: Mauricio Arian Choqueña Choque
"""

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd

PLOTLY_TEMPLATE = "plotly_dark"
COLOR_SEQUENCE = ["#00D2FF", "#7928CA", "#FF0080", "#10B981", "#F59E0B", "#6366F1"]

def render_timeseries(df):
    daily = df.groupby(pd.Grouper(key="timestamp", freq="D")).agg({
        "revenue_usd": "sum",
        "profit_usd": "sum"
    }).reset_index()
    
    daily["revenue_7d_ma"] = daily["revenue_usd"].rolling(7, min_periods=1).mean()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=daily["timestamp"], y=daily["revenue_usd"],
        mode="lines",
        name="Ingresos Diarios ($)",
        line=dict(color="#00D2FF", width=1.5),
        opacity=0.65
    ))
    fig.add_trace(go.Scatter(
        x=daily["timestamp"], y=daily["revenue_7d_ma"],
        mode="lines",
        name="Media Móvil 7 Días",
        line=dict(color="#FF0080", width=3)
    ))
    fig.add_trace(go.Bar(
        x=daily["timestamp"], y=daily["profit_usd"],
        name="Beneficio Diario ($)",
        marker=dict(color="#7928CA", opacity=0.45)
    ))
    
    fig.update_layout(
        template=PLOTLY_TEMPLATE,
        title="<b>Evolución Temporal de Ingresos y Beneficio Neto</b>",
        hovermode="x unified",
        margin=dict(l=20, r=20, t=50, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        paper_bgcolor="rgba(19, 27, 46, 0.4)",
        plot_bgcolor="rgba(19, 27, 46, 0.4)"
    )
    return fig

def render_3d_scatter(df):
    sample = df.sample(min(len(df), 450), random_state=42)
    fig = px.scatter_3d(
        sample,
        x="revenue_usd",
        y="profit_usd",
        z="csat_score",
        color="category",
        size="active_users",
        hover_data=["region", "country"],
        title="<b>Análisis Multidimensional 3D: Ingresos vs Beneficio vs CSAT</b>",
        color_discrete_sequence=COLOR_SEQUENCE,
        template=PLOTLY_TEMPLATE
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=40, b=0),
        paper_bgcolor="rgba(19, 27, 46, 0.4)",
        scene=dict(
            xaxis_title="Ingresos ($)",
            yaxis_title="Beneficio ($)",
            zaxis_title="CSAT Score",
            bgcolor="rgba(10, 14, 23, 0.6)"
        )
    )
    return fig

def render_treemap(df):
    fig = px.treemap(
        df,
        path=[px.Constant("Global"), "region", "category", "country"],
        values="revenue_usd",
        color="profit_usd",
        color_continuous_scale="Purp",
        title="<b>Distribución Jerárquica de Ingresos y Margen (Treemap)</b>",
        template=PLOTLY_TEMPLATE
    )
    fig.update_layout(
        margin=dict(l=10, r=10, t=40, b=10),
        paper_bgcolor="rgba(19, 27, 46, 0.4)"
    )
    return fig

def render_country_choropleth(df):
    country_totals = df.groupby("country").agg({
        "revenue_usd": "sum",
        "profit_usd": "sum",
        "active_users": "sum",
        "csat_score": "mean"
    }).reset_index()
    
    # ISO-3 mapping for sample countries
    iso_map = {
        "USA": "USA", "Canada": "CAN", "Germany": "DEU", "UK": "GBR",
        "France": "FRA", "Spain": "ESP", "Japan": "JPN", "Singapore": "SGP",
        "Australia": "AUS", "India": "IND", "Peru": "PER", "Brazil": "BRA",
        "Mexico": "MEX", "Colombia": "COL", "Chile": "CHL"
    }
    country_totals["iso_alpha"] = country_totals["country"].map(iso_map)
    
    fig = px.choropleth(
        country_totals,
        locations="iso_alpha",
        color="revenue_usd",
        hover_name="country",
        hover_data={"revenue_usd": ":$,.2f", "active_users": ":,", "csat_score": ":.2f"},
        color_continuous_scale="Tealgrn",
        title="<b>Desempeño Global de Facturación por País (Choropleth Map)</b>",
        template=PLOTLY_TEMPLATE
    )
    fig.update_geos(
        showcoastlines=True,
        coastlinecolor="rgba(0, 210, 255, 0.3)",
        showland=True,
        landcolor="rgba(19, 27, 46, 0.8)",
        showocean=True,
        oceancolor="rgba(10, 14, 23, 0.9)",
        projection_type="natural earth"
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=40, b=0),
        paper_bgcolor="rgba(19, 27, 46, 0.4)"
    )
    return fig

def render_category_radar(df):
    cat_summary = df.groupby("category").agg({
        "revenue_usd": "mean",
        "profit_usd": "mean",
        "active_users": "mean",
        "csat_score": "mean",
        "latency_ms": "mean"
    }).reset_index()
    
    # Normalize values for radar
    numeric_cols = ["revenue_usd", "profit_usd", "active_users", "csat_score", "latency_ms"]
    labels = ["Ingresos", "Beneficio", "Usuarios", "CSAT", "Velocidad"]
    
    fig = go.Figure()
    for _, row in cat_summary.iterrows():
        # Scale between 0 and 100 for visual radar
        vals = [
            (row["revenue_usd"] / cat_summary["revenue_usd"].max()) * 100,
            (row["profit_usd"] / cat_summary["profit_usd"].max()) * 100,
            (row["active_users"] / cat_summary["active_users"].max()) * 100,
            (row["csat_score"] / 5.0) * 100,
            (1.0 - (row["latency_ms"] / cat_summary["latency_ms"].max())) * 100
        ]
        vals.append(vals[0])
        fig.add_trace(go.Scatterpolar(
            r=vals,
            theta=labels + [labels[0]],
            fill="toself",
            name=row["category"],
            opacity=0.35
        ))
        
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], color="#94A3B8"),
            bgcolor="rgba(15, 23, 42, 0.5)"
        ),
        title="<b>Evaluación Multidimensional por Categoría de Solución (Radar)</b>",
        template=PLOTLY_TEMPLATE,
        margin=dict(l=30, r=30, t=40, b=30),
        paper_bgcolor="rgba(19, 27, 46, 0.4)"
    )
    return fig
