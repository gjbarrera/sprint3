from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, validators, TextAreaField


    
class Formulario_Contacto(Form):
    nombre = StringField('Nombre y Apellido', 
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=25)
    ] )
    correo = StringField('E-mail',
    [ 
        validators.DataRequired('Campo Requerido para contacto'), 
        validators.Length(min=8,max=25) 
    ])
    mensaje = TextAreaField('Mensaje',
    [
        validators.DataRequired('Campo Requerido para contacto')
    ])
    enviar = SubmitField('Enviar')

class Formulario_Ingresar(Form):
    usuario = StringField('Usuario', 
    [ 
        validators.DataRequired('Campo Requerido para ingresar'), 
        validators.Length(min=8,max=25)
    ] )
    contraseña = StringField('Contraseña',
    [ 
        validators.DataRequired('Campo Requerido para ingresar'), 
        validators.Length(min=8,max=25) 
    ])
    
    login = SubmitField('Login')