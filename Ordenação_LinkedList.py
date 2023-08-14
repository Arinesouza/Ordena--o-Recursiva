class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def set_proximo(self, no):
        self.proximo = no

    def get_proximo(self):
        return self.proximo

    def ordene_selection_LinkedList(inicio):
        if inicio is None:
            return None
        
        atual = inicio
        while atual is not None:
            minimo = atual
            aux = atual.get_proximo()
            while aux is not None:
                if aux.valor < minimo.valor:
                    minimo = aux
                aux = aux.get_proximo()

            aux_valor = atual.valor
            atual.valor = minimo.valor
            minimo.valor = aux_valor

            atual = atual.get_proximo()
