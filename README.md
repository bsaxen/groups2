Directory structure:

app.py
templates/
  index.html


Prompt:

make web application (frontend, backend). Use html,python and javascript and no database.
The concept is: M is set of objects identified by a positive integer, Example 1,2,3,4,7,54,23,22
An object can have three states: 1,2,3. Initial state is always 3. The only allowed state transitions are: 3->1, 3->2

G is a set of groups (different size) made of objects with state 1 or 2. Use '+' state=1 and '-' for state=2. Example (+1,+4,-7), (-1,-23)

The groups are defined in a text file that can be uploaded to the web application. Syntax used in the groups file,example:
1:-3,-4,-11
2:+1,-2,-3
34:+3,+7,+9

Add function to reset object states to intial state = 3.
Add function to upload any group text file. When upploaded, the object states shall be reset to 3
The available unique objects shall be according to objects existing in the groups file.

The objects shall be presented to the left in the front-end user interface. It should be possible to change the state of the objects from this object view,
by clicking on the object. The object state shall be visualized using 3=blue,2=red,1=green


Typical number of objects can be 1000+ and number of groups 1000+. Make a compact view of the objects and the groups in respective view.

The groups shall be presented to the right in the front-end user interface. The objects in each group shall be colored as 2=red,1=green. The background of the group
shall initially be white.

If an object has state = 1 then for all groups having this object in state = 1, set the background color = yellow of the group
If an object has state = 2 then for all groups having this object in state = 2, set the background color = yellow of the group

If an object has state = 1 then for all groups having this object in state = 2, color the object in the group grey
If an object has state = 2 then for all groups having this object in state = 1, color the object in the group grey

If only one non-grey object left in a group then set the object state according to the state the object has in the group.

Add function: for each object still in state=3, change temporarly object state to 1 and check if any groups will have all objects grey . If all objects grey in the group,
are grey then set object state permamently to 2. Call this function BWL.
