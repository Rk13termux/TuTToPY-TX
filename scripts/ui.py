import os
import json
import subprocess
import random
import string
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from .modules_loader import list_json_files, display_json_content
from .animations import startup_animation, clear_screen

console = Console()

def adjust_width():
    """Calcula el ancho dinámico de los paneles y tablas según el ancho de la terminal."""
    return max(30, console.width - 4)  # Ajusta el margen y asegura un mínimo de 30 caracteres de ancho.

def main_menu():
    try:
        if not hasattr(main_menu, "initialized"):
            startup_animation()
            main_menu.initialized = True
        
        show_banner()
        
        # Mensaje de acción con el mismo tamaño y márgenes
        action_panel = Panel(
            "[bold white][blue]APRENDE[/blue][yellow] PYTHON[/yellow] Y COMIENZA A CREAR TUS PROPIOS SCRIPTS EN [green]15[/green] DIAS[/bold white]",
              border_style="magenta",
              width=adjust_width(), box=box.ROUNDED
        )
        console.print(action_panel)

        # Generar código aleatorio con el mismo tamaño de marco
        code = generate_random_code()
        console.print(Panel(
            f"[bold white] Code [bold green] WahtsApp [/bold green] [bold blue]{code}[/bold blue][/bold white]\n"
            "[bold cyan] Este [white]CODE[white] se utiliza para [green]ACTIVAR[/green] funciones [yellow]PREMIUM[/yellow] en la Comunidad haciendo que este curso sea Dinamico y [magenta]ORIGINAL[/magenta][/bold cyan] ",
              border_style="cyan", width=adjust_width(), box=box.ROUNDED
        ))

        # Mostrar menú principal después del código
        display_file_menu()

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

def generate_random_code(length=15):
    """Genera un código aleatorio de 15 caracteres (números y letras mayúsculas)."""
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def show_banner():
    """Mostrar el banner con márgenes consistentes."""
    terminal_width = adjust_width()
    banner = Panel(
        "[bold white]CURSO DE[bold yellow] PYTHON[/bold yellow]   ([bold red]HACKERS[/bold red])[/bold white]\n"
        "[bold blue]Termux[/bold blue] [bold red]Code[/bold red]",
        border_style="cyan", width=terminal_width, title="Menú Principal", title_align="center", box=box.ROUNDED
    )
    console.print(banner)

def display_file_menu():
    """Muestra el menú de archivos de los módulos con márgenes consistentes."""
    directory = './modules'
    files = list_json_files(directory)

    table = Table(show_header=True, header_style="bold red", style="cyan", box=box.ROUNDED)
    table.add_column("N°", style="red")
    table.add_column("Título", style="bold white")

    for index, file in enumerate(files):
        title = file.replace('.json', '').replace('_', ' ').title()
        table.add_row(str(index + 1), title)

    console.print(table)

    # Llamado a la acción con el mismo tamaño de marco
    console.print(Panel(
        "[bold white][red]ATENCION!!![/red]\n[blue]>> [/blue]Quieres ver los videos de este curso paso a paso Escribenos por [green]WhatsApp[/green] y te Eviaremos el link de [cyan]ACCESO[/cyan] [/bold white]",
        border_style="cyan", width=adjust_width(), box=box.ROUNDED
    ))

    # Selección del módulo con márgenes ajustados
    choice = int(input("Selecciona una lección por número: "))
    if 1 <= choice <= len(files):
        clear_screen()
        with open(os.path.join(directory, files[choice - 1]), 'r') as file:
            json_content = json.load(file)
        lesson_menu(json_content)
    else:
        console.print("[red]Selección inválida.[/red]")

def lesson_menu(json_content):
    """Mostrar el contenido de la lección con marcos y márgenes consistentes."""
    try:
        display_json_content(json_content)

        # Menú dentro de la lección con márgenes ajustados
        menu = Panel(
            "[bold white]1. [bold green]Ir a WhatsApp[/bold green] (DESBLOQUEAR)\n"
            "[bold white]2. [bold blue]Telegram[/bold blue] (SCRIPTS)\n"
            "[bold white]3. [bold cyan]Regresar[/bold cyan]",
            border_style="white", width=adjust_width(), box=box.ROUNDED
        )
        console.print(menu)

        choice = input("Selecciona una opción: ")
        if choice == '1':
            open_whatsapp()
        elif choice == '2':
            open_telegram()
        elif choice == '3':
            clear_screen()
            main_menu()
        else:
            console.print("[red]Opción inválida.[/red]")
            lesson_menu(json_content)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

def open_whatsapp():
    try:
        subprocess.run(["termux-open-url", "https://wa.me/573219329493"], check=True)
    except Exception as e:
        console.print(f"[red]Error al abrir WhatsApp: {e}[/red]")

def open_telegram():
    try:
        subprocess.run(["termux-open-url", "https://t.me/termcode"], check=True)
    except Exception as e:
        console.print(f"[red]Error al abrir Telegram: {e}[/red]")

if __name__ == "__main__":
    main_menu()
