#Imagen oficial de PostgreSQL como base
FROM postgres:latest

# Variables de entorno para configurar la base de datos
ENV POSTGRES_DB BankDBMgmt
ENV POSTGRES_USER LAMMTM
ENV POSTGRES_PASSWORD LAMMTMproy@

# Copia los archivos de configuración y datos persistentes
COPY ./db_data/config /etc/postgresql
COPY ./db_data/data /var/lib/postgresql/data

# Expone el puerto por defecto de PostgreSQL
EXPOSE 5433

# Comando para iniciar PostgreSQL al iniciar el contenedor
CMD ["postgres"]
