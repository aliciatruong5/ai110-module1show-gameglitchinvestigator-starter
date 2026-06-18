# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
   The purpose of the game is to see how well AI can implement a game, find what we can debug, and work with AI to fix it. It is a learning exercise built around a number guessing game.
- [ ] Detail which bugs you found.
   There were multiple bugs in the game. The first bug that I discovered was that the hint message was wrong whenever you submitted a guess. It was the opposite of what it should be: for example, you guessed 5 and the secret number is 3, but the hint message would say "Too Low". The second bug was the difficulty mode. It would not match the range that was given; for example, in Easy mode the range should be 1-20, but the secret number would be 50. It was hardcoded to 1-100. The third bug was that you could guess with a string and a number. It would accept the guess as long as it contained a number.
- [ ] Explain what fixes you applied.
   The fix for the first bug was to swap the status labels and hint messages, since they were returning the opposite of what they should be. For the second bug, I deleted the hardcoded range and made it into a variable based on the low and high of the range for the difficulty. I also added a different range for each difficulty individually. As for the third bug, I added a check that detects any string or float in the guess and returns "That is not a number".

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Select what difficulty to play at -> Normal
2. Enter in the box -> 50
3. Show hint would pop up -> "Too High" or "Too Low"
4. After every guess, it would return a hint
5. Score will update with every guess being made
6. Game will end when the correct is guessed or reached the limit amount of tries

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
============================= test session starts ==============================
collecting ... collected 15 items

tests/test_game_logic.py::test_winning_guess PASSED                      [  6%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 13%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 20%]
tests/test_game_logic.py::test_guess_below_secret_says_go_higher PASSED  [ 26%]
tests/test_game_logic.py::test_guess_above_secret_says_go_lower PASSED   [ 33%]
tests/test_game_logic.py::test_hard_range_is_wider_than_normal PASSED    [ 40%]
tests/test_game_logic.py::test_each_difficulty_returns_its_own_range PASSED [ 46%]
tests/test_game_logic.py::test_string_with_trailing_number_is_rejected PASSED [ 53%]
tests/test_game_logic.py::test_string_with_leading_number_is_rejected PASSED [ 60%]
tests/test_game_logic.py::test_pure_letters_are_rejected PASSED          [ 66%]
tests/test_game_logic.py::test_plain_integer_is_accepted PASSED          [ 73%]
tests/test_game_logic.py::test_integer_with_surrounding_whitespace_is_accepted PASSED [ 80%]
tests/test_game_logic.py::test_decimal_is_truncated_to_int PASSED        [ 86%]
tests/test_game_logic.py::test_non_finite_numbers_are_rejected PASSED    [ 93%]
tests/test_game_logic.py::test_empty_input_prompts_for_a_guess PASSED    [100%]

============================== 15 passed in 0.01s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
