
from modelos.servicio import Servicio


class AsesoriaEspecializada(Servicio):
    """
    Servicio especializado para asesorías profesionales
    de Software FJ.
    """

    def __init__(
        self, codigo, nombre, precio_base,
        especialidad, modalidad
    ):
        # Inicializar los atributos heredados.
        super().__init__(codigo, nombre, precio_base)

        # Validar especialidad.
        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError("La especialidad no es válida.")

        # Validar modalidad.
        modalidades_validas = ("virtual", "presencial")

        if (
            not isinstance(modalidad, str)
            or modalidad.strip().lower() not in modalidades_validas
        ):
            raise ValueError("La modalidad debe ser virtual o presencial.")

        self.__especialidad = especialidad.strip()
        self.__modalidad = modalidad.strip().lower()

    @property
    def especialidad(self):
        return self.__especialidad

    @property
    def modalidad(self):
        return self.__modalidad

    def validar_parametros(self, duracion, **kwargs):
        """Validar duración y porcentajes de la asesoría."""

        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
            or duracion <= 0
        ):
            raise ValueError(
                "La duración de la asesoría debe ser positiva."
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
        """Calcular el costo de la asesoría por horas."""

        self.validar_parametros(duracion, **kwargs)

        subtotal = self.precio_base * duracion

        descuento = kwargs.get("descuento", 0)
        impuesto = kwargs.get("impuesto", 0)

        subtotal -= subtotal * descuento / 100
        total = subtotal + (subtotal * impuesto / 100)

        return round(total, 2)

    def describir_servicio(self):
        """Describir las características de la asesoría."""

        return (
            f"Servicio: {self.nombre}\n"
            f"Código: {self.codigo}\n"
            f"Especialidad: {self.__especialidad}\n"
            f"Modalidad: {self.__modalidad}\n"
            f"Precio por hora: ${self.precio_base:,.2f}"
        )
