# შექმენით ლისტი სადაც სტრინგის სახით ჩაწერთ სამ ელემენტს (სამივე განსხვავებული ზომის ),
#  გამოთვალეთ ელემენტების სიმბოლოების რაოდენობა და რომელიც საშუალო იქნება ის დაპრინტეთ .

sport = ["basketball", "football", "rugby"]

basketball = len(sport[0])
football = len(sport[1])
rugby = len(sport[2])

if basketball > football and rugby < basketball :
    print(sport[0])
elif football > rugby and football < basketball:
    print(sport[1])
else:
    print(sport[2])