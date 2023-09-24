from tkinter import *
from GravacaodechapasChamadaFuncoes4 import ChamadaFuncoes

root = Tk()

class Programa(ChamadaFuncoes):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgetsFrame1()
        self.listaFrame2()
        root.mainloop()
    def tela(self):
        self.root.title("Cálculo de Chapas")
        self.root.configure(background="#008B8B")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.minsize(width=700, height=500)
        self.root.maxsize(width=700, height=500)
    def frames_da_tela(self):
        self.frame1 = Frame(self.root, bd_=4, bg="#A9A9A9", highlightbackground="#1C1C1C", highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame2 = Frame(self.root, bd_=4, bg="#A9A9A9", highlightbackground="#1C1C1C", highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
        self.root.label = Label(root,text='Número de páginas:',width=20,height=10)
    def widgetsFrame1(self):

        ###label quantidade de páginas
        self.lbPaginas = Label(self.frame1, text="Total de páginas:", bg="#A9A9A9")
        self.lbPaginas.place(relx=0.01, rely=0.05)
        self.entrada = Entry(self.frame1)
        self.entrada.place(relx=0.19, rely=0.05)
        ###botão total de páginas
        self.botao = Button(self.frame1, text='Total', command=self.botaoTotal)
        self.botao.place(relx=0.45, rely=0.05, relwidth=0.1, relheight=0.1)

        ###label páginas alteradas
        self.lbInserirPaginasAlteradas = Label(self.frame1, text="Páginas alteradas:", bg="#A9A9A9")
        self.lbInserirPaginasAlteradas.place(relx=0.01, rely=0.2)
        self.paginasAlteradas = Entry(self.frame1)
        self.paginasAlteradas.place(relx=0.20, rely=0.2, relwidth=0.15)
        self.paginasAlteradas2 = Entry(self.frame1)
        self.paginasAlteradas2.place(relx=0.34, rely=0.2, relwidth=0.15)
        ###botão páginas alteradas
        self.botaoCalcularChapas = Button(self.frame1, text='Calcular chapas', command=self.páginasCadernosChapasAlteradas)
        self.botaoCalcularChapas.place(relx=0.50, rely=0.2, relwidth=0.18, relheight=0.1)


        ###nome do material
        self.lbNomeMaterial = Label(self.frame1, text="Nome do Material:", bg="#A9A9A9")
        self.lbNomeMaterial.place(relx=0.01, rely=0.35)
        self.enNomeMaterial = Entry(self.frame1)
        self.enNomeMaterial.place(relx=0.20, rely=0.35)
        ###botão salvar PDF
        self.btSalvar = Button(self.frame1, text="Salvar PDF", command=self.exportarPdf)
        self.btSalvar.place(relx=0.46, rely=0.33, relwidth=0.12, relheight=0.15)

        ###botão limpar
        self.btLimpar = Button(self.frame1, text="Limpar", command=self.limpa_tela)
        self.btLimpar.place(relx=0.60, rely=0.33, relwidth=0.1, relheight=0.15)
        
        ###verso branco
        self.varVersoBranco = IntVar(self.frame1)
        self.versoBranco = Checkbutton(self.frame1, text="Páginas com verso branco", bg="#A9A9A9", highlightthickness=0, variable=self.varVersoBranco, onvalue=1, offvalue=0, command=self.checkboxQuantidadePaginas)
        self.versoBranco.place(relx=0.7, rely=0.05)

        ###Montagem de páginas
        self.varMontagem = IntVar(self.frame1, value=16)
        self.montagem1 = Radiobutton(self.frame1, text="16 páginas no caderno", bg="#A9A9A9", highlightthickness=0, variable=self.varMontagem, value=16)
        self.montagem1.place(relx=0.7, rely=0.18)
        self.montagem2 = Radiobutton(self.frame1, text="8 páginas no caderno", bg="#A9A9A9", highlightthickness=0, variable=self.varMontagem, value=8)
        self.montagem2.place(relx=0.7, rely=0.28)
        self.montagem3 = Radiobutton(self.frame1, text="32 páginas no caderno", bg="#A9A9A9", highlightthickness=0, variable=self.varMontagem, value=32)
        self.montagem3.place(relx=0.7, rely=0.38)

        ###label dados do material
        self.lbMaterial = Label(self.frame1, text="Material:", bg="#A9A9A9")
        self.lbMaterial.place(relx=0.4, rely=0.5)

        ###lista de total de páginas
        self.lbTotalPaginas = Label(self.frame1, text="Total de páginas:", bg="#A9A9A9")
        self.lbTotalPaginas.place(relx=0.01, rely=0.6)
        self.listaTotalPaginas = Listbox(self.frame1)
        self.listaTotalPaginas.place(relx=0.21, rely=0.6, relwidth=0.25, relheight=0.1)
        ###lista de total de cadernos
        self.lbTotalCadernos = Label(self.frame1, text="Total de cadernos:", bg="#A9A9A9")
        self.lbTotalCadernos.place(relx=0.01, rely=0.73)
        self.listaTotalCadernos = Listbox(self.frame1)
        self.listaTotalCadernos.place(relx=0.21, rely=0.73, relwidth=0.25, relheight=0.1)
        ###lista de total de chapas
        self.lbTotalChapas = Label(self.frame1, text="Total de chapas:", bg="#A9A9A9")
        self.lbTotalChapas.place(relx=0.01, rely=0.86)
        self.listaTotalChapas = Listbox(self.frame1)
        self.listaTotalChapas.place(relx=0.21, rely=0.86, relwidth=0.25, relheight=0.1)
        ###lista de páginas alteradas
        self.lbAlteradasPaginas = Label(self.frame1, text="Páginas alteradas:", bg="#A9A9A9")
        self.lbAlteradasPaginas.place(relx=0.52, rely=0.6)
        self.listaAlteradasPaginas = Listbox(self.frame1)
        self.listaAlteradasPaginas.place(relx=0.73, rely=0.6, relwidth=0.25, relheight=0.1)
        ###lista de cadernos alterados
        self.lbAlteradosCadernos = Label(self.frame1, text="Cadernos alterados:", bg="#A9A9A9")
        self.lbAlteradosCadernos.place(relx=0.52, rely=0.73)
        self.listaAlteradosCadernos = Listbox(self.frame1)
        self.listaAlteradosCadernos.place(relx=0.73, rely=0.73, relwidth=0.25, relheight=0.1)
        ###lista de chapas alteradas
        self.lbAlteradasChapas = Label(self.frame1, text="Chapas alteradas:", bg="#A9A9A9")
        self.lbAlteradasChapas.place(relx=0.52, rely=0.86)
        self.listaAlteradasChapas = Listbox(self.frame1)
        self.listaAlteradasChapas.place(relx=0.73, rely=0.86, relwidth=0.25, relheight=0.1)
    def listaFrame2(self):
        self.lista = Listbox(self.frame2)
        self.lista.place(relx=0.01, rely=0.05, relwidth=0.96, relheight=0.88)
        self.scrollbar = Scrollbar(self.frame2)
        self.scrollbar.pack(side=RIGHT, fill="both")
        self.lista.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.lista.yview)



Programa()
