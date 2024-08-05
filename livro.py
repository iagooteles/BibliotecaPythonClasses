class Livro:
    def __init__(self, titulo, autor, id, status_de_emprestimo, alugado_por) -> None:
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.status_de_emprestimo = status_de_emprestimo
        self.alugado_por = alugado_por
