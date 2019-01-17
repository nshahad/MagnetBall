from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Rectangle
import random

from kivy.config import Config
Config.set('graphics','resizable',0)
Window.clearcolor = (1,1,1,0)


def within(mousex, mousey, startx, starty, width, height):
    if mousex >= startx and mousex <= startx + width:
        if mousey >= starty and mousey <= starty + height:
            return True
    else: 
        return False

## Create Seperate Widgets if Object Sizes are Different
#####################  ALL WIDGETS: ########################################
class Main_Screen(Widget):
    def __init__(self, imageStr, **kwargs):
        super(Main_Screen, self).__init__(**kwargs)
        with self.canvas:
            ## Edit Size Here
            self.size = (Window.width, Window.height)
            self.rect_bg=Rectangle(source=imageStr,pos=self.pos,size=self.size)
            self.bind(pos=self.update_graphics_pos)
            self.x = self.center_x
            self.y = self.center_y
            self.pos = (self.x,self.y)
            self.rect_bg.pos = self.pos
    def update_graphics_pos(self, instance, value):
        self.rect_bg.pos = value
    def setSize(self,width,height):
        self.size = (width,height)
    def setPos(posx,posy):
        self.x = posx
        self.y = posy
class MainScreen(Main_Screen):
    def move(self):
        self.x = self.x
        self.y = self.y
    def update(self):
        self.move()
        
class Play_Button(Widget):
    def __init__(self, imageStr, **kwargs):
        super(Play_Button, self).__init__(**kwargs)
        with self.canvas:
            ## Edit Size Here
            self.size = (Window.width * 0.383, Window.height * 0.147)
            self.rect_bg=Rectangle(source=imageStr,pos=self.pos,size=self.size)
            self.bind(pos=self.update_graphics_pos)
            self.x = self.center_x
            self.y = self.center_y
            self.pos = (self.x,self.y)
            self.rect_bg.pos = self.pos
    def update_graphics_pos(self, instance, value):
        self.rect_bg.pos = value
    def setSize(self,width,height):
        self.size = (width,height)
    def setPos(posx,posy):
        self.x = posx
        self.y = posy
class PlayButton(Play_Button):
    def move(self):
        self.x = self.x
        self.y = self.y
    def update(self):
        self.move()

class Restart1(Widget):
    def __init__(self, imageStr, **kwargs):
        super(Restart1, self).__init__(**kwargs)
        with self.canvas:
            ## Edit Size Here
            self.size = (Window.width * 0.383, Window.height * 0.147)
            self.rect_bg=Rectangle(source=imageStr,pos=self.pos,size=self.size)
            self.bind(pos=self.update_graphics_pos)
            self.x = self.center_x
            self.y = self.center_y
            self.pos = (self.x,self.y)
            self.rect_bg.pos = self.pos
    def update_graphics_pos(self, instance, value):
        self.rect_bg.pos = value
    def setSize(self,width,height):
        self.size = (width,height)
    def setPos(posx,posy):
        self.x = posx
        self.y = posy
class Restart(Restart1):
    def move(self):
        self.x = self.x
        self.y = self.y
    def update(self):
        self.move()
        
class Hole_1 (Widget):
    def __init__ (self, imageStr, **kwargs):
        super (Hole_1, self).__init__(**kwargs)
        with self.canvas:
            ## Edit Size Here
            self.size = (Window.width * 0.07, Window.height * 0.07)
            self.rect_bg=Rectangle(source=imageStr,pos=self.pos,size=self.size)
            self.bind(pos=self.update_graphics_pos)
            self.x = self.center_x
            self.y = self.center_y
            self.pos = (self.x,self.y)
            self.rect_bg.pos = self.pos
    def update_graphics_pos(self, instance, value):
        self.rect_bg.pos = value
    def setSize(self,width,height):
        self.size = (width,height)
    def setPos(posx,posy):
        self.x = posx
        self.y = posy
class Hole(Hole_1):
    def move(self):
        self.x = self.x
        self.y = self.y
    def update(self):
        self.move()

