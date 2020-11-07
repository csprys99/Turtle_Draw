#Turtle Draw
#Authored By Chris Sprys   
#Intro to Computer Science
#Credits Eric Pogue, Dr. Ray Klump
#All Rights Reserved


import math
import turtle
print("")
print("")
print("Turle Draw")
print("Hello please input file name")
input(turtle.textinput)
print("")

TEXTFILENAME= 'turtle_drawtext.txt'


turtle.screensize(450, 450)
Stevetheturtle=turtle.Turtle()
Stevetheturtle.speed(0)
Stevetheturtle.pensize(5)
Stevetheturtle.penup()

turtleDrawTextFile=open(TEXTFILENAME, 'r')
line=turtleDrawTextFile.readline()
while line:
    print(line, end='')
    parts=line.split(' ')

    if(len(parts) == 3):
        color=parts[0]
        x= int(parts[1])
        y= int(parts[2])
    
    Stevetheturtle.color(color)
    Stevetheturtle.goto(x,y)
    Stevetheturtle.pendown()

    if (len(parts)==1):
        Stevetheturtle.penup()
    
    line=turtleDrawTextFile.readline()
p1=[36,29]
p2=[-49,128]
p3=[16,36]
p4=[54,71]
p5=[126,15]
p6=[180,177]
p7=[-57,-82]
p8=[-89,-50]
p9=[-155,61]
p10=[-78,-187]
p11=[72,161]
p12=[-160,-29]
p13=[-103,192]
p14=[-182,162]
p15=[-15,145]
p16=[13,97]
p17=[168,197]
p18=[48,1]
p19=[50,148]
p20=[102,-175]
p21=[133,-115]
p22=[52,-99]
p23=[130,136]
p24=[39,-191]
p25=[-58,-159]
p26=[53,139]
p27=[6,175]
p28=[-138,82]
p29=[87,33]
p30=[144,71]
p31=[-57,72]
p32=[-22,61]
p33=[58,164]
p34=[-45,26]
p35=[107,110]

distance1=math.sqrt((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)

distance2=math.sqrt((p3[0]-p4[0])**2)+ ((p3[1]-p4[1])**2)

distance3=math.sqrt((p5[0]-p6[0])**2)+ ((p5[1]-p6[1])**2)

distance4=math.sqrt((p7[0]-p8[0])**2)+ ((p7[1]-p8[1])**2)

distance5=math.sqrt((p9[0]-p10[0])**2)+ ((p9[1]-p10[1])**2)

distance6=math.sqrt((p11[0]-p12[0])**2)+ ((p11[1]-p12[1])**2)

distance7=math.sqrt((p13[0]-p14[0])**2)+ ((p13[1]-p14[1])**2)

distance8=math.sqrt((p15[0]-p16[0])**2)+ ((p15[1]-p16[1])**2)

distance9=math.sqrt((p17[0]-p18[0])**2)+ ((p17[1]-p18[1])**2)

distance10=math.sqrt((p19[0]-p20[0])**2)+ ((p19[1]-p20[1])**2)

distance11=math.sqrt((p21[0]-p22[0])**2)+ ((p21[1]-p22[1])**2)

distance12=math.sqrt((p21[0]-p22[0])**2)+ ((p21[1]-p22[1])**2)

distance13=math.sqrt((p21[0]-p22[0])**2)+ ((p21[1]-p22[1])**2)

distance14=math.sqrt((p22[0]-p23[0])**2)+ ((p22[1]-p23[1])**2)

distance15=math.sqrt((p24[0]-p25[0])**2)+ ((p24[1]-p25[1])**2)

distance16=math.sqrt((p26[0]-p27[0])**2)+ ((p26[1]-p27[1])**2)

distance17=math.sqrt((p28[0]-p29[0])**2)+ ((p28[1]-p29[1])**2)

distance18=math.sqrt((p30[0]-p31[0])**2)+ ((p30[1]-p31[1])**2)

distance19=math.sqrt((p32[0]-p33[0])**2)+ ((p32[1]-p33[1])**2)

distance20=math.sqrt((p34[0]-p35[0])**2)+ ((p34[1]-p35[1])**2)

totaldistance=(distance1+distance2+distance3+distance4+distance5+distance6+distance7+distance8+distance9+distance10
                +distance11+distance12+distance13+distance14+distance15+distance16+distance17+distance18+distance19+distance20)

turtle.write(totaldistance,align="center")

print("")
print("")
print(totaldistance)
print("End")

#Distance Formula
#A(x1,y1)
#B(x2,y2)
#Distance=sqrt((x1-x2)^2+(y1-y2)^2)

turtle.exitonclick()

# green 36 29
# green -49 128
# green -16 36
# stop
# blue 54 71
# black -126 15
# black 180 177
# black -57 -82
# stop
# black -89 -50
# green -155 61
# red -78 -187
# blue 72 161
# stop
# green -160 -29
# red -103 192
# red -182 162
# red -15 145
# stop
# red 13 -97
# stop
# black 168 -197
# green 48 1
# blue 50 148
# green 102 -175
# black 133 -115
# black 52 -99
# stop
# red 130 136
# blue 39 -191
# green -58 -159
# stop
# green 53 139
# green 6 175
# green -138 82
# stop
# blue 87 33
# stop
# green 144 71
# black -57 72
# stop
# black -22 61
# blue 58 164
# stop
# red -45 26
# blue 107 110



