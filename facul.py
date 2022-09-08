from contextlib import nullcontext


print('Jogo de perguntas e respostas, você tem duas chances de responder a cada pergunta, perguntas respondidas corretamente no segundo turno valem apenas metade do valor(5) dito isso vamos iniciar!')
print('Primeira pergunta...')

print('Quem descobriu o Brasil ?')

print(' A) Cristovo Colombo')
print(' B) Tiririca')
print(' C) Pedro Álvares Cabral')
print(' D) Pinzon')

soma = 0
contagemAcertos= 0

resposta1 = input('')

if ((resposta1 == "C") or (resposta1 == "c")):
    print('Correto!')
    contagemAcertos = contagemAcertos + 1
    soma = soma + 10
    segundatentativa = nullcontext

else:
    print('Resposta errada porém você ainda tem uma chance!')
    print('Qual a resposta correta?')
    segundatentativa = input('')

if ((segundatentativa == "C") or (segundatentativa == "c")):
    print('Agora sim! , bom trabalho!')
    soma = soma + 5

else:
    print('Vamos a próxima questão!')

print('Quem foi o primeiro presidente do Brasil?')

print(' A) Deodoro de Fonseca')
print(' B) Juscelino Kubitschek')
print(' C) Getúlio Vargas')
print(' D) Castelo Branco')

resposta1 = input('')

if ((resposta1 == "A") or (resposta1 == "a")):
    print('Correto!')
    soma = soma + 10
    contagemAcertos = contagemAcertos + 1

else:

    print('Resposta errada porém você ainda tem uma chance!')
    print('Qual a resposta correta?')
    segundatentativa = input('')

if ((segundatentativa == "A") or (segundatentativa == "a")):
    print('Agora sim! , bom trabalho!')
    soma = soma + 5


else:
    print('Vamos a próxima questão!')

print('Qual foi o primeiro modelo de carro fabricado no Brasil?')

print(' A) BYD D1')
print(' B) Fusca')
print(' C) DKW-Vemag')
print(' D) Romi-Isetta')

resposta1 = input('')

if ((resposta1 == "D") or (resposta1 == "d")):
    print('Correto!')
    soma = soma + 10
    contagemAcertos = contagemAcertos + 1
    
else:
    print('Resposta errada porém você ainda tem uma chance!')
    print('Qual a resposta correta?')
    segundatentativa = input('')

if ((segundatentativa == "D") or (segundatentativa == "d")):
    print('Agora sim! , bom trabalho!')
    soma = soma + 5

    
else:
    print('Vamos a próxima questão!')

print('Qual foi o primeiro produto exportado em larga escal do Brasil?')

print(' A) cafe')
print(' B) pau-brasil')
print(' C) especiarias')
print(' D) cana de açucar')

resposta1 = input('')

if ((resposta1 == "b") or (resposta1 == "B")):
    print('Correto!')
    soma = soma + 10
    contagemAcertos = contagemAcertos + 1
    
else:
    print('Resposta errada porém você ainda tem uma chance!')
    print('Qual a resposta correta?')
    segundatentativa = input('')

if ((segundatentativa == "B") or (segundatentativa == "b")):
    print('Agora sim! , bom trabalho!')
    soma = soma + 5
 
    

else:
    print('Vamos a próxima questão!')

print('Em qual ano foi proclamado a indenpendencia do Brasil?')

print(' A) 1822')
print(' B) 1800')
print(' C) 1820')
print(' D) 1818')

resposta1 = input('')

if ((resposta1 == "A") or (resposta1 == "a")):
    print('Correto!')
    soma = soma + 10
    contagemAcertos = contagemAcertos + 1
   
else:
    print('Resposta errada porém você ainda tem uma chance!')
    print('Qual a resposta correta?')
    segundatentativa = input('')

if ((segundatentativa == "A") or (segundatentativa == "a")):
    print('Agora sim! , bom trabalho!')
    soma = soma + 5

    

else:
    print('Vamos a próxima questão!')

print('Qual foi o maior conflito armado a qual ocorreu na America do sul?')

