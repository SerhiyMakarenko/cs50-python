amount_due = 50
while amount_due > 0:
    print("Amount Due: ", amount_due)
    coin = int(input("Insert Coin: "))
    match coin:
        case 25:
            amount_due = amount_due - coin
        case 10:
            amount_due = amount_due - coin
        case 5:
            amount_due = amount_due - coin
print("Change Owed: ", abs(amount_due))