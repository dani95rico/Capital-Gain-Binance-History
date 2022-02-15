#  EXAMPLE OF HOW CALCULATE THE CAPITAL GAIN WITH THE TRANSACTIONS HISTORY
#  THAT BINANCE PROVIDE US. FIFO SYSTEM. BY DANI95RICO

import pandas as pd

def main():
    df = pd.read_excel("trade_history.xlsx")

    df_reverse = df.iloc[::-1]
    df_reverse = df_reverse.reset_index()
    crypto_names = list(df_reverse["Market"].unique())
    print("You've trade with this cryptos: " + str(crypto_names))
    df_reverse
  
    for i, name in enumerate(crypto_names):
      calcular_plusvalias(name)

def calcular_plusvalias(name):
    index = []
    list_amount_purchase = []
    list_price_purchase = []
    list_plusvalia = []
    list_inv = []
    print("                            MONEDA: " + name)
    print()
    print("HISTORIAL DE OPERACCIONES")
    for i, row in df_reverse.iterrows(): 
        if row["Type"] == "BUY" and row["Market"] == name:
            list_amount_purchase.append(row["Amount"])
            list_price_purchase.append(row["Price"])
            list_inv.append(row["Total"])
            print("  TRANSACCIÓN "+ str(i) +"- Compra realizada: "+ str(row["Amount"]) +" monedas a un precio de "+ str(row["Price"]) +"€. Total invertido: "+ str(row["Total"])+"€")
        if row["Type"] == "SELL" and row["Market"] == name:
            if row["Amount"] > sum(list_amount_purchase):
                print("  You're trying to sell higher amount than you have")
                break
            amount_sale = row["Amount"]
            print("  TRANSACCIÓN "+ str(i) +"- Venta realizada: "+ str(row["Amount"]) +" monedas a un precio de "+ str(row["Price"]) +"€")
            print("  PLUSVALÍAS")
            for j,amount_purchase in enumerate(list_amount_purchase):
                plusvalia = row["Price"]*amount_sale-df_reverse["Price"][j]*amount_sale
                if amount_sale > amount_purchase:
                    list_plusvalia.append(plusvalia)
                    amount_sale = amount_sale - amount_purchase
                    list_amount_purchase[j] = 0
                elif amount_sale <= amount_purchase:
                    list_plusvalia.append(plusvalia)
                    rest_coin = amount_purchase - amount_sale
                    list_amount_purchase[j] = rest_coin
                    break
            print("    Plusvalia respecto a la transaccion "+ str(i-j) + ": "+ str(plusvalia) +"€  Dinero obtenido: "+ str(row["Total"]) +"€")
    print()        
    print("DINERO TOTAL INVERTIDO: "+ str(sum(list_inv)) +"€")
    total = sum(list_plusvalia) + sum(list_inv)
    print("DINERO TOTAL ACUMULADO: "+ str(total) +"€")
    print("PLUSVALÍA TOTAL: "+ str(sum(list_plusvalia)) +"€")
    print()
    
if __name__ == '__main__':
    main()
