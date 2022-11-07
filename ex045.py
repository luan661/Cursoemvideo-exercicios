import random
import time
rock = str('''
    _____
---'   ____)
      (_____)
      (_____)   
      (____)
---.__(___)
''')
paper = str('''
     _____
---'    ___)___
           ______)
          _______)  
         _______)
---.__________)
''')
scissors = str('''
    _____
---'   ___)___
          ______)
       __________)  
      (____)
---.__(___)
''')
escolha = str(input('''\nVamos brincar de JO-KEN-PÔ???
Escolha entre Pedra, papel e Tesoura!
           
[1]       
              
    _____                                            
---'   ____)                                                   
      (_____)                                                 
      (_____)                                                            
      (____)                                                          
---.__(___)      

[2]

     _____
---'    ___)___
           ______)
          _______)  
         _______)
---.__________)                                               

[3]

    _____
---'   ___)___
          ______)
       __________)  
      (____)
---.__(___)
           \n\n
'''))
escolha = int(escolha)
if escolha == 1:
    print('Escolheu???\n{}\nBoa sorte então hahahaha'. format(rock))
    time.sleep(3)
elif escolha == 2:
    print('Escolheu???\n{}\nSe está tão confiante... Vamo lá!'.format(paper))
    time.sleep(3)
elif escolha == 3:
    print('Escolheu???\n{}\nOlha ele perdendo kakaka'.format(scissors))
    time.sleep(3)
rps = list([rock, paper, scissors])
print('Pedra...')
time.sleep(1)
print('Papel...')
time.sleep(1)
print('Tesssssouraa!!!')
time.sleep(1)
pc = random.choice(rps)
print(pc)
ganhou = 'Você ganhou!!! Que sorte eih não vai acontecer denovo!'
empate = 'Aff! Empatamos. Vamos mais uma vez!'
perdeu = 'Você perdeu! Como previsto. Tente da próxima vez... PERDEDOR!!!!!! HAHAHAHAHAHAH'
if pc is rock and escolha == 2:
    print(ganhou)
elif pc is paper and escolha == 3:
    print(ganhou)
elif pc is scissors and escolha == 1:
    print(ganhou)
elif escolha == 1 and pc == rock or escolha == 2 and pc == paper or escolha == 3 and pc == scissors:
    print(empate)
else:
    print(perdeu)
