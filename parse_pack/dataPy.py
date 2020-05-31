class Data():
    def __init__(self, values):
        self.names = values[::3]

        del values[::3]

        self.buys = values[::2]
        self.sells = values[1::2]

        self.best_buy_value = max(self.buys)
        self.best_sell_value = min(self.sells)

    def get_list(self):
        message = ''
        i = 0
        while i < len(self.names):
            message += f'{self.names[i]}: \nПродажа: {self.buys[i]} \nПокупка:{self.sells[i]} \n\n'
            i+=1
        return message.rstrip()


    def __get_name_best_buy(self, values, best_value): 
        i = 0
        while i < len(self.buys):
            if values[i] == best_value:
                best_value = self.names[i]
                return self.names[i]
            else:
                i += 1

    def get_best_buy(self):
        best_buy_name = self.__get_name_best_buy(self.buys, self.best_buy_value)
        return f'{best_buy_name} - {self.best_buy_value}'

    def get_best_sell(self):
        best_buy_name = self.__get_name_best_buy(self.sells, self.best_sell_value)
        return f'{best_buy_name} - {self.best_sell_value}'
