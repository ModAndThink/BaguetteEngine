import tkinter as tk
from math import *
from random import *
import keyboard
import mouse
import time

colorList = ["red","blue","green","yellow","purple","white","pink"]
grid = []

class Model(object):
    instances = []
    def __init__(self,x=0,y=0,z=0,model = [],enable = True,visible = True):
        self.model = model
        self.position = [x,y,z]
        self.enable = enable
        self.visible = visible
        self.center_pos = [x,y,z]
        self.r = 0
        self.__class__.instances.append(self)
        self.CalculatePosV()
        self.CalculateModel()

    def distance(self,position):
        xr = position[0] - self.position[0]
        yr = position[1] - self.position[1]
        zr = position[2] - self.position[2]
        z_distance = sqrt((xr**2)+(zr**2))
        return sqrt((z_distance**2)+(yr**2))

    def sort_instances(app):
        swapped = True
        l = Model.instances
        while swapped:
            swapped = False
            for i in range(len(l) - 1):
                if app.distance(l[i].position) < app.distance(l[i + 1].position):
                    l[i], l[i + 1] = l[i + 1], l[i]
                    swapped = True
        Model.instances = l

    def sort_my_model(self,app):
        swapped = True
        l = self.model
        while swapped:
            swapped = False
            for i in range(len(l) - 1):
                if app.distance(l[i].position) < app.distance(l[i + 1].position):
                    l[i], l[i + 1] = l[i + 1], l[i]
                    swapped = True
        self.model = l

    def update(self):
        self.position[0] = self.center_pos[0] + sin(self.r)*2
        self.position[2] = self.center_pos[2] + cos(self.r)*2
        self.position[1] = self.center_pos[1] + sin(self.r)*-8
        self.r+=0.1
        self.CalculatePosV()
    
    def CalculateModel(self):
        neightbour = 0
        for i in self.model:
            neightbour = 0
            for j in self.model:
                if j.x + 1 == i.x and j.y == i.y and j.z == i.z:
                    neightbour += 1
                    i.west_enable = False
                
                if j.x - 1 == i.x and j.y == i.y and j.z == i.z:
                    neightbour += 1
                    i.east_enable = False
                
                if j.x == i.x and j.y + 1 == i.y and j.z == i.z:
                    neightbour += 1
                    i.bottom_enable = False

                if j.x == i.x and j.y - 1 == i.y and j.z == i.z:
                    neightbour += 1
                    i.top_enable = False

                if j.x == i.x and j.y == i.y and j.z - 1 == i.z:
                    neightbour += 1
                    i.north_enable = False
            
                if j.x == i.x and j.y == i.y and j.z + 1 == i.z:
                    neightbour += 1
                    i.sud_enable = False
                if neightbour == 6:
                    i.visible = False
    def CalculatePosV(self):
        for i in self.model:
            i.position[0] = self.x + i.default_pos[0]
            i.position[1] = self.y + i.default_pos[1]
            i.position[2] = self.z + i.default_pos[2]
    def drawn(self,app):
        direction_x = app.direction[0]
        zr = self.position[2] - app.camera[2]
        xr = self.position[0] - app.camera[0]
        rot_z = zr*cos(direction_x)-xr*sin(direction_x)
        if rot_z > 1 and app.distance(self.position) < 50:
            self.CalculatePosV()
            if self.enable == True:
                for i in self.model:
                    direction_x = app.direction[0]
                    zr = i.position[2] - app.camera[2]
                    xr = i.position[0] - app.camera[0]
                    rot_z = zr*cos(direction_x)-xr*sin(direction_x)
                    if rot_z > 1 and app.distance(i.position) < 50:
                        if self.visible == True:
                            if i.north_enable:
                                a = i.distance(i.vec_north)
                                b = app.distance(i.vec_north)
                                c = app.distance(i.position)
                                angle = acos((a**2+c**2-b**2)/(2 *a*c))
                                if degrees(angle) < 88:
                                    app.drawnF(i.north,i.color)
                                
                            if i.sud_enable:
                                a = i.distance(i.vec_sud)
                                b = app.distance(i.vec_sud)
                                c = app.distance(i.position)
                                angle = acos((a**2+c**2-b**2)/(2 *a*c))
                                if degrees(angle) < 88:
                                    app.drawnF(i.sud,i.color)                            
                            if i.east_enable:
                                a = i.distance(i.vec_east)
                                b = app.distance(i.vec_east)
                                c = app.distance(i.position)
                                angle = acos((a**2+c**2-b**2)/(2 *a*c))
                                if degrees(angle) < 88:
                                    app.drawnF(i.east,i.color)
                                
                            if i.west_enable:
                                a = i.distance(i.vec_west)
                                b = app.distance(i.vec_west)
                                c = app.distance(i.position)
                                angle = acos((a**2+c**2-b**2)/(2 *a*c))
                                if degrees(angle) < 88:
                                    app.drawnF(i.west,i.color)
                            
                            if i.top_enable:
                                a = i.distance(i.vec_top)
                                b = app.distance(i.vec_top)
                                c = app.distance(i.position)
                                angle = acos((a**2+c**2-b**2)/(2 *a*c))
                                if degrees(angle) < 88:
                                    app.drawnF(i.top,i.color)
                    
                            if i.bottom_enable:
                                a = i.distance(i.vec_bottom)
                                b = app.distance(i.vec_bottom)
                                c = app.distance(i.position)
                                angle = acos((a**2+c**2-b**2)/(2 *a*c))
                                if degrees(angle) < 88:
                                    app.drawnF(i.bottom,i.color)
    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    @property
    def z(self):
        return self.position[2]
            

