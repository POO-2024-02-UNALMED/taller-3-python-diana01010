class TV:
    numTV = 0  

    def __init__(self, marca, estado):
        TV.numTV += 1  
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = None  

   
    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getCanal(self):
        return self.canal

    def setCanal(self, canal):
        self.canal = canal

    def getPrecio(self):
        return self.precio

    def setPrecio(self, precio):
        self.precio = precio

    def getVolumen(self):
        return self.volumen

    def setVolumen(self, volumen):
        self.volumen = volumen

    def getControl(self):
        return self.control

    def setControl(self, control):
        self.control = control

   
    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado

   
    def canalUp(self):
        if self.estado and self.canal < 120:
            self.canal += 1

    def canalDown(self):
        if self.estado and self.canal > 1:
            self.canal -= 1

   
    def volumenUp(self):
        if self.estado and self.volumen < 7:
            self.volumen += 1

    def volumenDown(self):
        if self.estado and self.volumen > 0:
            self.volumen -= 1

    
    @classmethod
    def getNumTV(cls):
        return cls.numTV
