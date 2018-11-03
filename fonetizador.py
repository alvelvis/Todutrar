# -*- coding: utf-8 -*-

import re
import string
import sys

def fonetiza(palavra):

	#CHECA SE A PALAVRA NÃO CONTÉM NÚMEROS NEM ESPAÇOS
	#CASO CONTRÁRIO, NÃO MODIFICA A PALAVRA (retorna ela própria)
	if re.match(r'[^\d\s]+', palavra):

		#CRIA A LISTA DAS REGRAS DE FONETIZAÇÃO
		expressao = list()

		#VOGAIS E CONSOANTESS
		v = r'AEIOUÁÉÍÓÚÃẼĨÕŨÀÈÌÒÙÂÊÎÔÛ@'
		c = r'BCDFGHJKLMNPQRSTVWXYZ"'

		#REGRAS DE FONETIZAÇÃO
		#('expressão regular', 'substituto', grupo anterior que permanece, grupo posterior que permanece)
		expressao.extend([							
								(r'Y','I',0,0),

								(r'W([LR'+v+'])','V',0,1),
								(r'W(['+c+'])','"0',0,1),

								(r'[AÃÁ][N]$','Ã',0,0),
								(r'[AÃÁ][M]$','ÃW',0,0),
								(r'[Ã][O]$','ÃW',0,0),
								(r'[EÉẼ][MN]$','ẼI',0,0),
								(r'[IÍĨ][MN]$','Ĩ',0,0),
								(r'[OÓÕ][MN]$','ÕW',0,0),
								(r'[UÚŨ][MN]$','Ũ',0,0),
								(r'[AÃÁ][N]S$','ÃS',0,0),
								(r'[AÁÃ][M]S$','ÃWS',0,0),
								(r'[Ã][O]S$','ÃWS',0,0),
								(r'[EÉẼ][MN]S$','ẼIS',0,0),
								(r'[IĨÍ][MN]S$','ĨS',0,0),
								(r'[OÓÕ][MN]S$','ÕWS',0,0),
								(r'[UÚŨ][MN]S$','ŨS',0,0),

								(r'([^SWNR])S(['+v+'])','Z',1,2),

								(r'[AÂÁ][MN]([^'+v+'H])','Ã',0,1),
								(r'[EÊÉ][MN]([^'+v+'H])','Ẽ',0,1),
								(r'[IÎÍ][MN]([^'+v+'H])','Ĩ',0,1),
								(r'[OÔÓ][MN]([^'+v+'H])','Õ',0,1),
								(r'[UÛÚ][MN]([^'+v+'H])','Ũ',0,1),
								(r'[AÂÁ]([MN]['+v+'])','Ã',0,1),
								(r'[EÊÉ]([MN]['+v+'])','Ẽ',0,1),
								(r'[IÎÍ]([MN]['+v+'])','Ĩ',0,1),
								(r'[OÔÒ]([MN]['+v+'])','Õ',0,1),
								(r'[UÛÚ]([MN]['+v+'])','Ũ',0,1),
								(r'[AÂÁ]([MN][H])','Ã',0,1),
								(r'[EÊÉ]([MN][H])','Ẽ',0,1),
								(r'[IÎÍ]([MN][H])','Ĩ',0,1),
								(r'[OÔÓ]([MN][H])','Õ',0,1),
								(r'[UÛÚ]([MN][H])','Ũ',0,1),

								(r'[AÁÂ][L]([^'+v+'H])','AW',0,1),
								(r'[EÉÊ][L]([^'+v+'H])','EW',0,1),
								(r'[IÍĨ][L]([^'+v+'H])','IW',0,1),
								(r'[OÓÔ][L]([^'+v+'H])','OW',0,1),
								(r'[UŨÚ][L]([^'+v+'H])','UW',0,1),
								(r'[AÁÂ][L]$','AW',0,0),
								(r'[EÉÊ][L]$','EW',0,0),
								(r'[IĨÍ][L]$','IW',0,0),
								(r'[OÓÔ][L]$','OW',0,0),
								(r'[UŨÚ][L]$','UW',0,0),
								(r'[AÁÂ][U]','AW',0,0),
								(r'[EÉÊ][U]','EW',0,0),
								(r'[IÍĨ][U]','IW',0,0),
								(r'[OÓÔ][U]','OW',0,0),
								(r'[UÚŨ][U]','UW',0,0),

								(r'[O]$','U',0,0),
								(r'[O][S]$','US',0,0),
								(r'[E]$','I',0,0),
								(r'[E][S]$','IS',0,0),
								(r'(.+)[A]$','@',1,0),
								(r'(.+)[A][S]$','@S',1,0),
								(r'[Z]$','S',0,0),

								(r'[T]([IĨÍ])','"T',0,1),
								(r'[D]([IĨÍ])','"D',0,1),

								(r'SS','S',0,0),
								(r'SH','X',0,0),
								(r'SC([EIẼĨÉÍ])','S',0,1),
								(r'SC([AUOÃŨÕÁÚÓ])','SK',0,1),
								(r'SCH','X',0,0),

								(r'TH','T',0,0),
								(r'^(E)X(['+v+'])','Z',1,2),
								(r'(E)X([AOUÁÓÚÃÕŨ])','KS',1,2),
								(r'(E)X([PTC])','S',1,2),
								(r'(E)X([^EIAOUẼĨÃÕŨÉÍÁÓÚ])','KS',1,2),
								(r'([DFMNPQSTVZ][AIOUÃĨÕŨÁÍÓÚ])X','KS',1,0),

								(r'CH(R)','K',0,0),
								(r'CH','X',0,0),
								(r'C([ÂAÃÔÕOÛŨU])','K',0,1),
								(r'C(['+c+'])','K',0,1),
								(r'C([EÊẼIÎĨ])','S',0,1),
								(r'C$','K',0,0),
								(r'Ç','S',0,0),
								(r'GH?([EẼÉIĨÍ])','J',0,1),
								(r'^H(['+v+'])','',0,1),
								(r'LH','"1',0,0),
								(r'N$','M',0,0),
								(r'NH','"3',0,0),
								(r'PH','F',0,0),

								(r'QU([IEĨẼÍÉÎÊ])','K',0,1),
								(r'Q(U[AOÃÕÁÓÂÔ])','K',0,1),
								(r'Q','K',0,0),
								(r'GU([IEĨẼÍÉÎÊ])','G',0,1),

								(r'^R','"2',0,0),
								(r'R$','"2',0,0),
								(r'RR','"2',0,0),
								(r'R(['+c+'])','"2',0,1),

								#CORREÇÃO
								(r'TAKS@','TAX@',0,0),
								(r'TAKSA','TAXA',0,0),
								(r'máKSĨ','máXĨ',0,0),
								(r'maKSĨ','maXĨ',0,0),	
						])

		#PASSA POR TODAS AS REGRAS DE TRANSFORMAÇÃO
		#PARA CADA REGRA, TRANSFORMA A VARIÁVEL "PALAVRA"
		k = 0
		while k < len(expressao):
			
			match = re.search(expressao[k][0], palavra, flags=re.IGNORECASE)
			if match:
				
				#GRUPOS QUE NÃO SERÃO SUBSTITUÍDOS
				antes = str(expressao[k][2])
				depois = str(expressao[k][3])
				if antes != '0':
					antes = '\\' + antes
				else:
					antes = ''
				if depois != '0':
					depois = '\\' + depois
				else:
					depois = ''
				
				palavra = re.sub(expressao[k][0], antes + expressao[k][1] + depois, palavra, flags=re.IGNORECASE)
			
			k += 1

	#RETORNA A "PALAVRA", TRANSFORMADA OU NÃO
	return palavra


