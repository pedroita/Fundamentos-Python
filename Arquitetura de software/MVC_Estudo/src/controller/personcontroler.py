class PessoaController:
    def __init__(self, pessoa, view):
        self.pessoa = pessoa
        self.view = view

    def set_nome(self, nome):
        self.pessoa.nome = nome

    def set_idade(self, idade):
        self.pessoa.idade = idade

    def atualizar_view(self):
        self.view.mostrar_detalhes(self.pessoa.nome, self.pessoa.idade)
        