import os
import json
from rich.console import Console
from rich.panel import Panel
from .utils import display_code_with_colors

console = Console()

def list_json_files(directory):
    """Lista los archivos JSON en un directorio dado."""
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"{directory} no es un directorio válido.")
    
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.json')]
    return files

def display_json_content(json_content):
    """Muestra el contenido del JSON completo con los márgenes y marcos apropiados."""
    try:
        if isinstance(json_content, str):
            json_content = json.loads(json_content)

        for lesson, sections in json_content.items():
            console.print(Panel(f"[bold yellow]{lesson}[/bold yellow]", title="Lección", title_align="center", border_style="cyan"))
            if isinstance(sections, dict):
                for section, description in sections.items():
                    if 'description' in description and isinstance(description['description'], str):
                        console.print(Panel(description['description'], title="Descripción", title_align="left", border_style="cyan"))
                    if 'content' in description and isinstance(description['content'], list):
                        for item in description['content']:
                            if isinstance(item, dict):
                                if 'title' in item and isinstance(item['title'], str):
                                    console.print(Panel(f"[bold cyan]{item['title']}[/bold cyan]", title="Contenido", title_align="left", border_style="cyan"))
                                if 'text' in item and isinstance(item['text'], str):
                                    console.print(Panel(item['text'], border_style="cyan"))
                                if 'example_code' in item and isinstance(item['example_code'], str):
                                    display_code_with_colors(item['example_code'])
                                if 'instructions' in item and isinstance(item['instructions'], str):
                                    console.print(Panel(item['instructions'], border_style="cyan"))
                                if 'example_code_command' in item and isinstance(item['example_code_command'], str):
                                    display_code_with_colors(item['example_code_command'])
                                if 'examples' in item and isinstance(item['examples'], list):
                                    for example in item['examples']:
                                        if 'title' in example and isinstance(example['title'], str):
                                            console.print(Panel(f"[bold cyan]{example['title']}[/bold cyan]", title="Ejemplo", title_align="left", border_style="cyan"))
                                        if 'code' in example and isinstance(example['code'], str):
                                            display_code_with_colors(example['code'])
        # Llamado a la acción
        console.print(Panel(
        "[bold cyan]¡Desbloquea el curso completo en videos y aprende Python desde cero en solo 15 días![/bold cyan]\n"
        "[bold white]Este curso está diseñado para llevartede principiante a avanzado con un enfoque intensivo y práctico.[/bold white]\n"
        "[bold green]Copia el [white]CODE[/white] del menu principal, envialo por WhatsApp y PIDE tu link de [blue]ACCESO[/blue]\n [yellow]SELECIONA LA OPCION 1 PARA [green]IR[/green] A[/yellow] [green]WHATSAPP[/green]  [/bold green]",
          border_style="cyan"
    ))
    except Exception as e:
        console.print(f"[red]Error al procesar el contenido del JSON: {e}[/red]")
