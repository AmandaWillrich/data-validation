class Cpf:
    def __init__(self, document):
        document = str(document)
        if self.cpf_is_valid(document):
            self.cpf = document
        else:
            raise ValueError('CPF inválido!')

    def cpf_is_valid(self, document):
        if len(document) == 11:
            return True
        else:
            return False
