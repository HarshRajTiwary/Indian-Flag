import turtle as t
import pygame
import threading

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()
    # Keep the music playing until it ends
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Start the music in a separate thread
music_thread = threading.Thread(target=play_music)
music_thread.start()

# Your turtle code
t.setup(width=1000, height=700)
t.title("Jai Hind Everyone")
t.speed(2)
t.penup()
t.goto(0,100)
t.pendown()
t.color("orange")
t.begin_fill()
t.backward(450)
t.lt(90)
t.fd(200)
t.rt(90)
t.fd(900)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(450)
t.end_fill()
t.penup()
t.goto(0,-5)
t.pendown()
t.pencolor("blue")
t.pensize(5)
for i in range(24):
    for j in range(3):
        t.fd(100)
        t.lt(120)
    t.lt(15)
t.fd(95)
t.lt(90)
t.pensize(20)
t.circle(95)
t.penup()
t.goto(0,-110)
t.pendown()
t.pensize(1)
t.color("green")
t.begin_fill()
t.rt(90)
t.fd(450)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(900)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(450)
t.end_fill()
t.penup()
t.goto(0,-150)
t.mainloop()

# Wait for the music thread to finish when the turtle window is closed
music_thread.join()