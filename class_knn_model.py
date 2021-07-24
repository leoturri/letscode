# Criação de classe para exibição dos perfis de investimento considerando o modelo KNN
class Modelo_knn():
    def __init__ (self, k):
        self.k = k
        
    def calcular_distancia(self, a1, a2):
        """
        Método criado para cálculo da função entre dois pontos
        Usada a função zip para que os elementos das tuplas sejam buscados com base nas duas listas: com a classificação de perfis e sem a classificação de perfis.
    
        Args:
        a1 = ponto da tupla com perfil, variando de acordo com o índice
        a2 = ponto da tupla sem perfil, variando de acordo com o índice
    
        Retorno:
        Será retornado uma lista com os valores da distância entre a tupla (variando de acordo com o índice) da lista sem classificação com os outros 120 perfis já definidos.

        Exemplo:
        Tuplas com perfil definido -> (5100., 3500., 1400., 200.)
        Tuplas sem perfil definido -> (5800., 4000., 1200., 200.)

        Cálculo da distância será ((5100 - 5800) **2) + ((3500 - 4000)**2) + (1400 - 1200)**2) + (200 - 200)**2)
        A distância real será o valor encontrado acima elevado a 1/2 (raiz quadrada)
        """
        calc_dist = 0
        for investimento_a1, investimento_a2 in zip(a1, a2):
            calc_dist += ((investimento_a2-investimento_a1)**2)
        dist_real = (calc_dist)**(1/2)
        return dist_real

    def ordenar_lista(self, lista_class):
        """
        Método criado para ordenar a lista das distâncias encontradas comparando as tuplas sem perfil definido com as outras 120 tuplas com perfil definido
        De acordo com a distância e o índice da lista gerada, adicionamos o inverso dessas informações (índice e distância) na variável lista_invertida
        
        Args:
        lista_class: Lista contendo distância e índice
        
        Retorno:
        lista_invertida: Lista contendo índice e distância
        
        Exemplo: 
        lista_class [883.45748, 0]
        lista_invertida [0, 883.45748]
        """
        lista_invertida = []
        for indice, distancia in lista_class:
            lista_invertida.append((distancia, indice))
        lista_ordenada = sorted(lista_invertida)
        return lista_ordenada

    def identifica_dist(self, lista_k, lista_data):
        """
        Método criado para identificar o perfil das "k" distâncias mais próximas na lista com os perfis definidos
        
        Args:
        lista_k: tuplas com as k distâncias mais próximas
        lista_data: lista base com os perfis definidos
        
        Retorno:
        classificar: lista contendo as classificações das k distâncias mais próximas dos elementos lista_data
        
        Exemplo: 
        lista_k: [(412.31056256176606, 23), (583.09518948453, 10), (591.6079783099616, 26), (655.7438524302, 38), (678.2329983125268, 5)]
        lista_data: data
        
        classificar: ['Conservador', 'Conservador', 'Conservador', 'Conservador', 'Conservador']
        """
        
        classificar = []
        for item1, item2 in zip(lista_k, lista_data):
            classificar.append((item1[1]))
        tamanho = len(classificar)
        i = 0
        perfil = []
        for i in classificar:
            perfil.append(lista_data[i][1])
        return perfil

    def exibir_cpf(self, x):
        """
        Método criado para criação de lista contendo cpf que será adicionado ao dicionário com as informações dos clientes sem perfil definido
        
        Args:
        x: lista com os perfis definidos anteriormente
        
        Retorno:
        cpf_lista_real: lista contendo os CPF's dos clientes associados aos perfis da lista x
        """
        cpf_lista_real = []
        for pessoa in x:
            cpf_lista_real.append(pessoa[0])
        return cpf_lista_real