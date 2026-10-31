"""
Executive Report Generation and Export Component
Author: Mauricio Arian Choqueña Choque
"""

import io
import pandas as pd
import streamlit as st

def generate_markdown_summary(filtered_df):
    total_rev = filtered_df["revenue_usd"].sum()
    total_prof = filtered_df["profit_usd"].sum()
    avg_csat = filtered_df["csat_score"].mean()
    top_country = filtered_df.groupby("country")["revenue_usd"].sum().idxmax()
    top_cat = filtered_df.groupby("category")["revenue_usd"].sum().idxmax()
    
    report = f"""# REPORTE EJECUTIVO DE DESEMPEÑO EMPRESARIAL
**Proyecto:** OmniSight Analytics Dashboard
**Autor:** Mauricio Arian Choqueña Choque
**Repositorio:** mauchoquenachoque/Visualization-Reports-or-Dashboard---MCC
**Fecha de Generación:** 31 de Octubre de 2026

---

## 1. Métricas Clave Filtradas
- **Ingresos Totales:** ${total_rev:,.2f} USD
- **Beneficio Operativo Total:** ${total_prof:,.2f} USD
- **Margen de Ganancia Promedio:** {(total_prof / total_rev * 100):.2f}%
- **Puntuación Media CSAT:** {avg_csat:.2f} / 5.0
- **Total de Transacciones / Registros:** {len(filtered_df):,}

## 2. Líderes de Mercado
- **País con Mayor Facturación:** {top_country}
- **Categoría de Producto Líder:** {top_cat}

## 3. Resumen por Región Geográfica
"""
    reg_summary = filtered_df.groupby("region").agg({
        "revenue_usd": "sum",
        "profit_usd": "sum",
        "csat_score": "mean"
    }).reset_index()
    
    for _, r in reg_summary.iterrows():
        report += f"- **{r['region']}:** Ingresos: ${r['revenue_usd']:,.2f} | Beneficio: ${r['profit_usd']:,.2f} | CSAT: {r['csat_score']:.2f}\n"

    report += """
---
*Generado automáticamente mediante el pipeline de analítica de datos en Streamlit Cloud.*
"""
    return report

def render_report_export(filtered_df):
    st.markdown("### 📥 Centro de Exportación de Datos e Informes")
    st.write("Genera y descarga informes inmediatos del conjunto de datos activo con los filtros seleccionados.")
    
    col1, col2 = st.columns(2)
    with col1:
        csv_data = filtered_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📄 Descargar Dataset Filtrado (.CSV)",
            data=csv_data,
            file_name="omnisight_datos_filtrados.csv",
            mime="text/csv",
            use_container_width=True
        )
    with col2:
        md_report = generate_markdown_summary(filtered_df)
        st.download_button(
            label="📝 Descargar Resumen Ejecutivo (.MD)",
            data=md_report,
            file_name="resumen_ejecutivo_omnisight.md",
            mime="text/markdown",
            use_container_width=True
        )
        
    st.markdown("#### Vista Previa del Resumen Ejecutivo")
    st.markdown(f"```markdown\n{md_report}\n```")
