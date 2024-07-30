class Membro:
    def __init__(self, nome, id) -> None:
        self.nome = nome
        self.id = id

        self.idCount = 0
        self.historico = []

    def alugar_livro(self, livro):
        try:
            self.historico.append(livro)
            print(f'Livro: {livro}, alugado com sucesso!')
        except:
            print(f'Não foi possível alugar o livro: {livro}')

    def listar_historico(self):
        for i, livro in enumerate(self.historico):
            print(f'{i+1} - {livro}')
