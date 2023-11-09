line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
comp = position[0].lower()
letter_index= ["a","b","c"].index(comp)
number_index = int(position[1])-1
map[number_index][letter_index]= 'X'                          
print(f"{line1}\n{line2}\n{line3}")