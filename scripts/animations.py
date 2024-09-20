import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress

console = Console()

def clear_screen():
    """Limpia la pantalla del terminal."""
    os.system('clear')

def startup_animation():
    """Muestra una animación de inicio profesional con un mensaje de bienvenida."""
    clear_screen()
    console.print(Panel(
        "[bold white]¡Bienvenido a Termux Code![/bold white]\n\n"
        "[bold cyan]Este programa se actualiza regularmente con nuevas lecciones[/bold cyan].\n"
        "[bold yellow]Aprender a programar es una habilidad poderosa[/bold yellow] que te puede abrir puertas para [bold green]crear proyectos[/bold green], "
        "automatizar tareas y hasta generar [bold magenta]ingresos según tu creatividad[/bold magenta].\n\n"
        "[bold red]Recuerda que este programa tiene derechos de autor y pertenece a Termux Code.[/bold red]\n\n"
        "[bold cyan]¡Prepárate para aprender y crecer como programador![/bold cyan]",
        title="Bienvenida", title_align="center", border_style="cyan"
    ))
    
    console.print(Panel("[bold cyan]Presiona [bold green]Enter[/bold green] para continuar[/bold cyan]", border_style="cyan"))
    input()  # Espera a que el usuario presione Enter
    clear_screen()

    # Animación de carga
    with Progress() as progress:
        task = progress.add_task("[cyan]Cargando lecciones...", total=100)
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(0.02)
    clear_screen()
