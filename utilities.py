def colorir(texto, cor):
	cores = {
	        'vermelho': "\033[31m",
	        'verde': "\033[32m",
	        'amarelo': "\033[33m",
	        'azul': "\033[34m",
	        'padrao': "\033[0m"
	}

	if [c for c in cores if str(c) == cor] != []:
		texto_colorido = cores[cor] + texto + cores['padrao']
		return texto_colorido
	else:
		return quit()