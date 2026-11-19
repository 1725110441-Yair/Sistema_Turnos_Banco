import web
from controllers.turnos import fila_prioritaria, fila_normal, datos_globales

render = web.template.render('views')

class Estadisticas:
    def GET(self):
        prio = len(fila_prioritaria)
        norm = len(fila_normal)
        pendientes = prio + norm
        atendidos = datos_globales['atendidos']
        cancelados = datos_globales['cancelados']
        total = pendientes + atendidos + cancelados

        return render.stats(total, pendientes, atendidos, cancelados, prio, norm)
