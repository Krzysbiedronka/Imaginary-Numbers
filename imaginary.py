from math import sqrt


class ImaginaryNumber:

    """
    Class ImaginaryNumber: You can add, sub, multiply, divide imaginary nums
    Also you can calculate modulus and the conjugate
    :real, imaginary: real and imaginary parts of the imaginary number
    :type real, imaginary: ints (can be positive, negative, eqaul to 0)
    """

    def __init__(self, real=0, imaginary=0) -> None:
        self.set_real(real)
        self.set_imaginary(imaginary)

    def get_real(self):
        return self._real

    def get_imaginary(self):
        return self._imaginary

    def set_real(self, new_real):
        if type(new_real) == float:
            self._real = round(new_real, 2)
        else:
            self._real = int(new_real)

    def set_imaginary(self, new_imaginary):
        if type(new_imaginary) == float:
            self._imaginary = round(new_imaginary, 2)
        else:
            self._imaginary = int(new_imaginary)

    def __str__(self) -> str:
        if self._imaginary == 0:
            return str(self._real)
        if self._imaginary == 1:
            return f'{self._real} + i'
        if self._imaginary < 0:
            return f'{self._real} - {abs(self._imaginary)}i'
        return f'{self._real} + {self._imaginary}i'

    def __add__(self, other: "ImaginaryNumber") -> "ImaginaryNumber":
        new_real = self._real + other._real
        new_imaginary = self._imaginary + other._imaginary
        return ImaginaryNumber(new_real, new_imaginary)

    def __sub__(self, other: "ImaginaryNumber") -> "ImaginaryNumber":
        new_real = self._real - other._real
        new_imaginary = self._imaginary - other._imaginary
        return ImaginaryNumber(new_real, new_imaginary)

    def __mul__(self, other: "ImaginaryNumber") -> "ImaginaryNumber":
        a = self._real
        b = self._imaginary
        c = other._real
        d = other._imaginary
        new_real = a * c - b * d
        new_imaginary = a * d + b * c
        return ImaginaryNumber(new_real, new_imaginary)

    def modulus(self) -> float:
        return sqrt(self._real**2 + self._imaginary**2)

    def conjugate(self) -> "ImaginaryNumber":
        return ImaginaryNumber(self._real, -1 * self._imaginary)

    def __truediv__(self, other: "ImaginaryNumber") -> "ImaginaryNumber":
        if str(other) == '0':
            raise ZeroDivisionError('You cannot divide by 0.')
        numerator = self * other.conjugate()
        denominator = other * other.conjugate()
        if numerator._real % denominator._real == 0:
            new_real = numerator._real // denominator._real
        else:
            new_real = numerator._real / denominator._real
        if numerator._imaginary % denominator._real == 0:
            new_imaginary = numerator._imaginary // denominator._real
        else:
            new_imaginary = numerator._imaginary / denominator._real
        return ImaginaryNumber(new_real, new_imaginary)
