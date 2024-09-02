class NumeroComplejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __add__(self, otro):
        return NumeroComplejo(self.real + otro.real, self.imaginario + otro.imaginario)

    def __sub__(self, otro):
        return NumeroComplejo(self.real - otro.real, self.imaginario - otro.imaginario)

    def __mul__(self, otro):
        real = self.real * otro.real - self.imaginario * otro.imaginario
        imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return NumeroComplejo(real, imaginario)

    def __truediv__(self, otro):
        denominador = otro.real**2 + otro.imaginario**2
        real = (self.real * otro.real + self.imaginario * otro.imaginario) / denominador
        imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / denominador
        return NumeroComplejo(real, imaginario)

    def __str__(self):
        return f"({self.real} {'+' if self.imaginario >= 0 else '-'} {abs(self.imaginario)}i)"

# Ejemplo de uso
a = NumeroComplejo(3, 2)
b = NumeroComplejo(1, 7)

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
