def calcular_descuento(edad, cantidad):
    try:
        if edad < 0 or cantidad < 0:
            return "Error: La edad o cantidad no pueden ser negativas."

        precio_por_tarro = 9000

        total_sin_descuento = cantidad * precio_por_tarro

        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        elif edad > 30:
            descuento = total_sin_descuento * 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento - descuento

        return {
            "total_sin_descuento": round(total_sin_descuento),
            "descuento": round(descuento),
            "total_con_descuento": round(total_con_descuento)
        }
    except Exception as e:
        return f"Error en la función calcular_descuento: {e}"


def validar_usuario(usuario, contraseña):
    usuarios = {'juan': 'admin', 'pepe': 'user'}

    if usuario in usuarios:
        if usuarios[usuario] == contraseña:
            rol = "administrador" if usuario == 'juan' else "usuario"
            return f'Bienvenido {rol} {usuario}'
        else:
            return 'Contraseña incorrecta'
    return 'Usuario no encontrado'
