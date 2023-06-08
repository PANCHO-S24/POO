import unittest
from claseVehiculo import Vehiculo
from claseListaVehiculo import ListaVehiculos

class TestVehiculos(unittest.TestCase):
    def setUp(self):
        self.lista_vehiculos = ListaVehiculos()
        self.vehiculo1 = Vehiculo("Marca1", "Modelo1", 2000, 10000)
        self.vehiculo2 = Vehiculo("Marca2", "Modelo2", 3000, 15000)

    def test_agregar_vehiculo(self):
        self.lista_vehiculos.agregar(self.vehiculo1)
        self.assertEqual(self.lista_vehiculos.mostrar_informacion(0), self.vehiculo1)

    def test_insertar_vehiculo(self):
       self.lista_vehiculos.agregar(self.vehiculo1)
       self.lista_vehiculos.insertar(1, self.vehiculo2)
       self.assertEqual(self.lista_vehiculos.mostrar_informacion(1), self.vehiculo2)