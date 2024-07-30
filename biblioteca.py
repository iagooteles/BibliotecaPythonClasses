from membro import Membro
from livro import Livro

class Biblioteca:
    def __init__(self) -> None:
        
        self.membros = []
        self.livros = []
        # self.livros_disponiveis = []

    def registrar_livro(self):
        titulo = input('Qual o nome do Livro que desejas registrar? \n')
        autor = input('Qual o nome do Autor do livro que desejas registrar? \n')
        novo_livro = Livro(titulo, autor, len(self.livros), 'disponivel')
        self.livros.append(novo_livro)
        print('_____________________________________________')

    def listar_livros_disponiveis(self):
        if len(self.livros) == 0:
            print('Não há livros disponíveis')
            return
        
        print('Os livros disponíveis são: ')
        for i, livro in enumerate(self.livros):
            if livro.status_de_emprestimo == 'disponivel':
                print(f'{i + 1} - {livro.titulo} - Autor: {livro.autor}')
        print('_____________________________________________')

    def registrar_membro(self):
        nome = input('Qual o nome do membro que desejas registrar? \n')
        novo_membro = Membro(nome, len(self.membros))
        self.membros.append(novo_membro)
        print('_____________________________________________')

    def listar_membros(self):
        for membro in self.membros:
            print(f'Nome: {membro.nome} - ID: {membro.id}')
        print('_____________________________________________')

    def registrar_livro_pelo_sistema(self, titulo, autor, id, status_de_emprestimo):
        novo_livro = Livro(titulo, autor, id, status_de_emprestimo)
        self.livros.append(novo_livro)