class Again (Widget):
    def __init__ (self, imageStr, **kwargs):
        super (Again, self).__init__(**kwargs)
        with self.canvas:
            ## Edit Size Here
            self.size = (Window.width * 0.1, Window.height * 0.1)
            self.rect_bg=Rectangle(source=imageStr,pos=self.pos,size=self.size)
            self.bind(pos=self.update_graphics_pos)
            self.x = self.center_x
            self.y = self.center_y
            self.pos = (self.x,self.y)
            self.rect_bg.pos = self.pos
    def update_graphics_pos(self, instance, value):
        self.rect_bg.pos = value
    def setSize(self,width,height):
        self.size = (width,height)
    def setPos(posx,posy):
        self.x = posx
        self.y = posy
class restart(Again):
    def move(self):
        self.x = self.x
        self.y = self.y
    def update(self):
        self.move()

class Continue (Widget):
    def __init__ (self, imageStr, **kwargs):
        super (Continue, self).__init__(**kwargs)
        with self.canvas:
            ## Edit Size Here
            self.size = (Window.width * 0.1, Window.height * 0.1)
            self.rect_bg=Rectangle(source=imageStr,pos=self.pos,size=self.size)
            self.bind(pos=self.update_graphics_pos)
            self.x = self.center_x
            self.y = self.center_y
            self.pos = (self.x,self.y)
            self.rect_bg.pos = self.pos
    def update_graphics_pos(self, instance, value):
        self.rect_bg.pos = value
    def setSize(self,width,height):
        self.size = (width,height)
    def setPos(posx,posy):
        self.x = posx
        self.y = posy
class continue1(Continue):
    def move(self):
        self.x = self.x
        self.y = self.y
    def update(self):
        self.move()

class GameOver (Widget):
    def __init__ (self, imageStr, **kwargs):
        super (GameOver, self).__init__(**kwargs)
        with self.canvas:
            ## Edit Size Here
            self.size = (Window.width * 0.5, Window.height * 0.5)
            self.rect_bg=Rectangle(source=imageStr,pos=self.pos,size=self.size)
            self.bind(pos=self.update_graphics_pos)
            self.x = self.center_x
            self.y = self.center_y
            self.pos = (self.x,self.y)
            self.rect_bg.pos = self.pos
    def update_graphics_pos(self, instance, value):
        self.rect_bg.pos = value
    def setSize(self,width,height):
        self.size = (width,height)
    def setPos(posx,posy):
        self.x = posx
        self.y = posy
class Over(GameOver):
    def move(self):
        self.x = self.x
        self.y = self.y
    def update(self):
        self.move()
        
class Platform_1(Widget):
    def __init__(self, imageStr, **kwargs):
        super(Platform_1, self).__init__(**kwargs)
        with self.canvas:
            ## Edit Size Here
            self.size = (Window.width*1.2, Window.height *0.1)
            self.rect_bg=Rectangle(source=imageStr,pos=self.pos,size=self.size)
            self.bind(pos=self.update_graphics_pos)
            self.x = self.center_x
            self.y = self.center_y
            self.pos = (self.x,self.y)
            self.rect_bg.pos = self.pos
    def update_graphics_pos(self, instance, value):
        self.rect_bg.pos = value
    def setSize(self,width,height):
        self.size = (width,height)
    def setPos(posx,posy):
        self.x = posx
        self.y = posy
class Platform1(Platform_1):
    def move(self):
        self.x = self.x
        self.y = self.y
    def update(self):
        self.move()

class Game_Ball(Widget):
    def __init__(self, imageStr, **kwargs):
        super(Game_Ball, self).__init__(**kwargs)
        with self.canvas:
            ## Edit Size Here
            self.size = (Window.width*0.06, (Window.height / Window.width)* 0.8 * 0.08 * Window.height)
            self.rect_bg=Rectangle(source=imageStr,pos=self.pos,size=self.size)
            self.bind(pos=self.update_graphics_pos)
            self.x = self.center_x
            self.y = self.center_y
            self.pos = (self.x,self.y)
            self.rect_bg.pos = self.pos
    def update_graphics_pos(self, instance, value):
        self.rect_bg.pos = value
    def setSize(self,width,height):
        self.size = (width,height)
    def setPos(posx,posy):
        self.x = posx
        self.y = posy
        
class Ball(Game_Ball):
    def move(self):
        self.x = self.x
        self.y = self.y
    def update(self):
        self.move()
        

        
scoretotal= 0
score=0

