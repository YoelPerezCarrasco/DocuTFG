# API/Instalación/Modelos - Middleware

Este proyecto es una API desarrollada con **FastAPI** que permite gestionar usuarios, sus contribuciones a repositorios de **GitHub**, y optimizar equipos de trabajo mediante el uso de **Machine Learning** y **detección de comunidades**. El sistema implementa autenticación y autorización basada en **JWT**, y proporciona funcionalidades para asignar roles clave y analizar interacciones colaborativas.

## Tabla de Contenidos
- [Instalación](#instalacion)
- [Configuración](#configuracion)
- [Configuración de Docker](#configuracion-de-docker)
  - [Dockerfile](#dockerfile)
  - [docker-compose.yml](#docker-compose)
  - [Levantando los Servicios](#levantando-los-servicios)
- [Modelos de Base de Datos](#modelos-de-base-de-datos)
- [Autenticación y Autorización](#autenticacion-y-autorizacion)
- [Optimización de Equipos de Trabajo](#optimizacion-equipos-trabajo)
  - [Regresión Logística](#regresion-logistica)
  - [Algoritmo Louvain](#algoritmo-louvain)
- [Endpoints](#endpoints)
  - [Autenticación](#autenticacion)
  - [Usuarios](#usuarios)
  - [Organizaciones](#organizaciones)
  - [Contribuciones y Commits](#contribuciones-y-commits)
- [Manejo de Errores](#manejo-de-errores)
- [Logging](#logging)

---

## Instalación
(id=instalacion)=

Para instalar este proyecto, sigue los siguientes pasos:

1. Clona el repositorio.
2. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```
3. Configura la base de datos (ver sección [Configuración](#configuracion)).
4. Inicia la aplicación:
    ```bash
    uvicorn main:app --reload
    ```

## Configuración
(id=configuracion)=

### Variables de Entorno

- `SECRET_KEY`: Llave secreta utilizada para la generación de JWT.
- `ALGORITHM`: Algoritmo utilizado para la codificación de JWT (por defecto, `HS256`).
- `ACCESS_TOKEN_EXPIRES_MINUTES`: Tiempo de expiración del token de acceso en minutos.
- `DATABASE_URL`: URL de conexión a la base de datos.
- `GITHUB_API_TOKEN`: Token personal para interactuar con la API de GitHub.

### Base de Datos

La aplicación utiliza **SQLAlchemy** como ORM y **PostgreSQL** como base de datos. Las tablas son creadas automáticamente usando:

```python
Base.metadata.create_all(bind=engine)
```

---

## Configuración de Docker
<a id="configuracion-de-docker"></a>

El proyecto utiliza **Docker** y **Docker Compose** para levantar un entorno de desarrollo completo.

### Dockerfile
<a id="dockerfile"></a>

```Dockerfile
# Usar una imagen oficial de Python como imagen base
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requisitos e instalar las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente de la aplicación
COPY . .

# Exponer el puerto 8000 para FastAPI
EXPOSE 8000

# Ejecutar la aplicación
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose
<a id="docker-compose"></a>

```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      DATABASE_URL: postgresql://user:password@db:5432/mydatabase

  db:
    image: postgres:latest
    environment:
      POSTGRES_DB: mydatabase
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  pgadmin:
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: "admin@admin.com"
      PGADMIN_DEFAULT_PASSWORD: "admin"
    ports:
      - "5050:80"

volumes:
  postgres_data:
```

### Levantando los Servicios
<a id="levantando-los-servicios"></a>

```bash
docker-compose up --build
```

---

## Modelos de Base de Datos
(id=modelos-de-base-de-datos)=

### GitHubUserModel
Modelo que representa un usuario de GitHub:

- `id`: ID del usuario.
- `username`: Nombre de usuario en GitHub.
- `dominant_language`: Lenguaje de programación principal.

### UserConnections
Modelo que almacena las probabilidades de colaboración entre usuarios:

- `user_1`: ID del usuario 1.
- `user_2`: ID del usuario 2.
- `probabilidad_colaboracion`: Probabilidad calculada por el modelo de regresión logística.

---

## Optimización de Equipos de Trabajo
(id=optimizacion-equipos-trabajo)=

### Regresión Logística
Se utiliza para predecir la **probabilidad de colaboración** entre dos usuarios con base en:
- **Commits conjuntos.**
- **Contribuciones compartidas.**
- **Revisiones cruzadas.**

**Salida:** Un valor entre 0 y 1 que representa la probabilidad de que dos usuarios colaboren exitosamente.

### Algoritmo Louvain
- Detecta **comunidades (grupos de trabajo)** dentro de la red.
- Maximiza la **modularidad** para formar grupos con interacciones densas.
- Los grupos tienen un **tamaño mínimo de 8 miembros**.

---

## Endpoints

### Autenticación
- **POST** `/login`: Genera un token JWT.
- **POST** `/register`: Registra nuevos usuarios.

### Usuarios
- **GET** `/users/me`: Devuelve información del usuario autenticado.
- **GET** `/connections`: Devuelve las probabilidades de colaboración entre usuarios.

---

## Manejo de Errores
Los errores incluyen:
- **400:** Petición incorrecta.
- **401:** Autenticación fallida.
- **404:** Recurso no encontrado.

## Logging
El sistema registra las siguientes acciones:
- **Autenticación.**
- **Predicción de colaboración.**
- **Asignación de roles y formación de grupos.**

---

Este documento proporciona una guía completa para la instalación, configuración y uso de la API, así como una explicación de los algoritmos utilizados y los modelos implementados.
