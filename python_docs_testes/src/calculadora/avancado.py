"""
Operações matemáticas avançadas.

Complementa o módulo de operações básicas com funções como
potenciação, raiz quadrada e média aritmética.
"""

import math
from typing import List


def potencia(base: float, expoente: float) -> float:
    """Calcula a potência de um número.

    Args:
        base: A base da potenciação.
        expoente: O expoente da potenciação.

    Returns:
        O resultado de `base` elevado a `expoente`.

    Examples:
        >>> potencia(2, 10)
        1024.0
        >>> potencia(5, 0)
        1.0
        >>> potencia(9, 0.5)
        3.0
    """
    return math.pow(base, expoente)


def raiz_quadrada(numero: float) -> float:
    """Calcula a raiz quadrada de um número não-negativo.

    Args:
        numero: Valor do qual se deseja a raiz quadrada.
            Deve ser maior ou igual a zero.

    Returns:
        A raiz quadrada de `numero`.

    Raises:
        ValueError: Se `numero` for negativo.

    Examples:
        >>> raiz_quadrada(9)
        3.0
        >>> raiz_quadrada(2)
        1.4142135623730951
        >>> raiz_quadrada(-1)
        Traceback (most recent call last):
            ...
        ValueError: Não é possível calcular a raiz quadrada de um número negativo.
    """
    if numero < 0:
        raise ValueError(
            "Não é possível calcular a raiz quadrada de um número negativo."
        )
    return math.sqrt(numero)


def media(valores: List[float]) -> float:
    """Calcula a média aritmética de uma lista de números.

    Args:
        valores: Lista com os valores numéricos. Não pode ser vazia.

    Returns:
        A média aritmética dos valores fornecidos.

    Raises:
        ValueError: Se a lista `valores` estiver vazia.

    Examples:
        >>> media([1, 2, 3, 4, 5])
        3.0
        >>> media([10, 20])
        15.0
        >>> media([])
        Traceback (most recent call last):
            ...
        ValueError: A lista de valores não pode estar vazia.
    """
    if not valores:
        raise ValueError("A lista de valores não pode estar vazia.")
    return sum(valores) / len(valores)