class Voxel(object):
    instances = []
    visiblesVoxel = []
    def __init__(self,x = 0,y = 0,z = 0,visible = True,enable = True,color = "white",rotation = 0,voxel_type = None):
        self.position = [x,y,z]
        self.rotation = rotation
        self.color = color
        self.voxel_type = voxel_type
        self.enable = enable
        self.visible = visible
        self.north_enable = True
        self.sud_enable = True
        self.top_enable = True
        self.bottom_enable = True
        self.east_enable = True
        self.west_enable = True
        if voxel_type == None:
            self.__class__.instances.append(self)
        else:
            self.default_pos = [x,y,z]

    def distance(self,position):
        xr = position[0] - self.position[0]
        yr = position[1] - self.position[1]
        zr = position[2] - self.position[2]
        z_distance = sqrt((xr**2)+(zr**2))
        return sqrt((z_distance**2)+(yr**2))
    
    def calculateVisi(self):
        neightbour = 0
        for i in self.instances:
            if i.x + 1 == self.x and i.y == self.y and i.z == self.z:
                neightbour += 1
                self.west_enable = False
            
            if i.x - 1 == self.x and i.y == self.y and i.z == self.z:
                neightbour += 1
                self.east_enable = False
            
            if i.x == self.x and i.y + 1 == self.y and i.z == self.z:
                neightbour += 1
                self.bottom_enable = False

            if i.x == self.x and i.y - 1 == self.y and i.z == self.z:
                neightbour += 1
                self.top_enable = False

            if i.x == self.x and i.y == self.y and i.z - 1 == self.z:
                neightbour += 1
                self.north_enable = False
            
            if i.x == self.x and i.y == self.y and i.z + 1 == self.z:
                neightbour += 1
                self.sud_enable = False

        if neightbour != 6:
            self.__class__.visiblesVoxel.append(self)

    
    def drawn(self,app):
        if self.enable == True:
            direction_x = app.direction[0]
            zr = self.position[2] - app.camera[2]
            xr = self.position[0] - app.camera[0]
            rot_z = zr*cos(direction_x)-xr*sin(direction_x)
            if rot_z > 1 and app.distance(self.position) < 50:
                if self.visible == True:
                    if self.north_enable:
                        a = self.distance(self.vec_north)
                        b = app.distance(self.vec_north)
                        c = app.distance(self.position)
                        angle = acos((a**2+c**2-b**2)/(2 *a*c))
                        if degrees(angle) < 89:
                            app.drawnF(self.north,self.color)
                    
                    if self.sud_enable:
                        a = self.distance(self.vec_sud)
                        b = app.distance(self.vec_sud)
                        c = app.distance(self.position)
                        angle = acos((a**2+c**2-b**2)/(2 *a*c))
                        if degrees(angle) < 89:
                            app.drawnF(self.sud,self.color)
                    
                    if self.east_enable:
                        a = self.distance(self.vec_east)
                        b = app.distance(self.vec_east)
                        c = app.distance(self.position)
                        angle = acos((a**2+c**2-b**2)/(2 *a*c))
                        if degrees(angle) < 89:
                            app.drawnF(self.east,self.color)
                    
                    if self.west_enable:
                        a = self.distance(self.vec_west)
                        b = app.distance(self.vec_west)
                        c = app.distance(self.position)
                        angle = acos((a**2+c**2-b**2)/(2 *a*c))
                        if degrees(angle) < 89:
                            app.drawnF(self.west,self.color)
                    
                    if self.top_enable:
                        a = self.distance(self.vec_top)
                        b = app.distance(self.vec_top)
                        c = app.distance(self.position)
                        angle = acos((a**2+c**2-b**2)/(2 *a*c))
                        if degrees(angle) < 89:
                            app.drawnF(self.top,self.color)
                    
                    if self.bottom_enable:
                        a = self.distance(self.vec_bottom)
                        b = app.distance(self.vec_bottom)
                        c = app.distance(self.position)
                        angle = acos((a**2+c**2-b**2)/(2 *a*c))
                        if degrees(angle) < 89:
                            app.drawnF(self.bottom,self.color)
    
    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    @property
    def z(self):
        return self.position[2]
    
    @property
    def north(self):
        x = self.position[0]
        y = self.position[1]
        z = self.position[2]
        return [[0.5+x,0.5+y,0.5+z],
                [0.5+x,-0.5+y,0.5+z],
                [-0.5+x,0.5+y,0.5+z],
                [-0.5+x,-0.5+y,0.5+z]]
    
    @property
    def vec_north(self):
        x = self.position[0]
        y = self.position[1]
        z = self.position[2]
        return [x,y,z+0.5]
    @property
    def sud(self):
        x = self.position[0]
        y = self.position[1]
        z = self.position[2]
        return [[0.5+x,0.5+y,-0.5+z],
                [0.5+x,-0.5+y,-0.5+z],
                [-0.5+x,0.5+y,-0.5+z],
                [-0.5+x,-0.5+y,-0.5+z]]

    @property
    def vec_sud(self):
        x = self.position[0]
        y = self.position[1]
        z = self.position[2]
        return [x,y,z-0.5]
    
    @property
    def top(self):
        x = self.position[0]
        y = self.position[1]
        z = self.position[2]
        return [[0.5+x,0.5+y,0.5+z],
                [0.5+x,0.5+y,-0.5+z],
                [-0.5+x,0.5+y,0.5+z],
                [-0.5+x,0.5+y,-0.5+z]]
    @property
    def vec_top(self):
        x = self.position[0]
        y = self.position[1]
        z = self.position[2]
        return [x,y+0.5,z]
    
    @property
    def bottom(self):
        x = self.position[0]
        y = self.position[1]
        z = self.position[2]
        return [[0.5+x,-0.5+y,0.5+z],
                [0.5+x,-0.5+y,-0.5+z],
                [-0.5+x,-0.5+y,0.5+z],
                [-0.5+x,-0.5+y,-0.5+z]]
    @property
    def vec_bottom(self):
        x = self.position[0]
        y = self.position[1]
        z = self.position[2]
        return [x,y-0.5,z]
    @property
    def east(self):
        x = self.position[0]
        y = self.position[1]
        z = self.position[2]
        return [[0.5+x,-0.5+y,0.5+z],
                [0.5+x,0.5+y,0.5+z],
                [0.5+x,-0.5+y,-0.5+z],
                [0.5+x,0.5+y,-0.5+z]]
    @property
    def vec_east(self):
        x = self.position[0]
        y = self.position[1]
        z = self.position[2]
        return [x+0.5,y,z]

    @property
    def west(self):
        x = self.position[0]
        y = self.position[1]
        z = self.position[2]
        return [[-0.5+x,-0.5+y,0.5+z],
                [-0.5+x,0.5+y,0.5+z],
                [-0.5+x,-0.5+y,-0.5+z],
                [-0.5+x,0.5+y,-0.5+z]]
    @property
    def vec_west(self):
        x = self.position[0]
        y = self.position[1]
        z = self.position[2]
        return [x-0.5,y,z]

