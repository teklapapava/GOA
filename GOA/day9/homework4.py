# შექმენით სია სადაც შემოიტანთ რამდენმე რიცხვს 
# მაგ:"24,50,25,90"  რომელიმე რიცხვი ჩაანაცვლეთ და გამოითვალეთ ამ რიცხვევის ჯამი
list = [21, -3, 48, 29, 11, -31, 7, -34]
list.insert(6,77)

sum_list = 0

for i in list:
    if i > 0 :
        sum_list = sum_list + i

print (list)
print(sum_list)