"""Faça um programa que pergunte a quantidade de km percorridos popr um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R4 60 por dia e R$0.15 por km rodado"""

quantidadeKm = float(input('Digite a quantidade de km percorridos: '));
dias = int(input('Digite a quantidade de dias: '));

print('O valor a ser pago é de R${}'.format(quantidadeKm * 0.15 + dias * 60))

