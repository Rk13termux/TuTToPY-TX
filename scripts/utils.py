from rich.syntax import Syntax
from rich.console import Console
from rich.panel import Panel

console = Console()

def get_terminal_width():
    """Obtiene el ancho del terminal."""
    return console.width

def adjust_code_width(code, width):
    """Ajusta el código al ancho del terminal y lo formatea para que se muestre correctamente."""
    lines = code.splitlines()
    adjusted_lines = []
    
    for line in lines:
        while len(line) > width:
            split_point = line.rfind(' ', 0, width)
            if split_point == -1:
                split_point = width
            adjusted_lines.append(line[:split_point])
            line = line[split_point:].lstrip()
        adjusted_lines.append(line)
    
    return "\n".join(adjusted_lines)

def display_code_with_colors(code):
    """Muestra el código con colores y fondo negro, ajustado al tamaño del ancho del marco."""
    terminal_width = get_terminal_width() - 4  # Ajustar por los bordes del panel
    adjusted_code = adjust_code_width(code, terminal_width)
    syntax = Syntax(adjusted_code, "python", theme="monokai", line_numbers=True, background_color="black")
    console.print(Panel(syntax, title="Código Python", title_align="left", border_style="cyan"))
