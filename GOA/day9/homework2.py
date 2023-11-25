# შევქმნათ ორი List-ი. ერთში გოგონების სახელები ჩავწეროთ მეორეში ბიჭების. 
# დავპრინტოთ დაწყვილებულად

boys = ["nika", "giorgi", "levani", "sandro"]
girls = ["mariami", "tamuna", "sofo", "vika"]
i = 0
for name in boys:
    print(name + " " + girls[i])
    i += 1