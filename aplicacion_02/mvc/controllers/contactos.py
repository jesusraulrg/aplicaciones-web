# importamos la libreria web.py
import web

# Definimos la ruta del directorio de las vistas
render = web.template.render('mvc/views/')

# Creamos la clase Index
class Contactos:
    def GET(self):
        try:
            return render.contactos()
        except Exception as e:
            print(f'Error 101 - index {e.args}')
            