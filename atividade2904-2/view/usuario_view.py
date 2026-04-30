from flask import Flask, jsonify, request

class UsuarioView:
    def __init__(self, controller):
        self.app = Flask(__name__)
        self.controller = controller
        self._configurar_rotas()

    def _configurar_rotas(self):

        @self.app.route("/usuarios", methods=["POST"])
        def criar_usuario():
            dados = request.get_json()
            nome = dados.get("nome")
            email = dados.get("email")
            
            resposta = self.controller.request_criacao(nome, email)
            
            return jsonify({"mensagem": "Usuário criado com sucesso!", "dados": resposta}), 201

        @self.app.route("/usuarios", methods=["GET"])
        def listar_usuarios():

            usuarios = self.controller.request_lista()
            
            usuarios_serializados = [
                {"id": u.id, "nome": u.nome, "email": u.email} 
                for u in usuarios]
            
            return jsonify({"usuarios": usuarios_serializados}), 200

        @self.app.route("/usuarios/<int:usuario_id>", methods=["GET"])
        def consultar_usuario(usuario_id):
            resposta = self.controller.request_consulta(usuario_id)
            return jsonify(resposta), 200

    def run(self):
        self.app.run(debug=True)