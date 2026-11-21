
import re
from modelos.entidad import Entidad


class Cliente(Entidad):
    """
    Clase que representa a los clientes de Software FJ.
    Hereda los atributos y métodos de Entidad.
    """

    def __init__(self, identificador, nombre, correo, telefono):
        # Inicializar los atributos heredados de Entidad.
        super().__init__(identificador)

        # Validar el nombre.
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del cliente no es válido.")

        # Validar el correo electrónico.
        if not isinstance(correo, str) or not re.fullmatch(
            r"[^@\s]+@[^@\s]+\.[^@\s]+", correo.strip()
        ):
            raise ValueError("El correo electrónico no es válido.")

        # Validar el teléfono.
        if not isinstance(telefono, str) or not re.fullmatch(
            r"\+?\d{7,15}", telefono.strip()
        ):
            raise ValueError("El número de teléfono no es válido.")

        # Encapsular los datos personales.
        self.__nombre = nombre.strip()
        self.__correo = correo.strip().lower()
        self.__telefono = telefono.strip()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_informacion(self):
        """Mostrar la información del cliente."""
        return (
            f"Identificación: {self.identificador}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )
