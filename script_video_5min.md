# GUION OFICIAL DE VIDEO DEMOSTRATIVO (< 5 MINUTOS)
## PROYECTO: OMNISIGHT - DASHBOARD MULTI-HERRAMIENTA Y DESPLIEGUE CLOUD AUTOMATIZADO
**Estudiante:** Mauricio Arian Choqueña Choque  
**Duración Total Estimada:** 4 minutos y 30 segundos  
**Plataforma de Publicación Sugerida:** YouTube / TikTok / Facebook / Red Social Pública  

---

### 📋 FICHA TÉCNICA PARA YOUTUBE
- **Título del Video:**  
  `Construcción y Despliegue de Dashboard Analítico Multi-Herramienta (Streamlit, Plotly, Seaborn) con CI/CD en la Nube | Mauricio Choqueña`
- **Descripción del Video:**  
  ```text
  Demostración práctica de la construcción del dashboard analítico "OmniSight" por el estudiante Mauricio Arian Choqueña Choque.
  
  🔗 Repositorio GitHub: https://github.com/mauchoquenachoque/Visualization-Reports-or-Dashboard---MCC
  🌐 Aplicación en Vivo (Streamlit Cloud): https://mauchoquenachoque-visualization-dashboard.streamlit.app
  📝 Artículo en Dev.to: https://dev.to/mauchoquenachoque/building-next-gen-analytical-dashboards-streamlit-vs-dash-vs-seaborn-in-the-cloud-345
  
  ⏱️ Marcas de Tiempo:
  0:00 - Introducción y Objetivos
  0:40 - Arquitectura del Código y Herramientas (Streamlit, Plotly, Seaborn)
  1:40 - Demostración en Vivo del Dashboard Interactivo
  2:50 - Matriz Comparativa (Bokeh, Seaborn, Dash, Shiny, Streamlit)
  3:30 - Automatización CI/CD con GitHub Actions y Despliegue Cloud
  4:10 - Publicación en Dev.to y Conclusiones
  ```
- **Etiquetas / Tags:**  
  `Streamlit, Python, Data Science, Plotly, Seaborn, DevOps, GitHub Actions, Cloud Computing, Dashboard, Mauricio Choquena`

---

### 🎙️ ESTRUCTURA Y DIÁLOGO MINUTO A MINUTO

#### ⏱️ 0:00 - 0:40 | BLOQUE 1: INTRODUCCIÓN Y PRESENTACIÓN
- **Qué mostrar en pantalla:**
  - Mostrar la portada del proyecto en pantalla completa o la interfaz del navegador con el banner de OmniSight y el nombre: *Mauricio Arian Choqueña Choque*.
- **Voz en off / Lo que dices:**
  > "Hola a todos, bienvenidos a esta presentación. Mi nombre es Mauricio Arian Choqueña Choque y el día de hoy les presento el proyecto **OmniSight**, una plataforma analítica diseñada para resolver uno de los grandes desafíos de la ciencia de datos moderna: ¿cómo seleccionar y combinar adecuadamente las herramientas de visualización como Streamlit, Plotly, Seaborn y Bokeh, y cómo desplegar un dashboard de forma 100% automatizada en la nube con DevOps? En los próximos cuatro minutos recorreremos el código, la interactividad de la app y el flujo de integración continua."

---

#### ⏱️ 0:40 - 1:40 | BLOQUE 2: ESTRUCTURA DEL PROYECTO Y CÓDIGO
- **Qué mostrar en pantalla:**
  - Cambiar a VS Code.
  - Mostrar el árbol de archivos (`app.py`, `components/`, `data/sample_data.py`, `.github/workflows/ci-cd.yml`).
  - Mostrar brevemente `app.py` y `run.bat`.
- **Voz en off / Lo que dices:**
  > "El proyecto está estructurado de manera modular y limpia en Python. Contamos con una capa de datos sintéticos empresariales con 2,500 registros en `data/sample_data.py`, lo que permite que cualquier usuario pueda clonar el repositorio y ejecutar la aplicación de inmediato simplemente ejecutando `streamlit run app.py` o haciendo doble clic en el archivo `run.bat` sin requerir configuraciones complejas de bases de datos. En la carpeta `components` separamos las tarjetas KPI estilizadas con efectos glassmorphic, los gráficos tridimensionales de Plotly y los modelos estadísticos avanzados de Seaborn."

