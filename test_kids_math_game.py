import kids_math_game
from unittest.mock import patch
import random
import keyboard

def test_level_select_valid():
    with patch('builtins.input', return_value='2'):
        result = kids_math_game.level_select()
        assert result == 2

def test_level_select_invalid():
    with patch('builtins.input', return_value='5'):
        result = kids_math_game.level_select()
        assert result is None

def test_generate_problem_addition():
    num1, num2, answer, operation = kids_math_game.generate_problem(1)
    print(f"Generated num1 = {num1}, num2 = {num2}, answer = {answer}, operation = {operation}")
    assert operation == '+'
    assert answer == num1 + num2

def test_generate_problem_subtraction():
    random.seed(0)
    num1, num2, answer, operation = kids_math_game.generate_problem(2)
    print(f"Generated num1 = {num1}, num2 = {num2}, answer = {answer}, operation = {operation}")
    assert operation == '-'
    assert answer == num1 - num2

def test_generate_problem_multiplication():
    random.seed(0)
    num1, num2, answer, operation = kids_math_game.generate_problem(3)
    print(f"Generated num1 = {num1}, num2 = {num2}, answer = {answer}, operation = {operation}")
    assert operation == '*'
    assert answer == num1 * num2

def test_play_game_correct():
    with patch('builtins.input', return_value='14'):
        result = kids_math_game.play_game(2, 2, 4, '+')
        assert result is True

def test_play_game_correct():
    with patch('builtins.input', return_value='4'):  # Correct input
        result = kids_math_game.play_game(2, 2, 4, '+')
        assert result is True
