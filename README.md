# <a id="title"></a>EMX Event Management

<img src="" alt=""><br>
(By now this ReadMe is just copied from another project to serve as a template. The content will change during the project buildup.)

<h2>Project</h2>

Welcome to this Enduro and Motocross event handler.<br>
This is event handler for motocross and enduro, which will forfill a real life need. There is no good event handler to create events for motocross and enduro clubs. All clubs uses thier own systems. (Everything from Google sheets and mail groups all kind of temporary solutions.) There is one event hadler for official competitions handled by SVEMO a Swedish motorsport association.

# <a id="table-of-content"></a>Table of Content

- <a href="#title">EMX Event Management</a>
- <a href="#table-of-content">Table of Content</a>
- <a href="#demo">Demo</a>
- <a href="#agile">Thinking Agile</a>
- <a href="#user-experience">User Experience</a>
- <a href="#user-stories">User Stories</a>
  - <a href="#strategy">Strategy</a>
  - <a href="#scope">Scope</a>
  - <a href="#structure">Structure</a>
  - <a href="#skeleton">Skeleton</a>
  - <a href="#surface">Surface</a>
- <a href="#technologies">Technologies</a>
  - <a href="#flowshart">Flowshart</a>
- <a href="#features">Features</a>
- <a href="#finalizing">Finalizing</a>
- <a href="#more-features">More Features</a>
- <a href="#testing">Testing</a>
  - <a href="#validating">Validating</a>
  - <a href="#bugs">Bugs</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>
  - <a href="#acknowledgments">Acknowledgments</a>

# <a id="demo"></a>Demo

The live link to Heroku can be found here - <a href="https://emx-event-c84aa8e070ad.herokuapp.com/" target="_blank">https://emx-event-c84aa8e070ad.herokuapp.com/</a>

The idea for this project is to get create an event handler for motocross and enduro events. Riders can register to sign up for events. Competitions, training or other events.

# <a id="agile"></a>Thinking Agile

  I'm already familaar with the agile understanding. Just 6 month ago, I got an exam from two years part time studies from an Aglie Project Managment course where most of the agile concept was covered, all from scrum, SAFe, project owner to the legal aspects and also change management. To use the project board in Github was a new experience, as I'm use to mostly using Miro and Trello. But fun to learn something new. Using the User Stories on the board is a nice way to keep track of what to do and see the progress. Using the board on my own is a bit strange, as for example, the iterations and iteration planning will not be applicable in the same way. But to show my knowledge I first created a backlog to where I can apply the MoSCoW principle and sort out things to do and not to do etc. Also a column for things to be tested as a way of using Defenition of Done (DoD).<br>
  <img src="readmefiles/agile-board_01.jpg" width="75%" alt="Image showing a Project Board">
  
# <a id="user-experience"></a>User Experience

The idea is to make it simple and be able to easlily overview different events<br>
By registering as a user, the rider can store some data to the database so when signing up to events, some data can be prepopulated from the user data.

## <a id="user-stories"></a>User stories

A user should:

- Be able to register as a rider
- Be able to sign up for events.
- See other riders that has sined up for an event.

### <a id="strategy"></a>Strategy

I aimed for a text based role-playing game where a player should be able to create and name a character with some simple stats. The characters stats combined with dice rolls would determine the outcome. For example: If the character has more strength it will be able to fight the dragon. If it has more charisma it will be more "lucky with partners". Even if the main story will end up the same, there will be three different side events from every time the dice rolls.
The story should be able to be edited easily in a Google Sheet. That will act as a database for the story, dice roll events and saving player and character.

### <a id="scope"></a>Scope

This will show what I learnt with Python using Django and all things in earlier modules.<br>

### <a id="structure"></a>Structure

- Using Django and Python
- Linked to ElephantSQL to use Postages SQL
- User Summernote for a WYSIWYG editor for creating event.

### <a id="skeleton"></a>Skeleton

