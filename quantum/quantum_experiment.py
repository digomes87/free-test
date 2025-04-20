from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.result import Result
from typing import Dict


class QuantumExperiment:
    def __init__(self, num_qubits: int = 1):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits, num_qubits)
        self._build_superposition()


    def _build_superposition(self) -> None:
        for i in range(self.num_qubits):
            self.circuit.h(i)
            self.circuit.measure(i, i)

    def run(self, shots: int = 1000) -> Result:
        simulator = Aer.get_backend("qasm_simulator")
        job = simulator.run(self.circuit, shots=shots)
        return job.result()


    def show_counts(self, result: Result) -> None:
        counts: Dict[str, int] = result.get_counts()
        print("Resultado da medicao: ")
        for state, freq in sorted(counts.items(), reverse=True):
            print(f"State: |{freq}")



def main() -> None:
    print("Rodando")
    experiment =  QuantumExperiment(num_qubits= 1)
    result = experiment.run(shots=100)
    experiment.show_counts(result)



if __name__ == "__main__":
    main()
