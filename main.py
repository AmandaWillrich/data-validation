from cpf_cnpj import Document
from telefonesbr import TelephonesBr

first_cpf = '32007832062'
first_cnpj = '35379838000112'

document = Document.create_document(first_cnpj)
print(document)


tel = '552126481234'
tel_object = TelephonesBr(tel)

print(tel_object)
