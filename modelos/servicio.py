
from abc import ABC, abstractmethod


class Servicio(ABC):
    """
    Clase abstracta que representa los servicios
    ofrecidos por la empresa Software FJ.
    """

    def __init__(self, codigo, nombre, precio_base):
        # Validar el código del servicio.
        if not codigo or not str(codigo).strip():
            raise ValueError("El código del servicio no puede estar vacío.")

        # Validar el nombre.
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio no es válido.")

        # Validar el precio base.
        if (
            isinstance(precio_base, bool)
            or not isinstance(precio_base, (int, float))
            or precio_base <= 0
        ):
            raise ValueError("El precio base debe ser mayor que cero.")

        # Encapsular los atributos del servicio.
        self.__codigo = str(codigo).strip()
        self.__nombre = nombre.strip()
        self.__precio_base = float(precio_base)

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio_base(self):
        return self.__precio_base

    @abstractmethod
    def calcular_costo(self, duracion, **kwargs):
        """Calcular el costo según el tipo de servicio."""
        pass

    @abstractmethod
    def describir_servicio(self):
        """Describir las características del servicio."""
        pass

    @abstractmethod
    def validar_parametros(self, duracion, **kwargs):
        """Validar los parámetros del servicio."""
        pass
