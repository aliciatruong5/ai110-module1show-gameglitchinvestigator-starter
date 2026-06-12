from logic_utils import check_guess, get_range_for_difficulty, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# --- Targets the high/low hint-direction bug ---

def test_guess_below_secret_says_go_higher():
    # The exact reported bug: secret 74, guess 8 -> hint must point HIGHER, not lower
    outcome, message = check_guess(8, 74)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_guess_above_secret_says_go_lower():
    # A guess above the secret must point LOWER
    outcome, message = check_guess(90, 74)
    assert outcome == "Too High"
    assert "LOWER" in message

# --- Targets the difficulty-range bug ---

def test_hard_range_is_wider_than_normal():
    # The exact reported bug: Hard returned (1, 50), NARROWER than Normal (1, 100),
    # so picking Hard made the game easier. Hard must be the widest range.
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high

def test_each_difficulty_returns_its_own_range():
    # Switching difficulty must actually change the range, not return the same span.
    easy = get_range_for_difficulty("Easy")
    normal = get_range_for_difficulty("Normal")
    hard = get_range_for_difficulty("Hard")
    assert easy == (1, 20)
    assert normal == (1, 100)
    assert hard == (1, 500)
    assert len({easy, normal, hard}) == 3

# --- Targets the string-with-a-number parsing bug ---

def test_string_with_trailing_number_is_rejected():
    # The exact reported bug: "hello1" has a digit in it but is NOT a number,
    # so it must be rejected, just like "hello".
    ok, value, error = parse_guess("hello1")
    assert ok is False
    assert value is None
    assert error == "That is not a number."

def test_string_with_leading_number_is_rejected():
    # "1hello" likewise must be rejected, not parsed as 1.
    ok, value, error = parse_guess("1hello")
    assert ok is False
    assert value is None
    assert error == "That is not a number."

def test_pure_letters_are_rejected():
    ok, value, error = parse_guess("hello")
    assert ok is False
    assert error == "That is not a number."

def test_plain_integer_is_accepted():
    ok, value, error = parse_guess("12")
    assert ok is True
    assert value == 12
    assert error is None

def test_integer_with_surrounding_whitespace_is_accepted():
    ok, value, error = parse_guess("  7  ")
    assert ok is True
    assert value == 7

def test_decimal_is_truncated_to_int():
    ok, value, error = parse_guess("3.9")
    assert ok is True
    assert value == 3

def test_non_finite_numbers_are_rejected():
    # float() accepts these, but they aren't valid guesses.
    for bad in ("inf", "nan", "-inf"):
        ok, value, error = parse_guess(bad)
        assert ok is False, f"{bad!r} should be rejected"
        assert error == "That is not a number."

def test_empty_input_prompts_for_a_guess():
    ok, value, error = parse_guess("")
    assert ok is False
    assert error == "Enter a guess."
