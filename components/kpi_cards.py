"""
KPI Metrics Component for OmniSight Dashboard
Author: Mauricio Arian Choqueña Choque
"""

import streamlit as st

def render_kpi_cards(total_revenue, total_profit, avg_csat, avg_latency, uptime_pct):
    st.markdown("""
    <style>
    .kpi-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 16px;
        margin-bottom: 24px;
    }
    .kpi-card {
        background: linear-gradient(135deg, rgba(19, 27, 46, 0.85) 0%, rgba(15, 23, 42, 0.6) 100%);
        border: 1px solid rgba(0, 210, 255, 0.25);
        border-radius: 14px;
        padding: 18px 20px;
        box-shadow: 0 8px 24px -6px rgba(0, 0, 0, 0.4);
        transition: all 0.25s ease-in-out;
        position: relative;
        overflow: hidden;
    }
    .kpi-card:hover {
        transform: translateY(-4px);
        border-color: rgba(0, 210, 255, 0.65);
        box-shadow: 0 12px 28px -4px rgba(0, 210, 255, 0.25);
    }
    .kpi-title {
        font-size: 0.82rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #94A3B8;
        margin-bottom: 6px;
        font-weight: 600;
    }
    .kpi-value {
        font-size: 1.75rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 4px;
        font-family: 'Segoe UI', Tahoma, sans-serif;
    }
    .kpi-delta {
        font-size: 0.82rem;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 4px;
    }
    .delta-pos {
        color: #10B981;
    }
    .delta-neg {
        color: #EF4444;
    }
    .kpi-accent {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, #00D2FF, #7928CA);
    }
    </style>
    """, unsafe_allow_html=True)

    html_cards = f"""
    <div class="kpi-container">
        <div class="kpi-card">
            <div class="kpi-accent"></div>
            <div class="kpi-title">Ingresos Totales</div>
            <div class="kpi-value">${total_revenue:,.2f}</div>
            <div class="kpi-delta delta-pos">▲ +24.1% vs mes anterior</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-accent"></div>
            <div class="kpi-title">Beneficio Neto</div>
            <div class="kpi-value">${total_profit:,.2f}</div>
            <div class="kpi-delta delta-pos">▲ +18.7% margen operativo</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-accent"></div>
            <div class="kpi-title">Satisfacción CSAT</div>
            <div class="kpi-value">{avg_csat:.2f} / 5.0</div>
            <div class="kpi-delta delta-pos">▲ +4.2% fidelización</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-accent"></div>
            <div class="kpi-title">Latencia Media SLA</div>
            <div class="kpi-value">{avg_latency:.1f} ms</div>
            <div class="kpi-delta delta-pos">▼ -16.2 ms (óptimo)</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-accent"></div>
            <div class="kpi-title">Disponibilidad Cloud</div>
            <div class="kpi-value">{uptime_pct:.2f}%</div>
            <div class="kpi-delta delta-pos">● 99.9% SLA Cumplido</div>
        </div>
    </div>
    """
    st.markdown(html_cards, unsafe_allow_html=True)
