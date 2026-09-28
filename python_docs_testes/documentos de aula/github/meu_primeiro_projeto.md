# Meu Primeiro Projeto no GitHub

> **Objetivo:** criar um projeto que lê uma pequena tabela de notas, salvar os arquivos no computador e publicá-los no GitHub.

---

## Pré-requisitos

Antes de começar, você precisa ter:

- Uma conta no [GitHub](https://github.com)
- O Git instalado no computador

Para verificar a instalação, abra o Terminal e execute:

```bash
git --version
```

Se aparecer um número de versão, o Git está disponível.

---

## Estrutura do projeto

Ao final da atividade, sua pasta terá esta estrutura:

```
meu_primeiro_projeto/
├── README.md       ← texto que explica o projeto
├── dados.csv       ← tabela de dados
└── analisar.py     ← código Python que lê a tabela
```

### Conteúdo dos arquivos

**`README.md`**
```markdown
# Meu primeiro projeto

Este projeto lê um arquivo CSV e mostra o nome e a nota de cada aluno.
```

**`dados.csv`**
```csv
nome,nota
Ana,8
Bruno,7
Carla,9
```

**`analisar.py`**
```python
import csv

with open("dados.csv", encoding="utf-8") as arquivo:
    dados = csv.DictReader(arquivo)
    for aluno in dados:
        print(aluno["nome"], aluno["nota"])
```

Para testar, abra o Terminal dentro da pasta do projeto e execute:

```bash
python analisar.py
# Em alguns computadores: python3 analisar.py
```

Resultado esperado:
```
Ana 8
Bruno 7
Carla 9
```

---

## Caminho 1 — Criar primeiro no computador

### Passo 1 — Criar a pasta e os arquivos

No computador, crie uma pasta chamada `meu_primeiro_projeto` (por exemplo, dentro de `Documentos`). Abra-a no VS Code e crie os três arquivos com o conteúdo descrito acima.

Salve os três arquivos e teste com `python analisar.py` para confirmar que está funcionando.

---

### Passo 2 — Inicializar o Git na pasta

No Terminal, confirme que você está na pasta certa:

```bash
pwd
# O caminho deve terminar em meu_primeiro_projeto
```

Inicie o Git:

```bash
git init
```

Defina a branch principal como `main`:

```bash
git branch -M main
```

Confira os arquivos detectados pelo Git:

```bash
git status
```

Os arquivos devem aparecer como **untracked files** — existem, mas ainda não foram incluídos em nenhum commit.

---

### Passo 3 — Criar o primeiro commit

Selecione todos os arquivos da pasta:

```bash
git add .
```

Confira a seleção:

```bash
git status
```

Registre a primeira versão do projeto:

```bash
git commit -m "Cria projeto de análise de notas"
```

> Até aqui, o projeto e o histórico estão **apenas no seu computador**.

---

### Passo 4 — Criar o repositório no GitHub

1. Acesse [github.com/new](https://github.com/new)
2. Em **Repository name**, escreva `meu_primeiro_projeto`
3. Escolha **Public** ou **Private** conforme a orientação da aula
4. **Não marque** as opções para adicionar README, .gitignore ou licença — já começamos o projeto no computador
5. Clique em **Create repository**

Na página seguinte, copie o endereço HTTPS do repositório:

```
https://github.com/SEU_USUARIO/meu_primeiro_projeto.git
```

---

### Passo 5 — Conectar o computador ao GitHub

Volte ao Terminal (ainda dentro da pasta `meu_primeiro_projeto`). Substitua `SEU_USUARIO` pelo seu usuário do GitHub:

```bash
git remote add origin https://github.com/SEU_USUARIO/meu_primeiro_projeto.git
```

> `origin` é o apelido que o Git usa para o endereço do projeto no GitHub.

Confirme se o endereço ficou correto:

```bash
git remote -v
```

Envie o commit para o GitHub:

```bash
git push -u origin main
```

Abra a página do repositório no GitHub e atualize o navegador. Os arquivos `README.md`, `dados.csv` e `analisar.py` devem aparecer lá. ✅

> ⚠️ **Atenção:** no Terminal, cole a URL pura começando em `https://`. Não use formato Markdown como `[https://...](https://...)`.

---

## Caminho 2 — Criar primeiro no GitHub

Neste caminho, o GitHub cria o início do projeto e depois trazemos uma cópia para o computador.

### Passo 1 — Criar o repositório no GitHub

1. Acesse [github.com/new](https://github.com/new)
2. Em **Repository name**, escreva `meu_primeiro_projeto`
3. Escolha **Public** ou **Private**
4. Marque a opção **Add a README file**
5. Clique em **Create repository**

O GitHub já terá criado o primeiro arquivo e o primeiro commit.

---

### Passo 2 — Copiar o repositório para o computador

Na página do repositório, clique no botão verde **Code** e copie a URL da opção **HTTPS**:

```
https://github.com/SEU_USUARIO/meu_primeiro_projeto.git
```

Abra o Terminal e navegue até a pasta onde quer guardar seus projetos (exemplo no Mac):

```bash
cd ~/Documents
```

Faça a cópia local:

```bash
git clone https://github.com/SEU_USUARIO/meu_primeiro_projeto.git
```

Entre na pasta clonada:

```bash
cd meu_primeiro_projeto
```

```bash
git status
```

> 💡 Neste caminho **não usamos `git init`** — o `clone` já trouxe o repositório e a conexão com o GitHub.

---

### Passo 3 — Criar os arquivos do exercício

Abra a pasta no VS Code. Ela já contém o `README.md`. Crie o `dados.csv` e o `analisar.py` com o conteúdo descrito no início deste documento.

Salve e teste:

```bash
python analisar.py
# Se necessário: python3 analisar.py
```

---

### Passo 4 — Registrar e enviar as mudanças

Os arquivos novos estão no computador, mas ainda não aparecem no GitHub. Veja o que mudou:

```bash
git status
```

Selecione, confira, registre e envie:

```bash
git add .
git status
git commit -m "Adiciona dados e script de análise"
git push
```

Atualize a página do GitHub. Os dois arquivos novos devem aparecer. ✅

---

## Resumo dos comandos

| Comando | O que faz |
|---|---|
| `git init` | Inicia o Git em uma pasta |
| `git status` | Mostra o estado atual dos arquivos |
| `git add .` | Seleciona todos os arquivos para o próximo commit |
| `git commit -m "mensagem"` | Registra uma versão do projeto |
| `git remote add origin <url>` | Conecta a pasta ao repositório no GitHub |
| `git push -u origin main` | Envia os commits para o GitHub (primeira vez) |
| `git push` | Envia os commits para o GitHub (próximas vezes) |
| `git clone <url>` | Copia um repositório do GitHub para o computador |
