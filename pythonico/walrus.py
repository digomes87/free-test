import time

def sum_values_at_20(values):
    time.sleep(1)
    result = 0
    for value in values:
        if value > 20:
            result += value
            
    return result


values = [10, 30 ,45, 6,12,23]

init = time.time()

if (s:=sum_values_at_20(values)) > 50:
    result = s
    print(result)


end = time.time()

print(end -init)
