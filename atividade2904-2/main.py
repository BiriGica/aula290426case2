from controller.usuario_controller import UsuarioController
from view.usuario_view import UsuarioView 

def main():

    controller = UsuarioController(None)

    view = UsuarioView(controller)


    print("Iniciando servidor API...")
    view.run()

if __name__ == "__main__":
    main()