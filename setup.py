#KingOfMongeese
import os
import platform



def install():
    print('***Missing Module... art***')
    print('Installing module... art')
    try:
        os.system('pip install art')
        import art
    except:
        print('***Unable to install through pip***')
        cont = input('Try installing pip now?(y/n)').strip().lower()
        if cont.startswith('y'):
            if platform.system == 'Linux':
                os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
                os.system("python3 get-pip.py")
                os.system('pip install art')
            elif platform.system == "Windows":
                print("Windows")
                os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
                os.system("python get-pip.py")
                os.system('pip install art')
try:
    import art
    print('Art Found')
    print('setup complete')
    
except:
    install()
    try:
        import art
        print('art Found \nSetup complete')
    except:
        print('Setup incomplete. Is Python installed?')

    






