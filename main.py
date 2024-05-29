pessoa = {

 'Nome':'Gustavo Amaral',
 'Idade': 40,
 'Profissão': 'Programador'

}

nova_chave = input('Digite o nome do campo: ')
novo_valor = input('Informe o valor do novo campo: ')
pessoa[nova_chave] = novo_valor

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')