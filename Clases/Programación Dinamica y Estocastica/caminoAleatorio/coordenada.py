class Coordenada:

    def __init__(self):
        self.x = x
        self.y =y

    def mover(self,delta_x,delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)

    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x
        deñta_y = self.y - otra_coordenada.y

        return (delta_x**2 + delta_y**2)**0.5