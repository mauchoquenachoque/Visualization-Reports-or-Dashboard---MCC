@echo off
echo =====================================================================
echo  Iniciando OmniSight Analytics Dashboard - Mauricio Choquena
echo =====================================================================
echo Verificando dependencias...
python -m pip install -r requirements.txt
echo.
echo Ejecutando generador de datos si no existe...
python data\sample_data.py
echo.
echo Abriendo Dashboard en el navegador...
python -m streamlit run app.py
pause