class Application():
    def __init__(self,x=0,y=0,z=0,rx=0,ry=0,rz=0):
        self.screen = tk.Tk()
        self.canvas = tk.Canvas(master=self.screen,bg = "black",width = 400,height = 250)
        self.canvas.pack()
        self.screen_distance = 180
        self.camera = [x,y,z]
        self.td = 0
        self.direction = [rx,ry,rz]
    def run(self):
        list(map(lambda x:x.calculateVisi(),Voxel.instances))

    def drawn_element(self):
        Model.sort_instances(self)
        list(map(lambda x:x.sort_my_model(self),Model.instances))
        list(map(lambda x:x.drawn(self),Voxel.visiblesVoxel))
        list(map(lambda x:x.drawn(self),Model.instances))

    def Update(self):
        list(map(lambda x:x.update(),Model.instances))
        
    def distance(self,cube):
        xr = cube[0] - self.camera[0]
        yr = cube[1] - self.camera[1]
        zr = cube[2] - self.camera[2]
        z_distance = sqrt((xr**2)+(zr**2))
        return sqrt((z_distance**2)+(yr**2))
    def get_x_screen(self,posPoint,rotation):
        x = 0
        xr = posPoint[0] - self.camera[0]
        yr = posPoint[1] - self.camera[1]
        zr = posPoint[2] - self.camera[2]
        try:
            direction_x = self.direction[0]
            direction_y = self.direction[1]
            rot_x = zr*sin(direction_x)+xr*cos(direction_x)
            rot_z = zr*cos(direction_x)-xr*sin(direction_x)
            x = (self.screen_distance/rot_z)*rot_x
        except:
            x = 0
        return x
    def get_y_screen(self,posPoint,rotation):
        x = 0
        xr = posPoint[0] - self.camera[0]
        yr = posPoint[1] - self.camera[1]
        z = posPoint[2] - self.camera[2]
        try:
            direction_x = self.direction[0]
            direction_y = self.direction[1]
            rot_z = z*cos(direction_x)-xr*sin(direction_x)
            y = (self.screen_distance/rot_z)*(yr*-1) 
        except:
            y = 0
        return y
    def drawnF(self,Face,Color):
        self.canvas.create_polygon(self.get_x_screen(Face[0],0)+200,self.get_y_screen(Face[0],0)+125,
                                           self.get_x_screen(Face[1],0)+200,self.get_y_screen(Face[1],0)+125,
                                           self.get_x_screen(Face[3],0)+200,self.get_y_screen(Face[3],0)+125,
                                           self.get_x_screen(Face[2],0)+200,self.get_y_screen(Face[2],0)+125,
                                           fill=Color)
        
