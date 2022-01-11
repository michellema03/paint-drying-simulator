#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Title: Paint Drying Simulator
# Programmer: Michelle Ma
# Last modified: 17 June 2019
# Purpose: Final CS summative project!
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from tkinter import *
from math import *
from time import *
from random import *
import winsound

root = Tk()
s = Canvas(root, width=700, height=700, background="blanched almond")

# ~~~~~ INTRO SCREENS ~~~~~ #

def initialValues(): #set initial variables
    
    global allBugs, deadBugs, numBugs, paintQuality, paintDryness, frame, coins #values
    global fanEquipped, enoughMoney, paintEquipped, oopsMessageShowing, paintOn, fanOn #gameplay booleans
    global gameRunning, startPage, instPage, diffPage, endPage, statsPage #screen booleans
    global background, title1, title2, wall, wall1, wall2, wall3, wall4, wall5, wall6, wall7, fan1, fan2, fan3, paint1, paint2, paint3 #images
    global fanPic, bucketPic, brushBucket, paintPic, coinImage, dragonflyImage, spiderImage, flyingLadybug, landedLadybug, deadDragonfly, deadSpider, deadLadybug #images

    #wall pics
    title1 = PhotoImage(file = "title1.gif")
    title2 = PhotoImage(file = "title2.gif")
    wall1 = PhotoImage(file = "wall1.gif")
    wall2 = PhotoImage(file = "wall2.gif")
    wall3 = PhotoImage(file = "wall3.gif")
    wall4 = PhotoImage(file = "wall4.gif")
    wall5 = PhotoImage(file = "wall5.gif")
    wall6 = PhotoImage(file = "wall6.gif")
    wall7 = PhotoImage(file = "wall7.gif")

    #bug pics
    dragonflyImage = PhotoImage(file = "dragonfly.gif")
    spiderImage = PhotoImage(file = "spider.gif")
    flyingLadybug = PhotoImage(file = "flyingLadybug.gif") #extra little thing for flying/landed ladybugs :)
    landedLadybug = PhotoImage(file = "ladybug.gif")
    deadDragonfly = PhotoImage(file = "deadDragonfly.gif")
    deadSpider = PhotoImage(file = "deadSpider.gif")
    deadLadybug = PhotoImage(file = "deadLadybug.gif")
    allBugs = [dragonflyImage, spiderImage, flyingLadybug] #alive bug images
    deadBugs = [deadDragonfly, deadSpider, deadLadybug] #dead bug images

    #other pics
    background = PhotoImage(file = "background.gif")
    fan1 = PhotoImage(file = "fan1.gif")
    fan2 = PhotoImage(file = "fan2.gif")
    fan3 = PhotoImage(file = "fan3.gif")
    fanPic = fan1
    bucketPic = PhotoImage(file = "bucket.gif")
    brushBucket = PhotoImage(file = "brushbucket.gif")
    paint1 = PhotoImage(file = "paint1.gif")
    paint2 = PhotoImage(file = "paint2.gif")
    paint3 = PhotoImage(file = "paint3.gif")
    paintPic = paint1
    coinImage = PhotoImage(file = "coin.gif")

    #intro page booleans
    startPage = True
    instPage = False
    diffPage = False
    gameRunning = False

    #game parameters, values, and booleans
    frame = 0
    numBugs = 150
    paintQuality = 100
    paintDryness = 0
    fanEquipped = False
    paintEquipped = False
    paintOn = False
    fanOn = False
    enoughMoney = True
    oopsMessageShowing = False
    coins = 0

    #ending booleans
    statsPage = False
    endPage = False
    
    bugValues() #function for initial bug values
    introScreen() #brings user to intro screen

