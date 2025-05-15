import time


"""
Meu decorator, uma funcao que mostra o inicio
e fim da executacao que ira levar
"""
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result =  func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} levou {end_time - start_time} segundos para executar")
        return result
    return wrapper

@timer_decorator
def sum(a, b):
    time.sleep(1)
    return a + b


print(sum(5, 8))



"""
Decorator pode ser utilzado para criar logs,
Para construir alguma funcao personalizada,
Alterar algum comporatamento de algum metodo ou funcao

"""
