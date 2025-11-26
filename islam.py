try:
    import requests
except ModuleNotFoundError:
    print('xxxxxxx')
def inpu():
    h={}
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
        print(f'[{o}]   {get}')
inpu()