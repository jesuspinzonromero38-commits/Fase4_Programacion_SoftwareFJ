
"""
Excepciones personalizadas para el sistema Software FJ.
"""


class ErrorSoftwareFJ(Exception):
    """Excepción base del sistema Software FJ."""
    pass


class DatosInvalidosError(ErrorSoftwareFJ):
    """Se presenta cuando los datos ingresados no son válidos."""
    pass


class ServicioNoDisponibleError(ErrorSoftwareFJ):
    """Se presenta cuando un servicio no está disponible."""
    pass


class ReservaNoValidaError(ErrorSoftwareFJ):
    """Se presenta cuando una reserva no cumple los requisitos."""
    pass


class OperacionNoPermitidaError(ErrorSoftwareFJ):
    """Se presenta cuando se intenta realizar una operación no permitida."""
    pass


class ParametroFaltanteError(ErrorSoftwareFJ):
    """Se presenta cuando falta un parámetro obligatorio."""
    pass
