import keyboard
import json
from os import system
from time import sleep
from datetime import datetime
import colorama
from utilities import colorir
colorama.init()

# 0 para parede
# 1 para area livre
# 2 para personagem
# 3 para objetivo
# 4 para obstaculos

lista_colidores = [0,4]

mapa = [
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,4,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,3,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

def pegar_pos_objetivo(mapa):
        for linha in range(len(mapa)):
                for pixel in range(len(mapa[linha])):
                        if mapa[linha][pixel] == 3:
                                return (linha, pixel)

def salvar_mapa(mapa):
        map = {'mapa': mapa}
        with open("mapa.json", "w") as file:
                json.dump(map, file)


def tecla():
        teclas = ['s','w','a','d']
        while [tecla for tecla in teclas if keyboard.is_pressed(tecla)] == []:
                continue
        if keyboard.is_pressed("s"):
                return 0
        if keyboard.is_pressed("w"):
                return 1
        if keyboard.is_pressed("a"):
                return 2
        if keyboard.is_pressed("d"):
                return 3

def desenhar(mapa):
        for linha in range(len(mapa)):
                for pixel in range(len(mapa[linha])):
                        if mapa[linha][pixel] == 1:
                                mapa[linha][pixel] = " "
                        if mapa[linha][pixel] == 0:
                                mapa[linha][pixel] = ','
                        if mapa[linha][pixel] == 2:
                                mapa[linha][pixel] = colorir('.', 'vermelho')
                        if mapa[linha][pixel] == 3:
                                mapa[linha][pixel] = colorir('!', 'azul')
                        if mapa[linha][pixel] == 4:
                                mapa[linha][pixel] = colorir(':', 'amarelo')

        for linha in mapa:
                print("\n")
                for pixel in linha:
                        print(pixel, end="")

def mover(direcao, mapa):
        if direcao == 0:
                posicao = mapa[pegar_posicao(mapa)['y']+1][pegar_posicao(mapa)['x']]
                if posicao not in lista_colidores:
                        mapa[pegar_posicao(mapa)['y']+1][pegar_posicao(mapa)['x']] = 2
                        mapa[pegar_posicao(mapa)['y']][pegar_posicao(mapa)['x']] = 1

        if direcao == 1:
                posicao = mapa[pegar_posicao(mapa)['y']-1][pegar_posicao(mapa)['x']]
                if posicao not in lista_colidores:
                        mapa[pegar_posicao(mapa)['y']-1][pegar_posicao(mapa)['x']] = 2
                        mapa[pegar_posicao(mapa)['y']+1][pegar_posicao(mapa)['x']] = 1

        if direcao == 2:
                posicao = mapa[pegar_posicao(mapa)['y']][pegar_posicao(mapa)['x']-1]
                if posicao not in lista_colidores:
                        mapa[pegar_posicao(mapa)['y']][pegar_posicao(mapa)['x']-1] = 2
                        mapa[pegar_posicao(mapa)['y']][pegar_posicao(mapa)['x']+1] = 1

        if direcao == 3:
                posicao = mapa[pegar_posicao(mapa)['y']][pegar_posicao(mapa)['x']+1]
                if posicao not in lista_colidores:
                        mapa[pegar_posicao(mapa)['y']][pegar_posicao(mapa)['x']+1] = 2
                        mapa[pegar_posicao(mapa)['y']][pegar_posicao(mapa)['x']] = 1


def pegar_posicao(mapa):
        for linha in range(len(mapa)):
                for posicao in range(len(mapa[linha])):
                        if mapa[linha][posicao] == 2:
                                return {'x': posicao, 'y': linha}

y_objetivo, x_objetivo = pegar_pos_objetivo(mapa)
salvar_mapa(mapa)

inicio = datetime.now()
while True:
        desenhar(mapa)
        with open("mapa.json", "r") as file:
                mapa = json.load(file)['mapa']

        print(f"\n{colorir('posicao y:', 'verde')} {pegar_posicao(mapa)['y']}\n{colorir('posicao x:', 'verde')} {pegar_posicao(mapa)['x']}")

        if pegar_posicao(mapa)['y'] == y_objetivo and pegar_posicao(mapa)['x'] == x_objetivo:
                print(f"\n\n{colorir('parabéns', 'amarelo')}, você conseguiu chegar até o objetivo.\n")
                print(f"{colorir('tempo de jogo(horas, minutos, segundos):', 'amarelo')} {colorir(str(datetime.now() - inicio).split('.')[0], 'azul')}\n")
                input("aperte enter para fechar...")
                quit()

        if tecla() == 0:
                mover(0, mapa)
        elif tecla() == 1:
                mover(1, mapa)
        elif tecla() == 2:
                mover(2, mapa)
        elif tecla() == 3:
                mover(3, mapa)
        salvar_mapa(mapa)
        sleep(0.3)
        system("cls")
