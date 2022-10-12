#Lucas Vinicius Oliveira Galindo - RM95177
#Jose Vitor - RM95438

n_linhas = 3
n_colunas = 3

def inicializarTabuleiro(n_linhas, n_colunas):
    matriz_jogo = []
    for i in range(n_linhas):
        jogo=[]
        for j in range(n_colunas):
            jogo.append(0)
        matriz_jogo.append(jogo)
        
    return matriz_jogo

def imprimirTabuleiro(matriz_jogo):
    jogador1 = int(input("Escolha: (1 ou 2 ): "))
    if jogador1 == 1:
        jogador2 = 2
    if jogador1 == 2:
        jogador2 = 1
    
    return jogador1, jogador2
    
def imprimeMenuPrincipal(jogador1, jogador2,matriz_jogo):
    print(f'O primeiro jogador tem: {jogador1} \nO segundo jogador tem: {jogador2}')
    print("O tabuleiro se inicia assim: ","\n", matriz_jogo[0], "\n", matriz_jogo[1],"\n", matriz_jogo[2])
    pontuacao_jogador1 = 0
    pontuacao_jogador2 = 0
    
    return pontuacao_jogador1, pontuacao_jogador2
    
    
    
def leiaCordenadaLinha():
    linhas_jogador1 = int(input("jogador1: Qual linha deseja iniciar ?: obs: (1 ate 3)"))
    linhas_jogador2 = int(input("jogador2: Qual linha deseja iniciar ?: obs: (1 ate 3)"))
    
    return linhas_jogador1, linhas_jogador2
        
        
   
def leiaCordenadaColuna():
    coluna_jogador1 = int(input("jogador1: Qual coluna deseja iniciar ?: obs: (1 ate 3)"))
    coluna_jogador2 = int(input("jogador2: Qual coluna deseja iniciar ?: obs: (1 ate 3)"))
    
    return coluna_jogador1, coluna_jogador2

def imprimirPontuação(matriz_jogo, jogador1, jogador2, pontuacao_jogador1, pontuacao_jogador2):

    #jogdor 1 - pontuação - colunas
   if matriz_jogo[0][0] == jogador1 and matriz_jogo[1][0] == jogador1 and matriz_jogo[2][0] == jogador1:
        pontuacao_jogador1 += 100
   elif matriz_jogo[0][1] == jogador1 and matriz_jogo[1][1] == jogador1 and matriz_jogo[2][1] == jogador1:
        pontuacao_jogador1 += 100
   elif matriz_jogo[0][2] == jogador1 and matriz_jogo[1][2] == jogador1 and matriz_jogo[2][2] == jogador1:
        pontuacao_jogador1 += 100
    
    #jogador1 - pontuação - linhas
   if matriz_jogo[0][0] == jogador1 and matriz_jogo[0][1] == jogador1 and matriz_jogo[0][2] == jogador1:
        pontuacao_jogador1 += 100
   elif matriz_jogo[1][0] == jogador1 and matriz_jogo[1][1] == jogador1 and matriz_jogo[1][2] == jogador1:
        pontuacao_jogador1 += 100
   elif matriz_jogo[2][0] == jogador1 and matriz_jogo[2][1] == jogador1 and matriz_jogo[2][2] == jogador1:
        pontuacao_jogador1 += 100
        
    #jogador1 - pontuação - diagonal
    
   if matriz_jogo[0][0] == jogador1 and matriz_jogo[1][1] == jogador1 and matriz_jogo[2][2] == jogador1:
        pontuacao_jogador1 += 100
   elif matriz_jogo[0][2] == jogador1 and matriz_jogo[1][1] == jogador1 and matriz_jogo[0][2] == jogador1:
        pontuacao_jogador1 += 100
    
    #------------------------------------------------------------------------------
    
    #jogdor 2 - pontuação - colunas
   if matriz_jogo[0][0] == jogador2 and matriz_jogo[1][0] == jogador2 and matriz_jogo[2][0] == jogador2:
        pontuacao_jogador2 += 100
   elif matriz_jogo[0][1] == jogador2 and matriz_jogo[1][1] == jogador2 and matriz_jogo[2][1] == jogador2:
        pontuacao_jogador2 += 100
   elif matriz_jogo[0][2] == jogador2 and matriz_jogo[1][2] == jogador2 and matriz_jogo[2][2] == jogador2:
        pontuacao_jogador2 += 100
    
    #jogador 2 - pontuação - linhas
   if matriz_jogo[0][0] == jogador2 and matriz_jogo[0][1] == jogador2 and matriz_jogo[0][2] == jogador2:
        pontuacao_jogador2 += 100
   elif matriz_jogo[1][0] == jogador2 and matriz_jogo[1][1] == jogador2 and matriz_jogo[1][2] == jogador2:
        pontuacao_jogador2 += 100
   elif matriz_jogo[2][0] == jogador2 and matriz_jogo[2][1] == jogador2 and matriz_jogo[2][2] == jogador2:
        pontuacao_jogador2 += 100
        
    #jogador2 - pontuação - diagonal
    
   if matriz_jogo[0][0] == jogador2 and matriz_jogo[1][1] == jogador2 and matriz_jogo[2][2] == jogador2:
       pontuacao_jogador2 += 100
   elif matriz_jogo[0][2] == jogador2 and matriz_jogo[1][1] == jogador2 and matriz_jogo[0][2] == jogador2:
       pontuacao_jogador2 += 100
   print("-----------------------------------------------------------------------------------------")     
   print(f"O jogador numero 1 tem: {pontuacao_jogador1}\nO jogador numero 2 tem: {pontuacao_jogador2}")
   print("-----------------------------------------------------------------------------------------")  
   
   verificaVencedor(jogador1, jogador2, pontuacao_jogador1, pontuacao_jogador2)
   print("-----------------------------------------------------------------------------------------")  
   verificaVelha(pontuacao_jogador1, pontuacao_jogador2)
  


