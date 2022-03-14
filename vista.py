
class vistaAxiomasPorTerminal:
    def __init__(self,MaxAxioma):
        #atributos
        self.__axiomaInicial = 0
        self.MaxAxioma = MaxAxioma
       #metodos
    def mostrar(self, vAxioma):
        print("y el axioma es: ", vAxioma)
    def escojeAxioma(self):
        vResult = None
        vResult = input("Tipee el nro. de axioma que quiere ver: ")
        return vResult

    def mostrarAxiomaInicial(self):
        print('el axioma inicial: ',self.__axiomaInicial)

    def asignarAxiomaInicial(self, axiomaInicial):
        self.__axiomaInicial = axiomaInicial

class vistaAxiomasHTML(vistaAxiomasPorTerminal):
    def mostrar(self, vAxioma):
        vArchivoHtml = open('vistaMVC.html', 'w')

        vPlantilla = """
        <html>
        <head>
        <title> Telematica - Prog2 </title>
        </head>
        <body> 
        <h1>Modelo-Vista-Controlador (MVC)</h1>
        <h2>Vista html</h2>
        <table border="1">
        <tbody>
        <tr>
        <td>y el Axioma es: </td>
        </tr>
        <tr>
        <td>        
        """
        vPlantilla += vAxioma
        vPlantilla += """
        </td>
        </tr>
        </tbody>
        </table>
        </body>
        </html>
        """

        vArchivoHtml.write(vPlantilla)
        vArchivoHtml.close()

    def escojeAxioma(self):#polimorfismo
        vResult = None
        print('Vista por HTML')
        vResult = input("Tipee el nro. de axioma que quiere ver: ",self.MaxAxioma)
        return vResult
   

vista1 = vistaAxiomasPorTerminal(5)
vista1.asignarAxiomaInicial(1)
vista1.mostrarAxiomaInicial()