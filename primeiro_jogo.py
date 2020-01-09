from tkinter import *
from constantes import *
import random

#Canvas: bbox(tag), find_overlapping(x1, y1, x2, y2), find_closest(x, y, halo=None, start=None)

#bounding
#encontre intersecção
#encontre o mais próximo


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
        self.começar = Button(self.root, text='START', command=self.começa)
        self.começar.pack()

        #self.canvas.create_polygon((100, 200), (150, 250), (250, 250), (300, 200), (300, 100), (250, 50), (150, 50), (100, 100), fill='white')

        #Criamos os elementos para um novo jogo.
        self.novoJogo()

        #Inicializamos o tkinter
        self.root.mainloop()

    def novoJogo(self):
        """
        Cria os elementos de um novo jogo
        """

        #Definimos o player como sendo um retângulo com as dimensões indicadas
        self.player = self.canvas.create_rectangle((CANVAS_L//2, 350), (CANVAS_L//2 + 100, 370), fill='green')

        # Lista dos ratângulos
        self.r = []

        #E por fim as diversas fileiras de retângulos
        l, c, e = 5, 8, 2 #Linhas, colunas e espaçamento
        b, h, y0 = 48, 20, 50 #Base, altura e posição inicial dos retângulos
        for i in range(l):
            cor = random.choice(['green', 'orange', 'white', 'lightgray', 'yellow', 'purple'])
            for j in range(c):
                r = self.canvas.create_rectangle(b*j+(j+1)*e, i*h+(i+1)*e + y0, b*j+(j+1)*e+b, i*h+(i+1)*e + y0 + h, fill=cor)

                self.r.append(r)


        #Cria a bola do jogo
        raio = 30
        p = (100, 200)
        self.bola = self.canvas.create_oval(p[0], p[1], p[0] + raio, p[1] + raio, fill='red', outline='white', tag='bola')
        self.b_vx = self.b_vy = 5
        self.b_x, self.b_y = p

        #Inicializamos a variavel booleana indicando que o jogador esta jogando
        self.jogando = True

    def começa(self):
        """
        Inicia o jogo
        """
        self.jogar()


    def jogar(self):
        """
        Deve ser executado enquanto o jogo estiver rodando
        """
        if self.jogando:
            self.update()
            self.desenhar()

            self.root.after(10, self.jogar)
        else:
            self.acabou(self.msg)


    def desenhar(self):
        """
        Metodo para redesenhar a tela do jogo
        """
        pass

    def update(self):
        """
        Updatamos as condições do jogo
        """
        #Movemos a bola
        self.canvas.move('bola', self.b_vx, self.b_vy)

        #Atualizamos os valores de sua posição
        self.b_x += self.b_vx
        self.b_y += self.b_vy

        #Verificamos se a bola não está colidindo com nenhum extremo
        if self.b_x > CANVAS_L - 30 or self.b_x < 0:
            self.b_vx *= -1

        if self.b_y > CANVAS_A - 30 or self.b_y < 0:
            self.b_vy *= -1

        #Depois de mover a bola é preciso procurar as colisões
        self.VerificaColisão()

    def VerificaColisão(self):
        """
        Verifica se houve alguma colisão entre elementos do jogo
        """
        #Primeiro criamos uma bounding box para a bola
        coord = self.canvas.bbox('bola')
        #x1, y1, x2, y2

        #Depois pegamos a id de todos os objetos que colidem com a bola
        colisoes = self.canvas.find_overlapping(*coord)

        #Se o número de colisões for diferente de zero
        if len(colisoes) != 0:
            #verificamos se o id do objeto é diferente do player
            if colisoes[0] != self.player:
                #Vamos checar a colisão com o objeto mais próximo do topo
                #esquerdo da bola
                m_p = self.canvas.find_closest(coord[0], coord[1])

                #Depois temos que olhar para cada um dos retângulos
                #com quem a bola colidiu
                for r in self.r:
                    #tendo encontrado o retângulo
                    if r == m_p[0]:
                        #deletamos ele do topo
                        self.r.remove(r)
                        self.canvas.delete(r)

                        #E invertemos o sentido da velocidade da bola
                        self.b_vy *= -1

                        #Por fim saimos da função
                        return




if __name__ == '__main__':
    Jogo()