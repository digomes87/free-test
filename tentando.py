"""
Em python todas as excecoes herdam da classe base
BaseException, entao todos esse casos estao abaixo dessa classe
"""

from typing import Callable, List


class ExceptionDemo:
    """
    Class responsable for agreggation exmeplos of exceptions in python
    just for education
    """

    @staticmethod
    def arithmetic_error():
        raise ArithmeticError("Erro aritmético genericos")

    @staticmethod
    def floating_point_error():
        raise FloatingPointError("Erro de ponto flutuante simulado")

    @staticmethod
    def overflow_error():
        import math

        return math.exp(1000)

    @staticmethod
    def zero_division_error():
        return 1 / 0

    @staticmethod
    def assertion_error():
        assert False, "Falha na asserção"

    @staticmethod
    def attribute_error():
        return [].nonexistent_method()

    @staticmethod
    def buffer_error():
        import array
        import ctypes

        a = array.array("d", [1.0, 2.0, 3.0])
        m = memoryview(a)

        try:
            a.append(4.0)
        finally:
            m.release()

    @staticmethod
    def eof_error():
        raise EOFError("Fim de arquivo inesperado")

    @staticmethod
    def import_error():
        from math import non_existing

    @staticmethod
    def module_not_found_error():
        import modulo_que_nao_exist

    @staticmethod
    def index_error():
        return [1, 2, 3][99]

    @staticmethod
    def key_error():
        return {"a": 1}["b"]

    @staticmethod
    def lookup_error():
        raise LookupError("Erro de busca generica")

    @staticmethod
    def memory_error():
        raise MemoryError("memoria insuficiente")

    @staticmethod
    def name_error():
        return variavel_nao_definida

    @staticmethod
    def unbound_local_error():
        def func():
            print(x)
            x = 5

        func()


def run_safe(func: Callable):
    try:
        func()
    except Exception as e:
        print(f"[{func.__name__}] {type(e).__name__}: {e}")


def run_all():
    demo_methods: List[Callable] = [
        ExceptionDemo.arithmetic_error,
        ExceptionDemo.floating_point_error,
        ExceptionDemo.overflow_error,
        ExceptionDemo.zero_division_error,
        ExceptionDemo.assertion_error,
        ExceptionDemo.attribute_error,
        ExceptionDemo.buffer_error,
        ExceptionDemo.eof_error,
        ExceptionDemo.import_error,
        ExceptionDemo.module_not_found_error,
        ExceptionDemo.index_error,
        ExceptionDemo.key_error,
        ExceptionDemo.lookup_error,
        ExceptionDemo.memory_error,
        ExceptionDemo.name_error,
        ExceptionDemo.unbound_local_error,
    ]

    for method in demo_methods:
        run_safe(method)


if __name__ == "__main__":
    run_all()
