# Python Docs & Testes 🐍

Repositório de referência para **documentação** e **testes em Python**, voltado para a Turma 5 de Machine Learning.

## Estrutura

```
python_docs_testes/
├── src/
│   ├── calculadora/      # Módulo de operações matemáticas
│   └── utils/            # Utilitários gerais
├── tests/                # Testes com pytest
├── docs/
│   └── exemplos/         # Exemplos de docstrings e boas práticas
├── requirements.txt
└── README.md
```

## Como usar

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Rodar os testes

```bash
pytest tests/ -v
```

### 3. Rodar com cobertura de código

```bash
pytest tests/ --cov=src --cov-report=term-missing
```

### 4. Gerar documentação HTML (Sphinx)

```bash
cd docs
make html
```

## Conteúdo

| Módulo | Descrição |
|---|---|
| `src/calculadora` | Operações aritméticas com docstrings completas |
| `src/utils` | Funções utilitárias (strings, listas, validações) |
| `tests/` | Testes unitários com pytest, fixtures e parametrize |
| `docs/exemplos/` | Guias de boas práticas de documentação |

## Padrões adotados

- **Docstrings**: estilo Google (recomendado para projetos ML)
- **Testes**: `pytest` com `pytest-cov` para cobertura
- **Type hints**: anotações de tipo em todas as funções
