# Sistema de Gerenciamento de Biblioteca

Este projeto é um sistema de gerenciamento de biblioteca em Python que permite o controle de livros e usuários. Os principais recursos incluem empréstimo e devolução de livros, registro de usuários e gerenciamento do acervo da biblioteca.

## Estrutura do Projeto

O sistema é composto pelas seguintes classes:

- **Livro**: Representa um livro na biblioteca.
- **Usuario**: Representa um usuário que pode emprestar livros.
- **Biblioteca**: Gerencia os livros e usuários, permitindo operações de empréstimo e devolução.

## Classes

### 1. Livro

- **Atributos**:
  - `titulo` (str): Título do livro.
  - `autor` (str): Autor do livro.
  - `ano_publicacao` (int): Ano de publicação do livro.
  - `status` (bool): Indica se o livro está disponível (True) ou emprestado (False).

- **Métodos**:
  - `emprestar()`: Altera o status do livro para emprestado.
  - `devolver()`: Altera o status do livro para disponível.

### 2. Usuario

- **Atributos**:
  - `nome` (str): Nome do usuário.
  - `cpf` (str): CPF do usuário.
  - `livros_emprestados` (list[Livro]): Lista de livros que o usuário está emprestado.

- **Métodos**:
  - `solicitar_emprestimo(livro: Livro)`: Solicita o empréstimo de um livro.
  - `devolver_livro(livro: Livro)`: Devolve um livro emprestado.

### 3. Biblioteca

- **Atributos**:
  - `livros` (list[Livro]): Lista de livros na biblioteca.
  - `usuarios` (list[Usuario]): Lista de usuários registrados.

- **Métodos**:
  - `adicionar_livro(livro: Livro)`: Adiciona um livro à biblioteca.
  - `remover_livro(livro: Livro)`: Remove um livro da biblioteca.
  - `registrar_usuario(usuario: Usuario)`: Registra um novo usuário na biblioteca.
  - `emprestar_livro(usuario: Usuario, livro: Livro)`: Permite que um usuário empreste um livro.
  - `receber_devolucao(usuario: Usuario, livro: Livro)`: Recebe a devolução de um livro.

## Uso

Para utilizar o sistema, siga os passos abaixo:

1. Crie instâncias de `Livro` e `Usuario`.
2. Crie uma instância de `Biblioteca`.
3. Adicione livros à biblioteca.
4. Registre usuários.
5. Realize empréstimos e devoluções de livros.

### Exemplo de Uso

```python
# Criar instâncias de livros
livro1 = Livro(titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien", ano_publicacao=1954)

# Criar um usuário
usuario1 = Usuario(nome="João da Silva", cpf="123.456.789-00")

# Criar a biblioteca e adicionar livros
biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)

# Solicitar empréstimo de um livro
usuario1.solicitar_emprestimo(livro1)

# Devolver um livro
usuario1.devolver_livro(livro1)
```

### Clonando o Repositório

Para clonar este repositório em sua máquina local, utilize o seguinte comando:

```bash
git clone https://github.com/NickesMelo/sistema_gestao_biblioteca