from django.shortcuts import render
import requests
import json
# Create your views here.

def exchange(request):
    url = "https://api.apilayer.com/exchangerates_data/symbols"

    payload = {}
    headers= {
    "apikey": "j8bOXYJxbjFnEaiPcCjyaxydyE4pbxWb"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = json.loads(response.text)
    currencies = result['symbols'].keys()
    
    if request.method == 'GET':
        
        context = {
         "currencies":currencies
        }
        
        return render(request, 'index.html', context)
    
    if request.method == 'POST':
        from_amount = float(request.POST.get('from-amount'))
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')

        

        url = "https://api.apilayer.com/exchangerates_data/convert?to=" + to_curr + "&from=" + from_curr + "&amount=" + str(from_amount)

        payload = {}
        headers= {
            "apikey": "j8bOXYJxbjFnEaiPcCjyaxydyE4pbxWb"
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        status_code = response.status_code
        result = json.loads(response.text)
        converted_amount = round(result['result'], 2)
        
        context = {
            "currencies":currencies,
            "converted_amount": converted_amount,
            "to_curr": to_curr,
            "from_curr": from_curr,
            "from_amount": from_amount  

        }
        
        
        return render(request, 'index.html', context)



















def test(request):
    url = "https://api.apilayer.com/exchangerates_data/symbols"

    payload = {}
    headers= {
    "apikey": "j8bOXYJxbjFnEaiPcCjyaxydyE4pbxWb"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = json.loads(response.text)
    

    url = "https://api.apilayer.com/exchangerates_data/convert?to=GBP&from=EUR&amount=100"

    payload = {}
    headers= {
      "apikey": "j8bOXYJxbjFnEaiPcCjyaxydyE4pbxWb"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = json.loads(response.text)
    
    context = {
            'result': result['result']
        }
    return render(request, 'test.html', context)