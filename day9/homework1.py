# input ფუნქციით შემოატანინეთ წინადადება და შმოტანილ წინადედებაში პროგრამას დაათვლევინეთ თანხმოვნები

sentence = input("Please enter a sentence here: " )  #hello
vowels = "aeiouAEIOU"

consonant_count = 0

for char in  sentence:
    if char not in vowels:
        consonant_count += 1

print("In this sentence are", "" , consonant_count, "" , "consonants")
