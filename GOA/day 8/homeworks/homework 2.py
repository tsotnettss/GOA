#ბილეთის ფასი
ticket_price=25
#ჯგუფის წევრები
group=["of age","of age","of age","of age","of age","of age","of age","of age","of age","of age","teenager","teenager","teenager"]
#გადარჩული ჯგუფი
newlist=[]
#ჯგუფის "გაფილტვრის" ფუნქცია
newlist = [x for x in group if "of age" in x]
#ბილეთების საერთო ოდენობის ღირებულების ჯამის კალკულაცია
price=len(newlist)*25
print("ჯგუფის მიერ გადასახადი თანხა შეადგენს... "+str(price)+" ლარს რადგან არასრულწლოვანი მომხმარებლებისათვის შესვლა უფასოა")