def posicaoValida(linhas_jogador1, linhas_jogador2, coluna_jogador1, coluna_jogador2, matriz_jogo, jogador1, jogador2):
    
    matriz_jogo[linhas_jogador1 - 1][coluna_jogador1 - 1] = jogador1
    matriz_jogo[linhas_jogador2 - 1][coluna_jogador2 - 1] = jogador2

    print("\n",matriz_jogo[0],"\n", matriz_jogo[1],"\n", matriz_jogo[2])
    
    for i in range(9):
        #--------------------------------------------------
        linhas_jogador1 =  int(input("jogador1: Qual linha ?: obs: (1 ate 3)"))
        coluna_jogador1 = int(input("jogador1: Qual coluna  ?: obs: (1 ate 3)"))
        if matriz_jogo[linhas_jogador1 - 1][coluna_jogador1 - 1] == jogador2:
            while matriz_jogo[linhas_jogador1 - 1][coluna_jogador1 - 1] == jogador2:
                print("\n",matriz_jogo[0],"\n", matriz_jogo[1],"\n", matriz_jogo[2])
                print("esse espaço ja foi usado")
                linhas_jogador1 =  int(input("jogador1: Qual linha ?: obs: (1 ate 3)"))
                coluna_jogador1 = int(input("jogador1: Qual coluna  ?: obs: (1 ate 3)"))
                if  matriz_jogo[linhas_jogador1 - 1][coluna_jogador1 - 1] == jogador1:
                    break
        matriz_jogo[linhas_jogador1 - 1][coluna_jogador1 - 1] = jogador1
        print("\n",matriz_jogo[0],"\n", matriz_jogo[1],"\n", matriz_jogo[2])
        #---------------------------------------------------
        #--------------------------------------------------
        #--------------------------------------------------
        #jogador 1 linhas
        if matriz_jogo[0][0] == jogador1 and matriz_jogo[0][1] == jogador1 and matriz_jogo[0][2] == jogador1:
            print('JOGO ENCERRADO')
            break
        elif matriz_jogo[1][0] == jogador1 and matriz_jogo[1][1] == jogador1 and matriz_jogo[1][2] == jogador1:
            print('JOGO ENCERRADO')
            break
        elif matriz_jogo[2][0] == jogador1 and matriz_jogo[2][1] == jogador1 and matriz_jogo[2][2] == jogador1:
            print('JOGO ENCERRADO')
            break
        #--------------------------------------------------
        #jogador1 colunas
        if matriz_jogo[0][0] == jogador1 and matriz_jogo[1][0] == jogador1 and matriz_jogo[2][0] == jogador1:
            print('JOGO ENCERRADO')
            break
        elif matriz_jogo[0][1] == jogador1 and matriz_jogo[1][1] == jogador1 and matriz_jogo[2][1] == jogador1:
            print('JOGO ENCERRADO')
            break
        elif matriz_jogo[0][2] == jogador1 and matriz_jogo[1][2] == jogador1 and matriz_jogo[2][2] == jogador1:
            print('JOGO ENCERRADO')
            break
        #-------------------------------------------------------------------------------------------------------
        #jogador1 - diagonal
    
        if matriz_jogo[0][0] == jogador1 and matriz_jogo[1][1] == jogador1 and matriz_jogo[2][2] == jogador1:
            print('JOGO ENCERRADO')
            break
        elif matriz_jogo[0][2] == jogador1 and matriz_jogo[1][1] == jogador1 and matriz_jogo[2][0] == jogador1:
            print('JOGO ENCERRADO')
            break
        #------------------------------------------------
        
      
        #--------------------------------------------------
        linhas_jogador2 = int(input("jogador2: Qual linha ?: obs: (1 ate 3)"))
        coluna_jogador2 = int(input("jogador2: Qual coluna  ?: obs: (1 ate 3)"))
        if matriz_jogo[linhas_jogador2 - 1][coluna_jogador2 - 1] == jogador1:
            while matriz_jogo[linhas_jogador2 - 1][coluna_jogador2 - 1] == jogador1:
                print("\n",matriz_jogo[0],"\n", matriz_jogo[1],"\n", matriz_jogo[2])
                print("esse espaço ja foi usado")
                linhas_jogador2 = int(input("jogador2: Qual linha ?: obs: (1 ate 3)"))
                coluna_jogador2 = int(input("jogador2: Qual coluna  ?: obs: (1 ate 3)"))
                if matriz_jogo[linhas_jogador2 - 1][coluna_jogador2 - 1] == jogador2:
                    break
        matriz_jogo[linhas_jogador2 - 1][coluna_jogador2 - 1] = jogador2
        print("\n",matriz_jogo[0],"\n", matriz_jogo[1],"\n", matriz_jogo[2])
        #-------------------------------------------------
        #-------------------------------------------------
        #------------------------------------------------
        #jogador2 linhas
        if matriz_jogo[0][0] == jogador2 and matriz_jogo[0][1] == jogador2 and matriz_jogo[0][2] == jogador2:
            print('JOGO ENCERRADO')
            break
        elif matriz_jogo[1][0] == jogador2 and matriz_jogo[1][1] == jogador2 and matriz_jogo[1][2] == jogador2:
            print('JOGO ENCERRADO')
            break
        elif matriz_jogo[2][0] == jogador2 and matriz_jogo[2][1] == jogador2 and matriz_jogo[2][2] == jogador2:
            print('JOGO ENCERRADO')
            break
        #--------------------------------------------------
        #jogador2 colunas
        if matriz_jogo[0][0] == jogador2 and matriz_jogo[1][0] == jogador2 and matriz_jogo[2][0] == jogador2:
           print('JOGO ENCERRADO')
           break
        elif matriz_jogo[0][1] == jogador2 and matriz_jogo[1][1] == jogador2 and matriz_jogo[2][1] == jogador2:
           print('JOGO ENCERRADO')
           break
        elif matriz_jogo[0][2] == jogador2 and matriz_jogo[1][2] == jogador2 and matriz_jogo[2][2] == jogador2:
           print('JOGO ENCERRADO')
           break
       #-----------------------------------------------------
        #jogador2 - diagonal
    
        if matriz_jogo[0][0] == jogador2 and matriz_jogo[1][1] == jogador2 and matriz_jogo[2][2] == jogador2:
           print('JOGO ENCERRADO')
           break
        elif matriz_jogo[0][2] == jogador2 and matriz_jogo[1][1] == jogador2 and matriz_jogo[2][0] == jogador2:
           print('JOGO ENCERRADO')
           break
        if matriz_jogo[0][0] > 0 and matriz_jogo[0][1] > 0 and  matriz_jogo[0][2] > 0 and matriz_jogo[1][0] > 0 and matriz_jogo[1][1] > 0 and  matriz_jogo[1][2] > 0 and matriz_jogo[2][0] > 0 and matriz_jogo[2][1] > 0 and matriz_jogo[2][2] > 0:
           break

        
        

            
