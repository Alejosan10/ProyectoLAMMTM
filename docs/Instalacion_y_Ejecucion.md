## Instalación y Ejecución del Proyecto
## Aldaz, Morales y Moreno

### Requisitos Previos
- Asegúrate de tener Docker instalado en tu sistema.
- Clona este repositorio en tu máquina local.

### Pasos para Instalar y Ejecutar
1. **Construcción de la Imagen Docker**
   - Abre una terminal y navega hasta el directorio donde clonaste este repositorio que contiene el archivo 'Dockerfile'.
   - El nombre de la imagen (`nombre_imagen`) puede ser definido a gusto del usuario.
   - Ejecuta el siguiente comando para construir la imagen Docker:

     ```bash
     docker build -t nombre_imagen .
     ```

2. **Ejecución del Contenedor PostgreSQL**
   - Una vez construida la imagen, el nombre del contenedor (`nombre_contenedor`) puede ser definido a gusto del usuario.
   - Ejecuta el siguiente comando para iniciar el contenedor y mapear el puerto 5432 del contenedor al puerto 5433 del host:

     ```bash
     docker run -d --name nombre_contenedor -p 5433:5432 nombre_imagen
     ```

3. **Inicialización de la Base de Datos y Creación de Roles y Usuarios**
   - Con el contenedor en ejecución, ejecuta el script `init.sql` para inicializar la base de datos y configurar roles y tablas, según sea necesario:

     ```bash
     docker exec -i nombre_contenedor psql -U LAMMTM -d BankDBMgmt -a -f /ruta/a/init.sql
     ```

### Notas Adicionales
- Asegúrate de ajustar las rutas de acuerdo a la configuración de tu maquina.
- Consulta el archivo `README.md` para más detalles sobre el proyecto.
