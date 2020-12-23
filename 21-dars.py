#def bahola(ismlar):
#    baholar = {}
#    while ismlar:
#        ism = ismlar.pop()
#        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#        baholar[ism]=baho
#    return baholar

#talabalar = ['ali', 'vali', 'hasan', 'husan']
#baholar = bahola(talabalar.copy())
#print(baholar)
#print(talabalar)



#Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.

#def katta_harf(matnlar):
#    for i in range(len(matnlar)):
#        matnlar[i]=matnlar[i].title()
#    return matnlar

#ismlar = ['ali', 'vali', 'hasan', 'husan']

#yangi_ismlar =katta_harf(ismlar.copy())

#print(ismlar)

#print(yangi_ismlar)



#Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va asl ro'yxatga o'zgartirish
# kiritmasdan faqat lug'at qaytaradigan qilib yozing.




#def bahola(ismlar):
#    baholar = {}
#    while ismlar:
#        ism = ismlar.pop()
#        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#        baholar[ism]=baho
#    return baholar

#talabalar = ['ali', 'vali', 'hasan', 'husan']
#baholar = bahola(talabalar)
#print(baholar)

#def son(ism):
#    lu={}
#    for s in range(len(ism)):
#        baho = input(f"Talaba {ism[s]} bahosini kiriting: ")
#        lu[ism[s]]=baho
#    return lu
#talabalar = ['ali', 'vali', 'hasan', 'husan']
#baholar =son(talabalar)
#print(baholar)

talabalar = ['ali', 'vali', 'hasan', 'husan']


def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar


baholar = bahola(talabalar)
print(baholar)
print(talabalar)
