from src.controller.personcontroler import PessoaController
from src.model.person import Pessoa
from src.view.personview import PessoaView


if __name__ == "__main__":
    # Cria uma pessoa
    pessoa = Pessoa("João", 30)
    # Cria uma view para a pessoa
    view = PessoaView()
    # Cria um controller para a pessoa e sua view correspondente
    controller = PessoaController(pessoa, view)

    # Atualiza alguns dados da pessoa
    controller.set_nome("Maria")
    controller.set_idade(25)

    # Atualiza a view
    controller.atualizar_view()
    
    print(view)