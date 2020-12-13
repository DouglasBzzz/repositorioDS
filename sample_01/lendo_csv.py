import csv

with open('escape.txt') as arquivo_csv:
    #csv_reader = csv.DictReader(arquivo_csv, delimiter=',', quotechar = '"')
    csv_reader = csv.DictReader(arquivo_csv, delimiter=',', escapechar="|")
    contador_linha = 0
    for linha in csv_reader:
        if contador_linha == 0:
            print(f'Nomes das colunas: {", ".join(linha)}')
            contador_linha += 1
        #else:
        #print(f'\t{linha["nome"]} trabalha no departamento: {linha["endereco"]}, e nasceu no mes de {linha["idade"]}.')
        print(f'\t{linha["nome"]} mora no endereco: {linha["endereco"]}, e tem {linha["idade"]} anos.')
        contador_linha += 1

    print(f'Procedimento finalizado, foram processadas: {contador_linha} linhas')
