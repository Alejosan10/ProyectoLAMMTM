# ProyectoLAMMTM

# Administración de Base de Datos Bancaria

## Aldaz, Morales y Moreno

### Descripción
Este proyecto implementa una base de datos bancaria utilizando PostgreSQL en un contenedor Docker. La base de datos gestiona la información de clientes, cuentas, transacciones, préstamos, empleados, tarjetas, historial crediticio, inversiones y pagos de servicios.

### Contenidos del Repositorio
- **`Dockerfile`**: Archivo para construir la imagen Docker.
- **`db_data/`**: Directorio que contiene los archivos de configuración y datos persistentes.
  - **`config/`**: Configuraciones adicionales.
  - **`data/`**: Datos persistentes de PostgreSQL.
- **`scripts/`**: Scripts necesarios para la generación de datos.
  - **`generate_data.py`**: Script para generar datos aleatorios en la base de datos.
- **`docs/`**: Documentación del proyecto.
  - **`Diagrama Entidad_Relacion.pdf`**: Diagrama de modelo conceptual de la base de datos.
  - **`Diagrama Diseño_Fisico.pdf`**: Diagrama del modelo físico de la base de datos.
  - **`diccionario_datos.xlsx`**: Diccionario de datos.
  - **`Instalacion_y_Ejecucion.md`**: Instrucciones de instalación y ejecución del proyecto.
- **`init.sql`**: Script SQL para inicializar la base de datos.

## Instalación y Ejecución del Proyecto
Para instrucciones detalladas sobre la instalación y ejecución del proyecto, consulta el archivo [Instalacion_y_Ejecucion.md](docs/Instalacion_y_Ejecucion.md).

### Pasos Rápidos
1. **Construcción de la Imagen Docker**
   ```bash
   docker build -t nombre_imagen .
