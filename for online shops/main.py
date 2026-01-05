import re

text = """  .... """

# same ID and same cost collect qilish uchun)
lines = text.splitlines()
pairs = []
for i in range(len(lines) - 1):
    if re.fullmatch(r"\d{8}", lines[i].strip()):
        summa_match = re.search(r"(\d+)\s*сум", lines[i+1])
        if summa_match:
            summa = int(summa_match.group(1))
            pairs.append((lines[i].strip(), summa))

# bir xil id lar olib tashlanib faqat bittasi qoladi)
unique_pairs = list(set(pairs))

# Jami summa
total = sum(summa for _, summa in unique_pairs)

print("Jami summa:", total)




# FOR EXAMPLE:
# text= """ID	Ячейка	Дата заказа	  Дата приёмки	     Сумма	      Покупатель	  Телефон	Статус	     Тип оплаты	        Дата выдачи
#     86 978 562  111  01.01.26,23:01	04.01.26,09:56	138 000 сум	    shopper	        TEL	    Заказ выдан	  Постоплата	 4 января 2026 г. в 19:23
#     87 024 868  142  02.01.26,13:32	04.01.26,10:07	56 650 сум	    shopper 	    TEL	    Заказ выдан	  Постоплата	 4 января 2026 г. в 19:13"""