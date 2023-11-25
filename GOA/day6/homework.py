#მომხმარებლის ნიშნებისგან გამოანგარიშება საშუალო არითმეტიკული და თუ ცხრაზე მეტი იქნება:
#დაუპრინტეთ გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები
#თუ ეს იქნება 5ზე ნაკლები: დაუპრინტე გილოცავ გაექეცი მატრიცას
#თუ იქნება 5 იდან 9 მდე: დაუპრინტე YOU ARE MID
#თუ იქნება 10ზე მეტი ან 0ზე ნაკლები: დაუპრინტე there is something wrong with you 



first=10
second=8
third=5
fourth=9
fifth=7
sashualo_aritmetikuli=(first+second+third+fourth+fifth)/5
if sashualo_aritmetikuli>9:
    print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები")
elif sashualo_aritmetikuli<5:
    print("გილოცავ გაექეცი მატრიცას")
elif sashualo_aritmetikuli>5:
    if sashualo_aritmetikuli<9:
        print(" YOU ARE MID")
elif sashualo_aritmetikuli>10:
    print("there is something wrong with you ")
elif sashualo_aritmetikuli<0:
    print("there is something wrong with you ")

 #მომხმარებელს შეეკითხეთ ხელფასი
#თუ 10000ზე მეტია, დაუპრინტეთ, გოა-ში სწავლობდი?
#თუ 1000----10000 -ია , დაუპრინტეთ you mid
#თუ 1000-ზე დაბალია, დაუპრინტეთ, შემოსულიყავი გოაში, მატრიცელო

salary = int(input("Enter your salary"))
if salary>10000:
    print("გოა-ში სწავლობდი?")
elif salary>1000:
    if salary<10000:
        print("you mid")
elif salary<1000:
    print("შემოსულიყავი გოაში, მატრიცელო")



