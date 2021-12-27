# Game engine 100% python
  This game engine was create using only python. You can find a little demonstration on the file application.

## How do i use the engine ?

  The first thing to know is that for the 3D elements, all work around the Voxel object. It's has 7 arguments :
  * **x** : x position of the object
  * **y** : y position of the object
  * **z** : z position of the object
  * **visible** : boolean who define if the object is display
  * **enable** : a boolean who have no real utilitie but can be use for stop computation
  * **color** : color of the voxel
  * **voxel_type** : it's the most important argument who define if the voxel is alone (```None```) or a part of a model (```model```)
  
  The values:
  * **position ```[x,y,z]```** : it's the voxel position
  * **visible** : like in the arguments
  * **enable** : like in the arguments
  * **voxel_type** : like in the arguments
  * **color** : like in the arguments
  * **north_enable** : boolean who define if the face north is drawn
  * **sud_enable** : boolean who define if the face sud is drawn
  * **east_enable** : boolean who define if the face east is drawn
  * **west_enable** : boolean who define if the face west is drawn
  * **top_enable** : boolean who define if the face top is drawn
  * **bottom_enable** : boolean who define if the face bottom is drawn
  
  The methods :
  * **distance(a)** : get the distance between the position a (```[x,y,z]```) and the voxel's position
  * **x** : return the x position of the voxel
  * **y** : return the y position of the voxel
  * **z** : return the z position of the voxel
  
    So now we have sawn the voxels but if you want to create for example a zombie, it's would be hard to do it. So i introduce you the model, it can move a structure of voxel, run code when the game, ect...
  
  The arguments :
  * **x**
  * **y**
  * **z**
  * **model** : you need to enter here a list of voxel with the argument voxel_type set to ```"model"``` or you would get an error
  * **enable**
  * **visible**
  
  The values :
  * **position**
  * **enable**
  * **visible**
  * **model** : list who contain the voxel who constitue the model
  
  The methods :
  * **distance(a)** : get the distance between the position a (```[x,y,z]```) and the model's position
  * **start(self,app)** : run code when the application is start (we would see that later). The app argument is for get the application object
  * **update(self,app)** : run code at every update.
  
  So now we know the basic of the 3D engine, we need to know of to code a game. The object who would use is Application. Here we would find the camera who is a position (```[x,y,z]```). So here's how you need to organize your code :

```python
from BaguetteEngine import *
  
#create the Application object
app = Application.Application()
  
model_x = [Application.Voxel(voxel_type="model")]
  
#Create a new object from the object Model
class MyModel(Application.Model):
    def start(self,app):
        self.v = 0
    def update(self,app):
      self.v+=0.01
      self.position[1] = Application.sin(self.v)*10
  
MyModel(z=3,model = model_x)

app.screen_distance = 100 
#Initialize all
app.run()
  
while True:
    app.canvas.delete("all")
    app.Update()
    app.drawn_element()
    app.screen.update()
```
### How do i do to create a multiplayer game ?
  Before we start anything, i would to remenber that the use of public adress can expose to danger, so use a server own by compagnie that you can trust or use local adress. 
  So , for create your multiplayer game, you two objects, the ```Server``` and the ```Client``` (i think here it's not complicated). The server would have for function to send messages of client to the other (if a client send a message for said that he walk and the server would relai the message to the other client).
