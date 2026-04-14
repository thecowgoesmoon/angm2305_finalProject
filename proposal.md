# Art Idea Generator

## Repository
<[Repository Link](https://github.com/thecowgoesmoon/angm2305_finalProject/tree/main)>

## Description
This program will allow the user to choose a randomly generated art prompt based on a human or an environmental setting, 
as well as a color palette. The user can also choose whether or not the color palette will consist of three, four, or five colors.

## Features
- Feature 1
	- This feature generates a prompt based on three words (height/size, personality, occupation/general adjective) specifically targeted for humans when the user selects "humanoid" in the idea selection menu and provide the user with three humanoid-related words with the option of choosing another. For instance, the generated prompt may be a "tall angry optimist" or a "medium young chef." After the user is given the prompt, the user will then be prompted to choose a color palette.

- Feature 2
	- This feature generates a prompt based on three words (size, mood, setting) specifically targeted for environments when the user selects "environment" in the idea selection menu and provide the user with three setting-related words with the option of choosing another. For instance, the generated prompt may be a "large serene lake" or a "small spooky town." After the user is given the prompt, the user will then be prompted to choose a color palette.
 
- Feature 3
	- After the user has selected a prompt, the user can choose between a color palette of either three, four, or five colors. Once chosen, the program will output a color palette with the amount of colors that the user has chosen with the hex codes beneath each color. The user can re-roll their options an unlimited amount of times before being moved to a menu that displays their final prompt and color palette choices.

## Challenges
- Learning how to allow the color palette to generate a plethora of colors as opposed to only a select few may be necessary for this program.
- Researching the pygame library further as well as what makes an engaging UI in order to create a clear and appealing interface may be necessary for this program.
- Researching the keyboard input of the pygame library as well as any other library that can use mouse clicks for menu selection within the program may be necessary for this program.

## Outcomes
Ideal Outcome:
- The user will be able to choose between generating two prompts—one based on humans and one based on environments. Both prompts will relay three semi-correlating words that utilize adjectives/nouns for its respective human or environment correlated sentences. After relaying the sentence, the program should instruct the user to choose a color palette from anywhere between three to five colors and provide the user with a randomized color palette.

Minimal Viable Outcome:
- The program will generate a prompt based on adjectives /nouns for either humans or environments. The program will then generate a randomized color palette with a minimum of three colors.

## Milestones 

- Week 1
1. Ensures the general program can run somewhat via terminal prior to UI creation
2. Implement color palette randomizer by ensuring program can print color palettes in terminal prior to UI creation
3. Implement selection of either human or environment idea generation

- Week 2
1. Implement program window and functionable UI layout based on terminal tests from Week 1
2. Add choices for the user to choose between three, four and five colors from its color palette
3. Ensures window displays prompt text & randomized color palettes

- Week 3
1. Ensure program runs  as needed
2. Implement any necessary errors fallbacks for contingency
3. Make any window or function(s) adjustments if needed
