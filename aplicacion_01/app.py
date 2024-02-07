import web

urls = (
    '/', 'hello',
    '/pagina2', 'pagina2',
    '/contactos', 'contactos'
)
app = web.application(urls, globals())

class hello:
    def GET(self):
        return 'Hello, pagina 1'


class pagina2:
    def GET(self):
        return 'Hola Pagina 2'
    
class contactos:
    def GET(self):
        return 'Contactos'

if __name__ == "__main__":
    app.run()
