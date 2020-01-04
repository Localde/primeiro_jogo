from tkinter import *
from constantes import *

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
        self.canvas = Canvas(self.frame, bg='black', width=CANVAS_L, height=CANVAS_A)
        self.canvas.pack()

        #E colocamos um botão para começar o jogo
        #self.começar = Button(self.root, text = 'START', command=self.começa)
        #self.começar.pack()

        #self.novoJogo()

        self.root.mainloop()

if __name__ == '__main__':
    Jogo()