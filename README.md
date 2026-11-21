# Sistema Integral Software FJ

## 1. Descripción del proyecto

Software FJ es un sistema desarrollado en Python para gestionar clientes, servicios y reservas. Su propósito es facilitar el registro de información, la administración de servicios y el control de las reservas mediante una aplicación de consola.

## 2. Objetivo

Desarrollar un sistema aplicando los principios de la programación orientada a objetos, utilizando abstracción, herencia, encapsulamiento y polimorfismo, junto con el manejo de excepciones personalizadas.

## 3. Funcionalidades principales

- Registro y consulta de clientes.
- Visualización de servicios disponibles.
- Registro de nuevos servicios.
- Creación de reservas.
- Confirmación y cancelación de reservas.
- Procesamiento de reservas y cálculo de costos.
- Consulta del listado de reservas.
- Manejo de errores y excepciones personalizadas.

## 4. Estructura del proyecto

```text
Fase4_Programacion_SoftwareFJ/
│
├── modelos/
│   ├── entidad.py
│   ├── cliente.py
│   ├── servicio.py
│   ├── reserva_sala.py
│   ├── alquiler_equipo.py
│   ├── reserva.py
│   └── asesoria_especializada.py
│
├── excepciones/
│   └── excepciones_personalizadas.py
│
├── registros/
│
├── main.py
└── README.md
```

Nota: el archivo de ejecución utilizado actualmente se llama `main_corregido.py`.

## 5. Tecnologías utilizadas

- Lenguaje de programación: Python.
- Entorno de desarrollo: Visual Studio Code.
- Control de versiones: Git y GitHub.
- Programación orientada a objetos.

## 6. Ejecución del programa

1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir la terminal integrada.
4. Ejecutar el siguiente comando:

```bash
python main_corregido.py
```

## 7. Principios de programación orientada a objetos

El proyecto implementa los siguientes principios:

- **Abstracción:** mediante clases abstractas para definir estructuras y comportamientos.
- **Herencia:** mediante clases especializadas que heredan características de otras clases.
- **Encapsulamiento:** mediante atributos y propiedades que controlan el acceso a los datos.
- **Polimorfismo:** mediante la implementación de métodos especializados en los diferentes servicios.
- **Manejo de excepciones:** mediante excepciones personalizadas para controlar situaciones no válidas.

## 8. Autoría

Proyecto académico desarrollado para la Universidad Nacional Abierta y a Distancia (UNAD), en el marco de la actividad de programación correspondiente a la Fase 4.