# import requests
# url="https://coinmarketcap.com/"
# rq=requests.get(url)
# # url="https://coinmarketcap.com/"
# # rq=requests.get(url)
# pars=txt.split("<span>")
# coin=[]
# for tag in pars:
#     if tag.startswith("$"):
#         for t in tag.split("</span>"):
#             if t.startswith("$") and t[1].isdigit():
#                 coin.append(t)
#                 # print(coin)
#                 # print(t)
# print("Bitcoin =",coin[0])
# print("Elhereum =",coin[1])
# print("Tether USDT =",coin[2])
# print(pars)

# from bs4 import BeautifulSoup as BS
# import requests
# url="https://coinmarketcap.com/"
# rq=requests.get(url)
# if rq.status_code==200:
#     txt=BS(rq.text, features="html.parser")
#     pars=txt.find_all("a",{"href":"/currencies/bitcoin/#markets"})
#     print(pars)
#     res=pars[0].find("span")
#     print(res)
#     # print("Bitcoin =", res.text)


from bs4 import BeautifulSoup as BS
import requests
import pandas as PD
file="auto.csv"
url="https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&categories.main.id=1&country.import.usa.not=-1&price.currency=1&fuel.id[4]=5&abroad.not=0&custom.not=1&page=0&size=20&scrollToAuto=35321960"
def car(site=url):
rq=requests.get(url)
if rq.status_code==200:
    txt =BS(rq.text, features="html.parser")
    pars = txt.find_all("span", {"data-currency": "USD"})
    #print(pars)
    kol=0
    for i in pars:
        kol+=1;
        print("Авто №",i.text, sep="")
    # res = pars[0].find("span")
    # print(res)
    # print(" Audi A6 2018 =", i.text)
    print("\n")
    costAuto=[]
    for i in pars:
        costAuto.append(i.text)
    nameAuto=["Audi A6 2018","Volkswagen Golf 2016","Land Rover Range Rover 2021","Volvo XC90 2021","Ford Fusion 2019"]
    for i in range(5):
        print(nameAuto[i], "цена","$",costAuto[i],sep="")

if car()==True:
    print("Даные успешно сохранены в файле")
else:
    print("ошибка")

f=PD.DataFrame(data=car())
f.to_csv(file)

