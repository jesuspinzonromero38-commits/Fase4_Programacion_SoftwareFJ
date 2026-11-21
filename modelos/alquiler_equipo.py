
from modelos.servicio import Servicio


class AlquilerEquipo(Servicio):
    """
    Servicio especializado para el alquiler
    de equipos tecnológicos de Software FJ.
    """

    def __init__(
        self, codigo, nombre, precio_base,
        tipo_equipo, unidades_disponibles
    ):
        # Inicializar los atributos heredados.
        super().__init__(codigo, nombre, precio_base)

        # Validar el tipo de equipo.
        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise ValueError("El tipo de equipo no es válido.")

        # Validar las unidades disponibles.
        if (
            isinstance(unidades_disponibles, bool)
            or not isinstance(unidades_disponibles, int)
            or unidades_disponibles < 0
        ):
            raise ValueError("Las unidades disponibles no son válidas.")

        self.__tipo_equipo = tipo_equipo.strip()
        self.__unidades_disponibles = unidades_disponibles

    @property
    def tipo_equipo(self):
        return self.__tipo_equipo

    @property
    def unidades_disponibles(self):
        return self.__unidades_disponibles

    def validar_parametros(self, duracion, **kwargs):
        """Validar duración y cantidad de equipos solicitados."""

        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
            or duracion <= 0
        ):
            raise ValueError("La duración del alquiler debe ser positiva.")

        cantidad = kwargs.get("cantidad", 1)

        if (
            isinstance(cantidad, bool)
            or not isinstance(cantidad, int)
            or cantidad <= 0
        ):
            raise ValueError("La cantidad debe ser un entero positivo.")

        if cantidad > self.__unidades_disponibles:
            raise ValueError("No hay suficientes equipos disponibles.")

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
        """Calcular el costo total del alquiler."""

        self.validar_parametros(duracion, **kwargs)

        cantidad = kwargs.get("cantidad", 1)
        descuento = kwargs.get("descuento", 0)
        impuesto = kwargs.get("impuesto", 0)

        subtotal = self.precio_base * duracion * cantidad
        subtotal -= subtotal * descuento / 100

        total = subtotal + (subtotal * impuesto / 100)

        return round(total, 2)

    def describir_servicio(self):
        """Describir el servicio de alquiler."""

        return (
            f"Servicio: {self.nombre}\n"
            f"Código: {self.codigo}\n"
            f"Tipo de equipo: {self.__tipo_equipo}\n"
            f"Unidades disponibles: {self.__unidades_disponibles}\n"
            f"Precio por día: ${self.precio_base:,.2f}"
        )