def bugValues(): #sets initial bug values
    global aliveBug, deadBug, bugPics, bugX, bugY, bugSpeedX, bugSpeedY, maxHits #bug values
    global flying, landed, killed #bug states
    global bugBar, bugHealth, bugHits, barColour, monetaryValue #bug health

    aliveBug = []
    deadBug = []
    bugX = []
    bugY = []
    bugSpeedX = []
    bugSpeedY = []
    bugPics = []
    maxHits = []

    flying = []
    landed = []
    killed = []
    
    bugBar = []
    bugHealth = []
    bugHits = []
    barColour = []
    monetaryValue = []

    for i in range(numBugs): #assigns values to every bug

        bugNum = randint(0, 2) #randomly determines the type of bug
        aliveBug.append(allBugs[bugNum]) #assigns alive image of that bug
        deadBug.append(deadBugs[bugNum]) #assigns dead image of that bug
        
        if aliveBug[i] == dragonflyImage: #if the bug is a dragonfly, assign dragonfly values
            maxHits.append(7)

            #gives the dragonfly a starting location + speed --> dragonflies can fly diagonally and are fastest
            if randint(0, 2) == 0:
                bugX.append(randint(200, 400))
                if randint(0, 2) == 0:
                    bugY.append(-40)
                    bugSpeedY.append(randint(2, 3))
                else:
                    bugY.append(740)
                    bugSpeedY.append(randint(-3, -2))
                bugSpeedX.append(randint(-3, 3))
            else:
                bugY.append(randint(200, 400))
                if randint(0, 2) == 0:
                    bugX.append(-40)
                    bugSpeedX.append(randint(2, 3))
                else:
                    bugX.append(740)
                    bugSpeedX.append(randint(-3, -2))
                bugSpeedY.append(randint(-3, 3))

        #if the bug is a spider or a ladybug, assign respective values --> these can only fly linear and are slower
        elif aliveBug[i] == spiderImage or aliveBug[i] == flyingLadybug:
            if aliveBug[i] == spiderImage:
                maxHits.append(5)
            elif aliveBug[i] == flyingLadybug:
                maxHits.append(3)
            if randint(0, 2) == 0:
                bugX.append(randint(20, 680))
                if randint(0, 2) == 0:
                    bugY.append(-40)
                    bugSpeedY.append(randint(1, 2))
                else:
                    bugY.append(740)
                    bugSpeedY.append(randint(-2, -1))
                bugSpeedX.append(0)

            else:
                bugY.append(randint(20, 680))
                if randint(0, 2) == 0:
                    bugX.append(-40)
                    bugSpeedX.append(randint(1, 2))
                else:
                    bugX.append(740)
                    bugSpeedX.append(randint(-2, -1))
                bugSpeedY.append(0)

        bugPics.append(0)
        bugHits.append(0)
        bugBar.append(0)
        bugHealth.append(0)
        barColour.append("green")
        landed.append(False)
        flying.append(False)
        killed.append(False)
        monetaryValue.append(True)

def introScreen(): #draws intro screen
    global start1, start2, start3, start4, start5, start6, start7
    start7 = s.create_image(350, 350, image = background, anchor = CENTER) #background image
    start1 = s.create_rectangle(85, 280, 260, 390, fill = "chartreuse3", outline = "green4")
    start2 = s.create_text(172, 335, text = "PLAY", anchor = CENTER, font = "Verdana 30", fill = "white") #PLAY button
    start3 = s.create_rectangle(440, 280, 615, 390, fill = "DodgerBlue2", outline = "DodgerBlue3")
    start4 = s.create_text(527, 335, text = "INSTRUCTIONS", anchor = CENTER, font = "Verdana 15", fill = "white") #INSTRUCTIONS button
    start5 = s.create_image(350, 120, anchor = CENTER, image = title1) #title 
    start6 = s.create_image(355, 210, anchor = CENTER, image = title2)
    root.bind("<Button-1>", introClicks)

