import random

MIN_BET = 5
MAX_BET = 1000

balance = 0

point = 0

pass_bets = {'pass': 0, '4': 0, '5': 0, '6': 0, '8': 0, '9': 0, '10': 0}

dont_pass_bets = {'dont pass': 0}


def dice_roll():
    dice_art = {
        1: ("┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"),
        2: ("┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"),
        3: ("┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"),
        4: ("┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"),
        5: ("┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"),

        6: ("┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘")
    }
    dice = []
    total = 0
    num_of_dice = 2

    for die in range(num_of_dice):
        (dice.append(random.randint(1, 6)))

    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end="")
        print()

    for die in dice:
        total += die
    print(f"total: {total}")
    return total


def print_balance():
    print("Balance $" + str(balance))


def print_bets():
    print("Your current bets are: ")
    for k, v in pass_bets.items():
        if v != 0:
            print(str(k) + "= $" + str(v))
        if pass_bets.values == 0:
            print("No Bets")


def initial_bet():
    while True:
        p_dp = input("Would you like to bet on Pass Line or Don't Pass Line? (P/DP) ")
        if p_dp in ["P", "p", "pass", "Pass", "Pass Line", "pass line"]:
            amount = input("How much? $")
            if amount.isdigit():
                if MIN_BET <= int(amount) <= MAX_BET:
                    pass_bets['pass'] += pass_bets['pass'] + int(amount)
                    break
                else:
                    print(str(f"Please choose an amount between $" + str(MIN_BET) + " and $" + str(MAX_BET) + "."))
            else:
                print("Please use only numbers.")
        if p_dp in ["DP", "dp", "dont pass", "Dont pass", "Dont Pass", "don't pass", "Don't pass", "Don't Pass"]:
            amount = input("How much? $")
            if amount.isdigit():
                if MIN_BET <= int(amount) <= MAX_BET:
                    dont_pass_bets['dont pass'] += dont_pass_bets['dont pass'] + int(amount)
                    break
                else:
                    print(str(f"Please choose an amount between $" + str(MIN_BET) + " and $" + str(MAX_BET) + "."))
            else:
                print("Please use only numbers.")
        else:
            print("Please enter either 'p' or 'dp'")


def place_bet():
    while True:
        additional_bet = input("Would you like to place an additional bet?")
        if additional_bet in ["no", "n", "nope"]:
            break
        else:
            if additional_bet in ["yes", "y", "Yes", "Y"]:
                bet = input("What bet would you like to place? ")
                if bet in ["4", "5", "6", "8", "9", "10"]:
                    amount = input("How much $")
                    pass_bets[bet] += pass_bets[bet] + int(amount)
                else:
                    print("Please do not spell out numbers, use the corresponding number key.")
                    continue
            else:
                print("Please enter yes/no,")


def come_out_roll():
    while True:
        global balance
        global point
        global pass_bets
        total = dice_roll()
        come_out = total
        if come_out == 2:
            print("You Lose")
            balance = balance - pass_bets['pass']
            pass_bets['pass'] = 0
            main()
        if come_out == 3:
            print("You Lose")
            balance = balance - pass_bets['pass']
            pass_bets['pass'] = 0
            main()
        if come_out == 4:
            print("The Point is now 4")
            point = 4
            break
        if come_out == 5:
            print("The point is now 5")
            point = 5
            break
        if come_out == 6:
            print("The point is now 6")
            point = 6
            break
        if come_out == 7:
            print("You win!")
            balance = balance + pass_bets['pass']
        if come_out == 8:
            print("The point is now 8")
            point = 8
            break
        if come_out == 9:
            print("The Point is now 9")
            point = 9
            break
        if come_out == 10:
            print("The Point is now 10")
            point = 10
            break
        if come_out == 11:
            print("You win")
            balance = balance + pass_bets['pass']
        if come_out == 12:
            print("You lose")
            balance = balance - pass_bets['pass']
            pass_bets['pass'] = 0
            main()
        print(f"$" + str(balance))
        input("Press Enter to roll again")


def point_rolls():
    while True:
        global balance
        global point
        global pass_bets
        total = dice_roll()
        roll = total
        if roll == point:
            print("Front Line winner!")
            balance = balance + pass_bets['pass']
            pass_bets['pass'] = 0
            point = 0
            print_balance()
            print_bets()
            main()
        if roll == 2:
            print("(2) Snake Eyes!")
        if roll == 3:
            print("(3) Dice rolled a 3")
        if roll == 4:
            print("(4) Dice rolled a 4")
            if pass_bets['4'] > 0:
                balance = balance + pass_bets['4'] * 9/5
                print_balance()
                print_bets()
        if roll == 5:
            print("(5) No field 5")
            if pass_bets['5'] > 0:
                balance = balance + pass_bets['5'] * 7/5
                print_balance()
                print_bets()
        if roll == 6:
            print("(6) Dice rolled a 6")
            if pass_bets['6'] > 0:
                balance = balance + pass_bets['6'] * 7/6
                print_balance()
                print_bets()
        if roll == 7:
            print("(7) Dice rolled a 7")
            print("Big Red, game over!")
            balance = balance - sum(pass_bets.values())
            pass_bets = {'pass': 0, '4': 0, '5': 0, '6': 0, '8': 0, '9': 0, '10': 0}
            point = 0
            print_balance()
            main()
        if roll == 8:
            print("Dice rolled an 8")
            if pass_bets['8'] > 0:
                balance = balance + pass_bets['8'] * 7/6
                print_balance()
                print_bets()
        if roll == 9:
            print("(9) Dice rolled a 9")
            if pass_bets['9'] > 0:
                balance = balance + pass_bets['9'] * 7/6
                print_balance()
                print_bets()
        if roll == 10:
            print("(10) Dice rolled a 10")
            if pass_bets['10'] > 0:
                balance = balance + pass_bets['10'] * 9/5
                print_balance()
                print_bets()
        if roll == 11:
            print("(11) Dice rolled an 11")
        if roll == 12:
            print("(12) Boxcars")
        while True:
            additional_bet = input("Would you like to place an additional bet? ")
            if additional_bet in ["yes", "y", "Yes", "Y"]:
                bet = input("What bet would you like to place? ")
                if bet in ["4", "5", "6", "8", "9", "10"]:
                    amount = input("How much $")
                    pass_bets[bet] += pass_bets[bet] + int(amount)
                else:
                    print("Please do not spell out numbers, use the corresponding number key.")
            if additional_bet in ["no", "n", "nope"]:
                break
        input("Press Enter to roll again")


def get_bankroll():
    global balance
    if balance == 0:
        while True:
            balance = input("How much would you like to gamble with? $")
            if balance.isdigit():
                balance = int(balance)
                if balance > 0:
                    break
                else:
                    print("You must enter more than 0.")
            else:
                print("Please enter a whole number, without a comma or decimal point.")
        return balance


def main():
    get_bankroll()
    initial_bet()
    come_out_roll()
    place_bet()
    point_rolls()


main()


# make pass bet work
