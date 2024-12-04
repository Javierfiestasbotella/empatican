# Empatican - Sistema de Gestión para Servicios de Mascotas

**Empatican** es una aplicación avanzada de gestión de clientes y servicios para mascotas, diseñada para facilitar el trabajo de entrenadores, terapeutas de animales y cuidadores. La aplicación permite organizar información relevante de clientes, sus mascotas, las sesiones de entrenamiento, seminarios, pagos, y más, dentro de una interfaz amigable y fácil de utilizar.

## Estructura de Archivos del Proyecto

A continuación se detalla la estructura de archivos y carpetas del proyecto:

```
empatican/
├── db_setup.py          # Configuración de la base de datos
├── main.py              # Punto de entrada principal de la aplicación
├── models.py            # Definición de clases y métodos para la gestión de datos
├── requirements.txt     # Lista de dependencias del proyecto
├── test_app.py          # Pruebas unitarias de la aplicación
├── README.md            # Archivo de documentación
├── FACTURAS/            # Carpeta para almacenar archivos de facturas
└── ui/                  # Carpeta con la interfaz de usuario
    ├── main_window.py   # Ventana principal de la aplicación
    └── client_card_form.py # Formulario detallado de cliente
```

## Descripción de Archivos

### `main.py`

Archivo principal que inicia la aplicación. Su función principal es ejecutar la clase `MainWindow`, que representa la ventana principal de la interfaz de usuario, a partir de la cual se puede acceder a las diversas funcionalidades de la aplicación.

### `db_setup.py`

Este archivo configura la base de datos de PostgreSQL. Define dos funciones principales:

1. **create_connection**: Establece una conexión a la base de datos PostgreSQL.
2. **initialize_database**: Crea las tablas necesarias (clientes, perros, sesiones, seminarios, inscripciones a seminarios y pagos) si no existen.

Este archivo es clave para preparar el entorno de la base de datos y asegurar que todas las tablas necesarias estén listas antes de usar la aplicación.

### `models.py`

Define las clases principales de la aplicación, cada una con su funcionalidad específica para interactuar con la base de datos. Las clases son:

- **Cliente**: Representa a un cliente y permite guardar, obtener, y buscar clientes por ID.
- **Perro**: Representa a una mascota y permite asociarla a un cliente. Incluye métodos para guardar y obtener perros relacionados con un cliente.
- **Sesion**: Guarda detalles de las sesiones de entrenamiento o cuidado.
- **Seminario**: Permite registrar seminarios y asociar clientes a estos.
- **Pago**: Permite registrar pagos de clientes, con detalles como fecha, monto y método de pago.

Cada clase maneja sus propios datos y contiene métodos CRUD (Crear, Leer, Actualizar, Eliminar) específicos para sus entidades. Este archivo es la columna vertebral de la lógica de la aplicación.

### `requirements.txt`

Contiene todas las dependencias necesarias para la ejecución de la aplicación. Para instalar las dependencias, ejecuta el siguiente comando:

```
pip install -r requirements.txt
```

Este archivo incluye, entre otros, `psycopg2` para interactuar con PostgreSQL y `tkinter` para la interfaz gráfica.

### `test_app.py`

Este archivo contiene las pruebas unitarias que validan el funcionamiento de la aplicación. Incluye pruebas para:

- **Crear Cliente**: Verifica que los clientes se guarden correctamente en la base de datos.
- **Crear Perro**: Confirma que se puedan registrar perros y asociarlos a clientes.
- **Crear Seminario**: Valida el guardado de seminarios en la base de datos.
- **Crear Pago**: Asegura que los pagos se registren correctamente en la base de datos.

Estas pruebas se ejecutan con el siguiente comando:

```
python -m unittest test_app.py
```

### Carpeta `FACTURAS/`

Esta carpeta almacena archivos de facturas organizados por cliente. La estructura es la siguiente:

```
FACTURAS/
  └── <cliente_id>_<nombre_cliente>/
```

Cada cliente tiene su propia subcarpeta en `FACTURAS` donde se almacenan sus archivos de facturas. La función `subir_factura` en la interfaz gráfica se encarga de cargar archivos en esta carpeta y organizarlos automáticamente.

