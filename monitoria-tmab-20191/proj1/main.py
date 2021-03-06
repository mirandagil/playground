

### --- MENUS ---

#### lista de caracteres para enfeitar o menu
beautify_menu_top = ['\u250f','\u2501'*60]
beautify_menu_bottom = ['\u2517','\u2501'*60]

#### lista com opções de menu
menu_options = [['Bem vindo a calculadora de Matrizes da ABC-116','Operar matrizes','Modificar lista de matrizes', 'Configurações de software'],
['Você está no menu de modificação da lista de matrizes','Ler matrizes salvas', 'Inserir matriz manualmente', 'Inserir matrizes atráves de arquivo', 'Fazer backup do arquivo de matrizes','Limpar arquivo de matrizes'],
['Você está no menu de operações matriciais', 'Somar duas matrizes', 'Subtrair duas matrizes', 'Multiplicar uma matriz por escalar', 'Multiplicar duas matrizes entre si', 'Transpor matriz', 'Permutar linhas/colunas de uma matriz', 'Somar linhas/colunas de uma matriz', 'Multiplicar linha/coluna por escalar', 'Inverter matriz', 'Combinação linear de matrizes', 'Escalonamento', 'Resolução de sistema linear']]

### --- ARQUIVOS ---

#### Metódo para leitura do arquivo de matrizes ####

def read_db(file_name = 'db_matrix'):
    content = []
    matrix = []
    with open(file_name+'.matapl', 'r') as f:
        content = f.read().splitlines()
    content = content[15:]
    first_split = [i.strip(';') for i in content]
    second_split = [i.split('=') for i in first_split]
    third_split = [i[1].split(':') for i in second_split]
    fourth_split = []
    for i in third_split:
        n = len(i)
        fourth_split.append([j.split(',') for j in i])
        #    fourth_split.append(i[j].split(','))
    m_id = [j[0] for j in second_split]
    m_mn = [i[0] for i in fourth_split]
    m_data = [i[1:] for i in fourth_split]
    for i in range(len(m_id)):
        matrix.append([m_id[i],m_mn[i],m_data[i]])
    return matrix

#### Metódo do menu inicial
def menu():
    create_menu(0)
    m_opt = int(input('Escolha uma opção: '))
    if m_opt == 0: return 0
    elif m_opt == 2: menu_modifica()
    elif m_opt == 3: menu_opera()

#### Metódo para o menu de operar matrizes
def menu_opera():
    create_menu(2)
    m_opt = int(input('Escolha uma opção: '))
    if m_opt == 0: menu()
    else: return 0

#### Metódo para o menu de modificar arquivo de matrizes
def menu_modifica():
    create_menu(1)
    m_opt = int(input('Escolha uma opção: '))
    if m_opt == 0: menu()
    elif m_opt == 1: print(read_db())
    else: return 0

#### Metódo geral para diagramação dos menus
def create_menu(m):
    print(*beautify_menu_top, sep='')
    print('\u2503 %s' %menu_options[m][0])
    print('\u2503')
    if m != 0:
        print('\u2503 Para retornar ao menu anterior digite 0. Ou escolha uma das opções a seguir')
        print('\u2503')
    for i in range(1, len(menu_options[m])):
        print('\u2503 %d. %s' %(i,menu_options[m][i]))
    if m != 0: print('\u2503 0. Retornar ao menu anterior')
    else: print('\u2503 0. Sair do programa')
    print(*beautify_menu_bottom, sep='')

menu()
