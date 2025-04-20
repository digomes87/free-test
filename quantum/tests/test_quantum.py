from quantum_experiment import QuantumExperiment


def test_quantum_experiment_counts_sum_correctly():
    experiment = QuantumExperiment(num_qubits=1)
    result = experiment.run(shots=100)
    counts = result.get_counts()
    
    assert isinstance(counts, dict)
    assert sum(counts.values()) == 100
    for key in counts.keys():
        assert key in {"0", "1"}, f"Resultado inesperado: {key}"

