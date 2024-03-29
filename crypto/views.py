from django.shortcuts import render

def home(request):
    import requests
    import json
    #Grab crypto price Data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)
    
    
    #Grab crypto new
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})

#when a request is submitted
def prices(request):
    import requests
    import json
    
    
    
    
    
    if request.method =='POST':
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote':quote, 'crypto':crypto})
    else:
        notfound = "Enter a crypto currency symbol into the form above.."
        return render(request, 'prices.html',{'notfound': notfound})



