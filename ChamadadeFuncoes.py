from tkinter import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from Material import *

class ChamadaFuncoes(Material):

    #Clicar no botão Total, verifica a multiplicidade e coloca as informações do total de páginas, cadernos e chapas.
    def botaoTotal(self):
        self.novoMaterial = Material(self.entrada.get())
        self.novoMaterial.setVersoBranco(self.varVersoBranco.get())
        self.novoMaterial.setPaginasPorCaderno(self.varMontagem.get())
        self.novoMaterial.setPaginasTotal()

        numeros_int = int(self.novoMaterial.getPaginasTotal())
        numeros_float = float(self.novoMaterial.getPaginasTotal())
        if numeros_int % 4 != 0:
            self.lista.delete(0)
            self.lista.insert(END, str(numeros_int) + " não tem multiplicidade.")
            return
        
        elif self.novoMaterial.getPaginasPorCaderno() == 32:
            if numeros_int < 8 or 32 % numeros_float != 0 or 32 % numeros_float != 0.25 or 32 % numeros_float != 0.5 or 32 % numeros_float != 0.75:
                self.lista.delete(0)
                self.lista.insert(END, str(numeros_int) + " páginas são insuficientes para um caderno de 32 páginas.")
                return

        else:
            self.novoMaterial.setCadernos()
            self.novoMaterial.setChapas()
            self.novoMaterial.setDicionario()

            self.listaTotalPaginas.delete(0)
            self.listaTotalPaginas.insert(END, self.novoMaterial.getPaginasTotal())

            self.listaTotalCadernos.delete(0)
            self.listaTotalCadernos.insert(END, self.novoMaterial.getCadernos())

            self.listaTotalChapas.delete(0)
            self.listaTotalChapas.insert(END, self.novoMaterial.getChapas())

            self.lista.delete(0)
            self.lista.insert(END, self.novoMaterial.dicionario)
            
    def páginasCadernosChapasAlteradas(self):
        self.novoMaterial.setPaginasAlteradas(self.entradaPaginasAlteradas.get())
        self.novoMaterial.setDicionarioAlteradas()
        self.novoMaterial.setCadernosAlterados()
        self.novoMaterial.setChapasAlteradas()

        self.lista.insert(END, self.novoMaterial.getDicionarioAlteradas())

        self.listaAlteradosCadernos.delete(0)
        self.listaAlteradosCadernos.insert(END, self.novoMaterial.getCadernosAlterados())

        self.listaAlteradasChapas.delete(0)
        self.listaAlteradasChapas.insert(END, self.novoMaterial.getChapasAlteradas())

        self.listaAlteradasPaginas.delete(0)
        self.listaAlteradasPaginas.insert(END, self.novoMaterial.getPaginasAlteradas())

        self.entradaPaginasAlteradas.delete(0, END)

    def removerPaginasAlteradas(self):
        self.novoMaterial.setRemoverPaginasAlteradas(self.entradaPaginasAlteradas.get())
        self.novoMaterial.setDicionarioAlteradas()
        self.novoMaterial.setCadernosAlterados()
        self.novoMaterial.setChapasAlteradas()

        self.lista.insert(END, self.novoMaterial.getDicionarioAlteradas())

        self.listaAlteradosCadernos.delete(0)
        self.listaAlteradosCadernos.insert(END, self.novoMaterial.getCadernosAlterados())

        self.listaAlteradasChapas.delete(0)
        self.listaAlteradasChapas.insert(END, self.novoMaterial.getChapasAlteradas())

        self.listaAlteradasPaginas.delete(0)
        self.listaAlteradasPaginas.insert(END, self.novoMaterial.getPaginasAlteradas())

        self.entradaPaginasAlteradas.delete(0, END)


    #limpa toda tela.
    def limpa_tela(self):

        self.entrada.delete(0, END)
        self.entradaPaginasAlteradas.delete(0, END)
        self.lista.delete(0, END)
        self.listaTotalPaginas.delete(0, END)
        self.listaAlteradasPaginas.delete(0, END)
        self.listaTotalCadernos.delete(0, END)
        self.listaAlteradosCadernos.delete(0, END)
        self.listaTotalChapas.delete(0, END)
        self.listaAlteradasChapas.delete(0, END)
        self.enNomeMaterial.delete(0, END)

    ###salva em PDF
    def exportarPdf(self):
        nomeMaterial = self.enNomeMaterial.get()
        c = canvas.Canvas(nomeMaterial + ".pdf", pagesize=A4)
        c.drawString(230, 750, nomeMaterial)
        c.drawString(72, 700, "Total de páginas: " + str(self.novoMaterial.getPaginasTotal()))
        c.drawString(72, 650, "Total de cadernos: " + str(self.novoMaterial.getCadernos()))
        c.drawString(72, 600, "Total de chapas: " + str(self.novoMaterial.getChapas()))
        c.drawString(350, 700, "Páginas alteradas: " + str(self.novoMaterial.getPaginasAlteradas()))
        c.drawString(350, 650, "Cadernos alterados: " + str(self.novoMaterial.getCadernosAlterados()))
        c.drawString(350, 600, "Chapas alteradas: " + str(self.novoMaterial.getChapasAlteradas()))
        c.drawString(72, 550, "Lista de páginas alteradas:")
        
        i = 0
        linha = 500
        while i < len(self.novoMaterial.getDicionarioAlteradas()):
            c.drawString(72, linha, self.novoMaterial.getDicionarioAlteradasPorCaderno(i))
            linha -= 30
            i += 1
        
        c.save()
        