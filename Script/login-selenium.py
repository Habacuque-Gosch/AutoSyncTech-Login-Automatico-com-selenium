from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#driver manager atualizado pela web
servico = Service(ChromeDriverManager().install())

#navegador a ser utilizadp
navegador = webdriver.Chrome(service=servico)

#link do site desejado
link = "https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M"
navegador.get(url=link)

#campo nome
nome  = "haba"
#campo email
email = "habacuqwe132465@gmail.com"
#campo senha
senha = "haba"
#campo numero
numero = "48992074300"

#campo nome na web
navegador.find_element('xpath',
                        '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys(nome)

#campo E-mail
navegador.find_element('xpath',
                        '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys(email)

#campo numero na web
navegador.find_element('xpath',
                        '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys(numero)

#-----------------------------------------sistema OFF pra rodar no on----------------------------------------#
# nome1  = input("nome?\n")
# email1 = input("email?\n")
# senha1 = input("senha?\n")
# numero1 = input("numero?\n")

# nome = nome1
# email = email1
# senha = senha1
# numero = numero1

# def iniciar():
#     link = "https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M"
#     navegador.get(url=link)
#     #campo nome
#     navegador.find_element('Xpath',
#                         '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys(nome)

#     #campo E-mail
#     navegador.find_element('Xpath',
#                         '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys(email)

#     navegador.find_element('Xpath',
#                         '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys(numero)

# if nome == "" and email == "" and senha == "" and numero == "":
#     print("Flash: criterios não atendido")
# else:
#     iniciar()

#-------------------------------------------instruções--------------------------------------------------------#

#busca o elemento pelo Xpath
#navegador.find_element('Xpath',
# '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input')

#executa ações do tipo escrita ou clique
#.send_keys("palavra")
#.click('posição')