def main(caminho, output='fonetizado.txt', CODE='utf8', CODEFINAL='utf8'):

	#SE FOR INTERNO, O TEXTO ESTÁ NA VARIÁVEL OUTPUT
	#CASO CONTRÁRIO, CARREGAR O ARQUIVO E SEPARAR LINHAS EM LISTAS
	if caminho != 'interno':
		texto = open(caminho, 'r', encoding=CODE).read().splitlines()
	else:
		texto = output.splitlines()

	#DESTACA A PONTUAÇÃO E SEPARA AS PALAVRAS (critério: espaço)
	for i in range(len(texto)):
		for ponto in string.punctuation:
			texto[i] = texto[i].replace(ponto, ' ' + ponto + ' ')
		texto[i] = texto[i].split()

	#FONETIZA PALAVRA POR PALAVRA
	for i, linha in enumerate(texto):
		for w, palavra in enumerate(linha):
			texto[i][w] = fonetiza(texto[i][w])

	#REFORMATA ARQUIVO NOS MOLDES DO ORIGINAL
	for i,linha in enumerate(texto):
		texto[i] = " ".join(texto[i])

	#SE FOR INTERNO, PRINTA
	#SE NÃO, SALVA ARQUIVO OUTPUT
	if caminho != 'interno':
		open(output, 'w', encoding=CODEFINAL).write("\n".join(texto))
	else:
		print("\n".join(texto))


if __name__ == '__main__':

	#CHECA ARGUMENTOS
	if len(sys.argv) <= 1:
		print('Argumentos esperados para o fonetizador')
		print('uso: fonetizador.py entrada saída codificação-da-entrada codificação-da-saída')
		print("Com o comando `-t' é possível digitar o texto diretamente")
		print("Tente `-h' para mais informações")
	else:
		if sys.argv[1] == '-h':
			print('uso: fonetizador.py entrada saída codificação-da-entrada codificação-da-saída')
			print("É obrigatório informar a entrada (arquivo de texto original) OU o texto que será transcrito, após o comando `-t'")
			print('Saída padrão: "fonetizado.txt"')
			print('Codificação padrão: utf8')
		elif sys.argv[1] == '-t': main('interno', " ".join(sys.argv[2:]))
		elif len(sys.argv) == 2: main(sys.argv[1])
		elif len(sys.argv) == 3: main(sys.argv[1], sys.argv[2])
		elif len(sys.argv) == 4: main(sys.argv[1], sys.argv[2], sys.argv[3])
		elif len(sys.argv) == 5: main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
		else:
			print('Argumentos demais')
			print("Tente `-h' para mais informações")