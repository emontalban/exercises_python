from functools import reduce

# Haz una funcion que realice el elevado a una potencian manualmente
# 

def manual_exponent_one(number, exponent):
    result = 1
    for i in range(exponent):
        result *= number

    return result

print(manual_exponent_one(5,2))

# Otra solucion con While

def manual_exponent_two(num, exp):
    counter = exp - 1
    total = num

    while counter > 0:
        total *= num
        counter -= 1

    return total

print(manual_exponent_two(2, 3))




# La función reduce() en Python, perteneciente al módulo functools, 
# aplica de forma acumulativa una función de dos argumentos a los elementos
# de un iterable (izquierda a derecha), reduciéndolos a un único valor final

def manual_exponent_three(number, exponent):

    return reduce(lambda result, element: result * number, range(exponent), 1)

print(manual_exponent_three(6,2))

# Otra solucion 

def manual_exponent_four(number, exponent):
    computed_list = [number] * exponent

    return reduce(lambda total, element : total * element,computed_list)

print(manual_exponent_four(7,3))


