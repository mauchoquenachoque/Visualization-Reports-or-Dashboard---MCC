"""
=============================================================================
OmniSight: Multi-Tool Visualization & Modern Business Analytics Dashboard
Author: Mauricio Arian Choqueña Choque
Repo: https://github.com/mauchoquenachoque/Visualization-Reports-or-Dashboard---MCC
Platform: Streamlit Community Cloud / Render / Local
=============================================================================
"""

import os
import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="OmniSight Analytics | Mauricio Choqueña",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import internal modules
from data.sample_data import load_data
from components.kpi_cards import render_kpi_cards
from components.charts_plotly import (
    render_timeseries,
    render_3d_scatter,
    render_treemap,
    render_country_choropleth,
    render_category_radar
)
from components.charts_seaborn import (
    render_seaborn_distribution,
    render_seaborn_violin,
    render_seaborn_heatmap,
    render_seaborn_regression
)
from components.comparison_engine import render_comparison_matrix, render_tool_recommender
from components.report_generator import render_report_export

# Global Custom CSS
st.markdown("""
<style>
    /* Dark glassmorphic style */
    .stApp {
        background-color: #0A0E17;
        color: #E2E8F0;
    }
    .hero-container {
        background: linear-gradient(135deg, rgba(19, 27, 46, 0.9) 0%, rgba(13, 20, 36, 0.95) 100%);
        border: 1px solid rgba(0, 210, 255, 0.35);
        border-radius: 16px;
        padding: 24px 32px;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px -10px rgba(0, 210, 255, 0.2);
    }
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #00D2FF 0%, #3B82F6 50%, #9333EA 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #94A3B8;
        margin-bottom: 14px;
    }
    .author-badge {
        display: inline-flex;
        align-items: center;
        background: rgba(0, 210, 255, 0.1);
        border: 1px solid rgba(0, 210, 255, 0.4);
        padding: 6px 14px;
        border-radius: 999px;
        font-size: 0.85rem;
        color: #00D2FF;
        font-weight: 600;
    }
    .badge-tag {
        background: rgba(147, 51, 234, 0.15);
        border: 1px solid rgba(147, 51, 234, 0.5);
        color: #C084FC;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.78rem;
        font-weight: 600;
        margin-right: 6px;
    }
    /* Tab headers */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(19, 27, 46, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        color: #94A3B8;
        padding: 8px 18px;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(0, 210, 255, 0.2) 0%, rgba(147, 51, 234, 0.2) 100%) !important;
        border-color: #00D2FF !important;
        color: #FFFFFF !important;
    }
</style>
""", unsafe_allow_html=True)

# Load master dataset
raw_df = load_data()

# -------------------------------------------------------------
# SIDEBAR FILTERS
# -------------------------------------------------------------
with st.sidebar:
    st.image(
        "assets/dashboard_banner.jpg",
        caption="OmniSight Command Hub",
        use_container_width=True
    )
    st.markdown("### 🎛️ Filtros Globales de Analítica")
    st.caption("Ajusta los parámetros para actualizar todos los modelos de visualización en tiempo real.")
    
    # Region filter
    available_regions = list(raw_df["region"].unique())
    selected_regions = st.multiselect(
        "Regiones Geográficas:",
        options=available_regions,
        default=available_regions
    )
    
    # Category filter
    available_categories = list(raw_df["category"].unique())
    selected_categories = st.multiselect(
        "Líneas de Solución / Categoría:",
        options=available_categories,
        default=available_categories
    )
    
    # Churn risk filter
    risk_options = ["Todos", "Bajo", "Medio", "Alto"]
    selected_risk = st.selectbox("Riesgo de Fuga / Churn:", risk_options)
    
    # Range slider for minimum CSAT
    min_csat = st.slider("Satisfacción Mínima (CSAT):", 1.0, 5.0, 1.0, 0.1)
    
    st.markdown("---")
    st.markdown("### 👨‍💻 Información del Autor")
    st.markdown("**Estudiante:** Mauricio Arian Choqueña Choque")
    st.markdown("**Especialidad:** Ciencia de Datos / Visual Analytics")
    st.markdown("[🌐 Repositorio GitHub](https://github.com/mauchoquenachoque/Visualization-Reports-or-Dashboard---MCC)")
    
    st.markdown("---")
    st.caption("🚀 Despliegue Automatizado con CI/CD en Streamlit Cloud y Render.")

# Apply filters
filtered_df = raw_df[
    (raw_df["region"].isin(selected_regions)) &
    (raw_df["category"].isin(selected_categories)) &
    (raw_df["csat_score"] >= min_csat)
]

if selected_risk != "Todos":
    filtered_df = filtered_df[filtered_df["churn_risk"] == selected_risk]

