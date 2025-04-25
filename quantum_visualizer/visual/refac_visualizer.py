import time
import math
import os
from dataclasses import dataclass



@dataclass
class QubitState:
    alpha: float
    beta: float


    @property
    def probabilities(self):
        return self.alpha ** 2, self.beta ** 2


class QuantumSuperpositionVisualizer:
    
    def __init__(self, refresh_rate: float = 0.1, pause_interval: float = 3.1):
        self.refresh_rate = refresh_rate
        self.pause_interval = pause_interval
        self.last_pause_time = time.time()


    def calculate_terminal(self, t: float)-> QubitState:
        alpha = math.cos(t)
        beta = math.sin(t)
        return QubitState(alpha, beta)
    
    
    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def display_state(self, state: QubitState):
        alpha, beta = state.alpha, state.beta
        print(f"|ψ⟩ = {alpha:.2f}|0⟩ + {beta:.2f}|1⟩")


    def display_probabilities(self, state: QubitState):
        prob_0, prob_1 = state.probabilities
        print("\nMedição teórica:")
        print(f"- Prob(|0⟩) = {prob_0:.2f}")
        print(f"- Prob(|1⟩) = {prob_1:.2f}")
        print("\nContinuando em 2 segundos...")
        time.sleep(2)
    
    def run(self):
        t = 0.0
        while True:
            state = self.calculate_terminal(t)
            self.clear_terminal()
            self.display_state(state)

            now = time.time()
            if now - self.last_pause_time >= self.pause_interval:
                self.display_probabilities(state)
                self.last_pause_time = now

            t += self.refresh_rate
            time.sleep(self.refresh_rate)






