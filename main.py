import csv



baza = "Пьеро вскочил, размахивая руками. Веди меня к ней… Если ты мне поможешь отыскать Мальвину, я тебе открою тайну золотого ключик."

shifr = "‡tШhоZн{оЦ)лMhюіsю])Zюяhу{юs)ЖЎШ*)sШся{сШ`–Ђнл)}бsсШgоsо=ШДtо}бн{ю}tМюлtZ)суMя}ШlШо}{hоа}ю`суіоло}оuо{лаЦ){Ж"

shrie = "П9еЇiгв%4iuЈRmгЇё>Жё–ЈвёягЇҐ4ёЖЈЌгЬеБЈгЖе яг4г е&)гx%RЈгШђгЖ ег iЖiже†9гiШђ%4ёШ9гІёR9вЈ ҐmгягШе\егiШ4Їi?гШё& Ґг>iRiШiniг4R?uЈ4Ќ"

slova = baza.split()
mass = []
# #print(slova)

# for el in slova:
#     index = baza.find(el)
#     print(shifr[:index])
#     shifr = shifr[:index] + " " + shifr[index:]

# print(baza)
# print(shifr)

for el in slova:
    mass.append(len(el))

# print(mass)

count = 0
print(baza)
for el in mass:
    count += el
    shifr = shifr[:count] + " " + shifr[count:]
    shrie = shrie[:count] + " " + shrie[count:]
    #print(shifr)

# print(count)
#print(shifr[:mass[0]])

with open('egg.csv', "w+", newline="") as file:
    write = csv.writer(file, delimiter="+")
    write.writerow(list(baza))
    write.writerow(list(shifr))
    write.writerow(list(shrie))

print(list(shrie))