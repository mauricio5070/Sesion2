class Animal:
    def __init__(self,esp,ed):
        self.especie=esp
        self.edad=ed

    def correr(self):
        print('Hola soy un {}.''Estoy corriendo '.format(self.especie))

    def crecer(self, edad):
        self.edad=edad


    perro= Animal('Perro',3)

    print('Hola soy un {}.''Tengo {} años '.format(perro.especie, perro.edad))