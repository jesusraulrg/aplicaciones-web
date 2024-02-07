#Framework web.py
import web

#Rutas de los controladores
urls = (
    '/', 'mvc.controllers.hello.Hello',
    '/pagina2', 'mvc.controllers.pagina2.Pagina2',
    '/contactos', 'mvc.controllers.contactos.Contactos'
)

app = web.application(urls, globals())


#Punto de entrada
if __name__ == "__main__":
    app.run()
