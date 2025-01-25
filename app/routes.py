from flask import Blueprint, render_template, request
from .funciones import calcular_descuento, validar_usuario

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('Index.html')


@bp.route('/Ejercicio_1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        edad = request.form.get('edad', '')
        tarros = request.form.get('tarros', '')

        try:
            edad = int(edad)
            tarros = int(tarros)

            resultado = calcular_descuento(edad, tarros)
            if isinstance(resultado, str): 
                return render_template('Ejercicio_1.html', error=resultado)

            return render_template(
                'Ejercicio_1.html',
                nombre=nombre,
                total_sin_descuento=resultado["total_sin_descuento"],
                descuento=resultado["descuento"],
                total_con_descuento=resultado["total_con_descuento"]
            )
        except ValueError:
            return render_template('Ejercicio_1.html', error="Por favor, ingresa valores válidos.")

    return render_template('Ejercicio_1.html')



@bp.route('/Ejercicio_2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ''
    if request.method == 'POST':
        usuario = request.form.get('usuario', '').strip()
        contraseña = request.form.get('contraseña', '').strip()

        mensaje = validar_usuario(usuario, contraseña)

    return render_template('Ejercicio_2.html', mensaje=mensaje)