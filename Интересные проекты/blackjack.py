import random, sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BLACKSIDE = 'blackside'

def main():
    print("Добро пожаловать в игру БлекДжек!")
    print("Правила игры: ")
    money = 5000
    while True:
        if money <= 0:
            print("Ты проиграл все свои деньги!")
            sys.exit()
        print(f"Money: {money}")
        #Ставка игрока на раунд
        bet = getBet(money)
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(),deck.pop()]
        #бработка действий игрока:
        print(f"Ваша ставка: {bet}")
        while True: #будем продолжать цикл, пока у игрока не будет перебор
        # или он не скажет хватит
            displayHands(playerHand, dealerHand, False)
def displayHands(playerHand, dealerHand, showDealerHand):
    # Отображаем карты игрока и диллера. Скрываем первую карту дилера,
    # если showDealerHand равно False.
    print()
    if showDealerHand:
        print(f"ДИЛЛЕР: {getHandValue(dealerHand)}")
        displayCards(dealerHand)
    else:
        print(f"ДИЛЛЕР: ???")
        displayCards([BLACKSIDE] + dealerHand[1:])
    print(f"Игрок: {getHandValue(playerHand)}")
    displayCards(playerHand)
def getHandValue(cards):
    #Вернем стоимость карт. Фигурные карты стоят 10, тузы - 11 или 1.
    value = 0
    numberOfAces = 0
    for card in cards:
        rank = card[0]
        if rank == "A":
            numberOfAces += 1
        elif rank in ('K',"Q","J"):
            value += 10
        else:
            value += int(rank)
    #Добавляем стоимость тузов
    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    return value
#Функция создания колоды
def getDeck():
    deck = []
    #Вернуть список кортежей(номинал, масть) для всех 52 карт
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank), suit)) #добавляем числовые карты
        for rank in ('J','Q','K','A'):
            deck.append(((rank), suit)) #Добавляем старшие карты
    random.shuffle(deck) #тасуем
    return deck
#Функция для ставки
def getBet(maxBet):
    while True:
        #Спрашиваем игрока, сколько он ставит на этот раунд
        print(f"Вы можете поставить от 1 до {maxBet}, пропуск - QUIT")
        bet = input('--> ').upper().strip()
        if bet == "QUIT":
            print("Спасибо за игру!")
            sys.exit()
        if not bet.isdecimal():
            continue #Если игрок не ответил
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

if __name__ == '__main__':
    main()