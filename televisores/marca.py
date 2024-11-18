class Marca:
    def __init__(self, nombre):
        self._nombre = nombre  # Atributo privado (convención de privacidad)

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre
