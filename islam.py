from colorama import Fore, Style
m = r"""              
██╗  ██╗ █████╗  ██████╗██╗  ██╗     ██╗   ██╗███████╗██╗          
██║  ██║██╔══██╗██╔════╝██║ ██╔╝     ██║   ██║██╔════╝██║          
███████║███████║██║     █████╔╝█████╗██║   ██║█████╗  ██║          
██╔══██║██╔══██║██║     ██╔═██╗╚════╝██║   ██║██╔══╝  ██║          
██║  ██║██║  ██║╚██████╗██║  ██╗     ╚██████╔╝███████╗███████╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝      ╚═════╝ ╚══════╝╚══════╝
                            
"""
try:
    import requests
except ModuleNotFoundError:
    print('xxxxxxx')
def inpu():
    num = 0
    numr = 0
    print(Fore.GREEN,m)
    x=input("url:  ").rstrip("/")
    l=input('file:  ')
    try:
        file=open(l,'r')
    except FileNotFoundError:
        print("the file is not found")
    for line in file:
        try:
            get=f'{x}/{line.strip()}'
            respons= requests.get(get)
        except Exception as r :
            print (f"eroor: {r}")
    
        o= respons.status_code
        if o <=200:
            print(Fore.GREEN+f'[{o}]  {get}')
            num = num+1
        else:
            print(Fore.RED+f'[{o}]  {get}')
            numr=numr+1
    print(Fore.GREEN,f"get  {num}")
    print(Fore.RED,f'eroor   {numr}')
inpu()
