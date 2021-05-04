import pandas
import turtle
screen = turtle.Screen()
screen.title("Items List")
image = "pic.gif"
screen.addshape(image)
turtle.shape(image)
correct = 0
import turtle
df = pandas.read_csv('items.csv')
items = df["item"].to_list()
while correct != 11:
    answer = screen.textinput(title=f"Guess the item {correct}/{11}", prompt="Enter the item name")
    ans = answer.lower()
    if ans == "exit":
        print("Items to Learn")
        print(items)
        new_data = pandas.DataFrame(items)
        new_data.to_csv("items to learn.csv")
        break
    for i in items:
        if ans == i.lower():
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            xCor = int(df[df.item == i]["x"]) 
            yCor = int(df[df.item == i]["y"]) 
            t.goto(xCor, yCor)
            t.write(i,font=("Calibri", 18, "bold"))
            items.remove(i)
            correct += 1
        else:
            continue
screen.exitonclick()