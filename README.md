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
  
  The arguments:
  * **x**
  * **y**
  * **z**
  * **model** : you need to enter here a list of voxel with the argument voxel_type set to ```"model"``` or you would get an error
