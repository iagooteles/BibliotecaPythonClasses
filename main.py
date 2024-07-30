from livro import Livro
from membro import Membro
from biblioteca import Biblioteca

eragon = Livro('Eragon', 'Robert dafon', 1, 'disponivel')

iago = Membro('Iago', 1)

bib = Biblioteca()
bib.registrar_livro_pelo_sistema('O princípio', 'Matin lupp', 0, 'disponivel')
bib.registrar_livro_pelo_sistema('A Ascensão', 'Carla Diaz', 1, 'disponivel')
bib.registrar_livro_pelo_sistema('A Travessia', 'Rafael Monteiro', 2, 'disponivel')
bib.registrar_livro_pelo_sistema('Encontro', 'Ana Souza', 3, 'disponivel')
bib.registrar_livro_pelo_sistema('O Destino', 'Lucas Pereira', 4, 'disponivel')
bib.registrar_livro_pelo_sistema('Jornada', 'Bruna Lima', 5, 'disponivel')

bib.registrar_membro_pelo_sistema('pandora', 0)
bib.registrar_membro_pelo_sistema('Bilas', 1)

running = True
while running:
    print('_____________________________________________')
    print('Selecione uma opção: ')

    print('1 - Listar livros disponíveis na biblioteca.')
    print('2 - Registrar livro na biblioteca.')

    print('3 - Registrar membro na biblioteca.')
    print('4 - Listar membros da biblioteca.')

    print('5 - Alugar um livro.')
    print('6 - Listar histórico de um membro.')

    print('0 - Sair do programa.')

    op = input('Selecione a opção desejada.\n')

    match op:
        case '1':
            bib.listar_livros_disponiveis()
        case '2':
            bib.registrar_livro()
        case '3':
            bib.registrar_membro()
        case '4':
            bib.listar_membros()
        case '5':
            nome_membro = input('Quem deseja alugar um livro? Digite seu nome. \n')
            nome_livro = input('Qual livro será alugado? Digite o nome do livro. \n')
            bib.alugar_livro(nome_membro, nome_livro)
        case '6':
            nome = input('De qual membro desejas ver o histórico? \n')
            bib.listar_historico_do_membro(nome)
        case '0':
            running = False