def introClicks(event): #whenever mouse is clicked during INTRO SCREENS
    global startPage, instPage, diffPage, diffNum, gameRunning
    if gameRunning == False: #only happens when user is on intro screens
        
        if startPage == True: #if user is on the starting screen
            if 85 < event.x < 260 and 280 < event.y < 390: #if PLAY button is clicked
                s.delete(start1, start2, start3, start4, start5, start6, start7) #deletes starting screen graphics
                startPage = False #sets booleans to guide future clicks
                diffPage = True
                difficulty() #moves user to difficulty set page
            elif 440 < event.x < 615 and 280 < event.y < 390: #if the instructions button is clicked 
                s.delete(start1, start2, start3, start4, start5, start6, start7)
                startPage = False
                instPage = True
                instructions()
                
        elif instPage == True: #if user is on the instructions page 
            if 40 < event.x < 210 and 600 < event.y < 670: #if BACK button is clicked
                s.delete(ins1, ins2, ins3, ins4, ins5, ins6, ins7, ins8, ins9, ins10, ins11, ins12, ins13)
                startPage = True
                instPage = False
                introScreen()
            elif 380 < event.x < 650 and 600 < event.y < 670: #if PLAY button is clicked
                s.delete(ins1, ins2, ins3, ins4, ins5, ins6, ins7, ins8, ins9, ins10, ins11, ins12, ins13)
                instPage = False
                diffPage = True
                difficulty()
                
        elif diffPage == True: #if user is on the difficulty set page
            if 100 < event.x < 600:
                if 150 < event.y < 250: #if EASY button is clicked
                    diffNum = 17000 #sets the frequency bugs appear on the screen
                    winsound.PlaySound("summer.wav", winsound.SND_ASYNC) #plays background music
                elif 300 < event.y < 400: #MEDIUM button
                    diffNum = 13000
                    winsound.PlaySound("entertainer.wav", winsound.SND_ASYNC) #plays background music
                elif 450 < event.y < 550: #HARD button
                    diffNum = 9000
                    winsound.PlaySound("bumblebee.wav", winsound.SND_ASYNC) #plays background music

                if 150 < event.y < 250 or 300 < event.y < 400 or 450 < event.y < 550: #in all three cases
                    s.delete(diff1, diff2, diff3, diff4, diff5, diff6, diff7, difftext)
                    gameRunning = True 
                    diffPage = False
                    gamePlay() #triggers gameplay
                
def instructions(): #instructions page
    global ins1, ins2, ins3, ins4, ins5, ins6, ins7, ins8, ins9, ins10, ins11, ins12, ins13
    #all just graphics
    ins1 = s.create_rectangle(0, 0, 700, 700, fill = "pale turquoise")
    ins2 = s.create_text(30, 250, text = "CLICK on the bugs to kill them.\nCLICK on the fan to equip it - press SPACE to turn it " +
                         "on.\nCLICK on the paint bucket to equip it - press SPACE to repaint.", anchor = NW, font = "Verdana 13")
    ins3 = s.create_rectangle(40, 600, 210, 670, fill = "gold", outline = "goldenrod")
    ins6 = s.create_text(125, 635, text = "BACK", font = "Verdana 20")
    ins4 = s.create_text(30, 30, text = "Congratulations! The Queen has hired you to repaint the walls of\nBuckingham " +
                         "Palace.\nSeems like a simple job, right? Think again.\n\nThe instant you finish painting, " +
                         "a swarm of bugs suddenly appear!\nIf they land on the wet paint, the paint quality will go down, and the \nQueen will be exorbitantly"
                         + " disappointed.\n\nDestroy them before they destroy your career!",
                         anchor = NW, font = "Verdana 13")
    ins5 = s.create_rectangle(380, 600, 650, 670, fill = "chartreuse3", outline = "green4")
    ins7 = s.create_text(505, 635, text = "PLAY", font = "Verdana 20")
    ins8 = s.create_image(150, 360, anchor = CENTER, image = landedLadybug)
    ins9 = s.create_image(150, 450, anchor = CENTER, image = spiderImage)
    ins10 = s.create_image(150, 545, anchor = CENTER, image = dragonflyImage)
    ins11 = s.create_text(180, 360, anchor = W, text = " = 3 clicks to kill, drops 5 gold", font = "Verdana 15")
    ins12 = s.create_text(180, 450, anchor = W, text = " = 5 clicks to kill, drops 10 gold", font = "Verdana 15")
    ins13 = s.create_text(180, 540, anchor = W, text = " = 7 clicks to kill, drops 15 gold", font = "Verdana 15")
    
def difficulty(): #difficulty setting page
    global diff1, diff2, diff3, diff4, diff5, diff6, diff7, difftext
    #more graphics
    diff7 = s.create_rectangle(0, 0, 700, 700, fill = "pale turquoise")
    difftext = s.create_text(350, 90, text = "Please select your difficulty.", anchor = CENTER, font = "Verdana 20")
    diff1 = s.create_rectangle(100, 150, 600, 250, fill = "chartreuse3", outline = "green4")
    diff2 = s.create_rectangle(100, 300, 600, 400, fill = "gold", outline = "goldenrod")
    diff3 = s.create_rectangle(100, 450, 600, 550, fill = "firebrick2", outline = "firebrick3")
    diff4 = s.create_text(350, 200, text = "EASY", anchor = CENTER, font = "Verdana 25")
    diff5 = s.create_text(350, 350, text = "NORMAL", anchor = CENTER, font = "Verdana 25")
    diff6 = s.create_text(350, 500, text = "HARD", anchor = CENTER, font = "Verdana 25")