The skeleton is based on a Django blog.

**Wireframe**

When starting this project I tried to get my ideas in to a word document.<br>
<img src="" width="" alt="">

### <a id="surface"></a>Surface

What is possible to do with a text based game?
I wanted the player to experience some visual features that will happen for different event.

- First I added some ascii art. There is a dragon.
- Second, I wanted the story text to stand out from the "console text" so I found a way to colorize the text. The story text as yellow and dice rolls as blue text.
<img src="readmefiles/roll-dice-event.jpg" alt="Image example of text came with yellow story text and blue roll dice event text.">

## <a id="technologies"></a>Technologies

1. Python - to create functions for the game.
2. Django - using Django blog as a foundation.
3. Cloudinary - to host images.
4. Summernote - to apply a wysiwyg editor.

## <a id="flowshart"></a>Flowshart

<img src=""  alt=""><br>

- Game start with a short preface for the game and also explaining some game commands.
- Player enter their name and create a simple character.
- Role-playing game start to get a story block from a Google Sheet.
- After each text block the player is asked to continue.
- The text block is checked for two different ending phrases.
- If a text block ends with the phase "Time to roll your dice" the player will be asked to roll.
  - From each of the dice roll event there will be three different scenarios. Then a player is asked continue.
  - The game continue to the main story efter the scenario from the dice roll event.
- If a text block end whith the phrase "The end!" that will trigger the ending sequense where player is asked to confirm game end.
- Game will reboot.

## <a id="features"></a>Features

<h3>Existing Features</h3>

Game starting:
The game starts with a preface and explain how to play the game.<br>
<img src="readmefiles/preface.jpg" alt="Image example of the preface text."><br>

The player will have to be able to use a keyboard to type letters to operate the game.<br>
First of all to enter a name, and then create a character with name and stats.<br>
<img src="readmefiles/screenshot_01a.jpg" alt="Image example of the game starting."><br>

Through the game it will ask if the player would like to continue or quit using the keys "c" respectively "q".<br>
<img src="readmefiles/screenshot_02a.jpg" alt="Image example of option to continue or quit game."><br>

The game will also ask if the player would like to roll the dice by typing letters "y" or "n".<br>
<img src="readmefiles/screenshot_02b.jpg" alt="Image example of option to roll dice or not."><br>

<h3>Google Sheet</h3>

The game use a Google Sheet as a database. This to easily edit the text of the story. There is one sheet for the main story,<br>
<img src="readmefiles/google-sheet_04.jpg" alt="Image example google sheet story sheet."><br>
 one sheet for events from the roll dice,<br>
 <img src="readmefiles/google-sheet_05.jpg" alt="Image example google sheet diceroll sheet."><br>
 and one sheet for the player and character data.<br>
 <img src="readmefiles/google-sheet_03.jpg" alt="Image example google sheet player sheet."><br>

<h3>Play mechanics</h3>

There is one main story in the Google Sheet document.
Each section of the game has its on row in the sheet.
Each line in the sheet will be checked if it's been used. If not, it will be printed and marked with "x" to be able to continue.
The length of the sentences are set to mach the width of the Heroku console. Just so that the row brake doesn't happen within a word. Also the text block are small enough to fit within the console windows to prevent the need of scrolling to read the text.<br>
<img src="readmefiles/google-sheet_01.jpg" alt="Example from a marked google sheet row"><br>
To mark the row with "x" also gives the benefits to manually set or remove an "x" in the sheet. For example to be able to run a specific text block over and over again in the console while testing.<br>

If the text in the story ends with "Time to roll your dice:" it will trigger next roll dice event.<br>
<img src="readmefiles/google-sheet_02.jpg" alt="Example from text ending with Time to roll your dice:"><br>

<h3>Error handling</h3>

The game has error handling to:

