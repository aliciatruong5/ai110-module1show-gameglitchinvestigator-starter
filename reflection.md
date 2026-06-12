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
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
