#Newtons method for approximation of square roots


def square_root (num):
    guess=1
    prev_guess=-1
    while(1):
        quotient=num/guess
        print("The Quotient is ",quotient)
        guess=(quotient+guess)/2
        if (prev_guess==guess):
            break
        print(guess)
        prev_guess=guess
        

square_root(2)
#square_root(49)
#square_root(7777777777777777777777777777777)
