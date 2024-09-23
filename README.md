# CheckLink


CheckLink es una herramienta de línea de comandos diseñada para validar y verificar varios tipos de enlaces y direcciones en línea. Desde grupos de WhatsApp hasta perfiles de redes sociales, CheckLink te ayuda a confirmar la validez y obtener información sobre diversos recursos en línea.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Opciones Disponibles](#opciones-disponibles)
- [Verificaciones Masivas](#verificaciones-masivas)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## ✨ Características

- Validación de grupos de WhatsApp y Telegram
- Verificación de perfiles de Facebook e Instagram
- Comprobación de disponibilidad de dominios DNS
- Validación de sitios web
- Verificación de direcciones de correo electrónico
- Soporte para verificaciones masivas con archivos TXT

## 🛠 Requisitos Previos

- Python 3.6+
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar el repositorio)

## 💻 Instalación

1. Clona el repositorio (o descárgalo como ZIP):
   ```
   git clone https://github.com/obed-tc/checkLink
   ```

2. Navega al directorio del proyecto:
   ```
   cd checklink
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## ⚙️ Configuración

Para utilizar las funciones de verificación de correo electrónico, necesitarás tokens de API de Abstract API y MailBox Validator. Sigue estos pasos para configurarlos:

1. Regístrate en [Abstract API](https://www.abstractapi.com/) y [MailBox Validator](https://www.mailboxvalidator.com/) para obtener tus tokens API gratuitos.

2. Abre el archivo `checklink.py` y busca las siguientes líneas:

   ```python
   keyAbstract = "TU TOKEN AQUI"
   keyMailBox = "TU TOKEN AQUI"
   ```

3. Reemplaza los valores de `keyAbstract` y `keyMailBox` con tus propios tokens.

## 🚀 Uso

Para ejecutar CheckLink, usa el siguiente comando en la terminal:

```
python checklink.py
```

Sigue las instrucciones en pantalla para seleccionar la opción deseada y proporcionar la información necesaria.

## 🔍 Opciones Disponibles

1. **Grupo de WhatsApp**: Verifica la validez de enlaces de grupos de WhatsApp.
2. **Grupo de Telegram**: Comprueba la validez de enlaces de grupos de Telegram.
3. **Correo Electrónico**: Valida direcciones de correo electrónico.
4. **Número de Teléfono**: (Próximamente) Verificación de números telefónicos.
5. **Perfil de Facebook**: Valida perfiles de Facebook.
6. **Perfil de Instagram**: Verifica perfiles de Instagram.
7. **DNS**: Comprueba la disponibilidad de dominios DNS.
8. **Sitios Web**: Verifica la accesibilidad de sitios web.
9. **URL de Zoom**: (Próximamente) Validación de enlaces de Zoom.
10. **URL de Google Meet**: (Próximamente) Verificación de enlaces de Google Meet.

## 📊 Verificaciones Masivas

CheckLink permite realizar verificaciones masivas utilizando archivos TXT. En el repositorio encontrarás archivos de ejemplo para cada tipo de verificación. Para usar esta función:

1. Selecciona la opción deseada en el menú principal.
2. Cuando se te solicite, elige la opción de verificación masiva.
3. Introduce la ruta del archivo TXT (por ejemplo, `ejemplos/whatsapp_groups.txt`).

Los resultados de las verificaciones masivas se guardarán en un nuevo archivo TXT en el directorio del proyecto.
> **Nota:** Este contenido se proporciona únicamente con fines educativos. Por favor, utilízalo de manera responsable.


## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios importantes antes de crear un pull request.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

Desarrollado con ❤️ por obed-tc
