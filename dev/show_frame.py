from guizero import App, Waffle, PushButton

def clicked(x,y):
    frame.set_pixel(x,y,"red")
    print("{}.{}".format(x,y))
    print(frame.get_all())
    frame.width = 5
    frame.height = 5
    frame.pixel_size = 50
    frame.dotty = True
    frame.pad = 25
    frame.color = "green"

app = App()
frame = Waffle(app, command = clicked, height = 15, width = 15)
frame.bg=(255,200,150)
frame.set_all("red")
frame.set_pixel(0,0,"blue")
frame.set_pixel(8,1,"#00ff00")
frame.set_pixel(3,4,"blue")
frame.pixel(1,2).dotty = True
print(frame[8,1].color)

button = PushButton(app, command= frame.reset)

app.display()