#~~~~~GAMEPLAY~~~~~#
    
def mouseMotionDetector(event): #gets coordinates whenever mouse is moved
    global mouseX, mouseY
    mouseX = event.x
    mouseY = event.y
 
def gameplayClicks(event): #whenever mouse is clicked
    global mouseX, mouseY, fanEquipped, paintEquipped
    if gameRunning == True: #runs only during gameplay
        #function for killing bugs
        if fanEquipped == False and paintEquipped == False: #ensures user can't kill bugs while equipped with fan or paint
            for i in range(numBugs):
                if killed[i] == False: #for every bug as long as it hasn't been killed yet
                    if getDistance(bugX[i], bugY[i], mouseX, mouseY) <= 20:
                        bugHits[i] += 1 #if the user clicks on it, the bug hits of that specific bug increases by one

        #function for equipping/unequipping fan
        if getDistance(620, 590, mouseX, mouseY) <= 70 and paintEquipped == False: #can't equip fan if paint is already equipped
            if fanEquipped == True: 
                fanEquipped = False #unequips fan if equipped
            else:
                fanEquipped = True #otherwise, equips fan

        #function for equipping/unequipping paint
        if getDistance(100, 580, mouseX, mouseY) <= 60 and fanEquipped == False: #can't equip paint if fan is already equipped
            if paintEquipped == True:
                paintEquipped = False #unequips paint if equipped
            else:
                paintEquipped = True #otherwise, equips paint

def keyPressDetector(event): #whenever a key is pressed
    global coins, paintDryness, paintQuality, frame, fanPic, paintPic, enoughMoney, fanOn, paintOn #, paintPic
    frame += 1 #increase frame number (for fan animation)
    if event.keysym == "space" and gameRunning == True: #if spacebar is pressed during gameplay

        #turns FAN on/off
        if fanEquipped == True:
            fanOn = True
            if coins <= 0: #if user doesn't have enough money
                enoughMoney = False
                coins = 0 #resets in case values skip past zero
            else: #if user has enough money
                enoughMoney = True
                coins -= 1.3 #subtracts coins
                paintDryness += 0.3 #increases paint dryness
                if frame%6 <= 0: #animates spinning fan
                    fanPic = fan1
                elif frame%6 <= 2:
                    fanPic = fan2
                elif frame%6 <= 4:
                    fanPic = fan3

        #turns REPAINTING on/off
        elif paintEquipped == True:
            paintOn = True
            if coins <= 0: #if user doesn't have enough money (similar to above)
                enoughMoney = False
                coins = 0
            else:
                enoughMoney = True
                coins -= 3.5 #repainting costs more than the fan
                paintQuality += 0.3

                if frame%6 <= 0: #animates repainting
                    paintPic = paint1
                elif frame%6 <= 2:
                    paintPic = paint2
                elif frame%6 <= 4:
                    paintPic = paint3
                
def keyReleased(event): #whenever a key is released
    global fanOn, paintOn, paintPic
    if event.keysym == "space" and gameRunning == True: #if the spacebar is released during gameplay
        if fanEquipped == True:
            fanOn = False #turns off the fan
        elif paintOn == True: 
            paintOn = False #turns off the repainting
            paintPic = paint1
            
def getDistance(x1, y1, x2, y2): #gets distance between two points
    return sqrt((x2 - x1)**2 + (y2-y1)**2)

def oopsMessage(): #displays "oops!" message if user tries to run fan or repaint without enough money
    global oops, oopsMessageShowing
    if enoughMoney == False and (paintOn == True or fanOn == True): #if message isn't already shown
        oopsMessageShowing = True
        oops = s.create_text(60, 60, text = "Oops! You don't have enough money.", anchor = NW, font = "Verdana 15", fill = "white")
    elif fanOn == False and paintOn == False: #if user stops trying to run fan or repaint
        oopsMessageShowing = False
        oops = s.create_rectangle(-1,-1, 0, 0, fill = "white") #so that oops message doesn't show
    else:
        oops = s.create_rectangle(-1, -1, 0, 0, fill = "white")