################################################################################
        ################### MAIN APP LOOP: #############################

class MainGUI(Widget):
    ## Constant Variables Ex: Screen Selector Arrays
    screens = ['main_screen']
    #delaytimer = 0

    ball_dir1 = ['r']
    ball_dir2 = ['r']
    
    openplatform = False
    opentimer = 0

    InitialYspeed = 2
    InitialXspeed = 3
    Yspeed = InitialYspeed
    Xspeed = InitialXspeed

    score = 0
    counter= 1
    


    #######
    def __init__(self, **kwargs):
        super(MainGUI, self).__init__(**kwargs)

        ## Load all Images
        ## main_screen:
        self.mainscreen = MainScreen(imageStr = 'main_screen.png')
        self.mainscreen.x = 0
        self.mainscreen.y = 0
        self.add_widget(self.mainscreen)

        self.play = PlayButton(imageStr = 'play.png')
        self.play.x = 0.3085 * Window.width
        self.play.y = 0.15 * Window.height
        self.add_widget(self.play)

        

        self.settings = Ball(imageStr = 'settings.png')
        self.settings.x = 0.9 * Window.width
        self.settings.y = 0.9 * Window.height
        self.add_widget(self.settings)

        ## Levels:
        self.background = MainScreen(imageStr = 'background.png')
        self.background.x = 2*Window.width
        self.background.y = 2*Window.height
        self.add_widget(self.background)
        
        self.platform1 = Platform1(imageStr = 'platform.png')
        self.platform1.x = 2*Window.width
        self.platform1.y = 2*Window.height
        self.add_widget(self.platform1)

        self.ball1 = Ball(imageStr = 'ball.png')
        self.ball1.x = 3*Window.width
        self.ball1.y = 3*Window.height
        self.add_widget(self.ball1)

##        self.gameball2 = Ball(imageStr = 'object1.png')
##        self.gameball2.x = 3*Window.width
##        self.gameball2.y = 3*Window.height
##        self.add_widget(self.gameball2)
        
        self.hole1 = Hole (imageStr = 'hole.png')
        self.hole1.x = Window.width
        self.hole1.y = Window.height
        self.add_widget (self.hole1)

        self.GameOver = Over (imageStr = 'Game_Over.png')
        self.GameOver.x = Window.width
        self.GameOver.y = Window.height
        self.add_widget (self.GameOver)

        self.Again = restart (imageStr = 'restart.png')
        self.Again.x = Window.width 
        self.Again.y = Window.height
        self.add_widget (self.Again)

        self.Continue = restart (imageStr = 'continue.png')
        self.Continue.x = Window.width 
        self.Continue.y = Window.height
        self.add_widget (self.Continue)

    def on_touch_move(self, touch):
        pass
    def on_touch_down(self, touch):
        currentscreen = self.screens[0]

        if currentscreen == 'main_screen':
            if within(touch.x, touch.y, self.play.x, self.play.y,
                       self.play.size[0], self.play.size[1]):
                self.mainscreen.x = 2*Window.width
                self.mainscreen.y = 2*Window.height
                self.play.x = 2*Window.width
                self.play.y = 2*Window.height

                self.settings.x = 2 * Window.width
                self.settings.y = 2 * Window.height

                self.background.x = 0
                self.background.y = 0
                
                self.platform1.x = -0.090 * Window.width
                self.platform1.y = 0
                
                self.ball1.x = Window.width * round(random.uniform(0,1),2)
                self.ball1.y = Window.height

                self.screens.insert(0, 'levels')

        else:
            if within(touch.x, touch.y, self.platform1.x, self.platform1.y,
                      self.platform1.size[0], self.platform1.size[1]):
               
                if self.openplatform == False:
                    self.hole1.x = touch.x - Window.width*0.0315
                    self.hole1.y = 0.014 *Window.height
                    self.openplatform = True
                    self.opentimer = 60

