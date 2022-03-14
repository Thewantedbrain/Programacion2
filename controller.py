import modelo
import vista


class axiomaTerminalController:
    def __init__(self):
        self.model = modelo.axiomaModel()
        self.view = vista.vistaAxiomasPorTerminal(5)

    def run(self):
        vNroDeAxiomaEscogido = int(self.view.escojeAxioma())
        if vNroDeAxiomaEscogido >=1:
         vAxioma = self.model.obtenerAxioma(vNroDeAxiomaEscogido)
         self.view.mostrar(vAxioma)
        else:
            print('El numero no es mayor a 1')