print(' A) Contestado Franco-Brasileiro')
print(' B) Guerra do Paraguai')
print(' C) Guerra do Chaco')
print(' D) Guerra do Pacifico')

resposta1 = input('')

if ((resposta1 == "B") or (resposta1 == "b")):
    print('Correto!')
    soma = soma + 10
    contagemAcertos = contagemAcertos + 1
    
else:
    print('Resposta errada porém você ainda tem uma chance!')
    print('Qual a resposta correta?')
    segundatentativa = input('')

if ((segundatentativa == "B") or (segundatentativa == "b")):
    print('Agora sim! , bom trabalho!')
    soma = soma + 5

    

else:
    print('Vamos a próxima questão!')

print('Qual foi a primeira moeda do Brasil?')

print(' A) Cruzeiro')
print(' B) Cruzado')
print(' C) Dobrão')
print(' D) Cruzeiro Real')

resposta1 = input('')

if ((resposta1 == "A") or (resposta1 == "a")):
    print('Correto!')
    soma = soma + 10
    contagemAcertos = contagemAcertos + 1
   
else:
    print('Resposta errada porém você ainda tem uma chance!')
    print('Qual a resposta correta?')
    segundatentativa = input('')

if ((segundatentativa == "A") or (segundatentativa == "a")):
    print('Agora sim! , bom trabalho!')
    soma = soma + 5

    

else:
    print('Vamos a próxima questão!')

print('Qual o ano em que o Brasil entrou na primeira guerra mundial?')

print(' A) 1916')
print(' B) 1920')
print(' C) 1917')
print(' D) 1914')

resposta1 = input('')

if ((resposta1 == "D") or (resposta1 == "d")):
    print('Correto!')
    soma = soma + 10
    contagemAcertos = contagemAcertos + 1
    
else:
    print('Resposta errada porém você ainda tem uma chance!')
    print('Qual a resposta correta?')
    segundatentativa = input('')

if ((segundatentativa == "D") or (segundatentativa == "d")):
    print('Agora sim! , bom trabalho!')
    soma = soma + 5

    

else:
    print('Vamos a próxima questão!')

print('Qual Pais é considerado o principal parceiro comercial do Brasil?')

print(' A) China')
print(' B) Russia')
print(' C) Estados Unidos')
print(' D) India')

resposta1 = input('')

if ((resposta1 == "A") or (resposta1 == "a")):
    print('Correto!')
    soma = soma + 10
    contagemAcertos = contagemAcertos + 1
    
else:
    print('Resposta errada porém você ainda tem uma chance!')
    print('Qual a resposta correta?')
    segundatentativa = input('')

if ((segundatentativa == "A") or (segundatentativa == "a")):
    print('Agora sim! , bom trabalho!')
    soma = soma + 5


else:
    print('Vamos a próxima questão!')

print('Em qual ano começou a ditadura Militar? ')

print(' A) 1964')
print(' B) 1967')
print(' C) 1960')
print(' D) 1965')

resposta1 = input('')

if ((resposta1 == "A") or (resposta1 == "a")):
    print('Correto!')
    soma = soma + 10
    contagemAcertos = contagemAcertos + 1
    
else:
    print('Resposta errada porém você ainda tem uma chance!')
    print('Qual a resposta correta?')
    segundatentativa = input('')

if ((segundatentativa == "A") or (segundatentativa == "a")):
    print('Agora sim! , bom trabalho!')
    soma = soma + 5

    
    print('Vamos ao resultado Final: ')
    
if soma < 24 : 
    print('Resultado: PÉSSIMO ')

if soma >= 25 and soma <= 49 :
    print('Resultado: REGULAR ')
    
if soma >= 50  and soma <= 74 :
    print('Resultado: BOM ')
    
if soma >= 75  and soma <= 99 :
    print('Resultado: ÓTIMO  ')
    
if soma == 100:
    print('Resultado: EXCELENTE ')
    
print('Deseja a quantidade de erros e acertos ? S/N')
resposta = input('')

if resposta == 'S' or 's':
    print('Você acertou: ',contagemAcertos)
    print('Você errou: ',((contagemAcertos-10)*-1))
 





    
    
    