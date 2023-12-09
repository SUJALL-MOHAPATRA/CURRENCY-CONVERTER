from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
import currency_codes as cc #self made module(uploaded/attached)

#Currency Conversion
def curconv():
    rate=CurrencyRates()
    cc.show_codes()
    print('\n')
    amt=float(input("Enter the amount of currency:"))
    fc=input("From currency: ").upper()
    tc=input("To currency: ").upper()
    
    
    try:
        valid= rate.get_rates(fc)
        if tc in valid:
            cr=rate.get_rate(fc,tc)       
            new_amt=amt*cr

            print(amt,fc,"=",new_amt,tc,'\n')
        else:
            print("Invalid currency. Please enter a valid currency.\n")
        
    except: #For RatesNotAvailableError
        print("currency rate not available for",fc,'\n')
    
#Bitcoin Conversion
def bitconv():
    btc=BtcConverter()
    cc.show_codes()
    print('\n')

    ct=input("currency type:").upper()
    print("\n1.BITCOIN TO CURRENCY\n2.CURRENCY TO BITCOIN")
    c=int(input("enter choice:"))
    if c==1:
        amt=float(input("Enter the amount of bitcoin:"))
        print("Currency amount:",btc.convert_btc_to_cur(amt,ct),'\n')
    elif c==2:
        amt=float(input("Enter the amount of currency:"))
        print("Bitcoin amount:",btc.convert_to_btc(amt,ct),'\n')



#MAIN PROGRAM
print("\t\tCURRENCY CONVERTER")
p='y'
while p in ['y','Y','YES','yes']:
    print("\n1.Currency Conversion\n2.Bitcoin Conversion")
    c=int(input("Enter choice number:"))
    f='y'
    if c==1:
        
        while f in ['y','Y','YES','yes']:
            curconv()
            f=input("more conversion?.....(y/n):")
            if f in ['n','N','NO','no']:
                break

        
    elif c==2:
        
        while f in ['y','Y','YES','yes']:
            bitconv()
            f=input("more conversion?.....(y/n):")
            if f in ['n','N','NO','no']:
                break

    
    p=input("continue program?.....(y/n):")
    if p in ['n','N','NO','no']:
        break

print("\n\t\tPROGRAM CLOSED")
        
