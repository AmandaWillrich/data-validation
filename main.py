import requests

from cep_acesso import AddressSearch
from cpf_cnpj import Document
from datas_br import DatesBr
from telefonesbr import TelephonesBr

first_cpf = '32007832062'
first_cnpj = '35379838000112'

document = Document.create_document(first_cnpj)
print(document)


tel = '552126481234'
tel_object = TelephonesBr(tel)

print(tel_object)

register = DatesBr()
print(register)

cep = 24837988
cep_object = AddressSearch(cep)
print(cep_object)

r = requests.get('https://viacep.com.br/ws/01001000/json/')
print(r.text)
