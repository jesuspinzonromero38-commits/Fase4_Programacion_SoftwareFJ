
import logging
import os

from modelos.cliente import Cliente
from modelos.reserva import Reserva
from modelos.reserva_sala import ReservaSala
from modelos.alquiler_equipo import AlquilerEquipo
from modelos.asesoria_especializada import AsesoriaEspecializada

from excepciones.excepciones_personalizadas import (
    ErrorSoftwareFJ,
    DatosInvalidosError,
    ServicioNoDisponibleError,
    ReservaNoValidaError,
    OperacionNoPermitidaError,
    ParametroFaltanteError,
)

# Crear la carpeta de registros si no existe.
os.makedirs("registros", exist_ok=True)

# Configurar el archivo de registro de eventos y errores.
logging.basicConfig(
    filename=os.path.join("registros", "software_fj.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)

# Listas internas del sistema.
clientes = []
servicios = []
reservas = []


def cargar_servicios_iniciales():
    """Cargar los servicios iniciales de Software FJ."""

    servicios.append(
        ReservaSala("S001", "Reserva de sala", 50000, "Sala 1", 20)
    )

    servicios.append(
        AlquilerEquipo("S002", "Alquiler de equipos", 30000, "Portátil", 10)
    )

    servicios.append(
        AsesoriaEspecializada(
            "S003", "Asesoría especializada", 80000,
            "Tecnología", "virtual"
        )
    )

    logging.info("Servicios iniciales cargados correctamente.")


def buscar_cliente(identificador):
    for cliente in clientes:
        if cliente.identificador == identificador:
            return cliente
    return None


def buscar_servicio(codigo):
    for servicio in servicios:
        if servicio.codigo == codigo:
            return servicio
    return None


def buscar_reserva(codigo):
    for reserva in reservas:
        if reserva.codigo == codigo:
            return reserva
    return None


def registrar_cliente():
    print("\n--- REGISTRAR CLIENTE ---")

    try:
        identificador = input("Identificación: ").strip()

        if buscar_cliente(identificador):
            raise DatosInvalidosError(
                "Ya existe un cliente con esa identificación."
            )

        nombre = input("Nombre completo: ").strip()
        correo = input("Correo electrónico: ").strip()
        telefono = input("Teléfono: ").strip()

        cliente = Cliente(
            identificador, nombre, correo, telefono
        )

        clientes.append(cliente)

    except (ValueError, TypeError, DatosInvalidosError) as error:
        logging.error("Error al registrar cliente: %s", error)
        print(f"\nError: {error}")

    else:
        logging.info("Cliente registrado: %s", identificador)
        print("\nCliente registrado correctamente.")

    finally:
        print("Finalizó el registro del cliente.")


def mostrar_clientes():
    print("\n--- LISTA DE CLIENTES ---")

    if not clientes:
        print("Todavía no hay clientes registrados.")
        return

    for cliente in clientes:
        print("-" * 40)
        print(cliente.mostrar_informacion())


def mostrar_servicios():
    print("\n--- SERVICIOS DISPONIBLES ---")

    if not servicios:
        print("No hay servicios disponibles.")
        return

    for servicio in servicios:
        print("-" * 40)
        print(servicio.describir_servicio())


def registrar_servicio():
    print("\n--- REGISTRAR SERVICIO ---")
    print("1. Reserva de sala")
    print("2. Alquiler de equipos")
    print("3. Asesoría especializada")

    try:
        tipo = input("Seleccione el tipo: ").strip()

        codigo = input("Código del servicio: ").strip()
        nombre = input("Nombre del servicio: ").strip()
        precio = float(input("Precio base: "))

        if buscar_servicio(codigo):
            raise DatosInvalidosError(
                "Ya existe un servicio con ese código."
            )

        if tipo == "1":

            numero_sala = input("Número de sala: ").strip()
            capacidad = int(input("Capacidad máxima: "))

            servicio = ReservaSala(
                codigo, nombre, precio, numero_sala, capacidad
            )

        elif tipo == "2":

            tipo_equipo = input("Tipo de equipo: ").strip()
            unidades = int(input("Unidades disponibles: "))

            servicio = AlquilerEquipo(
                codigo, nombre, precio, tipo_equipo, unidades
            )

        elif tipo == "3":

            especialidad = input("Especialidad: ").strip()
            modalidad = input("Modalidad (virtual/presencial): ").strip()

            servicio = AsesoriaEspecializada(
                codigo, nombre, precio, especialidad, modalidad
            )

        else:
            raise ValueError("El tipo de servicio no existe.")

        servicios.append(servicio)

    except (ValueError, TypeError, DatosInvalidosError) as error:
        logging.error("Error al registrar servicio: %s", error)
        print(f"\nError: {error}")

    else:
        logging.info("Servicio registrado: %s", codigo)
        print("\nServicio registrado correctamente.")

    finally:
        print("Finalizó el registro del servicio.")


def crear_reserva():
    print("\n--- CREAR RESERVA ---")

    if not clientes:
        print("Primero debe registrar un cliente.")
        return

    if not servicios:
        print("No hay servicios disponibles.")
        return

    try:
        identificador = input("Identificación del cliente: ").strip()

        cliente = buscar_cliente(identificador)

        if cliente is None:
            raise DatosInvalidosError(
                "El cliente no está registrado."
            )

        mostrar_servicios()

        codigo_servicio = input(
            "\nCódigo del servicio: "
        ).strip()

        servicio = buscar_servicio(codigo_servicio)

        if servicio is None:
            raise ServicioNoDisponibleError(
                "El servicio seleccionado no existe."
            )

        duracion = float(
            input("Duración en horas o días: ")
        )

        codigo_reserva = f"R{len(reservas) + 1:03d}"

        reserva = Reserva(
            codigo_reserva, cliente, servicio, duracion
        )

        reservas.append(reserva)

    except (
        ValueError,
        TypeError,
        DatosInvalidosError,
        ServicioNoDisponibleError,
        ReservaNoValidaError
    ) as error:

        logging.error("Error al crear reserva: %s", error)
        print(f"\nError: {error}")

    else:
        logging.info("Reserva creada: %s", codigo_reserva)
        print(
            f"\nReserva {codigo_reserva} creada correctamente."
        )
        print("Estado: pendiente")


def seleccionar_reserva():
    codigo = input("Código de la reserva: ").strip()

    reserva = buscar_reserva(codigo)

    if reserva is None:
        raise ReservaNoValidaError(
            "No existe una reserva con ese código."
        )

    return reserva


def confirmar_reserva():
    print("\n--- CONFIRMAR RESERVA ---")

    try:
        reserva = seleccionar_reserva()
        mensaje = reserva.confirmar()

    except (
        ValueError,
        TypeError,
        ReservaNoValidaError,
        OperacionNoPermitidaError
    ) as error:

        logging.error("Error al confirmar reserva: %s", error)
        print(f"\nError: {error}")

    else:
        logging.info("Reserva confirmada: %s", reserva.codigo)
        print(mensaje)


def cancelar_reserva():
    print("\n--- CANCELAR RESERVA ---")

    try:
        reserva = seleccionar_reserva()
        mensaje = reserva.cancelar()

    except (
        ValueError,
        TypeError,
        ReservaNoValidaError,
        OperacionNoPermitidaError
    ) as error:

        logging.error("Error al cancelar reserva: %s", error)
        print(f"\nError: {error}")

    else:
        logging.info("Reserva cancelada: %s", reserva.codigo)
        print(mensaje)


def procesar_reserva():
    print("\n--- PROCESAR RESERVA ---")

    try:
        reserva = seleccionar_reserva()

        parametros = {}

        if isinstance(reserva.servicio, ReservaSala):
            parametros["asistentes"] = int(
                input("Cantidad de asistentes: ")
            )

        elif isinstance(reserva.servicio, AlquilerEquipo):
            parametros["cantidad"] = int(
                input("Cantidad de equipos: ")
            )

        descuento = float(
            input("Descuento porcentual (0 si no aplica): ")
        )

        impuesto = float(
            input("Impuesto porcentual (0 si no aplica): ")
        )

        parametros["descuento"] = descuento
        parametros["impuesto"] = impuesto

        costo = reserva.procesar(**parametros)

    except (
        ValueError,
        TypeError,
        ReservaNoValidaError,
        ServicioNoDisponibleError,
        OperacionNoPermitidaError,
        ParametroFaltanteError,
        RuntimeError
    ) as error:

        logging.exception("Error al procesar reserva.")
        print(f"\nNo se pudo procesar: {error}")

    else:
        logging.info(
            "Reserva %s procesada. Costo: %.2f",
            reserva.codigo, costo
        )

        print("\nReserva procesada correctamente.")
        print(f"Costo total: ${costo:,.2f}")

    finally:
        print("Finalizó el intento de procesamiento.")


def mostrar_reservas():
    print("\n--- LISTA DE RESERVAS ---")

    if not reservas:
        print("Todavía no hay reservas registradas.")
        return

    for reserva in reservas:
        print("-" * 40)
        print(reserva.mostrar_informacion())


def mostrar_menu():
    print("\n" + "=" * 48)
    print("        SISTEMA INTEGRAL SOFTWARE FJ")
    print("=" * 48)

    print("1. Registrar cliente")
    print("2. Mostrar clientes")
    print("3. Mostrar servicios")
    print("4. Registrar nuevo servicio")
    print("5. Crear reserva")
    print("6. Confirmar reserva")
    print("7. Cancelar reserva")
    print("8. Procesar reserva y calcular costo")
    print("9. Mostrar reservas")
    print("0. Salir")

    print("=" * 48)


def main():
    cargar_servicios_iniciales()

    while True:
        mostrar_menu()

        # Leer la opción dentro del ciclo para que el menú
        # vuelva a solicitar una opción después de cada operación.
        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                registrar_cliente()

            elif opcion == "2":
                mostrar_clientes()

            elif opcion == "3":
                mostrar_servicios()

            elif opcion == "4":
                registrar_servicio()

            elif opcion == "5":
                crear_reserva()

            elif opcion == "6":
                confirmar_reserva()

            elif opcion == "7":
                cancelar_reserva()

            elif opcion == "8":
                procesar_reserva()

            elif opcion == "9":
                mostrar_reservas()

            elif opcion == "0":
                logging.info("El usuario cerró el sistema.")
                print("\\nGracias por utilizar Software FJ.")
                break

            else:
                print("\\nOpción no válida. Seleccione un número del 0 al 9.")

        except Exception as error:
            logging.exception(
                "Error no controlado en el menú principal."
            )
            print(
                f"\\nSe presentó un error. "
                f"El sistema continúa funcionando: {error}"
            )


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        logging.warning("Ejecución interrumpida por el usuario.")
        print("\\nPrograma interrumpido.")

    finally:
        logging.info("Finalizó la ejecución de Software FJ.")
