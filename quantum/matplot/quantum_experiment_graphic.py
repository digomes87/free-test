import matplotlib.pyplot as plt
from qiskit.result import Result
from typing import Dict


class QuantumPlotter:
    def __init__(self, result: Result) -> None:
        self._counts: Dict[str, int] = result.get_counts()


    def plot_counts(self) -> None:
        labels = list(self._counts.keys())
        values = list(self._counts.values())


        plt.figure(figsize=(6, 4))
        bars = plt.bar(labels, values, color='#69b3a2')

        plt.xlabel("Estados")
        plt.ylabel("Frequencia")
        plt.title("Resultados da Medição QUantica")



        for bar in bars:
            height = bar.get_height()
            plt.annotate(
                f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0,3),
                textcoords="offset points",
                ha='center',
                va='bottom'
            )


        plt.tight_layout()
        plt.show()




