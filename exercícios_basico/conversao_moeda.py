'''

Problema: Converta um valor em reais para dólares usando uma taxa fixa de câmbio.

'''

def convert_to_dollar(amount_in_reais, exchange_rate): 
    return round(amount_in_reais / exchange_rate, 2)

print(convert_to_dollar(500, 4.85)) # 103.09 (exemplo)