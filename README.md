
## How to clone and play

Download https://git-scm.com/download/win

git clone https://github.com/Nalgrin/Final-Project-Office-Escape.git

pip install pgzero

pgzrun main.py



## Office Escape

## Game States
Intro
Title: Office Escape
Caption: How You Play: Jump over the desks so you don't lose. If you hit a lamp you lose one of your lives. Make sure to collect those staplers you see to gain points
Caption 2: game. Press enter to start

## GamePlay
	title hidden
  btnReset hidden	
  btnQuit hidden
  All sprites shown
  score and health reset

Quit
	Game ends

## Sprites
Employee
Space Bar to jump 
If the employee hits a desk the boss catches you but if its a lamp thye lose only 1 life
Will be running across the scene with obstacles
		You gain points each time you collect a stapler


	

## Boss
Boss will continue to run after you till you have either ran out of lives or you hit a desk and which case he wins
Boss will run at a certain speed 
If the boss captures you you reset and however many staplers you had is your score 

## Stapler		
If the stapler collides with the employee they get a point added to the scoreboard
Boss captures employee staplers will reset 

## Desk 
If the desk collides with the employee they lose the boss captures them 
If jumped over, the game continues 
The desk will spawn continuously with a duration of 1 sec in between to give the player time to get back on the ground 

## Lamp
If the employee hits a lamp it slows them down so the boss gets closer to them
The lamp will spawn randomly

## UI components
Background
Office space that is continuous
	
## Title
Name of game
Basic instructions 
How to start the game

## Health
Label showing the current health which will be set to 3
When player hits a lamp their health goes down by 1


## LblScore
Label showing current score
As the employee collects the staplers the score will go up 1

## BtnReset
Shows when paused and when the game ends
When clicked game goes back to the gameplay state
Hide buttons
Shows all sprites 
Restart score and health 
	
## BtnQuit
Appears on pause and when the game ends
When clicked, exits the entire game


## Sound Effects
Employee jumps

Collecting sounds of staplers
When hitting a lamp

 Backgrond music

## Milestones
Basic Gameplay
Implement the introduction screen with the game title, caption, and instructions
Create the basic gameplay environment with the employees and obstacles
Enable jumping functionality using the SPACE bar
Implement collision detection for employees with obstacles
Obstacles and Scoring
Introduce the boss character that chases the employee
Add stapler score that increase the employee's score when collected
Implement the desk obstacle, causing the employee to lose if they collide
Introduce the lamp obstacle that takes 1 life away  the employee when hit
Keep track of the score as the employee collects staplers

## User Interface and Health and Score
		Design and implement the background office space
Create labels for the game health and score display
Health will have 3 lives

## Sound Effects
Add jumping sounds for when the employee jumps
Background music as the employee runs throughout the map
When he hit the lamp ita makes a sound 
When employee colides with the stapler it make a stapler sound

## Game Tuning Parameters
Employee
Speed of employee
Adjust the gravity and jump height to make the player character's movements feel responsive and natural.

## Boss
reasonable speed for the boss to ensure a challenging but not overly frustrating experience


## Lamp
You have a health bar that goes down by one when hit by a lamp

## Desks
Desks when hit immediately end the game





## Stretch Goals
Invincibility power-up being able to crash through obstacles for a short time
Adding different obstacles that you can slide under
Having co-workers in the background working as you are running through








## Description
	
Through this project, I have learned how to use pgzero/pygame zero which was an interesting experience since I have never used it before. It is very similar to pygame but less complicated and less code to use. The main part I got stuck on the most was the sounds, for some reason, the sounds in Pygame Zero do not like to work. Took me forever to figure it out, but my most embarrassing part was setting up the health. When I was trying to have it if the the health was 0 it would end the game I kept putting = instead of ==. Instead of equaling I kept saying gets 0 and I spent more time on that than anything. The biggest part I feel that needs improvement is understanding Pygame Zero since it is still somewhat new to me. I know more than I did before but there is still a lot to learn. There were tons of way I would have done this differently, I was planning on doing a 3d aspect but it wasn't all that easy to do since there was not a lot of tutorials on how to write in Panda 3d, which made me very limited. I followed my game document but I did change some things as well. I added a heath, made the staplers a way to collect for a score, desks would immediately end the game if you touched them, and the lamps if you touched them brought you down one life. Overall you have 3 lives so you can lose 2 different ways. The way I stayed on track was not focusing on the graphics at all just the gameplay. I had literal cubes the whole time testing it to get it just right before I started adding art. That helped tremendously. 





## Work Cited
https://www.pinterest.com/pin/375839531386867163/ 

https://www.1001fonts.com/techno-fonts.html 

https://pixabay.com/music/motown-old-school-rnb-retro-funk-energetic-background-music-136122/

https://freesound.org/people/cabled_mess/sounds/350985/ 

https://freesound.org/people/luminousfridge/sounds/496191/

https://freesound.org/people/Under7dude/sounds/163441/

https://imagine.meta.com/?prompt=generate+a+pixel+art+anime-style+man+running+in+a+black+suit+with+a+solid+white+background++

https://imagine.meta.com/?prompt=generate+a+pixel+art+anime-style+man+running+in+a+white+shirt+and+tie+with+a+solid+white+background++

https://www.bing.com/images/create/office-stapler-in-2d-pixel-art-style-with-a-solid-/1-65715c405650478fb1b4ed2194dda6ab?id=TramXtARg9fb%2bg7X35LuMg%3d%3d&view=detailv2&idpp=genimg&FORM=GCRIDP&ajaxhist=0&ajaxserp=0

https://www.bing.com/images/create/office-with-computers2c-desk2cchairs-in-office-cubic/1-6571616ebe074175ba386458fe13232d?id=bALAqPQUdrP6LK7xpvSWoQ%3d%3d&view=detailv2&idpp=genimg&FORM=GCRIDP&ajaxhist=0&ajaxserp=0

https://www.bing.com/images/create/office-with-computers2c-desk2cchairs-in-office-cubic/1-6571616ebe074175ba386458fe13232d?id=E42XS6fBUWYhdlzXcXT%2bNw%3d%3d&view=detailv2&idpp=genimg&FORM=GCRIDP&ajaxhist=0&ajaxserp=0


	


