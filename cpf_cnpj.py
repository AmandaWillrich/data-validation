from validate_docbr import CNPJ, CPF


class Document:

    @staticmethod
    def create_document(document):
        if len(document) == 11:
            return CpfDoc(document)
        elif len(document) == 14:
            return CnpjDoc(document)
        else:
            raise ValueError('Quantidade de dígitos inválida')


class CpfDoc:
    def __init__(self, document):
        if self.cpf_is_valid(document):
            self.cpf = document
        else:
            raise ValueError('CPF inválido!')

    def cpf_is_valid(self, cpf):
        is_cpf_valid = CPF()
        return is_cpf_valid.validate(cpf)

    def format_cpf(self):
        mask = CPF()
        return mask.mask(self.cpf)

    def __str__(self):
        return self.format_cpf()


class CnpjDoc:
    def __init__(self, document):
        if self.cnpj_is_valid(document):
            self.cnpj = document
        else:
            raise ValueError('CNPJ inválido!')

    def cnpj_is_valid(self, cnpj):
        is_cnpj_valid = CNPJ()
        return is_cnpj_valid.validate(cnpj)

    def format_cnpj(self):
        mask = CNPJ()
        return mask.mask(self.cnpj)

    def __str__(self):
        return self.format_cnpj()
