from tkinter import *

dicionario = {}

grupoAlteradas = []

paginasPorCaderno = 16

numeroPaginasTotal = 0

class Funcoes():

    ###arruma os dados quando aperta o checkbox
    def quantidadeDePaginas(self):
        global numeroPaginasTotal
        if self.varVersoBranco.get() == 1:
            numeroPaginasTotal = int(self.listaTotalPaginas.get(0)) * 2

        elif self.varVersoBranco.get() == 0:
            numeroPaginasTotal = int(self.listaTotalPaginas.get(0)) / 2
        return int(numeroPaginasTotal)

    def quantidadePaginasTotal(self):
        global numeroPaginasTotal
        numeroPaginasTotal = self.entrada.get()
        return int(numeroPaginasTotal)

    #Calcula qual o caderno se localiza (para o total de páginas).
    def contaCaderno(self, pagina):
        paginasPorCaderno
        if pagina == paginasPorCaderno:
            return 1
        else:
            return round((pagina / paginasPorCaderno) + 0.5)
    
    #Verifica se a página está no caderno A ou B (para o total de páginas).
    def cadernoAB(self, pagina):
        paginasPorCaderno
        if self.varVersoBranco.get() == 0:
            resultado = int(pagina) % paginasPorCaderno
            if resultado == 1 or resultado == 4 or resultado == 5 or resultado == 8 or resultado == 9 or resultado == 12 or resultado == 13 or resultado == 16 or resultado == 17 or resultado == 20 or resultado == 21 or resultado == 24 or resultado == 25 or resultado == 28 or resultado == 29 or resultado == 0:
                dicionario[pagina] = str(self.contaCaderno(pagina)) + "A"
            elif resultado == 2 or resultado == 3 or resultado == 6 or resultado == 7 or resultado == 10 or resultado == 11 or resultado == 14 or resultado == 15 or resultado == 18 or resultado == 19 or resultado == 22 or resultado == 23 or resultado == 26 or resultado == 27 or resultado == 30 or resultado == 31:
                dicionario[pagina] = str(self.contaCaderno(pagina)) + "B"
        elif self.varVersoBranco.get() == 1:
            resultado = (int(pagina) + (int(pagina) - 1)) % paginasPorCaderno
            if resultado == 1 or resultado == 4 or resultado == 5 or resultado == 8 or resultado == 9 or resultado == 12 or resultado == 13 or resultado == 16 or resultado == 17 or resultado == 20 or resultado == 21 or resultado == 24 or resultado == 25 or resultado == 28 or resultado == 29 or resultado == 0:
                dicionario[pagina] = str(self.contaCaderno(pagina)) + "A"
            elif resultado == 2 or resultado == 3 or resultado == 6 or resultado == 7 or resultado == 10 or resultado == 11 or resultado == 14 or resultado == 15 or resultado == 18 or resultado == 19 or resultado == 22 or resultado == 23 or resultado == 26 or resultado == 27 or resultado == 30 or resultado == 31:
                dicionario[pagina] = str(self.contaCaderno(pagina)) + "B"


    #Cria um dicionario com 8 páginas em cada caderno.
    def cadernoPaginas(self):
        global paginasPorCaderno
        paginasPorCaderno = self.varMontagem.get()
        paginasTotal = []
        numeros_int = int(numeroPaginasTotal)
        global dicionario

        x = range(numeros_int)

        for n in x:
            paginasTotal.append(n + 1)
        
        while len(paginasTotal) > 0:
            if len(paginasTotal) > (paginasPorCaderno - 1):
                calculoTR = numeros_int % paginasPorCaderno
                if calculoTR == 0:
                    while len(paginasTotal) > 0:
                        self.cadernoAB(paginasTotal[0])
                        paginasTotal.pop(0)
                elif calculoTR == (paginasPorCaderno / 4):
                    while len(paginasTotal) > (paginasPorCaderno / 4):
                            self.cadernoAB(paginasTotal[0])
                            paginasTotal.pop(0)
                elif calculoTR == (paginasPorCaderno / 2):
                    while len(paginasTotal) > (paginasPorCaderno / 2):
                            self.cadernoAB(paginasTotal[0])
                            paginasTotal.pop(0)
                elif calculoTR == (paginasPorCaderno * 75 / 100):
                    while len(paginasTotal) > (paginasPorCaderno * 75 / 100):
                            self.cadernoAB(paginasTotal[0])
                            paginasTotal.pop(0)
            elif len(paginasTotal) == (paginasPorCaderno / 4):
                while len(paginasTotal) > 0:
                    dicionario[paginasTotal[0]] = str(self.contaCaderno(paginasTotal[0])) + "TR-TR"
                    paginasTotal.pop(0)
            elif len(paginasTotal) == (paginasPorCaderno / 2):
                while len(paginasTotal) > 0:
                    dicionario[paginasTotal[0]] = str(self.contaCaderno(paginasTotal[0])) + "TR"
                    paginasTotal.pop(0)
            elif len(paginasTotal) == (paginasPorCaderno * 75 / 100):
                while len(paginasTotal) > (paginasPorCaderno / 4):
                    dicionario[paginasTotal[0]] = str(self.contaCaderno(paginasTotal[0])) + "TR"
                    paginasTotal.pop(0)

    #Calcula o número de cadernos e chapas (Total).
    def calculoCadernosTotal(self):
        numeroPaginasTotalInt = int(numeroPaginasTotal)
        numeroPaginasTotalFloat = float(numeroPaginasTotal)
        cadernosTotal = int(numeroPaginasTotalInt / paginasPorCaderno)
        cadernosFloat = numeroPaginasTotalFloat / paginasPorCaderno
        
        tr = ""

        if cadernosFloat - cadernosTotal == 0.25:
            tr = " + 1TR-TR"
        elif cadernosFloat - cadernosTotal == 0.5:
            tr = " + 1TR"
        elif cadernosFloat - cadernosTotal == 0.75:
            tr = " + 1TR + 1TR-TR"
        
        return str(cadernosTotal) + tr
    
    def calculoChapasTotal(self):
        numeroPaginasTotalInt = int(numeroPaginasTotal)
        numeroPaginasTotalFloat = float(numeroPaginasTotal)
        cadernosTotal = int(numeroPaginasTotalInt / paginasPorCaderno)
        cadernosFloat = numeroPaginasTotalFloat / paginasPorCaderno

        tr2 = 0

        if cadernosFloat - cadernosTotal == 0.25:
            tr2 = 4
        elif cadernosFloat - cadernosTotal == 0.5:
            tr2 = 4
        elif cadernosFloat - cadernosTotal == 0.75:
            tr2 = 8
        else:
            tr2 = 0

        return (cadernosTotal * 8) + tr2

    def bubble_sort(self, listaTemporaria):
        for i in range(len(listaTemporaria)-1):
            for j in range(len(listaTemporaria)-i-1):
                if(listaTemporaria[j] > listaTemporaria[j+1]):
                    listaTemporaria[j], listaTemporaria[j+1] = listaTemporaria[j+1], listaTemporaria[j]

    #Faz o grupo das páginas alteradas e seu caderno.
    def calculoAlteradas(self):
        global paginasAlteradas
        global paginasAlteradas2
        paginaInicial = self.paginasAlteradas.get()
        paginaFinal = self.paginasAlteradas2.get()
        
        global grupoAlteradas
        global dicionario

        if paginaFinal == "":
            temporarioGrupoAlteradas = paginaInicial.split(" ")
            i = 0
            while i < len(temporarioGrupoAlteradas):
                if int(temporarioGrupoAlteradas[i]) in grupoAlteradas:
                    None
                else:
                    grupoAlteradas.append(int(temporarioGrupoAlteradas[i]))
                i += 1
        else:
            z = range(int(paginaInicial), int(paginaFinal) + 1)
            for n in z:
                if n in grupoAlteradas:
                    None
                else:
                    grupoAlteradas.append(int(n))
        
        if len(grupoAlteradas) > 1:
            self.bubble_sort(grupoAlteradas)

        self.lista.delete(0, END)

        i = 0
        while i < len(grupoAlteradas):
            self.lista.insert(END, str(grupoAlteradas[i]) + " " + str(dicionario.get(int(grupoAlteradas[i]))))
            i += 1

        return grupoAlteradas

    #calcula o número de cadernos alerados e páginas alteradas
    def calculoChapasCadernosAlteradas(self):
        
        global dicionario
        global grupoAlteradas
        grupoCadernosAlterados = []

        i = 0
        while i < len(grupoAlteradas):
            if dicionario.get(int(grupoAlteradas[i])) in grupoCadernosAlterados:
                i += 1
            else:
                grupoCadernosAlterados.append(dicionario.get(int(grupoAlteradas[i])))
                i += 1

        CadernosAlterados = len(grupoCadernosAlterados) / 2

        return CadernosAlterados

        #limpa toda tela.
    def limpa_tela2(self):
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
        