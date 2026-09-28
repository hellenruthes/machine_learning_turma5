"""
Módulo calculadora
==================

Fornece operações aritméticas básicas e avançadas com
tratamento de erros e type hints.
"""

from .operacoes import somar, subtrair, multiplicar, dividir
from .avancado import potencia, raiz_quadrada, media

__all__ = [
    "somar",
    "subtrair",
    "multiplicar",
    "dividir",
    "potencia",
    "raiz_quadrada",
    "media",
]
