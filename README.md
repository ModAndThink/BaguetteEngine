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
  
  note : DONT use voxel, they dont drawn correctly with the models.
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
  So , for create your multiplayer game, you two objects, the ```Server``` and the ```Client``` (i think here it's not complicated). The server would have for function to send messages of client to the other (if a client send a message for said that he walk and the server would relai the message to the other client). So we are going to start by the most simple, the server.

#### The server

Parameters : 
* **port** : the port were information go
* **ip** : the adress to listen

Value :
* **clients** : all the clients connect

Methods :
* **start** : start the server
* **send** : for send messages with ```msg``` the message to send and ```conn``` the recever (use the list clients).

#### The client

Parameters :
* **port** : the port of the server where the client would connect
* **ip** : the ip of the server

Values :
* **port**
* **ip**
* **ClientNumber** : the number of client (i would explain later of to update it)
* **VCN** : boolean who say if the value ClientNumber have been update

Methods :
* **send(msg)** : send a message to the other client
* **UpdateValue(lm)** : i would come to it later
* **run** : start the client
* **start** : execute code when the run method is call
* **left** : disconnect the client

Now we know more the objects client and server but how all is working ? To start , the messages are divide into two part : TheAction|value. The first part is about the content of the message (if it's the update of the position of a player for example), the next part is the value (the new position of the player). All are in string format. The function UpdateValue is for treat the message . The lm value is a list who contain the two famous part of the message. For example, for threat the player score in a party of two players, we can do that : 

Client side :

```python
from BaguetteEngine import *

my_score = 0

app = Application.Application()

class ClientForScore(Client.Client):
    def UpdateValue(self,lm):
        if lm[0] == "new_score":
            self.the_score_of_the_ennemi = int(lm[1])
    def start(self):
        self.the_score_of_the_ennemi = 0

class ScoreLabel(Application.Label):
    def update(self,app):
        self.text = str(app.Cs.the_score_of_the_ennemi)+" : "+str(my_score)

try:
    app.Cs = ClientForScore(ip = "192.168.1.64")
    app.Cs.run()
    
    #here we send a special protocol for get the current number of client
    app.Cs.send("TOTAL_CLIENT")
    while not app.Cs.VCN:
        pass
      
    if app.Cs.ClientNumber > 2:
        print(app.Cs.ClientNumber)
        print("party full")
        app.Cs.left()
        ee
      
    if app.Cs.ClientNumber == 1:
        print("waiting for a another player")
        while app.Cs.ClientNumber < 2:
            app.Cs.send("TOTAL_CLIENT")
            while not app.Cs.VCN:
                pass
            app.Cs.VCN = False
      
    print("We're ready")
except:
  print("the ip is invalide or the server is offline")
ScoreLabel(x=100)

while True:
    app.canvas.delete("all")
    app.Update()
    if Application.keyboard.is_pressed('space'):
        my_score+=1
        app.Cs.send("new_score|"+str(my_score))
    app.drawn_element()
    app.screen.update()

```

Server side :

```python
from BaguetteEngine import *

ServerScore = Server.Server()
ServerScore.start()
```
