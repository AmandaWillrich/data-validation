import re


class TelephonesBr:
    def __init__(self, telephone):
        if self.validate_telephone(telephone):
            self.telephone_number = telephone
        else:
            raise ValueError('Telefone incorreto!')

    def validate_telephone(self, telephone):
        pattern = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        answer = re.findall(pattern, telephone)
        if answer:
            return True
        else:
            return False

    def __str__(self):
        return self.format_telephone_number()

    def format_telephone_number(self):
        pattern = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        answer = re.search(pattern, self.telephone_number)
        formatted_tel_number = (
            f'+ {answer.group(1)}({answer.group(2)}){answer.group(3)}-{answer.group(4)}')
        return formatted_tel_number
