class Livro:
    # Construtor da classe Livro
    def __init__(self, titulo: str, autor: str, ano_publicacao: int, status: bool = True):
        self._titulo = titulo  # Atributo privado
        self._autor = autor    # Atributo privado
        self._ano_publicacao = ano_publicacao  # Atributo privado
        self._status = status  # Status inicial do livro, disponível por padrão
        
    def emprestar(self):
        if self._status:  # Verifica se o livro está disponível
            self._status = False  # Altera o status para emprestado
        else:
            raise Exception("Livro não está disponível para empréstimo.")  # Lança exceção se não disponível

    def devolver(self):
        self._status = True  # Altera o status para disponível

class Usuario:
    # Construtor da classe Usuario
    def __init__(self, nome: str, cpf: str, livros_emprestados: list[Livro] = None):
        self._nome = nome  # Atributo privado
        self._cpf = cpf  # Atributo privado
        self._livros_emprestados = livros_emprestados if livros_emprestados is not None else []  # Inicializa como lista vazia se não fornecido
        
    def solicitar_emprestimo(self, livro: Livro):
        if len(self._livros_emprestados) < 3:  # Limite de 3 livros emprestados
            livro.emprestar()  # Chama o método do livro
            self._livros_emprestados.append(livro)  # Adiciona o livro à lista de livros emprestados
        else:
            raise Exception("Limite de livros emprestados atingido.")  # Lança exceção se o limite for atingido

    def devolver_livro(self, livro: Livro):
        if livro in self._livros_emprestados:  # Verifica se o livro está na lista de livros emprestados
            livro.devolver()  # Chama o método de devolução do livro
            self._livros_emprestados.remove(livro)  # Remove o livro da lista
        else:
            raise Exception("Este livro não está emprestado a você.")  # Lança exceção se o livro não estiver na lista

class Biblioteca:
    # Construtor da classe Biblioteca
    def __init__(self, livros: list[Livro] = None, usuarios: list[Usuario] = None):
        self._livros = livros if livros is not None else []  # Inicializa a lista de livros
        self._usuarios = usuarios if usuarios is not None else []  # Inicializa a lista de usuários
        
    def adicionar_livro(self, livro: Livro):
        self._livros.append(livro)  # Adiciona o livro à lista de livros
    
    def remover_livro(self, livro: Livro):
        self._livros.remove(livro)  # Remove o livro da lista de livros
    
    def registrar_usuario(self, usuario: Usuario):
        self._usuarios.append(usuario)  # Adiciona o usuário à lista de usuários
    
    def emprestar_livro(self, usuario: Usuario, livro: Livro):
        usuario.solicitar_emprestimo(livro)  # Chama o método do usuário
    
    def receber_devolucao(self, usuario: Usuario, livro: Livro):
        usuario.devolver_livro(livro)  # Chama o método do usuário para devolução

        
livro1 = Livro(titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien", ano_publicacao=1954)
livro2 = Livro(titulo="1984", autor="George Orwell", ano_publicacao=1949)

usuario1 = Usuario(nome="João da Silva", cpf="123.456.789-00")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

try:
    usuario1.solicitar_emprestimo(livro1)  # O usuário tenta emprestar "O Senhor dos Anéis"
    print(f"{usuario1._nome} emprestou '{livro1._titulo}' com sucesso!")
except Exception as e:
    print(e)


try:
    usuario1.devolver_livro(livro1)  # O usuário tenta devolver "O Senhor dos Anéis"
    print(f"{usuario1._nome} devolveu '{livro1._titulo}' com sucesso!")
except Exception as e:
    print(e)
    
usuario2 = Usuario(nome="Maria Oliveira", cpf="987.654.321-00")
biblioteca.registrar_usuario(usuario2)


try:
    usuario2.solicitar_emprestimo(livro2)  # Maria tenta emprestar "1984"
    print(f"{usuario2._nome} emprestou '{livro2._titulo}' com sucesso!")
except Exception as e:
    print(e)