def drawFan(): #draws fan
    global fan
    if fanEquipped == False: #draws fan in its corner location when not equipped
        fan = s.create_image(620, 590, anchor=CENTER, image=fanPic)
    else: #if equipped, fan tracks user's mouse
        fan = s.create_image(mouseX, mouseY, anchor = CENTER, image = fanPic)

def drawPaint(): #draws paint bucket/paintbrush
    global paint, bucket
    if paintEquipped == False: #if paint isn't equipped
        bucket = s.create_image(100, 580, anchor = CENTER, image = brushBucket) #shows image with brush in bucket
        paint = s.create_rectangle(-1, -1, 0, 0, fill = "white") #no paintbrush
    else: #if paint is equipped
        bucket = s.create_image(100, 580, anchor = CENTER, image = bucketPic) #shows image without brush in bucket
        paint = s.create_image(mouseX, mouseY, anchor = CENTER, image = paintPic) #paintbrush tracks user's mouse

def checkIfFlying(): #makes bugs fly onto the screen
    global flying
    for i in range(numBugs): 
        if flying[i] == False: #for every non-flying bug
            if randint(0, diffNum) < 1: #frequency/probability depends on the difficulty --> the harder the level, the more frequent
                flying[i] = True

def checkIfLanded(): #makes bugs land on the screen
    global landed, flying
    for i in range(numBugs):
        if flying[i] == True: #prevents "landing" when bugs haven't flown yet which results in still bugs off the screen
            if landed[i] == False:
                if randint(0, 450) <= 2 and 100 <= bugX[i] <= 600 and 0 <= bugY[i] <= 600: #set frequency for how often/when bug lands
                    #(also, prevents bugs from landing behind bucket/fan)
                    landed[i] = True
                    flying[i] = False

def checkIfKilled(): #checks if bugs are killed
    global landed, flying, killed
    for i in range(numBugs):
        if bugHits[i] >= maxHits[i]: #if the number of hits exceeds its max hits
            killed[i] = True
            landed[i] = False
            flying[i] = False

def updateBugs(): #updates bug values
    global bugX, bugY, bugSpeedX, bugSpeedY, flying, landed, killed, paintQuality
    checkIfFlying()
    checkIfLanded()
    checkIfKilled()
    
    for i in range(numBugs):
        if flying[i] == True: #if bug is flying
            bugX[i] += bugSpeedX[i]
            bugY[i] += bugSpeedY[i]
 
        elif landed[i] == True: #if bug is landed
                bugSpeedX[i] = 0
                bugSpeedY[i] = 0
                if 10 < bugX[i] < 690 and 10 < bugY[i] < 690: #if the bug lands visibly on the screen
                    paintQuality -= 0.01 #lowers paint quality
                bugX[i] += bugSpeedX[i]
                bugY[i] += bugSpeedY[i]
            
        elif killed[i] == True: #if bug is killed
            bugSpeedX[i] = 0
            bugSpeedY[i] = 4 #bug starts to fall down
            bugX[i] += bugSpeedX[i]
            bugY[i] += bugSpeedY[i]

def drawBugs(): #draws bugs
    global bugPics, bugBar, bugHealth, barColour
    for i in range(numBugs):
        if aliveBug[i] == flyingLadybug and landed[i] == True: #changes image of ladybugs when they land
            bugPics[i] = s.create_image(bugX[i], bugY[i], anchor=CENTER, image = landedLadybug) 
        else:
            if killed[i] == False:
                bugPics[i] = s.create_image(bugX[i], bugY[i], anchor=CENTER, image = aliveBug[i]) #draws alive bugs if not killed
            else:
                bugPics[i] = s.create_image(bugX[i], bugY[i], anchor=CENTER, image = deadBug[i]) #draws bug as dead if killed
        barLength = 5*maxHits[i] #calculates length of health bar
        bugBar[i] = s.create_rectangle(bugX[i] - barLength/2, bugY[i] - 15, bugX[i] +(barLength/2), bugY[i] - 11, fill = barColour[i]) #draws health bar
        bugHealth[i] = s.create_rectangle((bugX[i] + barLength/2) - (bugHits[i]*int(barLength/maxHits[i])),
                                          bugY[i] - 15, bugX[i] + barLength/2, bugY[i] - 11, fill = "red") #draws decreasing health/hit bar
            
