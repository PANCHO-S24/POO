from claseVehiculo import Vehiculo

class Usado (Vehiculo):
    __patente: str
    __kilometros: int
    __anio: int

    def __init__(self, mod, cantPuertas, color, precioBase, patente, km, año) -> None:
        super().__init__(mod, cantPuertas, color, precioBase)
        self.__patente = patente
        self.__kilometros = kilometros
        self.__anio = anio

    def __str__(self) -> str:
        s = f'Modelo: {super().getModelo()}, Cant. de puertas: {super().getCantidadPuertas()}, Color: {super().getColor()}, precio base: {super().getPrecioBase()}, patente: {self.__patente}, kilometros: {self.__km}, año: {self.__anho}'
        return s

    def __str__(self) -> str:
        return super().__str__()

    def getPatente (self):
        return self.__patente

    def getKm (self):
        return self.__kilometros

    def getAño (self):
        return self.__anio

    def setPrecioBase (self, precio):
        super().setPB(precio)
    
    def calcular_importe_venta_usado(self):
        precio_venta = self.precio_base_venta
        if self.anio:
            precio_venta -= (2023 - self.anio) * 1000  # Restar 1000 por cada año de antigüedad
        if self.kilometraje:
            precio_venta -= self.kilometraje * 0.1  # Restar 0.1 por cada kilómetro recorrido
        return precio_venta