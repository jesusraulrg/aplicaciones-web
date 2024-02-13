import web

#Importar la clase ModeloIndex
from mvc.models.modelo_index import ModeloIndex

render = web.template.render('mvc/views/')

#objeto de la clase ModeloIndex
m_index = ModeloIndex()

class Index:
    def GET(self):
        try:
            return render.index(m_index.nombre)
        except Exception as e:
            print(f'Error 101 - index {e.args}')