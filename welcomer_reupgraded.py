"""
Welcome function for whoever in three languages
"""

def welcome():
    print("Please, choose a language.")
    language = input()
    if language == "english":
        print('Hello ' + 'Who am I talking to?')
        print('Please, type your name.')
        yourname = input()
        print('Welcome ' + yourname + '.' + ' I am Python.')
        return print("Nice to meet you. Later!")
    
    elif language == "french":
        print('Bonjour' + ' À qui je parle?')
        print("S'il vous plaît, tapez votre nom.")
        yourname = input()
        print('Welcome ' + yourname + '.' + ' Je suis Python.')
        return print("Ravi de vous rencontrer. Au revoir!")
    
    elif language == "spanish":
        print('Hola ' + ' A quién le hablo?')
        print('Por favor, escriba su nombre.')
        yourname = input()
        print('Bienvenido ' + yourname + '.' + ' Me llamo Python.')
        return print("Mucho gusto. Hasta pronto!")
    else:
        return print("Sorry, I don't speak " + language + '. Please try another one.')

welcome()