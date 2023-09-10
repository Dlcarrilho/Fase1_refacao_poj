def game_maiorValor(amostra):
    nome_games = []
    ano_games = []
    valor_maior_zero = []
    
    for p in range(len(amostra)):

      if float(amostra[p][6]) > 0:
        valor_maior_zero.append(float(amostra[p][6]))
            
    maior_valor = max(valor_maior_zero)
    
    for i in range(len(amostra)):
      if float(amostra[i][6]) == float(maior_valor):
        nome_games.append(str(amostra[i][1]))
        ano_games.append(str(amostra[i][2]))
    print()
    print(f'==> O maior valor de venda: ${maior_valor} <==')
    print()
    print(f'==> Títulos do(s) GAME(S) com maior valor/venda: <==')
    print()
    print(f'Título: {nome_games} | Ano-Lançamento: {ano_games}')

    if __name__ == "__main__": # tornando o arquivo utilizável tanto como script quanto como um módulo importável
    import sys
    fib(int(sys.argv[1]))