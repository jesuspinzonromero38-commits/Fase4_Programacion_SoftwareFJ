
from modelos.servicio import Servicio


class ReservaSala(Servicio):
    """
    Servicio especializado para reservar salas
    de reuniones de la empresa Software FJ.
    """

    def __init__(self, codigo, nombre, precio_base, numero_sala, capacidad):
        # Inicializar los atributos heredados.
        super().__init__(codigo, nombre, precio_base)

        # Validar el número de sala.
        if not isinstance(numero_sala, str) or not numero_sala.strip():
            raise ValueError("El número de sala no es válido.")

        # Validar la capacidad.
        if (
            isinstance(capacidad, bool)
            or not isinstance(capacidad, int)
            or capacidad <= 0
        ):
            raise ValueError("La capacidad debe ser un entero positivo.")

        self.__numero_sala = numero_sala.strip()
        self.__capacidad = capacidad

    @property
    def numero_sala(self):
        return self.__numero_sala

    @property
    def capacidad(self):
        return self.__capacidad

    def validar_parametros(self, duracion, **kwargs):
        """Validar duración, asistentes, impuestos y descuentos."""

        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
            or duracion <= 0
        ):
            raise ValueError("La duración debe ser mayor que cero.")

        asistentes = kwargs.get("asistentes", 1)

        if (
            isinstance(asistentes, bool)
            or not isinstance(asistentes, int)
            or asistentes <= 0
            or asistentes > self.__capacidad
        ):
            raise ValueError(
                "La cantidad de asistentes supera la capacidad de la sala."
            )

        for parametro in ("descuento", "impuesto"):
            porcentaje = kwargs.get(parametro, 0)

            if (
                isinstance(porcentaje, bool)
                or not isinstance(porcentaje, (int, float))
                or not 0 <= porcentaje <= 100
            ):
                raise ValueError(
                    f"El porcentaje de {parametro} debe estar entre 0 y 100."
                )

        return True

    def calcular_costo(self, duracion, **kwargs):
        """Calcular el costo de reservar una sala por horas."""

        self.validar_parametros(duracion, **kwargs)

        subtotal = self.precio_base * duracion

        descuento = kwargs.get("descuento", 0)
        impuesto = kwargs.get("impuesto", 0)

        subtotal -= subtotal * descuento / 100
        total = subtotal + (subtotal * impuesto / 100)

        return round(total, 2)

    def describir_servicio(self):
        """Mostrar la descripción de la sala."""

        return (
            f"Servicio: {self.nombre}\n"
            f"Código: {self.codigo}\n"
            f"Número de sala: {self.__numero_sala}\n"
            f"Capacidad: {self.__capacidad} personas\n"
            f"Precio por hora: ${self.precio_base:,.2f}"
        )
