# Este ejercicio consiste en crear una función llamada dynamic_reducer
# que recibe una lista de números y un operador como string ("+", "-", "*", "/").
# La función debe aplicar esa operación a todos los elementos de la lista
# utilizando reduce y la librería operator, y devolver el resultado final.

from functools import reduce
import operator

def dynamic_reducer(numbers, op):
    
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    return reduce(operations[op], numbers)


numbers = [1, 2, 3]
operators = ["+", "-", "*", "/"]
for op in operators:
    print(op, dynamic_reducer(numbers, op))


#otra solucion usando la funcion lambda

def flexible_counter(collection, op):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    return reduce((lambda total, element: operators[op](total, element)), collection)

print(flexible_counter([1, 2, 3], '+'))
print(flexible_counter([1, 2, 3], '-'))
print(flexible_counter([1, 2, 3], '*'))
print(flexible_counter([1, 2, 3], '/'))