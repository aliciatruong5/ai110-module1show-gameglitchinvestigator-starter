# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game looked very simple and organized. It looked like everything would be functional with no errors. When I ran my first guess, I saw my first error which was the hints. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The first error I saw was that when I would guess a number that was lower than the secret number, the hint would be "GO LOWER" and the same thing goes for if I were to put a higher number than the secret number, it would say "GO HIGHER"
  2. The second error that I noticed was that when I would click new game to restart, it would change all the information like number of attempts and the secret number, but it would not allow me to guess a number.
  3. It seems that the game would also give us one attempt less than the attempts allowed like we have 6 attempts but we only guessed 5 times and it would say game over. 
  4. Another error would be the range when you would change difficulty. It seems like it is not changing. It looks like it is still 1-100. 
  5. I also noticed that when I were to put a string as a guess, it would return as that is not a number, but if I were to add a string with a number like hello1, it would be seen as a number and return GO LOWER.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

|   Input    | Expected Behavior | Actual Behavior | Console Output / Error |
|------------|-------------------|-----------------|------------------------|
| guess: 4   | "GO HIGHER" hint  | "GO LOWER" hint |        none            |
|------------|-------------------|-----------------|------------------------|
| guess: 36  | "GO LOWER" hint   |"GO HIGHER" hint |        none            |
|------------|-------------------|-----------------|------------------------|
|  hello1    |That is not a number| "GO LOWER" hint |        none            |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Claude Code to help me on this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  When solving the first bug that I encountered which was the hint bug. I explained to Claude about the bug that whenever I were to guess a number it would give me the wrong hint. Claude then sugguested that I need to look at the function check_guess which is correct. I noticed that the status labels and hint messages were swapped thats why it was giving the wrong hint messages. Then I acceepted their edit to the function. After that I tested it by going into the game again and seeing if the hint will be correct for my guess which it was.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  One example of a Claude suggestion that was misleading was when I asked it to generate a pytest case in the tests game logic file, it started to make a whole new file rather than making one from the existing file. It made me think that there was an error in the exisiting file and thats why it had to make a brand new one. Then I realized that it was my prompt that was wrong since I did not put the correct file name, it made a new file with the name I typed. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  To see whether of not a bug was really fixed, I ran multiply pytest and made sure it all passed. I also played the game myself multiply times after every fix to make sure it was doing what it should be doing. If not, I would tell Claude that there is an error in this part or this part is still giving the wrong thing. 
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  One test that I ran was the hint messages. In the beginning, it would give you the wrong hint every time you would submit a guess. After fixing the bug, I went back into the game and tested if it would still give the wrong hint messages which it did not so I declared that the bug was fixed. It showed that sometimes even the smallest mistakes can be made by AI and it would only notice it until we point it.
- Did AI help you design or understand any tests? How?
  Yes, Claude helped me understand how you can accurately test every scenario to make sure that the bug is fixed. Sometimes I would not have thought of a scenario like having a string be surrounded by intergers to make it look as a number and having it pass as a guess. Claude helped me see that I can make more than number or strings as a guess.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit "reruns" is basically an tool that we can use to see our game or website function or run in our case. It helps us see how functions and if there are any errors. Session state would be a state that we go in when we run the streamlit and we can see the changes we make live and how it functions. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git. 
    Sometime that I would reused in future labs or projects would be making sure that I use git more effiently like making multiple commits. I am still not used to it so I think making a habit of doing one than one commit to git would help me see the changes or errors in the code/document.
- What is one thing you would do differently next time you work with AI on a coding task?
  One thing would be giving Claude a more detailed prompt of what I am doing to do to the code. Sometimes Claude would not make the right deletes on the file and it would have something missing. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  Claude is like my second pair of eyes and can see what I cannot see at times. 
