from os import system
index = 1
OTP = 1
condition = True
import time
r='\033[1;91m'
g='\033[1;92m'
y='\033[1;93m'
w='\033[1;97m'
m = g + ('#'*55) +w
print (m)
time.sleep(0.3)
print (m)
print (f'{g} ______________________________________________________')
time.sleep(0.3)
print (f'{g}						           ')
time.sleep(0.3)
print (f'{g}   {r}Author :{y} Sachindu Sahan{g}                   ')
time.sleep(0.3)
print (f'{g}						           ')
time.sleep(0.3)
print (f'{g}  {r} Github : {w}https://github.com/sachindusahan{g} ')
time.sleep(0.3)
print (f'{g}						           ')
time.sleep(0.3)
print (f'{g} ______________________________________________________{w}')
time.sleep(0.4)
x = g + ('#'*55) +w
print ('')
print (x)
n = g + ('#'*55) +w
time.sleep(0.4)
print (n)
print ('')
time.sleep(0.3)
list = ['Nano','Neovim','Vim','Emacs','Jupp','Micro','Zile']
   
while OTP < 10:
    print (f'''{g}
       1 Nano
       2 Neovim
       3 Vim
       4 Emacs
       5 Jupp
       6 Micro
       7 Zile
    ''')

    print (f"{w}If you want to Install Termux Code Editors Please Enter > {g}Related Numbar \n {w}Either If You want to Back This This script Enter > {r}Q {w}")
    editor_choice = input("Enter Related Number or Quit> Q  :")
    if editor_choice == '1':
        time.sleep(0.4)
        system('clear')
        system('apt update')
        system('apt upgrade -y')
        system('apt-get install nano -y')
        print ('install Completed')
        time.sleep(0.4)
    elif editor_choice == '2':
        time.sleep(0.4)
        system('clear')
        system('apt update')
        system('apt upgrade -y')
        system('apt-get install neovim -y')
    elif editor_choice == '3':
        time.sleep(0.4)
        system('clear')
        system('apt update')
        system('apt upgrade -y')
        system('apt-get install vim -y')
    elif editor_choice == '4':
        time.sleep(0.4)
        system('clear')
        system('apt update')
        system('apt upgrade -y')
        system('apt-get install emacs -y')
        time.sleep(0.4)
        system('clear')
    elif editor_choice == '5':
        time.sleep(0.4)
        system('clear')
        system('apt update')
        system('apt upgrade -y')
        system('apt-get install jupp -y')
        time.sleep(0.4)
        system('clear')
    elif editor_choice == '6':
        time.sleep(0.4)
        system('clear')
        system('apt update')
        system('apt upgrade -y')
        system('apt-get install micro -y')
        time.sleep(0.4)
        system('clear')
    elif editor_choice == '7':
        time.sleep(0.4)
        system('clear')
        system('apt update')
        system('apt upgrade -y')
        system('apt-get install micro -y')
        time.sleep(0.4)
        system('clear')
    elif editor_choice == 'Q':
        
        system('clear')
        time.sleep(0.4)
        print ('Thank You @')
        time.sleep(0.3)
        break
    elif editor_choice == 'q':
	
         system('clear')
         time.sleep(0.4)
         print (f'{r}Thank You @{w}')
         time.sleep(0.4)
         break
    elif editor_choice == 'quite':
	
        system('clear')
        time.sleep(0.5)
        print (f'{r}Thank You @{w}')
        time.sleep(0.5)
        break
 
    else:
        print (f'{r}{editor_choice}  {g}Not Found Error{w}')
        time.sleep(0.6)
        pass


    OTP += 1