##                print (self.ball1.x)
##                print (self.ball1.y)
##                print (self.hole1.x)
##                print (self.ball1.x - self.hole1.x)
##                print ((touch.x+31.5) - (self.ball1.x + 20.65))


    ##            if  self.ball1.x - self.hole1.x > 0 and (touch.x+31.5) - (self.ball1.x + 20.65) >0:
    ##                self.openplatform = True
    ##                self.opentimer = 30

            if within(touch.x, touch.y, self.Again.x, self.Again.y,
                      self.Again.size[0], self.Again.size[1]):

                self.counter += 1
                self.Again.x= 2* Window.width
                self.Again.y= 2* Window.height

                self.GameOver.x= 2* Window.width
                self.GameOver.y= 2* Window.width
                
                self.background.x = 0
                self.background.y = 0
                    
                self.platform1.x = -0.090 * Window.width
                self.platform1.y = 0
                    
                self.ball1.x = Window.width * round(random.uniform(0,1),2)
                self.ball1.y = Window.height

                self.screens.insert(0, 'levels')

                self.Yspeed = self.InitialYspeed
                self.Xspeed = self.InitialXspeed

                self.hole1.x = 2*Window.width
                self.hole1.y = 2*Window.height

            if within(touch.x, touch.y, self.Continue.x, self.Continue.y,
                      self.Continue.size[0], self.Continue.size[1]): 
                self.counter += 1
                self.Again.x= 2* Window.width
                self.Again.y= 2* Window.height

                self.GameOver.x= 2* Window.width
                self.GameOver.y= 2* Window.width

                self.Continue.x= 2* Window.width
                self.Continue.y= 2* Window.height
                
                self.background.x = 0
                self.background.y = 0
                    
                self.platform1.x = -0.090 * Window.width
                self.platform1.y = 0
                    
                self.ball1.x = Window.width * round(random.uniform(0,1),2)
                self.ball1.y = Window.height

                self.screens.insert(0, 'levels')

                self.hole1.x = 2*Window.width
                self.hole1.y = 2*Window.height
            

      
         
    
    def update(self,dt):
        currentscreen = self.screens[0]

        ##Open Platform Sequence:
        self.opentimer -= 1
        if self.openplatform and self.opentimer < 0:
            self.openplatform = False

        print (self.openplatform)
        print (self.opentimer)


        ## Update All Images
        if currentscreen == 'main_screen':
            self.mainscreen.update()
            self.play.update()
            self.settings.update()

        elif currentscreen == 'levels':
            if self.ball_dir1[0] == 'r':
                self.ball1.x += self.Xspeed
                self.ball1.y -= self.Yspeed
            elif self.ball_dir1[0] == 'l':
                self.ball1.x -= self.Xspeed
                self.ball1.y -= self.Yspeed
            if self.ball1.x + self.ball1.size[0] > Window.width:
                self.ball_dir1.insert(0,'l')
            elif self.ball1.x < 0:
                self.ball_dir1.insert(0,'r')
            self.background.update()                
            self.platform1.update()
            self.ball1.update()

            if self.openplatform == False:
                self.hole1.x = 2 * Window.width
                self.hole1.y = 2 * Window.height
            self.hole1.update()
            
            if 0 < self.ball1.y < self.platform1.size[1] and self.ball1.x - self.hole1.x > 0 and (self.hole1.x + 0.063 * Window.width) - (self.ball1.x + 0.02065 * Window.height) >0:
                    self.ball1.x = Window.width * round(random.uniform(0,1),2)
                    self.ball1.y = Window.height
                    
                    self.Xspeed += 2
                    self.Yspeed += 0.5

                    self.score += 1
                    
                    
            if self.ball1.y < 0: ##and self.openplatform == False:
                self.GameOver.x = 0.25625 * Window.width
                self.GameOver.y = 0.294 * Window.height
                self.hole1.x= 2* Window.width
                self.hole1.y= 2* Window.height
                if self.counter % 3 == 0:
                    self.Again.x = 0.365 *Window.width
                    self.Again.y = 0.338 *Window.height
                    self.Continue.x = 0.565 *Window.width
                    self.Continue.y = 0.338 *Window.height
                else:
                    self.Again.x = 0.465 *Window.width
                    self.Again.y = 0.338 *Window.height
                

        
                
           
            

            
                
            


#########################################################################
############## Initializing App ##################
        
class MainApp(App):
    def build(self):
        parent = Widget()
        app = MainGUI()
        Clock.schedule_interval(app.update, 1.0/60.0)
        parent.add_widget(app)
        return parent

if __name__ == '__main__':
    MainApp().run()

    
        
        




















    
    

