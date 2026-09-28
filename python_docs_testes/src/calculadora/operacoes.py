"""
Operações aritméticas básicas.

Este módulo contém as quatro operações fundamentais da matemática
com tratamento de erros e anotações de tipo.
"""


def somar(a: float, b: float) -> float:
    """Retorna a soma de dois números.

    Args:
        a: Primeiro operando.
        b: Segundo operando.

    Returns:
        A soma de `a` e `b`.

    Examples:
        >>> somar(2, 3)
        5
        >>> somar(-1, 1)
        0
        >>> somar(0.5, 0.5)
        1.0
    """
    return a + b


def subtrair(a: float, b: float) -> float:
    """Retorna a subtração de dois números.

    Args:
        a: Minuendo.
        b: Subtraendo.

    Returns:
        A diferença entre `a` e `b`.

    Examples:
        >>> subtrair(10, 4)
        6
        >>> subtrair(0, 5)
        -5
    """
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Retorna o produto de dois números.

    Args:
        a: Primeiro fator.
        b: Segundo fator.

    Returns:
        O produto de `a` por `b`.

    Examples:
        >>> multiplicar(3, 4)
        12
        >>> multiplicar(-2, 5)
        -10
        >>> multiplicar(0, 100)
        0
    """
    return a * b


def dividir(a: float, b: float) -> float:
    """Retorna a divisão de dois números.

    Args:
        a: Dividendo.
        b: Divisor. Não pode ser zero.

    Returns:
        O quociente de `a` por `b`.

    Raises:
        ValueError: Se `b` for igual a zero.

    Examples:
        >>> dividir(10, 2)
        5.0
        >>> dividir(7, 2)
        3.5
        >>> dividir(5, 0)
        Traceback (most recent call last):
            ...
        ValueError: Divisão por zero não é permitida.
    """
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b
