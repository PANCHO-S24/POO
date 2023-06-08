from claseVehiculo import Vehiculo

class Nuevo (Vehiculo):
    __version: str
    __marca: str

    def __init__(self, modelo, puertas, color, precio_base, version) -> None:
        super().__init__(modelo, puertas, color, precio_base)
        self.__version = version
        self.__marca= marca

    def __str__(self) -> str:
        s = f'Modelo: {super().getModelo()}, Cant. de puertas: {super().getCantidadPuertas()}, Color: {super().getColor()}, precio base: {super().getPrecioBase()}, version: {self.__version}'
        return s

    def getVersion (self):
        return self.__version
    def get_marca (self):
        return self.__marca