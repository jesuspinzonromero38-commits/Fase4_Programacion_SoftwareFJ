
from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa las entidades generales
    del sistema de gestión Software FJ.
    """

    def __init__(self, identificador):
        # Validar que el identificador no esté vacío.
        if not identificador or not str(identificador).strip():
            raise ValueError("El identificador no puede estar vacío.")

        # Encapsular el identificador.
        self._identificador = str(identificador).strip()

    @property
    def identificador(self):
        """Permite consultar el identificador."""
        return self._identificador

    @abstractmethod
    def mostrar_informacion(self):
        """
        Método abstracto que deberán implementar
        las clases que hereden de Entidad.
        """
        pass
