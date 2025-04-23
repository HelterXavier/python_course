import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()  # Inicia o cronômetro
        result = func(*args, **kwargs)  # Executa a função original
        end = time.time()  # Para o cronômetro

        print(f'Time Execution: {end - start:.4f} seconds')
        return result
    return wrapper


@measure_time  # Decorador que mede o tempo de execução
def process_data():
    time.sleep(5)  # Simula um processamento demorado # 2 segundos
    return "Data processed!"


print(process_data())  # Chama a função decorada
# Saída:
# Time Execution: 2.0001 seconds
# Data processed!
