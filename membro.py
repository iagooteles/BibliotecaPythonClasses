class Membro:
    def __init__(self, nome, id) -> None:
        self.nome = nome
        self.id = id

        self.idCount = 0
        self.historico = []

    def adicionar_livro_ao_historico(self, livro):
        try:
            self.historico.append(livro)
        except:
            print(f'Não foi possível adicionar o livro: {livro} ao histórico.')

    def listar_historico(self):
        if len(self.historico) == 0:
            print('Este membro não alugou livros.')
            return
        for i, livro in enumerate(self.historico):
            print(f'{i+1} - {livro.titulo}')