def verificaVencedor(jogador1, jogador2, pontuacao_jogador1, pontuacao_jogador2):
    
    if pontuacao_jogador1 == 100:
        print("Parabens o jogador 1 é o vencedor")
    else:
        print("O jogador 1 perdeu")
    
    if pontuacao_jogador2 == 100:
        print("Parabens o jogador 2 é o vencedor")
    else:
         print("O jogador 2 perdeu")
         
def verificaVelha(pontuacao_jogador1, pontuacao_jogador2):
    if pontuacao_jogador1 != 100 and pontuacao_jogador2 != 100:
        print("o jogo deu velha!!!")
        
        
def modoJogador():
    op = "S"
    while op == "S":
        matriz_jogo = inicializarTabuleiro(n_linhas, n_colunas)
        jogador1, jogador2 = imprimirTabuleiro(matriz_jogo)
        pontuacao_jogador1, pontuacao_jogador2 = imprimeMenuPrincipal(jogador1, jogador2, matriz_jogo)
        linhas_jogador1, linhas_jogador2 = leiaCordenadaLinha()
        coluna_jogador1, coluna_jogador2 = leiaCordenadaColuna()
        posicaoValida(linhas_jogador1, linhas_jogador2, coluna_jogador1, coluna_jogador2, matriz_jogo, jogador1, jogador2)
        imprimirPontuação(matriz_jogo, jogador1, jogador2, pontuacao_jogador1, pontuacao_jogador2)
        op = input("Deseja reniciar o jogo ? (S/N)").upper()
    
modoJogador()
