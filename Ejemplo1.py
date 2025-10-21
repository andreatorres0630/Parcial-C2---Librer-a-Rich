from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.markdown import Markdown
import time

console = Console()

console.print(Panel.fit(
    "[bold white on blue]Resumen Diario del Equipo de Desarrollo[/bold white on blue]\n\n"
    ":rocket: ¡Sigamos avanzando hacia la meta!",
    title="📋 [bold yellow]Reporte[/bold yellow]",
    subtitle="Fecha: [green]21 de octubre de 2025[/green]",
    border_style="bright_blue"
))

mensaje = """
# 💪 ¡Excelente trabajo equipo!

**Resumen del día:**
- Se cumplieron las metas planificadas.  
- Se identificaron áreas de mejora en el código.  
- Se planificaron nuevas tareas para mañana.

> *“La excelencia no es un acto, sino un hábito.”* – Aristóteles
"""

console.print(Markdown(mensaje))

table = Table(
    title="[bold underline]📋 Tareas Completadas[/bold underline]",
    border_style="green",
    show_lines=True
)

table.add_column("👤 Integrante", justify="center", style="bold cyan")
table.add_column("🛠️ Tarea", justify="left", style="bold magenta")
table.add_column("📊 Estado", justify="center", style="bold yellow")
table.add_column("🔢 Avance (%)", justify="center", style="bold white")

table.add_row("Marielena", "Optimización de base de datos", "[green]✅ Completado[/green]", "100%")
table.add_row("Alejandra", "Diseño de interfaz", "[green]✅ Completado[/green]", "100%")
table.add_row("Andrea", "Pruebas unitarias", "[green]✅ Completado[/green]", "100%")
table.add_row("Ariel", "Documentación técnica", "[yellow]🕒 En progreso[/yellow]", "75%")

console.print(table)

console.print("\n[bold blue]Progreso general del proyecto:[/bold blue]\n")

with Progress(
    TextColumn("🚀 [bold blue]{task.description}"),
    BarColumn(bar_width=None),
    "[progress.percentage]{task.percentage:>3.0f}%",
    TimeRemainingColumn(),
) as progress:
    tarea = progress.add_task("Cargando avance...", total=100)
    for _ in range(75):
        time.sleep(0.05)
        progress.update(tarea, advance=1)

console.rule("[bold green]📅 Fin del Reporte Diario[/bold green]")
