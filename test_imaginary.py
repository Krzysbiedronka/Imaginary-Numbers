from imaginary import ImaginaryNumber
from pytest import approx, raises


def test_create_imaginary_number():
    imaginary = ImaginaryNumber(3, 4)
    assert imaginary.get_real() == 3
    assert imaginary.get_imaginary() == 4
    assert str(imaginary) == '3 + 4i'


def test_create_imaginary_number_deafult():
    imaginary = ImaginaryNumber()
    assert imaginary.get_real() == 0
    assert imaginary.get_imaginary() == 0
    assert str(imaginary) == '0'


def test_create_imaginary_number_negative():
    imaginary = ImaginaryNumber(-3, -4)
    assert imaginary.get_real() == -3
    assert imaginary.get_imaginary() == -4
    assert str(imaginary) == '-3 - 4i'


def test_add_imaginary_numbers():
    imaginary1 = ImaginaryNumber(-3, -4)
    imaginary2 = ImaginaryNumber(5, 9)
    assert str(imaginary1 + imaginary2) == '2 + 5i'


def test_add_imaginary_numbers_to_0():
    imaginary1 = ImaginaryNumber(-3, 4)
    imaginary2 = ImaginaryNumber()
    assert str(imaginary1 + imaginary2) == '-3 + 4i'


def test_subtract_imaginary_numbers():
    imaginary1 = ImaginaryNumber(2, 8)
    imaginary2 = ImaginaryNumber(2, 8)
    assert str(imaginary1 - imaginary2) == '0'


def test_subtract_imaginary_numbers_from_0():
    imaginary1 = ImaginaryNumber()
    imaginary2 = ImaginaryNumber(-5, -5)
    assert str(imaginary1 - imaginary2) == '5 + 5i'


def test_multiply_imaginary_numbers():
    imaginary1 = ImaginaryNumber(2, 8)
    imaginary2 = ImaginaryNumber(9, -7)
    assert str(imaginary1 * imaginary2) == '74 + 58i'


def test_multiply_imaginary_numbers_by_0():
    imaginary1 = ImaginaryNumber(2, 8)
    imaginary2 = ImaginaryNumber(0)
    assert str(imaginary1 * imaginary2) == '0'


def test_multiply_imaginary_numbers_to_reduce_i():
    imaginary1 = ImaginaryNumber(2, 8)
    assert str(imaginary1 * imaginary1.conjugate()) == '68'


def test_modulus_typical():
    imaginary1 = ImaginaryNumber(2, 8)
    assert imaginary1.modulus() == approx(8.25, 0.1)


def test_modulus_deafult():
    imaginary1 = ImaginaryNumber()
    assert imaginary1.modulus() == 0


def test_modulus_negative():
    imaginary1 = ImaginaryNumber(-2, -4)
    assert imaginary1.modulus() == approx(4.47, 0.1)


def test_conjugate_typical():
    imaginary1 = ImaginaryNumber(-2, -4)
    assert str(imaginary1.conjugate()) == '-2 + 4i'


def test_conjugate_deafult():
    imaginary1 = ImaginaryNumber(0)
    assert str(imaginary1.conjugate()) == '0'


def test_divide_imaginary_number_by_0():
    imaginary1 = ImaginaryNumber(2, 8)
    imaginary2 = ImaginaryNumber(0)
    with raises(ZeroDivisionError):
        imaginary1 / imaginary2


def test_divide_divisible_imaginary_numbers():
    imaginary1 = ImaginaryNumber(1, 8)
    imaginary2 = ImaginaryNumber(2, 3)
    assert str(imaginary1 / imaginary2) == '2 + i'


def test_divide_0_by_imaginary_numbers():
    imaginary1 = ImaginaryNumber()
    imaginary2 = ImaginaryNumber(2, 3)
    assert str(imaginary1 / imaginary2) == '0'


def test_divide_not_divisible_imaginary_numbers():
    imaginary1 = ImaginaryNumber(2, -3)
    imaginary2 = ImaginaryNumber(5, 6)
    assert str(imaginary1 / imaginary2) == '-0.13 - 0.44i'
