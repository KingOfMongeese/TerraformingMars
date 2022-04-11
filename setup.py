#KingOfMongeese
import os




def install():
    print('Missing Module... art')
    print('Installing module... art')
    try:
        os.system('pip install art')
        import art
    except:
        print('Unable to install through pip')
        cont = input('Try installing pip now?(y/n)').strip().lower()
        if cont.startswith('y'):
            os.system('sudo apt update && sudo apt install python3-pip')
            os.system('pip install art')
try:
    import art
    print('art Found')
    print('setup complete')
    
except:
    install()
    try:
        import art
        print('art Found \nSetup complete')
    except:
        print('Setup incomplete')

    






