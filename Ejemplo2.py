from rich.console import Console
from rich.progress import Progress, BarColumn, TimeRemainingColumn
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown
import pandas as pd
import time

# Inicializar la consola Rich
console = Console()

# Ruta del archivo CSV
archivo = "continents2.csv"

# Mostrar título inicial
console.rule("[bold blue]🌍 Análisis de Países y Regiones - Rich & Python[/bold blue]")

# Leer el archivo con barra de progreso
with Progress(
    "[progress.description]{task.description}",
    BarColumn(),
    "[progress.percentage]{task.percentage:>3.0f}%",
    TimeRemainingColumn(),
    console=console,
) as progress:
    tarea = progress.add_task("[cyan]Cargando archivo CSV...", total=100)

    # Simular progreso (solo estético)
    for i in range(0, 100, 10):
        time.sleep(0.1)
        progress.update(tarea, advance=10)

# Leer los datos reales
df = pd.read_csv(archivo)

# Limpiar nombres de columnas (por si hay espacios)
df.columns = df.columns.str.strip().str.lower()

# Mostrar tamaño de datos
console.print(f"\n[bold green]✔ Archivo cargado correctamente.[/bold green]")
console.print(f"Total de registros: [bold yellow]{len(df)}[/bold yellow]\n")

# =====================
#  ANÁLISIS DE DATOS
# =====================

# Total de países por región (continente)
countries_by_region = df['region'].value_counts()

# Subregiones más comuness
top_subregions = df['sub-region'].value_counts().head(5)

# Cantidad de subregiones únicas por continente
subregions_per_region = (
    df.groupby('region')['sub-region'].nunique().sort_values(ascending=False)
)

# =====================
# MOSTRAR RESULTADOS
# =====================

# Mostrar resumen general en Markdown
summary_md = Markdown(f"""
# 🌎 Resumen del Análisis Geográfico
                      
**Total de países:** {len(df)}

**Continente con más países:** {countries_by_region.idxmax()}  
**Número de países en ese continente:** {countries_by_region.max()}

**Subregión más común:** {top_subregions.index[0]}  
**Cantidad de subregiones distintas:** {df['sub-region'].nunique()}
""")

console.print(
    Panel(summary_md, 
          title="[bold magenta]Resumen General[/bold magenta]",
          border_style="bright_magenta")
)

# Crear tabla de países por región
table_region = Table(title="🌍 Países por Región (Continente)")
table_region.add_column("Región", justify="left", style="cyan")
table_region.add_column("Cantidad de Países", justify="right", style="bold yellow")

for region, count in countries_by_region.items():
    table_region.add_row(region, str(count))

console.print(table_region)


# Crear tabla de subregiones más comunes
table_sub = Table(title="📌 Subregiones Más Frecuentes")
table_sub.add_column("Subregion", justify="left", style="green")
table_sub.add_column("Countries", justify="right", style="yellow")

for subregion, count in top_subregions.items():
    table_sub.add_row(subregion, str(count))

console.print(table_sub)

# Mostrar panel adicional con análisis

panel_extra = Panel(
    f"[bold blue]Continente con mayor diversidad de subregiones:[/bold blue] {subregions_per_region.index[0]}\n"
    f"[bold blue]Cantidad de subregiones únicas:[/bold blue] {subregions_per_region.max()}",
    title="[bold green]🌐 Análisis Complementario[/bold green]",
    border_style="bright_blue"
)
console.print(panel_extra)
console.rule("[bold magenta]Fin del Análisis[/bold magenta]")
