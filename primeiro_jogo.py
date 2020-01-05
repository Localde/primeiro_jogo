from tkinter import *
from constantes import *
import random

class Jogo(object):
    """
    Classe que organiza os elementos do jogo
    """
    def __init__(self):
        #Criamos o conteiner principal do jogo
        self.root = Tk()
        self.root.geometry('%ix%i'%(LARGURA, ALTURA))
        self.root.resizable(False, False)
        self.root.title('Joguinho Besta')

        #E uma frame para conter o canvas
        self.frame = Frame(bg='black')
        self.frame.pack()

        #Criamos a tela do jogo
        self.canvas = Canvas(self.frame, bg='black', width=CANVAS_L, height=CANVAS_A, cursor='target')
        self.canvas.pack()

        #E colocamos um botão para começar o jogo
        self.começar = Button(self.root, text='START')
        self.começar.pack()

        self.novoJogo()

        self.root.mainloop()

    def novoJogo(self):
        """
        Cria os elementos de um novo jogo
        """
        self.canvas.create_rectangle((CANVAS_L//2, 350), (CANVAS_L//2 + 100, 370), fill='green')

        #Lista dos ratângulos
        self.r = []

        #E por fim as diversas fileiras de retângulos
        l, c, e = 5, 8, 2 #Linhas, colunas e espaçamento
        b, h, y0 = 48, 20, 50 #Base, altura e posição inicial dos retângulos
        for i in range(l):
            cor = random.choice(['green', 'orange', 'white', 'lightgray', 'yellow', 'purple'])
            for j in range(c):
                self.canvas.create_rectangle(b*j+(j+1)*e, i*h+(i+1)*e + y0, b*j+(j+1)*e+b, i*h+(i+1)*e + y0 + h, fill=cor)
        self.canvas.create_text(CANVAS_L/2, CANVAS_A/2, text='OLA COLEGA!', fill='white')
if __name__ == '__main__':
    Jogo()