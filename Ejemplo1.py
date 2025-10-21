from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress
from rich.markdown import Markdown

# Creamos una consola Rich para imprimir contenido enriquecido
console = Console()

# Mostramos un panel decorativo con un título y estilo personalizado
console.print(Panel.fit(
    "[bold white on blue]Resumen Diario del Equipo de Desarrollo[/bold white on blue]",  # Texto con fondo azul y letras blancas en negrita
    title="📋 [bold yellow]Reporte[/bold yellow]",  # Título del panel con emoji y texto amarillo
    border_style="bright_blue"  # Color del borde del panel
))

# Creamos un mensaje en formato Markdown con título y texto motivacional
mensaje = """
# [bold green]¡Buen trabajo equipo! 🎉[/bold green]

**Este es el resumen de las tareas completadas hoy.**
Mantengan el ritmo y sigamos mejorando juntos.
"""
# Imprimimos el mensaje en Markdown
console.print(Markdown(mensaje))

# Creamos una tabla con título y estilo de bordes
table = Table(title="[bold underline]Tareas Completadas[/bold underline]", border_style="green")

# Añadimos columnas a la tabla con estilos de color y negrita
table.add_column("👤 Integrante", style="bold cyan", no_wrap=True)  # Columna para nombres
table.add_column("🛠️ Tarea", style="bold magenta")  # Columna para descripción de la tarea
table.add_column("📊 Estado", style="bold yellow")  # Columna para el estado de la tarea

# Añadimos filas con datos y estilos de color en los estados
table.add_row("Ana", "Optimización de base de datos", "[green]✅ Completado[/green]")
table.add_row("Luis", "Diseño de interfaz", "[green]✅ Completado[/green]")
table.add_row("María", "Pruebas unitarias", "[green]✅ Completado[/green]")
table.add_row("Carlos", "Documentación técnica", "[yellow]🕒 En progreso[/yellow]")

# Imprimimos la tabla en la consola
console.print(table)

# Creamos una barra de progreso para mostrar el avance general del proyecto
with Progress() as progress:
    # Definimos una tarea con un total de 100 unidades
    tarea = progress.add_task("[bold blue]Progreso general del proyecto...[/bold blue]", total=100)
    # Actualizamos la barra al 75% completado
    progress.update(tarea, completed=75)
