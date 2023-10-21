#პირობა: input ფუნქციაში მომხამრებელს შემოატანინიეთ წინადადება და პროგრამამ დაუთვალოს თანხმოვნების რაოდენობა.

ask=input("დაწერე ქართული შრიფტით რაიმე წინადადება..: ")
answer=[ask]
newlist=[]
newlist = [x for x in ask if "ბ" in x]
newlist1= [x for x in ask if "გ" in x]
newlist2 = [x for x in ask if "დ" in x]
newlist3= [x for x in ask if "ვ" in x]
newlist4= [x for x in ask if "ზ" in x]
newlist5= [x for x in ask if "თ" in x]
newlist6= [x for x in ask if "კ" in x]
newlist7= [x for x in ask if "ლ" in x]
newlist8= [x for x in ask if "მ" in x]
newlist9= [x for x in ask if "ნ" in x]
newlist10= [x for x in ask if "პ" in x]
newlist11= [x for x in ask if "ჟ" in x]
newlist12= [x for x in ask if "რ" in x]
newlist13= [x for x in ask if "ს" in x]
newlist14= [x for x in ask if "ტ" in x]
newlist15= [x for x in ask if "ფ" in x]
newlist16= [x for x in ask if "ქ" in x]
newlist17= [x for x in ask if "ღ" in x]
newlist18= [x for x in ask if "ყ" in x]
newlist19= [x for x in ask if "შ" in x]
newlist20= [x for x in ask if "ჩ" in x]
newlist21= [x for x in ask if "ც" in x]
newlist22= [x for x in ask if "ძ" in x]
newlist23= [x for x in ask if "წ" in x]
newlist24= [x for x in ask if "ჭ" in x]
newlist25= [x for x in ask if "ზ" in x]
newlist26= [x for x in ask if "ჯ" in x]
newlist27= [x for x in ask if "ჰ" in x]


y=len(newlist)+len(newlist1)+len(newlist2)+len(newlist3)+len(newlist4)+len(newlist5)+len(newlist6)+len(newlist7)+len(newlist8)+len(newlist9)+len(newlist10)+len(newlist11)+len(newlist12)+len(newlist13)+len(newlist14)+len(newlist15)+len(newlist16)+len(newlist17)+len(newlist18)+len(newlist19)+len(newlist20)+len(newlist21)+len(newlist22)+len(newlist23)+len(newlist24)+len(newlist25)+len(newlist26)+len(newlist27)
print("შენს მიერ დაბეჭდილი წინადადება შეიცავს...:  " + str(y)+ "  თანხმოვანს")
