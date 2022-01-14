import glfw
from OpenGL.GL import *
import numpy as np
import pyrr
from random import *

buffer = bytearray(800 * 600 * 3)
display = (800,600)

if not glfw.init():
    raise Exception("glfw can not be initialized!")

def CreateWindow(title="Baguette game",width=800,height=600):
    display = (width,height)
    window = glfw.create_window(width,height,title, None, None)
    glfw.set_window_pos(window,400,200)
    glfw.make_context_current(window)

    return window

def DrawTriangle(pointA=[-0.5, -0.5, 0.0],pointB=[0.5, -0.5,0.0],
                 pointC=[-0.5, 0, 0.0],color=[1.0,1.0,1.0]):
    vertices = [pointA[0], pointA[1], pointA[2],
                pointB[0], pointB[1], pointB[2],
                pointC[0], pointC[1], pointC[2]]

    colors = [color[0], color[1], color[2],
              color[0], color[1], color[2],
              color[0], color[1], color[2] ]
    
    v = np.array(vertices,dtype=np.float32)
    c = np.array(colors, dtype=np.float32)
    
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT,0,v)
    glEnableClientState(GL_COLOR_ARRAY)
    glColorPointer(3, GL_FLOAT,0,c)
    glDrawArrays(GL_TRIANGLES,0,3)

def Pixel(x,y):
    buffer_data = [randint(0,255), 0, 0] * (x * y)
    buffer = (GLubyte * (x * y * 3))(*buffer_data)
    glDrawPixels(x, y, GL_RGB, GL_UNSIGNED_BYTE, buffer)
    
if __name__=="__main__":
    window = CreateWindow()
    initialPosition = (0,0,0)
    z=1
    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        
        glTranslate(100,0,0)
        for i in range(8,0,-1):
            Pixel(i*100,600)
        
        glfw.swap_buffers(window)
    glfw.terminate()
