from tkinter import *
import re

class Material:

    def __init__(self, paginas):
        self.paginas = paginas
        self.versoBranco = False
        self.paginasPorCaderno = 16
        self.paginasTotal = 0
        self.dicionario = {}
        self.cadernos = 0
        self.chapas = 0
        self.paginasAlteradas = 0
        self.grupoAlteradas = []
        self.dicionarioAlteradas = {}
        self.cadernosAlterados = 0
        self.chapasAlteradas = 0
    
    #getter and setters das variáveis.

    def getPaginas(self):
        return self.paginas

    #Modifica o número de páginas.    
    def setPaginas(self, paginas):
        self.paginas = paginas
        return paginas

    def getVersoBranco(self):
        return self.versoBranco

    #Clicar no checkbox de verso branco.
    def setVersoBranco(self, varVersoBranco):
        if varVersoBranco == 1:
            return self.versoBranco == True
        else:
            return self.versoBranco == False

    def getPaginasPorCaderno(self):
        return self.paginasPorCaderno

    #Número de págias por caderno.
    def setPaginasPorCaderno(self, varMontagem):
        self.paginasPorCaderno = varMontagem
        return varMontagem

    def getPaginasTotal(self):
        return self.paginasTotal

    #Cálculo do total de páginas, dobra as páginas se tem o verso branco.
    def setPaginasTotal(self):
        if self.versoBranco == True:
            self.paginasTotal =  int(self.paginas) * 2
        else:
            self.paginasTotal = self.paginas
        
    def getCadernos(self):
        return self.cadernos

    #Cálculo do total de cadernos.
    def setCadernos(self):
        cadernosTotal = int(int(self.paginasTotal) / self.paginasPorCaderno)
        cadernosFloat = float(self.paginasTotal) / self.paginasPorCaderno
        
        tr = ""

        if cadernosFloat - cadernosTotal == 0.25:
            tr = " + 1TR-TR"
        elif cadernosFloat - cadernosTotal == 0.5:
            tr = " + 1TR"
        elif cadernosFloat - cadernosTotal == 0.75:
            tr = " + 1TR + 1TR-TR"
        
        self.cadernos = str(cadernosTotal) + tr

    def getChapas(self):
        return self.chapas

    #Cálculo do total de chaoas.
    def setChapas(self):
        cadernosTotal = int(int(self.paginasTotal) / self.paginasPorCaderno)
        cadernosFloat = float(self.paginasTotal) / self.paginasPorCaderno

        chapasRestantes = 0

        if cadernosFloat - cadernosTotal == 0.25:
            chapasRestantes = 4
        elif cadernosFloat - cadernosTotal == 0.5:
            chapasRestantes = 4
        elif cadernosFloat - cadernosTotal == 0.75:
            chapasRestantes = 8
        else:
            chapasRestantes = 0

        self.chapas = (cadernosTotal * 8) + chapasRestantes

    def getDicionario(self):
        return self.dicionario

    #Calcula qual o caderno se localiza a página.
    def contaCaderno(self, pagina):
        if pagina == self.paginasPorCaderno:
            return 1
        else:
            return round((pagina / self.paginasPorCaderno) + 0.5)
            

    #Verifica se a página está no caderno A ou B e coloca no dicionário.
    def cadernoAB(self, pagina):
        if self.versoBranco == False:
            resultado = int(pagina) % self.paginasPorCaderno
            if resultado == 1 or resultado == 4 or resultado == 5 or resultado == 8 or resultado == 9 or resultado == 12 or resultado == 13 or resultado == 16 or resultado == 17 or resultado == 20 or resultado == 21 or resultado == 24 or resultado == 25 or resultado == 28 or resultado == 29 or resultado == 0:
                return str(self.contaCaderno(pagina)) + "A"
            elif resultado == 2 or resultado == 3 or resultado == 6 or resultado == 7 or resultado == 10 or resultado == 11 or resultado == 14 or resultado == 15 or resultado == 18 or resultado == 19 or resultado == 22 or resultado == 23 or resultado == 26 or resultado == 27 or resultado == 30 or resultado == 31:
                return str(self.contaCaderno(pagina)) + "B"
        elif self.versoBranco == True:
            resultado = (int(pagina) + (int(pagina) - 1)) % self.paginasPorCaderno
            if resultado == 1 or resultado == 4 or resultado == 5 or resultado == 8 or resultado == 9 or resultado == 12 or resultado == 13 or resultado == 16 or resultado == 17 or resultado == 20 or resultado == 21 or resultado == 24 or resultado == 25 or resultado == 28 or resultado == 29 or resultado == 0:
                return str(self.contaCaderno(pagina)) + "A"
            elif resultado == 2 or resultado == 3 or resultado == 6 or resultado == 7 or resultado == 10 or resultado == 11 or resultado == 14 or resultado == 15 or resultado == 18 or resultado == 19 or resultado == 22 or resultado == 23 or resultado == 26 or resultado == 27 or resultado == 30 or resultado == 31:
                return str(self.contaCaderno(pagina)) + "B"

    #Cria um dicionario com o total de páginas em cada caderno junto com as funções contaCaderno e cadernoAB
    def setDicionario(self):
        grupoPaginasTotal = []

        x = range(int(self.paginasTotal))

        for n in x:
            grupoPaginasTotal.append(n + 1)
        
        while len(grupoPaginasTotal) > 0:

            if len(grupoPaginasTotal) > (self.paginasPorCaderno - 1):
                calculoTR = int(self.paginasTotal) % self.paginasPorCaderno
                if calculoTR == 0:
                    while len(grupoPaginasTotal) > 0:
                        if self.cadernoAB(grupoPaginasTotal[0]) in self.dicionario:
                            self.dicionario[self.cadernoAB(grupoPaginasTotal[0])].append(grupoPaginasTotal[0])
                        else:
                            self.dicionario[self.cadernoAB(grupoPaginasTotal[0])] = [grupoPaginasTotal[0]]
                        grupoPaginasTotal.pop(0)

                elif calculoTR == (self.paginasPorCaderno / 4):
                    while len(grupoPaginasTotal) > (self.paginasPorCaderno / 4):
                        if self.cadernoAB(grupoPaginasTotal[0]) in self.dicionario:
                            self.dicionario[self.cadernoAB(grupoPaginasTotal[0])].append(grupoPaginasTotal[0])
                        else:
                            self.dicionario[self.cadernoAB(grupoPaginasTotal[0])] = [grupoPaginasTotal[0]]
                        grupoPaginasTotal.pop(0)

                elif calculoTR == (self.paginasPorCaderno / 2):
                    while len(grupoPaginasTotal) > (self.paginasPorCaderno / 2):
                        if self.cadernoAB(grupoPaginasTotal[0]) in self.dicionario:
                            self.dicionario[self.cadernoAB(grupoPaginasTotal[0])].append(grupoPaginasTotal[0])
                        else:
                            self.dicionario[self.cadernoAB(grupoPaginasTotal[0])] = [grupoPaginasTotal[0]]
                        grupoPaginasTotal.pop(0)

                elif calculoTR == (self.paginasPorCaderno * 75 / 100):
                    while len(grupoPaginasTotal) > (self.paginasPorCaderno * 75 / 100):
                        if self.cadernoAB(grupoPaginasTotal[0]) in self.dicionario:
                            self.dicionario[self.cadernoAB(grupoPaginasTotal[0])].append(grupoPaginasTotal[0])
                        else:
                            self.dicionario[self.cadernoAB(grupoPaginasTotal[0])] = [grupoPaginasTotal[0]]
                        grupoPaginasTotal.pop(0)

            elif len(grupoPaginasTotal) == (self.paginasPorCaderno / 4):
                while len(grupoPaginasTotal) > 0:
                    if "TR-TR" in self.dicionario:
                        self.dicionario["TR-TR"].append(grupoPaginasTotal[0])
                    else:
                        self.dicionario["TR-TR"] = [grupoPaginasTotal[0]]
                    grupoPaginasTotal.pop(0)

            elif len(grupoPaginasTotal) == (self.paginasPorCaderno / 2):
                while len(grupoPaginasTotal) > 0:
                    if "TR" in self.dicionario:
                        self.dicionario["TR"].append(grupoPaginasTotal[0])
                    else:
                        self.dicionario["TR"] = [grupoPaginasTotal[0]]
                    grupoPaginasTotal.pop(0)

            elif len(grupoPaginasTotal) == (self.paginasPorCaderno * 75 / 100):
                while len(grupoPaginasTotal) > (self.paginasPorCaderno / 4):
                    if "TR" in self.dicionario:
                        self.dicionario["TR"].append(grupoPaginasTotal[0])
                    else:
                        self.dicionario["TR"] = [grupoPaginasTotal[0]]
                    grupoPaginasTotal.pop(0)

    def getPaginasAlteradas(self):
        return self.paginasAlteradas

    #Função para organizar as páginas alteradas.
    def bubble_sort(self, listaTemporaria):
        for i in range(len(listaTemporaria)-1):
            for j in range(len(listaTemporaria)-i-1):
                if(listaTemporaria[j] > listaTemporaria[j+1]):
                    listaTemporaria[j], listaTemporaria[j+1] = listaTemporaria[j+1], listaTemporaria[j]

    #Faz o grupo das páginas alteradas e seu caderno.
    def setPaginasAlteradas(self, paginasAlteradas):
        
        temporarioGrupoAlteradas = re.sub(" ","", str(paginasAlteradas))
        temporarioGrupoAlteradas = re.split(';|,|/|\\n', temporarioGrupoAlteradas)

        y = 0
        while y < len(temporarioGrupoAlteradas):
            string = temporarioGrupoAlteradas[y]
            
            if "-" in str(string):
                temporario = re.split('-', string)
                x = temporarioGrupoAlteradas.index(string)
                temporarioGrupoAlteradas.pop(x)
                z = range(int(temporario[0]), int(temporario[1]) + 1)
                for n in z:
                    if n in temporarioGrupoAlteradas:
                        None
                    else:
                        temporarioGrupoAlteradas.append(int(n))
            else:
                y += 1

        z = 0
        while z < int(len(temporarioGrupoAlteradas)):
            if int(temporarioGrupoAlteradas[z]) in self.grupoAlteradas:
                None
            else:
                self.grupoAlteradas.append(int(temporarioGrupoAlteradas[z]))
            z += 1
        
        self.paginasAlteradas = len(self.grupoAlteradas)

    def getGrupoAlteradas(self):
        return self.grupoAlteradas
    
    #Retorna o dicionário de cadernos alterados com suas respectivas páginas
    def getDicionarioAlteradas(self):
        return self.dicionarioAlteradas
    
    def getDicionarioAlteradasPorCaderno(self, caderno):
        dicionarioChaves = list(self.dicionarioAlteradas.keys())
        dicionarioValores = list(self.dicionarioAlteradas.values())
        return "Caderno: " + str(dicionarioChaves[caderno]) + ". " + "Páginas " + str(dicionarioValores[caderno])
    
    #Adiciona caderno e páginas alteradas ao dicionário
    def setDicionarioAlteradas(self):
        self.dicionarioAlteradas = {}
        if len(self.grupoAlteradas) > 1:
            self.bubble_sort(self.grupoAlteradas)

        dicionarioChaves = list(self.dicionario.keys())
        dicionarioValores = list(self.dicionario.values())

        i = 0

        while i < len(dicionarioChaves):

            x = dicionarioValores[i]
            j = 0

            while j < len(self.grupoAlteradas):

                if int(self.grupoAlteradas[j]) in x:
                    
                    chaveAlteradas = dicionarioChaves[i]
                    valorAlteradas = self.grupoAlteradas[j]
                    
                    if str(chaveAlteradas) in self.dicionarioAlteradas.keys():
                        if int(valorAlteradas) in self.dicionarioAlteradas[str(chaveAlteradas)]:
                            pass
                        else:
                            self.dicionarioAlteradas[str(chaveAlteradas)].append(valorAlteradas)
                    else:
                        self.dicionarioAlteradas[str(chaveAlteradas)] = [valorAlteradas]
                    
                    j = j + 1
                else:
                    j = j + 1

            i += 1

    #Remove páginas alteradas.
    def setRemoverPaginasAlteradas(self, paginasAlteradas):

        temporarioGrupoAlteradas = re.sub(" ","", str(paginasAlteradas))
        temporarioGrupoAlteradas = re.split(';|,|/|\\n', temporarioGrupoAlteradas)

        y = 0
        while y < len(temporarioGrupoAlteradas):
            string = temporarioGrupoAlteradas[y]
            
            if "-" in str(string):
                temporario = re.split('-', string)
                x = temporarioGrupoAlteradas.index(string)
                temporarioGrupoAlteradas.pop(x)
                z = range(int(temporario[0]), int(temporario[1]) + 1)
                for n in z:
                    if n in temporarioGrupoAlteradas:
                        None
                    else:
                        temporarioGrupoAlteradas.append(int(n))
            else:
                y += 1

        z = 0
        while z < int(len(temporarioGrupoAlteradas)):
            
            if int(temporarioGrupoAlteradas[z]) in self.grupoAlteradas:
                self.grupoAlteradas.remove(int(temporarioGrupoAlteradas[z]))
            else:
                None
            z += 1
        
        self.paginasAlteradas = len(self.grupoAlteradas)

    #Retorna os cadernos alterados.
    def getCadernosAlterados(self):
        return self.cadernosAlterados

    def setCadernosAlterados(self):
        dicionarioChaves = list(self.dicionarioAlteradas.keys())
        
        if len(dicionarioChaves) == 1:
                if "TR-TR" in dicionarioChaves[-1]:
                    self.cadernosAlterados = "TR-TR"
                elif "TR" in dicionarioChaves[-1]:
                    self.cadernosAlterados = "TR"
                else:
                    self.cadernosAlterados = len(self.dicionarioAlteradas) / 2
        else:
            if "TR-TR" in dicionarioChaves[-1] and "TR" in dicionarioChaves[-2]:
                self.cadernosAlterados = str(len((self.dicionarioAlteradas) - 1) / 2) + " + TR" + " + TR-TR"
            else:
                if "TR-TR" in dicionarioChaves[-1]:
                    self.cadernosAlterados = str((len(self.dicionarioAlteradas) - 1) / 2) + " + TR-TR"
                elif "TR" in dicionarioChaves[-1]:
                    self.cadernosAlterados = str((len(self.dicionarioAlteradas) - 1) / 2) + " + TR"
                else:
                    self.cadernosAlterados = len(self.dicionarioAlteradas) / 2

    #Retorna as chapas alteradas.
    def getChapasAlteradas(self):
        return self.chapasAlteradas

    def setChapasAlteradas(self):
        self.chapasAlteradas = int(len(self.dicionarioAlteradas) / 2 * 8)

