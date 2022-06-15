secret_num= 7
guess=3
guess_count=0
while guess_count<guess:
    guss_num= int(input('Enter your guess'))
    guess_count+=1
    if guss_num==secret_num:
        print('you are right!')
        break
else:
    print('you lose')
