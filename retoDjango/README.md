# RetoDjango
es un reto con django

Mini reto python/django

Enunciado: Hacer un aplicación en django, que me permita crear usuarios, simular el envío de correos en paralelo y mostrar el listado en cliente(No admin).

- Generar usuarios con los campos: usuario, contraseña y correo, cada uno de forma aleatoria con la combinación de alfanumérica(A-Z0-9), la generación de usuarios debe realizar a partir de un envío de formulario de tipo POST con los campos en cliente:
	- Cantidad de usuarios a generar
	- Correo de donde enviar
	- Asunto
	- Mensaje

dominio del correo debe ser: imedia.pe
→ ejem el resultado del correo generado debe quedar algo como: user_srgdded12@imedia.pe, para almacenar usar la base de datos usar sqlite3
- Una vez terminado de crear los usuarios, simular el envío de correos de forma paralela.
  para la simulación configurar el EMAIL_BACKEND en consola, en configuraciones de django.
- Mostrar el listado de usuarios al cliente con su correspondiente GRUD(Editar, eliminar), puede emplear tablas o datatables.
