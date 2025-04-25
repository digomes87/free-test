from time import sleep
import math
from rich.console import Console
from rich.live import Live
from rich.panel import Panel


class QuantumStateVisualizer:

    def __init__(self, refresh_rate: float = 0.05):
        self.console = Console()
        self.step = 0.0
        self.refresh_rate = refresh_rate


    def _compute_state(self) -> tuple[float, float]:
        
        alpha = math.cos(self.step)
        beta = math.sin(self.step)
        return alpha, beta


    def _build_frame(self) -> Panel:
        
        alpha, beta = self._compute_state()
        state_repr = f"|ψ⟩ = {alpha:.2f}|0⟩ + {beta:.2f}|1⟩"

        art = f"""
        Superposição Quântica

             ⎛   •   ⎞
        |0⟩  ⎜       ⎟  |1⟩
             ⎝   ⟳   ⎠

        {state_repr}
        """

        return Panel(art.strip(), title="Qubit em Superposicao", subtitle="Visualizacacao terminal")


    def run(self) -> None:
        with Live(self._build_frame(), refresh_per_second=1 /self.refresh_rate) as live:
            while True:
                live.update(self._build_frame())
                self.step += 0.1
                sleep(self.refresh_rate)