---

#### ⏱️ 1:40 - 2:50 | BLOQUE 3: DEMO EN VIVO DEL DASHBOARD
- **Qué mostrar en pantalla:**
  - Navegar en vivo por la aplicación abierta en el navegador (`localhost:8501` o en Streamlit Cloud).
  - Interactuar con la barra lateral: cambiar un filtro de región o mover el slider de CSAT.
  - Mostrar la pestaña 1 (KPIs y mapa de facturación global).
  - Cambiar a la pestaña 2 (Plotly): rotar con el ratón el gráfico 3D de dispersión y hacer zoom.
  - Cambiar a la pestaña 3 (Seaborn): mostrar las curvas KDE de densidad y el diagrama de violín.
- **Voz en off / Lo que dices:**
  > "Aquí vemos el dashboard en funcionamiento. En la parte superior tenemos las tarjetas KPI con deltas porcentuales calculados al vuelo. Al mover los filtros de la barra lateral, todas las métricas y gráficos se recalculan en tiempo real. En la pestaña de Plotly, los usuarios tienen interactividad completa: podemos rotar en 360 grados este espacio tridimensional que relaciona Ingresos, Beneficios y Satisfacción del Cliente. Si pasamos a la pestaña de Seaborn, observamos gráficos de alta precisión estadística: estimaciones de densidad de probabilidad y gráficos de violín que permiten detectar asimetrías y cuartiles de rendimiento de inmediato."

---

#### ⏱️ 2:50 - 3:30 | BLOQUE 4: MATRIZ COMPARATIVA Y RECOMENDADOR
- **Qué mostrar en pantalla:**
  - Clic en la pestaña 4: "⚖️ Comparativa de Herramientas".
  - Mostrar la tabla comparativa que evalúa Streamlit vs Dash vs Seaborn vs Bokeh vs Shiny.
  - Probar el "Asistente de Decisión Tecnológica" seleccionando una opción y dando clic en calcular.
- **Voz en off / Lo que dices:**
  > "Un requisito esencial de este trabajo fue el análisis comparativo entre tecnologías. Hemos incorporado una matriz que evalúa la curva de aprendizaje, reactividad y rendimiento de Streamlit, Plotly Dash, Seaborn, Bokeh y Shiny. Además, implementé un asistente interactivo donde el usuario responde tres preguntas sencillas sobre su tiempo y necesidades y el sistema le recomienda la herramienta exacta para su proyecto."

---

#### ⏱️ 3:30 - 4:10 | BLOQUE 5: AUTOMATIZACIÓN CI/CD Y CLOUD SAAS
- **Qué mostrar en pantalla:**
  - Abrir el navegador en el repositorio de GitHub: pestaña `Actions`.
  - Mostrar el pipeline de CI/CD ejecutado con check verde ✅.
  - Mostrar la app en vivo en el dominio de Streamlit Community Cloud.
- **Voz en off / Lo que dices:**
  > "Para la entrega del software, implementamos un pipeline automatizado de Integración y Despliegue Continuo con GitHub Actions. Cada vez que realizo un `git push` a la rama `main`, el workflow compila el código, ejecuta pruebas sintácticas de humo y notifica a la plataforma SaaS Streamlit Community Cloud, la cual actualiza el contenedor de producción en menos de 90 segundos con cero tiempo de inactividad y certificado SSL automático."

---

#### ⏱️ 4:10 - 4:35 | BLOQUE 6: PUBLICACIÓN EN DEV.TO Y CONCLUSIONES
- **Qué mostrar en pantalla:**
  - Abrir la pestaña del navegador con el artículo en Dev.to (`dev_to_article.md`) con las imágenes y formato prolijo.
  - Mostrar el archivo `INFORME_FINAL_MAURICIO_CHOQUENA.pdf`.
- **Voz en off / Lo que dices:**
  > "Todos los fundamentos teóricos, arquitecturas y código fuente han sido documentados y publicados en nuestro artículo en Dev.to, así como en el informe final en formato PDF incluido en la entrega del proyecto. Los enlaces al repositorio público en GitHub, la aplicación en vivo y el artículo se encuentran en la descripción del video. Muchas gracias por su atención."

---
*Fin del video (Duración exacta: ~4:30)*
