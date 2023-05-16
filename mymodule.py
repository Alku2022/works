# from turtle import *



# turt=turtle.Turtle()

# #turt.bgcolor("black")
# turt.color("cyan")
# turt.shape("turtle")
# turt.pensize(10)
# turt.right(90)
# turt.fd(130)
# turt.bk(100)
# turt.fd(50)
# turt.left(90)
# turt.circle(40,180)
# turt.right(180)



# turt.pensize(10)
# turt.penup()
# turt.fd(110)
# turt.pendown()
# turt.right(110)
# turt.fd(125)
# turt.bk(65)
# turt.right(110)
# turt.fd(50)
# turt.right(140)


# turt.pensize(10)
# turt.penup()
# turt.fd(120)
# turt.right(90)
# turt.pendown()
# turt.fd(100)
# turt.bk(100)
# turt.left(90)
# turt.fd(40)
# turt.bk(80)



# turt.pensize(10)
# turt.penup()
# turt.fd(110)
# turt.pendown()
# turt.right(90)
# turt.fd(100)
# turt.bk(50)
# turt.left(90)
# turt.fd(50)
# turt.left(90)
# turt.fd(50)
# turt.bk(100)


# turt.pensize(10)
# turt.penup()
# turt.right(90)
# turt.fd(70)
# turt.pendown()
# turt.circle(50)




# turt.pensize(10)
# turt.penup()
# turt.fd(80)
# turt.left(90)
# turt.pendown()
# turt.fd(100)
# turt.right(140)
# turt.fd(120)
# turt.left(140)
# turt.fd(100)
# turtle.done()








import speech_recognition as sr
import pyttsx3
import turtle
 
# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     
     
# Loop infinitely for user to
# speak
 
while(1):   
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
 
            print("Did you say ",MyText)
            SpeakText(MyText)

            turtle.color("purple")
            style = ('Courier', 90, 'normal')
            turtle.write(MyText, font=style, align='center')
            turtle.hideturtle()
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")