def updateCoins(): #updates amount of gold coins user has
    global coins, monetaryValue, numCoins, coinMessage
    for i in range(numBugs):
        if monetaryValue[i] == True and killed[i] == True: #if bug is killed and still has money
            if maxHits[i] == 3: #ladybugs give 5 coins
                coins += 5 
            elif maxHits[i] == 5: #spiders give 10 coins
                coins += 10
            elif maxHits[i] == 7: #dragonflies five 15 coincs
                coins += 15
            monetaryValue[i] = False #bugs lose their monetary value after money is collected
    numCoins = "= " + "$" + str(int(coins*100) /100) #rounds to nearest cent
    coinMessage = s.create_text(500, 140, text = numCoins, anchor = W, font = "Verdana 15", fill = "white") #displays coins

def checkWallQuality(): #changes background depending on paint quality
    global wall
    if paintQuality >= 90: #background slowly changes as wall quality decreases
        wall = wall1
    elif paintQuality >= 80:
        wall = wall2
    elif paintQuality >= 70:
        wall = wall3
    elif paintQuality >= 60:
        wall = wall4
    elif paintQuality >= 50:
        wall = wall5
    elif paintQuality >= 30:
        wall = wall6
    elif paintQuality >= 10:
        wall = wall7
        
def drawBackground(): #draws gameplay background
    global paintDryness, qualityBar, drynessBar, background, quality, dryness, coin, qualityText, drynessText
    paintDryness += 0.005 #increases paint dryness every frame
    checkWallQuality()
    background = s.create_image(350, 350, anchor = CENTER, image = wall) #draws wall
    quality = s.create_line(470, 50, 670, 50, width = 20, fill = "green") #paint quality bar
    dryness = s.create_line(470, 100, 670, 100, width = 20, fill = "red") #paint dryness bar
    qualityText = s.create_text(470, 30, text = "PAINT QUALITY", anchor = W, fill = "white") #labels
    drynessText = s.create_text(470, 80, text = "PAINT DRYNESS", anchor = W, fill = "white")
    coin = s.create_image(480, 140, anchor=CENTER, image=coinImage) #coin icon
    if paintQuality >= 100: #prevents paint quality from exeeding 100 percent
        qualityBar = s.create_line(470, 50, 670, 50, width = 20, fill = "green")
    else:
        qualityBar = s.create_line(670 - ( (100-paintQuality)*(200/100)), 50, 670, 50, width = 20, fill = "red") #draws quality decreasing
    drynessBar = s.create_line(470, 100, 470 + (paintDryness*(200/100)), 100, width = 20, fill = "green") #draws dryness increasing

def checkEnd(): #check for game end
    global paintQuality, paintDryness, gameRunning, end, endPage, time2, endText, endRole
    
    #if paint quality reaches zero
    if paintQuality <= 0:
        endText = "Your wall is utterly destroyed." #sets ending messages
        endRole = "Pitiful Painter :("
        gameRunning = False
        endPage = True
        paintQuality = 0
        winsound.PlaySound("end.wav", winsound.SND_ASYNC) #plays ending jingle
        time2 = time() #sets ending time

    #if paint fully dries
    elif paintDryness >= 100:
        if paintQuality <= 50: #if paint quality is below 50
            endText = "She shakes her head and gives you a sympathetic smile."
            endRole = "Meh-Painter."
        elif paintQuality <= 75: #if paint quality is 51-75
            endText = "She nods and gives you an encouraging smile."
            endRole = "Painting Connesiour."
        elif paintQuality < 100: #if paint quality is above 76
            endText = "She jumps up and down with delight and gives you a high five."
            endRole = "Painting Ultimate Master!"
        gameRunning = False
        endPage = True
        winsound.PlaySound("end.wav", winsound.SND_ASYNC)  #ending jingle
        time2 = time() #ending time
        
def delete(): #deletes objects
    for i in range(numBugs):
        s.delete(bugPics[i], bugBar[i], bugHealth[i]) #bugs
    s.delete(qualityBar, drynessBar, fan, coinMessage, paint, bucket, background, quality, dryness, coin, oops, qualityText, drynessText) #everything else


#~~~~~ENDING SCREENS~~~~~#
    
