#Name : Aman Ali
#Roll number : 07

#ANS 1

Scores = [35, 50, 20, 30, 55, 75, 90, 95, 66, 80]

for score in Scores:
    if score > 70:
        print("distinction")
    elif score >= 60:
        print("first class")
    elif score >= 50:
        print("second class")
    elif score >= 35:
        print("just pass")
    else:
        print("fail")

#ANS 2

Book_price = {'Python': 600, 'Java': 400, 'Web_Tech': 550, 'OS': 450, 'IT': 700}

for book, price in Book_price.items():
    if price > 500:
        print(book,price)

#ANS 3

list=[1,2,3,4,5,6]
for i in list:
    i=i**2
    print(i)

#ANS 4

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
for i in list1:
    for j in list2:
        print(i + j)

#ANS 5

List = [100, 200, 300, 400, 500]
i=List[::-1]
print(i)

#ANS 6

List = [1000, 2000, 3000, 4000, 5000, 6000, 8000]
List.insert(List.index(6000) + 1, 7000)
print(List)

#ANS 7

list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

# Access the innermost list
innermost_list = list[2][1][2]

# Append the sub-list to the innermost list
innermost_list.extend(sub_list)

print(list)

#ANS 8

list1=[5, 10, 15, 20, 25, 50, 20]
index=list1.index(20)
list1[index]=200
list1

#ANS 9

Player_game = {'Sachin': 'Cricket', 'Rahul': 'Cricket', 'Messi': 'Football', 'Federer': 'Tennis', 'Anand': 'Chess'}
for Player ,game in Player_game.items():
    if game=='Cricket':
        print(Player)

#ANS 10

List = [1, 2, 4, 5, 10, 20, 4, 5]

list_sum = sum(List)

print("Sum of all elements in List:", list_sum)
