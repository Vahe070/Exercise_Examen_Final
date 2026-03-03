def division(a, b):
    if b == 0:
        raise ZeroDivisionError("division par zero")
    return a / b

def puissance(a, n):
    if n < 0:
        raise ValueError("n negatif")
    return a ** n

def moyenne(notes):
    if len(notes) == 0:
        raise ValueError("liste vide")
    total = 0
    for note in notes:
        total = total + note
    return total / len(notes)