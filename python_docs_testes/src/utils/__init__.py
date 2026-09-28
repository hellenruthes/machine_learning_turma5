"""
Módulo utils
============

Utilitários gerais: manipulação de strings, listas e validações.
"""

from .strings import capitalizar, contar_palavras, inverter_string
from .listas import remover_duplicatas, achatar_lista, filtrar_pares
from .validacoes import validar_email, validar_cpf

__all__ = [
    "capitalizar",
    "contar_palavras",
    "inverter_string",
    "remover_duplicatas",
    "achatar_lista",
    "filtrar_pares",
    "validar_email",
    "validar_cpf",
]
