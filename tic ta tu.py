print("""
              ██╗    ██╗██████╗██╗     ██████╗ ██████╗ ███╗   ███╗██████╗ 
              ██║    ██║██╔═══╝██║    ██╔════╝██╔═══██╗████╗ ████║██╔═══╝ 
              ██║ █╗ ██║█████╗  ██║    ██║     ██║   ██║██╔████╔██║█████╗  
              ██║███╗██║██╔══╝  ██║    ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
              ╚███╔███╔╝██████╗██████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║██████╗ 
               ╚══╝╚══╝ ╚═════╝╚═════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ 
                                                            
                                ████████╗ ██████╗                           
                                ╚══██╔══╝██╔═══██╗                          
                                   ██║   ██║   ██║                          
                                   ██║   ██║   ██║                          
                                   ██║   ╚██████╔╝                          
                                   ╚═╝    ╚═════╝                           
                                                            
    ████████╗██╗ ██████╗     ████████╗ █████╗  ██████╗   ████████╗ ██████╗ ██████╗ 
    ╚══██╔══╝██║██╔════╝     ╚══██╔══╝██╔══██╗██╔════╝   ╚══██╔══╝██╔═══██╗██╔═══╝ 
       ██║   ██║██║             ██║   ███████║██║           ██║   ██║   ██║█████╗  
       ██║   ██║██║             ██║   ██╔══██║██║           ██║   ██║   ██║██╔══╝  
       ██║   ██║╚██████╗        ██║   ██║  ██║╚██████╗      ██║   ╚██████╔╝██████╗ 
       ╚═╝   ╚═╝ ╚═════╝        ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═╝    ╚═════╝ ╚═════╝ 
                                                                                
                          ██████╗  █████╗ ███╗   ███╗██████╗                          
                         ██╔════╝ ██╔══██╗████╗ ████║██╔═══╝                          
                         ██║  ███╗███████║██╔████╔██║█████╗                           
                         ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝                           
                         ╚██████╔╝██║  ██║██║ ╚═╝ ██║██████╗                          
                          ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝                          
""")



print("player 1 will play with x")
print("player 2 will play with o")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")
print("this is your board and at this board the position is define in no from 1-9")

x_o = [" "] * 9
def result():
    print(f" {x_o[0]} | {x_o[1]} | {x_o[2]} ")
    print("---+---+---")
    print(f" {x_o[3]} | {x_o[4]} | {x_o[5]} ")
    print("---+---+---")
    print(f" {x_o[6]} | {x_o[7]} | {x_o[8]} ")

def winner_system():
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 4, 8), (2, 4, 6), (0, 3, 6),
        (1, 4, 7), (2, 5, 8),
    ]
    for a, b, c in wins:
        if x_o[a] != " " and x_o[a] == x_o[b] == x_o[c]:
            return x_o[a]
    return None


   
   
while True:
    if not " " in x_o:
        print("game over(it's a draw)")
        break
    imp =input("x or o: ")
    if imp != "x" and imp != "o":
       print("⁉️‼️‼️‼️🫨‼️‼️‼️⁉️")
       print("invalid input only choose x or o ")
       continue

    position = int(input("choose the position digit: "))
    if position < 1 or position >9 :
       print("⁉️‼️‼️‼️🫨‼️‼️‼️⁉️")
       print("invalid input only choose from 1 to 9 ")
       continue

    if x_o[position- 1] != " ":
       print("‼️‼️‼️🫨‼️‼️‼️")
       print("the position is taken plz choose other position ")
       continue
       
       

    if imp == "x":
        if position ==1:
         x_o.pop(0)
         x_o.insert(0, imp)
         result()
         
    if imp == "x":
        if position ==2:
         x_o.pop(1)
         x_o.insert(1, imp)
         result()
    if imp == "x":
        if position ==3:
         x_o.pop(2)
         x_o.insert(2, imp)
         result()        
    if imp == "x":
        if position ==4:
         x_o.pop(3)
         x_o.insert(3, imp)
         result()  
    if imp == "x":
        if position ==5:
         x_o.pop(4)
         x_o.insert(4, imp)
         result()
    if imp == "x":
        if position ==6:
         x_o.pop(5)
         x_o.insert(5, imp)
         result()

    if imp == "x":
        if position ==7:
         x_o.pop(6)
         x_o.insert(6, imp)
         result()
    if imp == "x":
        if position ==8:
         x_o.pop(7)
         x_o.insert(7, imp)
         result()         
    if imp == "x":
        if position ==9:
         x_o.pop(8)
         x_o.insert(8, imp)
         result()
    if imp == "o":
        if position ==1:
         x_o.pop(0)
         x_o.insert(0, imp)
         result()
    if imp == "o":
        if position ==2:
         x_o.pop(1)
         x_o.insert(1, imp)
         result()
    if imp == "o":
        if position ==3:
         x_o.pop(2)
         x_o.insert(2, imp)
         result()        
    if imp == "o":
        if position ==4:
         x_o.pop(3)
         x_o.insert(3, imp)
         result()   
    if imp == "o":
        if position ==5:
         x_o.pop(4)
         x_o.insert(4, imp)
         result()
    if imp == "o":
        if position ==6:
         x_o.pop(5)
         x_o.insert(5, imp)
         result()

    if imp == "o":
        if position ==7:
         x_o.pop(6)
         x_o.insert(6, imp)
         result()
    if imp == "o":
        if position ==8:
         x_o.pop(7)
         x_o.insert(7, imp)
         result()       
    if imp == "o":
        if position ==9:
         x_o.pop(8)
         x_o.insert(8, imp)
         result()

    wins = winner_system()
    if wins is not None:
        print(f"game over 🏆{wins}🏆 winner‼️!🥳!‼️".upper())
        break






