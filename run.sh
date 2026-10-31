#!/usr/bin/env bash
echo "====================================================================="
echo " Iniciando OmniSight Analytics Dashboard - Mauricio Choquena"
echo "====================================================================="
pip install -r requirements.txt
python data/sample_data.py
streamlit run app.py