- Check the API connection to Google Sheet.
- Check that "rpg_p3" Google Sheet exists.
- Restrict the player name only to alphabetical letters and max 20 character long.
- Restrict the character name only to alphabetical letters and max 20 character long.
- Set the total value of character stats to 12.
- Make sure the player only enter numbers for stats.

## <a id="finalizing"></a>Finalizing

A screenshot form the game running in Heroku console.<br>
<img src="readmefiles/screenshot_03.jpg" alt="Image of the Heroku console when game is in action"><br>

## <a id ="more-features"></a>More Features?

Is there more to add to the game?<br>
It feels like this game can be expanded to endless.

- Option to go for different storylines.
- Feature to be able to answer the riddles.
- Different events can upgrade the character stats.
- Create a graphic interface.

## <a id="testing"></a>Testing

Through the developing of the EMX Events I had various challanges.
I followed the "I think, therefore I blog" walkthrough to set it up and use that blog as a base and then changed to my needs. At one part everything just fell apart. The Admin user interface stopped working. When logged in as an admin it showed nothing. Trying to fix it, it kind of went downhill from there. So I started over from scratch in a new repo and a new workspace and copied code piece by piece untill I was on track again. This will explain why the user stories in the project board are linked to two different repos.

I decided from the beginning that I should make sure to test everything I do. So from the first runnable skeleton of the project. I made sure it was working on Heroku by doing an early deploy. Through the whole process of developing the EMX Events app I hade it running with `python3 manage.py runserver` and checked that all was working about when I did each commit.

- Allauth : `../.pip-modules/lib/` doesn't work in Codeanywhere. It gives: `ls: cannot access '../.pip-modules/lib/': No such file or directory` the solution was found in Slack and I used this command instead: `cp -r /home/codeany/.local/lib/python3.9/site-packages/allauth/templates/* ./templates/.`



### <a id="validating"></a>Validating

I googled for any PEP8 and Python code validators, but could not find anyone working. I think I tried like five or six different. Some just threw errors on the API credentials and some didn't work at all. After spending some time to find a validator that worked I gave up. I relying on my telling me that it looked nice.

### <a id="bugs"></a>Bugs?

I haven't really encountered any bugs in this project.<br>
I got stuck several times in order to figure out different things but that is all about learning.

## <a id="deployment"></a>Deployment

The site was deployed to Heroku. Using the Code institute guidence from Love Sandwiches walkthrough.

- I used the GitHub template to create my own repository.
- Used Codeanywhere as IDE.
- Made a Google sheet and set up the API according to the videos in the Love Sandwiches walkthrough.
- I deployed the project to Heroku going through these steps.
    1. Create new app.
    2. Named it: rpg-p3 (Short for Role Playing Game - Project 3).
    3. Choose Europe as region.
    4. I went to the Settings tab to create config vars for CREDS and PORT.
    5. I added the buildpacks Python and Nodejs.
    6. In the Deploy tab I connected to GitHub repository "rpg-p3".
    7. I manually deployed branch (main).

I have in two occations experienced that Heroku stopped working and I had to redeploy branch. Seems like there is some time of timelimit?
I truly do hope that it is still running when it is time for review.
Otherwise just slack me (Robert Ahlin) and I will redeploy again.

## <a id="credits"></a>Credits

- I Think, Therefore I Blog - The base foundation for the skeleton setup from this walkthrough.
- Google search engine is frequently used. It's hard to remember how to write codes.
- A lot of help comes from search hits at the "stack overflow" forums.
- <a href="<https://djangocentral.com/authentication-using-an-email-address/" target="_blank">Djangocentral</a> - Code examples and help.
- ChatGPT - While exploring the endless possibilies using ChatGPT I have used this to troubleshoot and ask for help for code snippets.
- Using <a href="https://www.online-spellcheck.com/" target="_blank">https://www.online-spellcheck.com/</a> for spelling.

### <a id="acknowledgments"></a>Acknowledgments

- Thanks to my fiancé for supporting me when I get stuck.
