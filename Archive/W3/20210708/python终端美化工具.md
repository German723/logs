# rich -- python终端美化工具

`pip install rich`

# 美化python的print

```python
from rich import rich
print(“HELLO,[bold megenta]WORLD[bold magenta]!”)
```

## 美化console

(1) console.print

```python
from rich.console import Console
console = Console()
console.print("hello,world!",style="bold red")
console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")
```

