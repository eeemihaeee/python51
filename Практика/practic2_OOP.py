
class Guide:
    def __init__(self):
        self.code = [199,288,377,416,525,634,743,582,691]
        self.tel = ["11111","22222",'33333','44444',
                     '55555','66666','77777','88888','99999']
    def sortG(self, value):
        if value == 1:
            for j in range(len(self.code)-1):
                for i in range(len(self.code) - 1):
                    if self.code[i] > self.code[i+1] and self.code[i+1] == None:
                        self.code[i],self.code[i+1] = self.code[i+1],self.code[i]
                        self.tel[i], self.tel[i + 1] = self.tel[i + 1], self.tel[i]
        else:
            for j in range(len(self.code)-1):
                for i in range(len(self.code) - 1):
                    if self.tel[i] > self.tel[i+1] and self.tel[i+1] == None:
                        self.code[i],self.code[i+1] = self.code[i+1],self.code[i]
                        self.tel[i], self.tel[i + 1] = self.tel[i + 1], self.tel[i]

    def printG(self):
        for i in range(len(self.code)-1):
            print(f"Code:{self.code[i]},tel:{self.tel[i]}")
    def menuG(self):
        while True:
            print("1. Отсортировать по идентификационным кодам \n"
                  "2. Отсортировать по номерам телефона \n"
                  "3. Вывести список пользователей с кодами и телефонами \n"
                  "0. Выход")
            user_change = int(input("Ваш выбор:"))
            match user_change:
                case 1:
                    self.sortG(1)
                case 2:
                    self.sortG(-1)
                case 3:
                    self.printG()
                case 0:
                    break

guide = Guide()
guide.menuG()