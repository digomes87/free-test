import time
from typing import List, Callable


print("Aqui")

def esperar(segundos=2.5):
    time.sleep(segundos)


def acordar():
    print("⏰ Acordar! Vamos Começar o dia !")
    esperar()


def escovar_dentes():
    print("🪥 Escovando os dentes")
    esperar()

def tomar_cafe():
    print("☕️ Comendo um Cereal Com um bom Cafe")
    esperar()


def dia_de_uma_crianca(tarefas: List[Callable]):
    print("🌞 Bom dia Vamos começar a aventura\n")
    esperar()
    for tarefa in tarefas:
        tarefa()

    print("\n🍌 Dia concluido com Sucesso")


meu_dia = [
    acordar,
    escovar_dentes,
    tomar_cafe,
]

print("Depois")

if __name__ == "__main__":
    dia_de_uma_crianca(meu_dia)
