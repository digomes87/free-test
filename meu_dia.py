from typing import List, Callable


def acordar():
    print("Acordei vamos começar o dia")


def escovar_dentes():
    print("Esconvando os dentes")


def tomar_cafe():
    print("Tomando cafe")


def ir_pra_escola():
    print("Indo pra escola")


def estudar():
    print("Estudando")


def brincar():
    print("Brincando")


def jantar():
    print("Brincando")


def dormir():
    print("Dormindo")


def dia_de_uma_crianca(tarefas: List[Callable]):
    print("Começando o dia 👌\n")
    for tarefa in tarefas:
        tarefa()

    print("Fim do Dia")


meu_dia = [
    acordar,
    escovar_dentes,
    tomar_cafe,
    ir_pra_escola,
    estudar,
    brincar,
    jantar,
    dormir,
]


if __name__ == "__main__":
    dia_de_uma_crianca(meu_dia)
