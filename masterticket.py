TICKET_PRICE = 10
SERVICE_CHARGE = 2
ticket_remaining = 100

def calc_price(numer_of_tickets):
    return (TICKET_PRICE * numer_of_tickets)+SERVICE_CHARGE


while ticket_remaining >= 1:
    print ("There are {} tickets remaing".format(ticket_remaining))
    name = input("What is your name?:   ")
    ticket_amount = input("How many tickets would you like to purchse?:  ")
    try:
        ticket_amount = int(ticket_amount)
        if ticket_amount > ticket_remaining:
            raise ValueError("There are only {} tickets remaining".format(ticket_remaining))
    except ValueError as err:
        print("Invalid! Sorry not enough tickets. {}".format(err))
    else:
        total = calc_price(ticket_amount)
        print("Thank you {}. Your are total for {} tickets will be ${}".format(name, ticket_amount, total))
        proceed = input("Would you like purchase your tickets? (yes or no):   ")
        if proceed.lower() == "yes":
            print("sold")
            ticket_remaining = ticket_remaining - ticket_amount
        else:
            print("Thank You {}, come again!".format(name))
print("Sorry All Sold Out")
