
from modelos.cliente import Cliente
from modelos.servicio import Servicio


class Reserva:
    """
    Clase que administra las reservas de Software FJ.
    Integra clientes, servicios, duración y estado.
    """

    def __init__(self, codigo, cliente, servicio, duracion):
        # Validar el código.
        if not codigo or not str(codigo).strip():
            raise ValueError("El código de reserva no puede estar vacío.")

        # Validar el cliente.
        if not isinstance(cliente, Cliente):
            raise TypeError("La reserva requiere un cliente válido.")

        # Validar el servicio.
        if not isinstance(servicio, Servicio):
            raise TypeError("La reserva requiere un servicio válido.")

        # Validar la duración.
        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
            or duracion <= 0
        ):
            raise ValueError("La duración debe ser mayor que cero.")

        # Encapsular los atributos.
        self.__codigo = str(codigo).strip()
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion

        # Estado inicial de la reserva.
        self.__estado = "pendiente"
        self.__costo = None

    @property
    def codigo(self):
        return self.__codigo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    def confirmar(self):
        """Confirmar una reserva pendiente."""

        if self.__estado != "pendiente":
            raise ValueError(
                "Solamente se pueden confirmar reservas pendientes."
            )

        self.__estado = "confirmada"
        return "Reserva confirmada correctamente."

    def cancelar(self):
        """Cancelar una reserva pendiente o confirmada."""

        if self.__estado not in ("pendiente", "confirmada"):
            raise ValueError(
                "No se puede cancelar una reserva procesada o cancelada."
            )

        self.__estado = "cancelada"
        return "Reserva cancelada correctamente."

    def procesar(self, **kwargs):
        """
        Procesar la reserva y calcular su costo.
        Utiliza encadenamiento de excepciones.
        """

        if self.__estado != "confirmada":
            raise ValueError(
                "La reserva debe estar confirmada antes de procesarse."
            )

        try:
            self.__costo = self.__servicio.calcular_costo(
                self.__duracion, **kwargs
            )

            self.__estado = "procesada"

            return self.__costo

        except (ValueError, TypeError) as error:
            raise RuntimeError(
                "No fue posible procesar la reserva."
            ) from error

    def mostrar_informacion(self):
        """Mostrar los datos generales de la reserva."""

        return (
            f"Código de reserva: {self.__codigo}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion}\n"
            f"Estado: {self.__estado}\n"
            f"Costo: {self.__costo if self.__costo is not None else 'Pendiente'}"
        )
