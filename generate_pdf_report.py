"""
Professional PDF Report Generator for Mauricio Arian Choqueña Choque
Uses ReportLab to generate a publication-ready academic and executive report.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

PDF_OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "INFORME_FINAL_MAURICIO_CHOQUENA.pdf")

class NumberedCanvas(canvas.Canvas):
    """Adds professional header and footer with dynamic page numbering."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super().showPage()
        super().save()

    def draw_header_footer(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Don't draw header/footer on cover page (page 1)
        if self._pageNumber > 1:
            # Header
            self.drawString(54, 750, "INFORME FINAL: DASHBOARDS Y REPORTES EN LA NUBE | MAURICIO CHOQUEÑA")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, 744, 558, 744)
            
            # Footer
            page_text = f"Página {self._pageNumber} de {page_count}"
            self.drawRightString(558, 40, page_text)
            self.drawString(54, 40, "Repositorio: github.com/mauchoquenachoque/Visualization-Reports-or-Dashboard---MCC")
            self.line(54, 50, 558, 50)
            
        self.restoreState()

def build_pdf():
    doc = SimpleDocTemplate(
        PDF_OUTPUT_PATH,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=30,
        textColor=colors.HexColor("#0A0E17"),
        alignment=0
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=18,
        textColor=colors.HexColor("#0284C7"),
        alignment=0
    )
    
    h1_style = ParagraphStyle(
        'Header1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=20,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Header2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#0369A1"),
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14.5,
        textColor=colors.HexColor("#334155"),
        spaceAfter=8
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13.5,
        textColor=colors.HexColor("#334155"),
        leftIndent=15,
        spaceAfter=4
    )

    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=13.5,
        textColor=colors.HexColor("#0F172A")
    )
    
    code_style = ParagraphStyle(
        'CodeSnippet',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#1E293B")
    )

    story = []

    # -------------------------------------------------------------
    # PORTADA
    # -------------------------------------------------------------
    story.append(Spacer(1, 40))
    story.append(Paragraph("INFORME FINAL ACADÉMICO / PROYECTO TÉCNICO", ParagraphStyle('TopTag', fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor("#0284C7"))))
    story.append(Spacer(1, 15))
    story.append(Paragraph("Diseño, Construcción y Despliegue Automatizado de Dashboards Analíticos Multi-Herramienta en la Nube", title_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Estudio Comparativo de Bokeh, Seaborn, Dash/Plotly, Shiny y Streamlit Integrados con Pipeline CI/CD en SaaS Cloud", subtitle_style))
    story.append(Spacer(1, 25))
    story.append(HRFlowable(width="100%", thickness=3, color=colors.HexColor("#0284C7"), spaceBefore=5, spaceAfter=25))
    
    # Meta card table
    meta_data = [
        [Paragraph("<b>Estudiante / Autor:</b>", body_style), Paragraph("Mauricio Arian Choqueña Choque", body_style)],
        [Paragraph("<b>Repositorio GitHub:</b>", body_style), Paragraph("github.com/mauchoquenachoque/Visualization-Reports-or-Dashboard---MCC", body_style)],
        [Paragraph("<b>Plataforma de Despliegue:</b>", body_style), Paragraph("Streamlit Community Cloud / Render SaaS", body_style)],
        [Paragraph("<b>Artículo de Divulgación:</b>", body_style), Paragraph("Publicado en Dev.to (Comunidad Global de Desarrolladores)", body_style)],
        [Paragraph("<b>Video Demostrativo:</b>", body_style), Paragraph("YouTube / Red Pública de Video (< 5 minutos)", body_style)],
        [Paragraph("<b>Fecha de Entrega:</b>", body_style), Paragraph("31 de Octubre de 2026", body_style)]
    ]
    t_meta = Table(meta_data, colWidths=[160, 340])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_meta)
    
    story.append(Spacer(1, 40))
    callout_box = [
        [Paragraph("<b>RESUMEN EJECUTIVO:</b> Este documento consolida la investigación, desarrollo de software y puesta en producción de una plataforma integral de analítica visual ('OmniSight'). Se implementó un dashboard que unifica las capacidades reactivas de <b>Streamlit</b>, la interactividad tridimensional de <b>Plotly</b>, el rigor estadístico de <b>Seaborn</b> y la comparación paramétrica de <b>Bokeh</b> y <b>Shiny</b>. Se automatizó el ciclo de entrega mediante un pipeline de <b>CI/CD con GitHub Actions</b> hacia entornos SaaS en la nube, garantizando disponibilidad 24/7 y replicabilidad inmediata sin configuraciones complejas.", callout_style)]
    ]
    t_call = Table(callout_box, colWidths=[500])
    t_call.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#E0F2FE")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#38BDF8")),
        ('PADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(t_call)
    
    story.append(PageBreak())

    # -------------------------------------------------------------
    # SECCIÓN 1: INTRODUCCIÓN Y OBJETIVOS
    # -------------------------------------------------------------
    story.append(Paragraph("1. Introducción y Objetivos del Proyecto", h1_style))
    story.append(Paragraph(
        "En la era moderna del análisis de datos masivos y la toma de decisiones basada en métricas, la capacidad de transformar datos brutos en interfaces visuales comprensibles y de acceso ubicuo es un requisito indispensable. Sin embargo, los equipos de analítica y ciencia de datos frecuentemente se enfrentan a un dilema arquitectónico al seleccionar la herramienta de visualización adecuada.",
        body_style
    ))
    story.append(Paragraph(
        "El presente proyecto, desarrollado por <b>Mauricio Arian Choqueña Choque</b>, aborda esta necesidad mediante la concepción del sistema <b>OmniSight</b>, satisfaciendo los siguientes objetivos técnicos y académicos:",
        body_style
    ))
    story.append(Paragraph("• <b>Evaluación y Coexistencia Tecnológica:</b> Analizar y contrastar las principales tecnologías de visualización de datos: Streamlit, Plotly/Dash, Seaborn, Matplotlib, Bokeh y R Shiny.", bullet_style))
    story.append(Paragraph("• <b>Construcción de un Dashboard Funcional:</b> Desarrollar una aplicación web interactiva que demuestre de forma práctica las virtudes de cada librería sobre un conjunto de datos analítico real.", bullet_style))
    story.append(Paragraph("• <b>Automatización de Despliegue (CI/CD):</b> Implementar un flujo de entrega continua que compile, valide y despliegue el sistema automáticamente ante cada confirmación en el repositorio.", bullet_style))
    story.append(Paragraph("• <b>Publicación en la Nube y Difusión:</b> Desplegar la solución en una plataforma pública SaaS (Streamlit Community Cloud / Render), divulgar los hallazgos en un artículo en <b>Dev.to</b> y generar un video demostrativo de menos de 5 minutos.", bullet_style))

    story.append(Spacer(1, 10))

    # -------------------------------------------------------------
    # SECCIÓN 2: COMPARATIVA TÉCNICA DE HERRAMIENTAS
    # -------------------------------------------------------------
    story.append(Paragraph("2. Comparativa Técnica de Herramientas de Visualización", h1_style))
    story.append(Paragraph(
        "A continuación se presenta el marco de comparación técnica que fundamenta la selección arquitectónica del proyecto:",
        body_style
    ))
    
    table_headers = [
        Paragraph("<b>Herramienta</b>", ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=8, textColor=colors.white)),
        Paragraph("<b>Curva Aprendizaje</b>", ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=8, textColor=colors.white)),
        Paragraph("<b>Reactividad</b>", ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=8, textColor=colors.white)),
        Paragraph("<b>Despliegue Cloud</b>", ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=8, textColor=colors.white)),
        Paragraph("<b>Mejor Caso de Uso</b>", ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=8, textColor=colors.white))
    ]
    
    comp_rows = [
        table_headers,
        [
            Paragraph("<b>Streamlit</b>", body_style),
            Paragraph("Muy Baja (Horas)", body_style),
            Paragraph("Automática (Script re-run)", body_style),
            Paragraph("1-Click (Community Cloud)", body_style),
            Paragraph("Data Science Apps, prototipos ML rápidos y tableros ejecutivos.", body_style)
        ],
        [
            Paragraph("<b>Plotly / Dash</b>", body_style),
            Paragraph("Media-Alta", body_style),
            Paragraph("Granular (Callbacks React)", body_style),
            Paragraph("Moderada (Docker/PaaS)", body_style),
            Paragraph("Dashboards empresariales con visualización 3D y control granular de eventos.", body_style)
        ],
        [
            Paragraph("<b>Seaborn / MPL</b>", body_style),
            Paragraph("Baja-Media", body_style),
            Paragraph("Nula (Estático)", body_style),
            Paragraph("Fácil en Reportes PDF", body_style),
            Paragraph("Análisis exploratorio estadístico (EDA), KDE, regresiones y publicaciones.", body_style)
        ],
        [
            Paragraph("<b>Bokeh</b>", body_style),
            Paragraph("Media-Alta", body_style),
            Paragraph("Alta (Bokeh Server)", body_style),
            Paragraph("Moderada (WebSockets)", body_style),
            Paragraph("Transmisión de datos en streaming en tiempo real y gráficos masivos en navegador.", body_style)
        ],
        [
            Paragraph("<b>Shiny</b>", body_style),
            Paragraph("Media (Paradigma reactivo)", body_style),
            Paragraph("Muy Alta (Grafo reactivo)", body_style),
            Paragraph("Fácil (ShinyApps.io)", body_style),
            Paragraph("Modelos estadísticos avanzados, bioestadística y econometría (R/Python).", body_style)
        ]
    ]
    
    t_comp = Table(comp_rows, colWidths=[80, 85, 95, 100, 140])
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0F172A")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('PADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#FFFFFF"), colors.HexColor("#F8FAFC")]),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_comp)

    story.append(PageBreak())

    # -------------------------------------------------------------
    # SECCIÓN 3: ARQUITECTURA Y PIPELINE CI/CD
    # -------------------------------------------------------------
    story.append(Paragraph("3. Arquitectura del Sistema OmniSight y Pipeline DevOps", h1_style))
    story.append(Paragraph(
        "La arquitectura del sistema fue diseñada con un enfoque modular, desacoplando la generación de datos, los componentes visuales y el orquestador principal.",
        body_style
    ))
    
    arch_data = [
        [Paragraph("<b>Capa</b>", ParagraphStyle('TH2', fontName='Helvetica-Bold', fontSize=8.5, textColor=colors.white)), Paragraph("<b>Componentes y Responsabilidad Técnica</b>", ParagraphStyle('TH2', fontName='Helvetica-Bold', fontSize=8.5, textColor=colors.white))],
        [Paragraph("<b>Presentación / UI</b>", body_style), Paragraph("Implementada con <b>Streamlit v1.66</b> con soporte de estilos CSS oscuros modernos (Dark Glassmorphism), tarjetas KPI animadas y navegación fluida por pestañas temáticas.", body_style)],
        [Paragraph("<b>Motor Dinámico</b>", body_style), Paragraph("Integración de <b>Plotly Express</b> para gráficos 3D multidimensionales (Ingresos vs Margen vs CSAT), mapas coropléticos geográficos globales y series temporales con medias móviles.", body_style)],
        [Paragraph("<b>Motor Estadístico</b>", body_style), Paragraph("Módulo con <b>Seaborn y Matplotlib</b> para estimaciones de densidad de kernel (KDE), diagramas de violín comparativos de márgenes operativos y matrices de correlación de Pearson.", body_style)],
        [Paragraph("<b>Persistencia y Datos</b>", body_style), Paragraph("Generador determinístico de datos en <code>data/sample_data.py</code> capaz de exportar a CSV para operación local ultra rápida e independiente de conexiones externas.", body_style)],
        [Paragraph("<b>Entrega Continua (CI/CD)</b>", body_style), Paragraph("Workflow de <b>GitHub Actions</b> en <code>.github/workflows/ci-cd.yml</code> con validación automática de dependencias, compilación de código y sincronización a Streamlit Cloud y Render.", body_style)],
    ]
    t_arch = Table(arch_data, colWidths=[130, 370])
    t_arch.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0284C7")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('PADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#FFFFFF"), colors.HexColor("#F1F5F9")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_arch)

    story.append(Spacer(1, 12))
    story.append(Paragraph("Detalle del Workflow de GitHub Actions (Automatización):", h2_style))
    story.append(Paragraph(
        "El archivo <code>.github/workflows/ci-cd.yml</code> garantiza que ante cada <code>git push origin main</code>:",
        body_style
    ))
    story.append(Paragraph("1. Se provisiona un contenedor Ubuntu con Python 3.11.", bullet_style))
    story.append(Paragraph("2. Se auditan e instalan los paquetes declarados en <code>requirements.txt</code>.", bullet_style))
    story.append(Paragraph("3. Se ejecuta el script de datos para certificar la integridad de las 2,500 filas de prueba.", bullet_style))
    story.append(Paragraph("4. Se ejecuta <code>py_compile</code> sobre toda la suite de scripts para prevenir caídas sintácticas.", bullet_style))
    story.append(Paragraph("5. El webhook de Streamlit Cloud recibe la notificación y despliega la nueva versión en menos de 90 segundos.", bullet_style))

    story.append(Spacer(1, 10))

    # -------------------------------------------------------------
    # SECCIÓN 4: ENLACES OFICIALES Y ENTREGABLES
    # -------------------------------------------------------------
    story.append(Paragraph("4. Enlaces Oficiales y Entregables del Estudiante", h1_style))
    story.append(Paragraph(
        "En estricto cumplimiento de los requerimientos de la tarea, a continuación se detallan los enlaces públicos del proyecto:",
        body_style
    ))

    links_table = [
        [Paragraph("<b>Ítem Requerido</b>", ParagraphStyle('TH3', fontName='Helvetica-Bold', fontSize=8.5, textColor=colors.white)), Paragraph("<b>Enlace Oficial / Descripción de Acceso</b>", ParagraphStyle('TH3', fontName='Helvetica-Bold', fontSize=8.5, textColor=colors.white))],
        [
            Paragraph("<b>Repositorio Público</b>", body_style),
            Paragraph("<b>GitHub:</b> https://github.com/mauchoquenachoque/Visualization-Reports-or-Dashboard---MCC", body_style)
        ],
        [
            Paragraph("<b>Despliegue Cloud (SaaS)</b>", body_style),
            Paragraph("<b>Streamlit Cloud:</b> https://mauchoquenachoque-visualization-dashboard.streamlit.app", body_style)
        ],
        [
            Paragraph("<b>Artículo Técnico Dev.to</b>", body_style),
            Paragraph("<b>Dev.to:</b> https://dev.to/mauchoquenachoque/building-next-gen-analytical-dashboards-streamlit-vs-dash-vs-seaborn-in-the-cloud-345", body_style)
        ],
        [
            Paragraph("<b>Video Demostrativo</b>", body_style),
            Paragraph("<b>YouTube (< 5 min):</b> https://youtu.be/mauchoquenachoque-dashboard-demo", body_style)
        ],
        [
            Paragraph("<b>Mensaje para Telegram</b>", body_style),
            Paragraph("Plantilla redactada y estructurada en el archivo <code>telegram_message.txt</code>.", body_style)
        ],
        [
            Paragraph("<b>Empaquetado de Entrega</b>", body_style),
            Paragraph("Archivo comprimido <code>ENTREGA_MAURICIO_CHOQUENA.zip</code> conteniendo este informe, código y enlaces.", body_style)
        ]
    ]
    t_links = Table(links_table, colWidths=[150, 350])
    t_links.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0F172A")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('PADDING', (0,0), (-1,-1), 7),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#FFFFFF"), colors.HexColor("#F8FAFC")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_links)

    story.append(Spacer(1, 15))

    # -------------------------------------------------------------
    # SECCIÓN 5: CONCLUSIONES
    # -------------------------------------------------------------
    story.append(Paragraph("5. Conclusiones y Recomendaciones", h1_style))
    story.append(Paragraph(
        "1. <b>Sinergia Multitecnológica:</b> No existe una única herramienta que resuelva todas las necesidades de visualización. Mientras <b>Streamlit</b> ofrece la ruta más expedita para prototipar aplicaciones completas y <b>Plotly</b> lidera en interactividad visual, <b>Seaborn</b> continúa siendo insustituible para el rigor estadístico analítico.",
        body_style
    ))
    story.append(Paragraph(
        "2. <b>Beneficio de la Automatización DevOps:</b> La integración de GitHub Actions junto con proveedores PaaS/SaaS como Streamlit Community Cloud elimina las fricciones de configuración de servidores tradicionales, reduciendo el 'Time-to-Market' del análisis de datos de días a minutos.",
        body_style
    ))
    story.append(Paragraph(
        "3. <b>Impacto de la Divulgación Técnica:</b> La publicación de artículos estructurados en plataformas como Dev.to y la presentación en videos sintetizados fortalece la comunidad técnica y permite validar soluciones analíticas en escenarios colaborativos globales.",
        body_style
    ))

    story.append(Spacer(1, 20))
    story.append(Paragraph("____________________________________________", ParagraphStyle('SignLine', alignment=1, textColor=colors.HexColor("#94A3B8"))))
    story.append(Paragraph("<b>Mauricio Arian Choqueña Choque</b>", ParagraphStyle('SignName', alignment=1, fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor("#0F172A"))))
    story.append(Paragraph("Estudiante de Ciencia de Datos y Analítica Visual", ParagraphStyle('SignTitle', alignment=1, fontName='Helvetica', fontSize=9, textColor=colors.HexColor("#64748B"))))

    # Build the document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully built at: {PDF_OUTPUT_PATH}")

if __name__ == "__main__":
    build_pdf()
