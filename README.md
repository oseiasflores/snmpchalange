# snmpchalange
1 - Para correta execução deste programa, é necessário uma versão de python >= 3.5
Seu desenvolvimento todo foi realizado utilizando a versão 3.8.

É importante que as seguintes bibliotecas estejam disponiveis para o funcionamento do programa: 

* requests
* json

=================== IMPORTANTE ===================

Por default, tais bibliotecas já vem incluidas nas versões de python >= 3.5. Caso a versão de python seja superior a 3.5 desconsiderar o item 2 deste guia e ir direto para o item 3.

Para verificar a versão de python, basta executar em seu terminal:

$ python --version

2 - Caso não esteja disponivel uma versão igual ou superior, é possivel instalar utilizando pip3 em outras versões anteriores de python3. 

(!!!!!!! O programa não tem suporte a versão python2 !!!!!!!)

Instalar pip3 (Caso a versão de python seja < 3.5 & >= 3):

$ sudo apt install python3-pip

Comandos para instalar as bibliotecas utilizadas (Caso a versão de python seja < 3.5):

Biblioteca requests:

$ sudo pip3 install requests

Biblioteca json:

$ sudo pip3 install json

3 - Para executar o programa, basta chamar o python (>= 3.5) seguido do arquivo enable_snmp.py:

$ python enable_snmp.pyd 

Dados que eu utilizei para acesso ao AP:

API: http://citeb.com.br/izeus/apiary/v3/

As informações contidas na API cobrem 100% das necessidades do desafio, porem foram necessários alguns ajustes quanto a biblioteca requests.
Pois alguns dos metedos sofreram pequenas alterações e não houve a necessidade utilizar a biblioteca urllib2 nem sua versão para python3 urllib3. A biblioteca requests por si só já me amparou em todas necessidades que tive.

O programa pode ser dividido em 4 partes:

* Função para verificar o estado do serviço snmp;
* Função para habilitar o serviço snmp;
* Função para desabilitar o serviço snmp;
* Função menu de opções para viabilizar navegação entre as funções anteriores;

Dentro das funções habilitar/desabilitar eu implementei, seguindo as orientações da API, um request para gravar as alterações em flash.
Eu tratei todas requests em respostas em texto no terminal, conforme solicitado na proposta deste desafio
