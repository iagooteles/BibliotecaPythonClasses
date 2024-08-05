from membro import Membro
from livro import Livro

class Biblioteca:
    def __init__(self) -> None:        
        self.membros = []
        self.livros = []

    def registrar_livro(self):
        titulo = input('Qual o nome do Livro que desejas registrar? \n')
        autor = input('Qual o nome do Autor do livro que desejas registrar? \n')
        novo_livro = Livro(titulo, autor, len(self.livros), 'disponivel')
        self.livros.append(novo_livro)
        print('_____________________________________________')

    def listar_todos_livros(self):
        pass

    def listar_livros_disponiveis(self):
        if len(self.livros) == 0:
            print('Não há livros disponíveis')
            return
        
        print('Os livros disponíveis são: ')
        for i, livro in enumerate(self.livros):
            if livro.status_de_emprestimo == 'disponivel':
                print(f'{i + 1} - {livro.titulo} - Autor: {livro.autor}')
        print('_____________________________________________')

    def listar_livros_alugados(self):
        print('Os livros alugados são: ')
        for i, livro in enumerate(self.livros):
            if livro.status_de_emprestimo == 'alugado':
                print(f'{i + 1} - {livro.titulo} - Autor: {livro.autor} - Foi alugado por: {livro.alugado_por}')
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

    def registrar_livro_pelo_sistema(self, titulo, autor, id, status_de_emprestimo, alugado_por):
        novo_livro = Livro(titulo, autor, id, status_de_emprestimo, alugado_por)
        self.livros.append(novo_livro)

    def registrar_membro_pelo_sistema(self, nome, id):
        novo_membro = Membro(nome, id)
        self.membros.append(novo_membro)

    def alugar_livro(self, nome_membro, nome_livro):
        membro = next((membro for membro in self.membros if membro.nome.lower() == nome_membro.lower()), None)
        livro = next((livro for livro in self.livros if livro.titulo.lower() == nome_livro.lower()), None)
        
        if not membro:
            print('Membro não encontrado!')
            return
        
        if not livro:
            print('Livro não encontrado!')
            return
        
        if livro.status_de_emprestimo != 'disponivel':
            print(f'O livro "{livro.titulo}" não está disponível para aluguel.')
            return

        livro.alugado_por = membro.nome
        livro.status_de_emprestimo = 'alugado'
        membro.adicionar_livro_ao_historico(livro)
        print(f'O livro "{livro.titulo}" foi alugado por {membro.nome}.')
        print('_____________________________________________')

    def listar_historico_do_membro(self, nome_membro):
        membro = next((membro for membro in self.membros if membro.nome.lower() == nome_membro.lower()), None)

        if not membro:
            print('Membro não encontrado!')
            return

        membro.listar_historico()

        print('_____________________________________________')

    def devolver_livro(self, nome_membro, nome_livro):
        membro = next((membro for membro in self.membros if membro.nome.lower() == nome_membro.lower()), None)
        livro = next((livro for livro in self.livros if livro.titulo.lower() == nome_livro.lower()), None)

        if not membro:
            print('Membro não encontrado!')
            return
        
        if not livro:
            print('Livro não encontrado!')
            return
        
        if livro.status_de_emprestimo != 'alugado':
            print(f'O livro "{livro.titulo}" encontra-se disponível.')
            return
        
        livro.alugado_por = ''
        livro.status_de_emprestimo = 'disponivel'
        print(f'O livro "{livro.titulo}" foi devolvido por {membro.nome}.')
        
        print('_____________________________________________')