if __name__=="__main__":
    app = Application()
    lastMousePos = mouse.get_position()
    doProcess = True
    mousePos = mouse.get_position()
    l = [Voxel(y=1,voxel_type = "model",color="cyan"),
         Voxel(voxel_type = "model",color="grey"),Voxel(x=1,voxel_type = "model",color="grey"),Voxel(x=-1,voxel_type = "model",color="grey"),
         Voxel(z=1,voxel_type = "model",color="grey"),Voxel(x=1,z=1,voxel_type = "model",color="grey"),Voxel(x=-1,z=1,voxel_type = "model",color="grey"),
         Voxel(z=-1,voxel_type = "model",color="grey"),Voxel(x=1,z=-1,voxel_type = "model",color="grey"),Voxel(x=-1,z=-1,voxel_type = "model",color="grey")]
    for i in range(0,10):
        Model(model = l,z=randint(i,30),y=randint(i,30))
    app.camera[1] = 0
    lastD = time.time()/1000
    app.run()
    lastj = keyboard.is_pressed('f')
    j = keyboard.is_pressed('f')
    while True:
        j = keyboard.is_pressed('f')
        if j:
            if j != lastj:
                if doProcess:
                    doProcess = False
                else:
                    doProcess = True
        mousePos = mouse.get_position()
        if doProcess:
            app.canvas.delete("all")
            if keyboard.is_pressed('w'):
                app.camera[0]-= 0.5*sin(app.direction[0])
                app.camera[2]+= 0.5*cos(app.direction[0])
            if keyboard.is_pressed('s'):
                app.camera[0]+= 0.5*sin(app.direction[0])
                app.camera[2]-= 0.5*cos(app.direction[0])
            if keyboard.is_pressed('d'):
                app.camera[2]+= 0.5*sin(app.direction[0])
                app.camera[0]+= 0.5*cos(app.direction[0])
            if keyboard.is_pressed('a'):
                app.camera[2]-= 0.5*sin(app.direction[0])
                app.camera[0]-= 0.5*cos(app.direction[0])
            if keyboard.is_pressed('space'):
                app.camera[1]+= 1
            if keyboard.is_pressed('shift'):
                app.camera[1]-= 1
            app.direction[0]-=(mousePos[0]-lastMousePos[0])/100
            app.direction[1]-=(mousePos[1]-lastMousePos[1])/100
            app.drawn_element()
            app.Update()
        app.screen.update()
        lastMousePos = mousePos
        lastj = j
        time.sleep(0.02)
