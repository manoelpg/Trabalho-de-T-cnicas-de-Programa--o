# from datetime import datetime
class Sensor:
    min = 5000.0
    max = 0.0
    soma = 0.0
    conta = 0
    media = 0.0
    devP = 0.0

    def __init__(self, nomeArq):
        self.numArq = nomeArq
        self.readData(nomeArq) #Chamada do método para ler e processar as temperaturas.

#########################################################################
# Método que recebe como parâmetro o nome do arquivo de Temperaturas
# Este método tem como objetivo, extrair os dados do arquivo e converter
# as string em float e depois fazer os calculos simulando um sensor de
# coleta de dados.
#########################################################################
    def readData(self, nomeArq):
        ref_arquivo = open(nomeArq, "r")
        linha = ref_arquivo.readline()
        while linha:
            valores = linha.split()
            val = float(valores[0])
            if val < self.min:
                self.min = val
            if val > self.max:
                self.max = val
            self.soma += val
            self.conta += 1
            self.devP = (self.soma / self.conta) ** 0.5
            self.media = self.soma / self.conta
            linha = ref_arquivo.readline()
            print(f'id: {self.conta} Máximo: {self.min:.2f} Mínimo: {self.max:.2f} Soma: {self.soma:.2f} Média: {self.media:.2f} Desvio Padrão: {self.devP:.2f}')

        ref_arquivo.close()

#########################################################################
# Métodos get, para pegar os dados dos atributos da class e retornam o
# valor
#########################################################################
    def getMax(self):
        return self.max

    def getMin(self):
        return self.min

    def getConta(self):
        return self.conta

    def getSoma(self):
        return self.soma

    def getDesvioPadrao(self):
        return self.devP

    def getMedia(self):
        return self.media

#########################################################################
#Programa Principal onde criamos o objeto e chamamos o método
#########################################################################
app = Sensor('temperature.csv')
print('~' * 75)
print(f'Foram processados: {app.getConta():.2f} temperaturas.')
print(f'A maior temperatura foi de: {app.getMax():.2f}⁰')
print(f'A menor temperatura foi de: {app.getMin():.2f}⁰')
print(f'A soma das {app.getConta()} temperaturas é: {app.getSoma():.2f}')
print(f'A média das temperaturas foi: {app.getMedia():.2f}')
print(f'O desvio padrão das temperaturas é de: {app.getDesvioPadrao():.2f}')
print('~' * 75)