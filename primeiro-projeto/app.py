import os

restaurantes = [{'nome':'Plaza', 'categoria':'Pizza', 'ativo': False},
                {'nome':'Tiete', 'categoria':'Churrasco', 'ativo':True},
                {'nome':'Donald', 'categoria':'Hamburguer', 'ativo': False}]

def exibir_nome():
    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar para o menu ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alterar Estado do Restaurante')
    print('4. Sair')

# funcoes
def finalizar_programa():
    exibir_subtitulo('Encerrando o programa...')

def opcao_invalida():
    exibir_subtitulo('Opcao inválida')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''
    Docstring for cadastrar_novo_restaurante
    Essa função é responsável por cadastrar um novo restaurante
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_cadastro = {'nome': {nome_do_restaurante}, 'categoria': {categoria}, 'ativo': False}
    restaurantes.append(dados_do_cadastro)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''
    Docstring for listar_restaurantes
    Essa função é responsável por listar os restaurantes
    '''
    exibir_subtitulo('Listar Restaurantes')

    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Estado')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo =  'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
 
    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    '''
    Docstring for alterar_estado_restaurante
    Essa função é responsável por alterar o Estado do restaurante (ativo ou inativo)
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')


    voltar_ao_menu_principal(0)



def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
    # print(f'A opção escolhida foi: {opcao_escolhida}')
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            finalizar_programa()        
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()