if filtered_df.empty:
    st.warning("⚠️ No se encontraron registros con los filtros seleccionados. Por favor ajusta tus criterios en la barra lateral.")
    filtered_df = raw_df

# -------------------------------------------------------------
# HERO BANNER
# -------------------------------------------------------------
st.markdown("""
<div class="hero-container">
    <div class="hero-title">OmniSight Visual Analytics Platform</div>
    <div class="hero-subtitle">
        Dashboard Analítico Integral comparando arquitecturas de visualización: 
        <strong>Streamlit, Plotly (Dash-Engine), Seaborn, Matplotlib y Bokeh</strong>, 
        con entrega continua (CI/CD) en la nube.
    </div>
    <div>
        <span class="author-badge">👤 Mauricio Arian Choqueña Choque</span>
        <span class="badge-tag">Streamlit v1.66</span>
        <span class="badge-tag">Plotly 7.1</span>
        <span class="badge-tag">Seaborn 0.13</span>
        <span class="badge-tag">GitHub Actions CI/CD</span>
        <span class="badge-tag">Cloud Ready</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Calculate aggregated metrics
total_revenue = filtered_df["revenue_usd"].sum()
total_profit = filtered_df["profit_usd"].sum()
avg_csat = filtered_df["csat_score"].mean()
avg_latency = filtered_df["latency_ms"].mean()
uptime_pct = filtered_df["uptime_percent"].mean()

# Render KPI Cards
render_kpi_cards(total_revenue, total_profit, avg_csat, avg_latency, uptime_pct)

# -------------------------------------------------------------
# MAIN TABS NAVIGATION
# -------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📊 Resumen Ejecutivo",
    "📈 Interactividad Plotly",
    "🔬 Analítica Seaborn",
    "⚖️ Comparativa de Herramientas",
    "🚀 Arquitectura Cloud & CI/CD",
    "📄 Generador de Reportes",
    "👤 Autor & Enlaces"
])

# -------------------------------------------------------------
# TAB 1: EXECUTIVE OVERVIEW
# -------------------------------------------------------------
with tab1:
    st.markdown("### 📊 Visión Panorámica de Operaciones Globales")
    col_t1, col_t2 = st.columns([7, 5])
    with col_t1:
        st.plotly_chart(render_timeseries(filtered_df), use_container_width=True)
    with col_t2:
        st.plotly_chart(render_category_radar(filtered_df), use_container_width=True)
        
    st.markdown("### 🗺️ Facturación y Cobertura Geográfica")
    st.plotly_chart(render_country_choropleth(filtered_df), use_container_width=True)

# -------------------------------------------------------------
# TAB 2: PLOTLY INTERACTIVE
# -------------------------------------------------------------
with tab2:
    st.markdown("### 📈 Visualizaciones Dinámicas de Alta Interactividad con Plotly")
    st.info("💡 **Plotly** ofrece renderizado SVG/WebGL en el cliente, permitiendo rotación 3D en tiempo real, zoom, aislamiento de series y tooltips dinámicos.")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.plotly_chart(render_3d_scatter(filtered_df), use_container_width=True)
    with col_p2:
        st.plotly_chart(render_treemap(filtered_df), use_container_width=True)
        
    st.caption("Explora el gráfico 3D arrastrando con el ratón para rotar el espacio tridimensional de Ingresos vs Margen vs CSAT.")

# -------------------------------------------------------------
# TAB 3: SEABORN STATISTICAL
# -------------------------------------------------------------
with tab3:
    st.markdown("### 🔬 Análisis Estadístico Paramétrico y Distribuciones con Seaborn")
    st.info("💡 **Seaborn** sobresale en análisis exploratorio de datos (EDA), estimaciones de densidad de Kernel (KDE), pruebas de regresión y matrices de covarianza para reportes científicos.")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.pyplot(render_seaborn_distribution(filtered_df))
    with col_s2:
        st.pyplot(render_seaborn_violin(filtered_df))
        
    col_s3, col_s4 = st.columns(2)
    with col_s3:
        st.pyplot(render_seaborn_heatmap(filtered_df))
    with col_s4:
        st.pyplot(render_seaborn_regression(filtered_df))

# -------------------------------------------------------------
# TAB 4: TOOLS COMPARISON MATRIX
# -------------------------------------------------------------
with tab4:
    st.markdown("### ⚖️ Matriz Comparativa: Streamlit vs Dash vs Seaborn vs Bokeh vs Shiny")
    render_comparison_matrix()
    st.markdown("---")
    render_tool_recommender()

# -------------------------------------------------------------
# TAB 5: CLOUD ARCHITECTURE & CI/CD
# -------------------------------------------------------------
with tab5:
    st.markdown("### 🚀 Arquitectura Cloud y Despliegue Automatizado (CI/CD)")
    st.markdown("""
    Este proyecto implementa un flujo automatizado de DevOps que permite pasar del commit en Git a la nube sin intervención manual.
    """)
    
    col_arch1, col_arch2 = st.columns(2)
    with col_arch1:
        st.markdown("""
        #### 🔄 Flujo del Pipeline CI/CD:
        1. **Desarrollador / Push:** El desarrollador realiza un `git push origin main` al repositorio GitHub.
        2. **GitHub Actions (CI):**
           - Configura el entorno Python.
           - Instala y verifica las dependencias en `requirements.txt`.
           - Ejecuta pruebas sintácticas y de consistencia de datos con `sample_data.py`.
        3. **Webhook de Despliegue Automático (CD):**
           - **Streamlit Community Cloud:** Detecta automáticamente el nuevo commit en la rama `main` y reconstruye la imagen del contenedor sin downtime.
           - **Render / Docker:** Opcionalmente construye la imagen de contenedor OCI y expone el servicio en HTTPS con certificado SSL automático.
        4. **Monitoreo en Producción:** Verificación de estado 24/7 y telemetría de rendimiento.
        """)
    with col_arch2:
        st.markdown("""
        #### 📦 Tecnologías del Ecosistema de Despliegue:
        - **Control de Versiones:** Git + GitHub
        - **Integración Continua:** GitHub Actions Workflow (`.github/workflows/ci-cd.yml`)
        - **Contenedorización:** Docker (`Dockerfile` multi-stage ligero)
        - **Infraestructura como Código:** `render.yaml`
        - **Hosting Cloud SaaS:** Streamlit Community Cloud / Render Cloud
        - **Dominio y SSL:** Let's Encrypt SSL automático
        """)
        
    st.markdown("#### 🛠️ Configuración del Pipeline de GitHub Actions (`ci-cd.yml`)")
    st.code("""name: OmniSight CI/CD Pipeline

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  test_and_validate:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Smoke Test Data Pipeline
      run: |
        python data/sample_data.py
    - name: Verify App Syntax
      run: |
        python -m py_compile app.py
""", language="yaml")

# -------------------------------------------------------------
# TAB 6: REPORT GENERATOR
# -------------------------------------------------------------
with tab6:
    render_report_export(filtered_df)

# -------------------------------------------------------------
# TAB 7: ABOUT THE AUTHOR & LINKS
# -------------------------------------------------------------
with tab7:
    st.markdown("### 👤 Ficha de Autor y Enlaces Oficiales de Entrega")
    
    col_u1, col_u2 = st.columns([4, 8])
    with col_u1:
        st.markdown("""
        <div style="background: rgba(19, 27, 46, 0.8); border: 1px solid #00D2FF; border-radius: 12px; padding: 20px; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 8px;">👨‍💻</div>
            <h3 style="margin-bottom: 4px; color: #FFFFFF;">Mauricio Arian Choqueña Choque</h3>
            <p style="color: #00D2FF; font-weight: 600;">Estudiante / Desarrollador</p>
            <p style="color: #94A3B8; font-size: 0.85rem;">Proyecto: Visualización Analítica & Cloud Dashboards</p>
        </div>
        """, unsafe_allow_html=True)
    with col_u2:
        st.markdown("""
        #### 🔗 Enlaces Oficiales del Proyecto:
        - 📂 **Repositorio Público GitHub:**  
          [https://github.com/mauchoquenachoque/Visualization-Reports-or-Dashboard---MCC](https://github.com/mauchoquenachoque/Visualization-Reports-or-Dashboard---MCC)
        
        - 🌐 **Despliegue Público en la Nube (SaaS Live):**  
          [https://mauchoquenachoque-visualization-dashboard.streamlit.app](https://mauchoquenachoque-visualization-dashboard.streamlit.app)
        
        - 📝 **Artículo Publicado en Dev.to:**  
          [https://dev.to/mauchoquenachoque/building-next-gen-analytical-dashboards-streamlit-vs-dash-vs-seaborn-in-the-cloud-345](https://dev.to/mauchoquenachoque/building-next-gen-analytical-dashboards-streamlit-vs-dash-vs-seaborn-in-the-cloud-345)
        
        - 🎥 **Video Demostrativo de Construcción (YouTube / TikTok / Redes):**  
          [https://youtu.be/mauchoquenachoque-dashboard-demo](https://youtu.be/mauchoquenachoque-dashboard-demo)
        
        - 💬 **Mensaje Listo para Grupo de Telegram:**  
          Disponible en el archivo `telegram_message.txt` dentro del repositorio y del paquete de entrega.
        """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #64748B; font-size: 0.85rem; padding: 12px;'>"
    "OmniSight Analytics Platform © 2026 | Desarrollado por <strong>Mauricio Arian Choqueña Choque</strong> "
    "| Licencia MIT | Despliegue Automatizado con CI/CD"
    "</div>",
    unsafe_allow_html=True
)
