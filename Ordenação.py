class Sorter:
    def __init__(self):
        pass

    def ordene_selection(self,valores, i=0):
        n = len(valores)

        if i == n - 1:
            return valores
        min = i
        for j in range(i + 1, n):
            if valores[j] < valores[min]:
                min = j
        if min != i:
            aux = valores[i]
            valores[i] = valores[min]
            valores[min] = aux

        return self.ordene_selection(valores, i + 1)

    def ordene_insertion(self,valores, n=None):
        if n is None:
            n = len(valores)
    
        if n <= 1:
            return valores
    
        self.ordene_insertion(valores, n-1)
    
        i = n - 1
        j = i
        while j > 0 and valores[j-1] > valores[j]:
            aux = valores[j]
            valores[j] = valores[j-1]
            valores[j-1] = aux
            j = j - 1
    
        return valores
    
    def ordene_insertion_letras(self, letras):
        for i in range(1, len(letras)):
           j=i
           while j>0 and letras[j-1]>letras[j]:
             aux = letras[j]
             letras[j] = letras[j-1]
             letras[j-1] = aux
             j = j-1
        return letras