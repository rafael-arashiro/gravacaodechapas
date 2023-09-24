from tkinter import *
from reportlab.pdfgen.canvas import Canvas
from GravacaodechapasFuncoes4 import Funcoes

class ChamadaFuncoes(Funcoes):

    #Clicar no checkbox de páginas
    def checkboxQuantidadePaginas(self):
        if self.listaTotalPaginas.get(0) == "":
            self.lista.delete(0)
            self.lista.insert(END, "Total de páginas vazio.")
        else:
            global numeroPaginasTotal
            numeroPaginasTotal = self.quantidadeDePaginas()
            self.funcDicionario()

    #Clicar no botão Total
    def botaoTotal(self):
        global numeroPaginasTotal
        numeroPaginasTotal = self.quantidadePaginasTotal()
        self.funcDicionario()
        self.quantidadeDePaginas()

    #Cria o dicionário de paǵinas e cadernos e coloca o total de páginas.
    def funcDicionario(self):
        numeros_int = int(numeroPaginasTotal)

        if numeros_int % 4 != 0:
            self.lista.delete(0)
            self.lista.insert(END, str(int(numeroPaginasTotal)) + " não tem multiplicidade.")
        elif self.varMontagem.get() == 32 and numeroPaginasTotal < 8:
            self.lista.delete(0)
            self.lista.insert(END, str(int(numeroPaginasTotal)) + " páginas são insuficientes para um caderno de 32 páginas.")
        else:
            cadernosTotal = ""
            chapasTotal = 0

            self.cadernoPaginas()
            cadernosTotal = self.calculoCadernosTotal()
            chapasTotal = self.calculoChapasTotal()

            self.listaTotalPaginas.delete(0)
            self.listaTotalPaginas.insert(END, numeroPaginasTotal)

            self.listaTotalCadernos.delete(0)
            self.listaTotalCadernos.insert(END, cadernosTotal)

            self.listaTotalChapas.delete(0)
            self.listaTotalChapas.insert(END, chapasTotal)

    def páginasCadernosChapasAlteradas(self):
        grupoAlteradas = self.calculoAlteradas()
        CadernosAlterados = self.calculoChapasCadernosAlteradas()

        self.listaAlteradosCadernos.delete(0)
        self.listaAlteradosCadernos.insert(END, CadernosAlterados)

        self.listaAlteradasChapas.delete(0)
        self.listaAlteradasChapas.insert(END, (CadernosAlterados * 8))

        self.listaAlteradasPaginas.delete(0)
        self.listaAlteradasPaginas.insert(END, len(grupoAlteradas))

        self.paginasAlteradas.delete(0, END)
        self.paginasAlteradas2.delete(0, END)

    #limpa toda tela.
    def limpa_tela(self):
        global dicionario
        dicionario = {}
        global grupoAlteradas
        grupoAlteradas = []
        self.entrada.delete(0, END)
        self.paginasAlteradas.delete(0, END)
        self.paginasAlteradas2.delete(0, END)
        self.lista.delete(0, END)
        self.listaTotalPaginas.delete(0, END)
        self.listaAlteradasPaginas.delete(0, END)
        self.listaTotalCadernos.delete(0, END)
        self.listaAlteradosCadernos.delete(0, END)
        self.listaTotalChapas.delete(0, END)
        self.listaAlteradasChapas.delete(0, END)
        self.limpa_tela2()

    ###salva em PDF
    def exportarPdf(self):
        nomeMaterial = str(self.enNomeMaterial.get())
        canvas = Canvas(nomeMaterial + ".pdf", pagesize="A4")
        canvas.drawString(230, 750, nomeMaterial)
        canvas.drawString(72, 700, "Total de páginas: " + str(self.listaTotalPaginas.get(0)))
        canvas.drawString(72, 650, "Total de cadernos: " + str(self.listaTotalCadernos.get(0)))
        canvas.drawString(72, 600, "Total de chapas: " + str(self.listaTotalChapas.get(0)))
        canvas.drawString(350, 700, "Páginas alteradas: " + str(self.listaAlteradasPaginas.get(0)))
        canvas.drawString(350, 650, "Cadernos alterados: " + str(self.listaAlteradosCadernos.get(0)))
        canvas.drawString(350, 600, "Chapas alteradas: " + str(self.listaAlteradasChapas.get(0)))
        canvas.drawString(72, 550, "Lista de páginas alteradas: " + str(self.lista.get(0, 9)))
        i = 10
        linha = 520
        while i < self.lista.size():
            ultimo = i + 9
            canvas.drawString(72, linha, str(self.lista.get(i, ultimo)))
            linha = linha - 30
            i += 10

        canvas.save()