# შექმენით მეოთხე ჯგუფის წევრების სია .დაწერეთ კოდი ისე,რომ გაიგოთ ყველა სახელსა და გვარში 
# ერთად რამდენი  ,,ი" და ,,ა"   იქნება.

my_list = ["zuzadze", "lobjanidze", "abuladze", "atabegashvili", "papava","kacitadze", "gelashvili", 
           "labadze", "goglichadzze", "luka","guriko", "giorgi"]
other_char = 0
i_counter = 0
a_counter = 0
for element in my_list:
    for char in element:
        if char == "i":
            i_counter += 1
        elif char == "a":
            a_counter += 1
        else:
            other_char += 1
print("am siashi ertad aris 'a' da 'i' shemdegi raodenobit: " + str(i_counter+a_counter))