def endScreen(): #draws endscreen
    s.create_rectangle(0, 0, 700, 700, fill = "pale turquoise") #background
    finalText = "Exhausted, you present your work to the Queen.\n\n" + endText + "\n\nYou have earned the role of:\n\n" + endRole
    s.create_text(320, 120, text = finalText, anchor = CENTER, font = "Verdana 15") #displays ending message
    s.create_rectangle(100, 250, 600, 350, fill = "dark orchid", outline = "blue violet") #SCORING/STATS button
    s.create_text(350, 300, text = "SCORING", anchor = CENTER, font = "Verdana 20", fill = "white")
    s.create_rectangle(100, 400, 600, 500, fill = "chartreuse3", outline = "green4") #REPLAY button
    s.create_text(350, 450, text = "REPLAY", anchor = CENTER, font = "Verdana 20", fill = "white")
    s.create_rectangle(100, 550, 600, 650, fill = "firebrick2", outline = "firebrick3") #QUIT button
    s.create_text(350, 600, text = "QUIT", font = "Verdana 20", fill = "white")
    s.bind( "<Button-1>", endingClicks)

def endingClicks(event): #if user clicks during ending screens
    global statsPage, endPage

    #if user is on the ending page
    if endPage == True:
        if 100 < event.x < 600:
            if 250 <= event.y <= 350: #if user clicks on SCORING button
                statsPage = True
                endPage = False
                stats()
            elif 400 <= event.y <= 500: #if user clicks on REPLAY button
                s.delete("all")
                initialValues()
            elif 550 <= event.y <= 650: #if user clicks on QUIT button
                quitGame()

    #if user is on the stats page
    elif statsPage == True:
        if 150 < event.x < 550 and 350 < event.y < 450: #if user clicks on BACK button
            endPage = True
            statsPage = False
            endScreen()
        elif 150 < event.x < 550 and 500 < event.y < 600: #if user clicks on QUIT button
            quitGame()

def stats(): #draws scoring screen
    s.delete("all")
    s.create_rectangle(0, 0, 700, 700, fill = "pale turquoise")
    totalDrags = 0
    totalSpids = 0
    totalLadys = 0
    for i in range(numBugs):
        if killed[i] == True: 
            if aliveBug[i] == dragonflyImage: #counts total killed dragonflies
                totalDrags += 1
            elif aliveBug[i] == spiderImage: #counts total killed spiders
                totalSpids += 1
            elif aliveBug[i] == flyingLadybug: #counts total killed ladybugs
                totalLadys += 1
                
    gameTime = float(int((time2-time1)*100)/100) #calculates and rounds gameplay time
    statText1 = "Total ladybugs killed: " + str(totalLadys) + "\n\nTotal spiders killed: " + str(totalSpids) + "\n\nTotal dragonflies killed: " + str(totalDrags)
    statText2 = "\n\nTime taken: " + str(gameTime) + " seconds" + "\n\nFinal paint quality: " + str(int(paintQuality*100)/100) #final scoring message
    statText = statText1 + statText2
    s.create_text(50, 40, anchor = NW, font = "Verdana 15", text = statText) #displays stats
    s.create_rectangle(150, 350, 550, 450, fill = "gold", outline = "goldenrod") #draws BACK button
    s.create_text(350, 400, text = "BACK", font = "Verdana 25")
    s.create_rectangle(150, 500, 550, 600, fill = "firebrick2", outline = "firebrick3") #draws QUIT button
    s.create_text(350, 550, text = "QUIT", anchor = CENTER, font = "Verdana 25")

def quitGame(): #quits game/program completely by closing the window
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS) #plays exit jingle
    root.destroy() #closes the window

def gamePlay(): #actual game function
    global time1
    time1 = time() #sets initial starting time
    while gameRunning == True: #gameplay loop
        drawBackground()
        updateBugs()
        updateCoins()
        drawBugs()
        drawFan()
        drawPaint()
        checkEnd()
        oopsMessage()
        s.update()
        sleep(0.01)
        delete()
    endScreen()

s.bind("<Button-1>", gameplayClicks) #binds mouse clicks to gameplayClicks function
s.bind("<Key>", keyPressDetector) #binds key presses to keyPressDetector function
s.bind("<Motion>", mouseMotionDetector) #calls mouseMotionDetector every time the mouse is moved
s.bind("<KeyRelease>", keyReleased) #calls keyReleased every time a key is released

root.after(0, initialValues) #calls the starting procedure immediately after the window is created

s.pack() #creates screen, sets event listener
s.focus_set()
root.mainloop() #starts program
