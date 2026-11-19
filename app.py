import web
from controllers.turnos import ListaTurnos, RegistrarTurno, AtenderTurno, CancelarTurno
from controllers.estadisticas import Estadisticas

urls = (
    '/', 'ListaTurnos',
    '/registrar', 'RegistrarTurno',
    '/atender', 'AtenderTurno',
    r'/cancelar/(\d+)', 'CancelarTurno',
    '/estadisticas', 'Estadisticas'
)

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
