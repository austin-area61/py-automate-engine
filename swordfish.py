while True:
    print('Who do you love?')
    name = input()
    if name != 'Maggie':
        print("did not quite get that. Try again")
    else:
        print('Where did you meet?')
        place = input()
        if place != 'Rafiki':
            print('You dont have any more trials')
        else:
            break
print('Congratulations! Level 2 unlocked!')
