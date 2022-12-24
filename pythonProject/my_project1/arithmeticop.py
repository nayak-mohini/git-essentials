# Debugging a simple Program

def addition(a,b):
    result = a + b
    return result


def multiplication(a,b):
    result = a * b
    return result


def division(a,b):
    result = a / b
    return result


print("result is:",division(multiplication(addition(5,2),10),2))