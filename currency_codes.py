def show_codes():
    codes={'US Dollar':'USD','Euro':'EUR','Austrakian Dollar':'AUD','Taka':'BDT','Indian Rupee':'INR','Brazilian Real':'BRL','Canadian Dollar':'CAD','Japanese Yen':'JPY','Bulgarian Lev':'BGN','Czech Koruna':'CZK','Denmark Danish Crone':'DKK','Pound Sterling':'GBP','Hungary Forint':'HUF','Poland Zloty':'PLN','Romanian Leu':'RON','Indonesia Rupiah':'IDR','Korea Won':'KRW','Malaysian Ringgit':'MYR','Mexican Peso':'MXN','New Zealand Dollar':'NZD'}
    print('\nCURRENCY','-','CODE')
    for i in codes:
        print(i,'-',codes[i])
