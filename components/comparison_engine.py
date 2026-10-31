"""
Visualization Framework Comparison Matrix and Recommender
Author: Mauricio Arian Choqueña Choque
"""

import streamlit as st
import pandas as pd

COMPARISON_DATA = [
    {
        "Herramienta": "Streamlit",
        "Ecosistema": "Python",
        "Curva de Aprendizaje": "Muy Baja (Horas)",
        "Reactividad / Interactividad": "Media-Alta (Widgets nativos)",
        "Rendimiento / Big Data": "Bueno (Caching integrado)",
        "Despliegue Cloud / SaaS": "1-Click (Streamlit Cloud, Render, HuggingFace)",
        "Casos de Uso Ideales": "Data Science apps, Dashboards rápidos, prototipos de IA/ML, MVPs empresariales",
        "Puntuación": "9.4 / 10"
    },
    {
        "Herramienta": "Plotly / Dash",
        "Ecosistema": "Python / R / Julia",
        "Curva de Aprendizaje": "Media-Alta (Callbacks complejos)",
        "Reactividad / Interactividad": "Extrema (Control granular React.js)",
        "Rendimiento / Big Data": "Excelente (WebGL, Dash Enterprise)",
        "Despliegue Cloud / SaaS": "Moderado (Docker, Render, AWS, Heroku)",
        "Casos de Uso Ideales": "Aplicaciones analíticas de misión crítica, interfaces financieras, dashboards altamente personalizados",
        "Puntuación": "9.2 / 10"
    },
    {
        "Herramienta": "Seaborn / Matplotlib",
        "Ecosistema": "Python (Data Science)",
        "Curva de Aprendizaje": "Baja-Media (Sintaxis concisa)",
        "Reactividad / Interactividad": "Baja (Renderizado estático/PNG)",
        "Rendimiento / Big Data": "Alto para gráficos estáticos",
        "Despliegue Cloud / SaaS": "Fácil en notebooks/reportes PDF",
        "Casos de Uso Ideales": "Investigación científica, papers académicos, análisis exploratorio estadístico (EDA), reportes impresos",
        "Puntuación": "8.8 / 10"
    },
    {
        "Herramienta": "Bokeh / HoloViews",
        "Ecosistema": "Python",
        "Curva de Aprendizaje": "Media-Alta (Modelos BokehJS)",
        "Reactividad / Interactividad": "Alta (Streaming de datos, Server websockets)",
        "Rendimiento / Big Data": "Muy Alto (BokehJS en navegador)",
        "Despliegue Cloud / SaaS": "Moderado (Bokeh Server en contenedor)",
        "Casos de Uso Ideales": "Visualización de streaming de datos en tiempo real, grandes conjuntos de datos en navegador",
        "Puntuación": "8.7 / 10"
    },
    {
        "Herramienta": "Shiny (R & Python)",
        "Ecosistema": "R y Python",
        "Curva de Aprendizaje": "Media (Paradigma puramente reactivo)",
        "Reactividad / Interactividad": "Muy Alta (Grafos de reactividad)",
        "Rendimiento / Big Data": "Alto (Shiny Server, Posit Connect)",
        "Despliegue Cloud / SaaS": "Fácil (ShinyApps.io, Posit Cloud)",
        "Casos de Uso Ideales": "Estadística biomédica, econometría, equipos con fuerte presencia de R y bioestadística",
        "Puntuación": "9.0 / 10"
    }
]

def render_comparison_matrix():
    df_comp = pd.DataFrame(COMPARISON_DATA)
    st.dataframe(
        df_comp,
        column_config={
            "Herramienta": st.column_config.TextColumn("Herramienta / Framework", width="medium"),
            "Curva de Aprendizaje": st.column_config.TextColumn("Curva Aprendizaje", width="small"),
            "Puntuación": st.column_config.TextColumn("Rating Global", width="small")
        },
        use_container_width=True,
        hide_index=True
    )

def render_tool_recommender():
    st.markdown("### 🎯 Asistente de Decisión Tecnológica para Dashboards")
    st.write("Responde estas 3 preguntas y te diremos cuál es la mejor herramienta para tu proyecto:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        time_budget = st.selectbox(
            "Tiempo disponible para construir:",
            ["Menos de 1 semana (Urgente)", "1 a 3 semanas", "Más de un mes (Proyecto a largo plazo)"]
        )
    with col2:
        interactivity_level = st.selectbox(
            "Nivel de interactividad requerido:",
            ["Filtros y KPIs ejecutivos básicos", "Gráficos interactivos 2D/3D (Zoom, Hover, Drilldown)", "Aplicación web completa tipo SaaS con microservicios"]
        )
    with col3:
        deployment_target = st.selectbox(
            "Destino de despliegue principal:",
            ["Plataforma Cloud Gratuita / 1-Click (Streamlit Cloud, Render)", "Infraestructura Cloud Empresarial (AWS, GCP, Kubernetes)", "Documentos estáticos / Informes Académicos"]
        )
        
    if st.button("🔍 Calcular Herramienta Óptima", use_container_width=True):
        if "Urgente" in time_budget or "Streamlit Cloud" in deployment_target:
            st.success("🏆 **Recomendación: Streamlit**\n\nEs la mejor opción para entregar valor de inmediato, cuenta con widgets reactivos automáticos, soporte nativo de Plotly/Seaborn y despliegue automatizado en Streamlit Community Cloud en 2 minutos sin configurar servidores.")
        elif "SaaS con microservicios" in interactivity_level or "Empresarial" in deployment_target:
            st.info("🏆 **Recomendación: Plotly / Dash**\n\nSi necesitas control pixel-perfect sobre el DOM, arquitectura frontend React.js bajo el capó y callbacks complejos interconectados, Dash es la solución industrial ideal.")
        elif "Académicos" in deployment_target:
            st.info("🏆 **Recomendación: Seaborn + Matplotlib con ReportLab**\n\nPara publicaciones científicas e informes PDF que requieren máxima calidad tipográfica y fidelidad vectorial estática sin dependencias de servidor.")
        else:
            st.success("🏆 **Recomendación: Streamlit integrado con Plotly**\n\nLa combinación ganadora utilizada en este proyecto OmniSight: la agilidad de desarrollo de Streamlit junto con la interactividad de Plotly.")