### Carpeta `ui/`

Contiene los elementos de la interfaz de usuario de la aplicación. Los archivos dentro de esta carpeta son responsables de la experiencia visual y de interacción del usuario:

- **main_window.py**: Define la ventana principal de la aplicación. Muestra una lista de clientes y un menú de navegación para acceder a funcionalidades como la gestión de clientes, mascotas, sesiones y pagos.
- **client_card_form.py**: Define el formulario de cliente donde se visualizan y editan los detalles del cliente, incluyendo la información de sus mascotas y los pagos. También permite la carga de facturas.

## Funcionalidades Clave de la Aplicación

### Gestión de Clientes

- **Agregar Cliente**: Permite registrar un cliente con información básica.
- **Ver Clientes**: Muestra una lista de clientes en la ventana principal para acceso rápido.
- **Editar y Eliminar Cliente**: Permite modificar y eliminar clientes desde la lista principal.

### Gestión de Mascotas

- **Agregar Mascota**: Permite registrar datos específicos de una mascota, como nombre, raza y edad.
- **Visualizar Mascotas**: Asociado al cliente seleccionado, permite ver detalles de las mascotas registradas.

### Sesiones de Entrenamiento

- **Registrar Sesión**: Guarda la información de una sesión de entrenamiento, incluyendo fecha, duración y descripción.
- **Ver Historial de Sesiones**: Lista de todas las sesiones realizadas para una mascota específica, asociadas a un cliente.

### Seminarios

- **Registrar Seminario**: Permite registrar un seminario en la base de datos con detalles como nombre, descripción, fecha y costo.
- **Inscripción de Clientes a Seminarios**: Permite registrar la participación de un cliente en un seminario específico.

### Pagos

- **Registrar Pago**: Permite guardar detalles de pagos realizados por los clientes, incluyendo fecha, monto y método de pago.
- **Ver Historial de Pagos**: Muestra el historial de pagos asociados a un cliente específico.

### Subida de Facturas

La aplicación permite almacenar facturas en formato PDF dentro de carpetas organizadas por cliente en `FACTURAS/<cliente_id>_<nombre_cliente>`. La función crea las carpetas necesarias y organiza los archivos automáticamente para facilitar la gestión de documentos.

## Instalación y Configuración

1. **Instalar dependencias**: Ejecuta el siguiente comando para instalar las dependencias.

   ```
   pip install -r requirements.txt
   ```

2. **Configurar PostgreSQL**: Crea una base de datos y usuario en PostgreSQL. Modifica `db_setup.py` con los detalles de conexión (nombre de la base de datos, usuario, y contraseña).

3. **Crear las tablas**: Ejecuta `db_setup.py` para inicializar la base de datos y crear las tablas necesarias.

   ```
   python db_setup.py
   ```

4. **Iniciar la aplicación**: Ejecuta `main.py` para abrir la interfaz gráfica.

   ```
   python main.py
   ```

## Pruebas

Para ejecutar las pruebas unitarias y verificar el correcto funcionamiento de la aplicación, usa el siguiente comando:

```
python -m unittest test_app.py
```

Estas pruebas verifican la correcta creación de registros en la base de datos y el funcionamiento adecuado de las principales funcionalidades de la aplicación.

## Ejecución en Otros Entornos

Para compartir la aplicación con otros usuarios, se recomienda el uso de un entorno virtual con las dependencias instaladas. Si deseas crear un ejecutable para simplificar la distribución, puedes utilizar **PyInstaller**:

```
pyinstaller --onefile main.py
```

## Diagramas y Flujo de Información

### Diagrama de Estructura de Archivos

```
empatican/
├── db_setup.py
├── main.py
├── models.py
├── requirements.txt
├── test_app.py
├── README.md
├── FACTURAS/
└── ui/
    ├── main_window.py
    └── client_card_form.py
```

Este diagrama muestra la organización y dependencia entre archivos, donde `main.py` es el punto de entrada principal, `models.py` contiene la lógica de negocio, `ui/` alberga la interfaz gráfica, y `db_setup.py` inicializa la base de datos.
