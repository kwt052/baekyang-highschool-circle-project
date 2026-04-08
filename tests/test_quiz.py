# tests/test_quiz.py
# 선생님이 미리 작성한 테스트 — 학생 1이 quiz.py를 완성하면 통과됩니다
import pytest
from unittest.mock import patch
from quiz import check_answer, ask_question


def test_correct_answer():
    result = check_answer("1", "1")
    assert result == True


def test_wrong_answer():
    result = check_answer("2", "1")
    assert result == False


def test_ask_question_returns_true_on_correct():
    with patch("builtins.input", return_value="1"):
        result = ask_question(
            "테스트 질문",
            ["1. 선택지A", "2. 선택지B"],
            "1"
        )
    assert result == True


def test_ask_question_returns_false_on_wrong():
    with patch("builtins.input", return_value="2"):
        result = ask_question(
            "테스트 질문",
            ["1. 선택지A", "2. 선택지B"],
            "1"
        )
    assert result == False


def test_ask_question_prints_question(capsys):
    with patch("builtins.input", return_value="1"):
        ask_question("이것은 질문입니다", ["1. A", "2. B"], "1")
    captured = capsys.readouterr()
    assert "이것은 질문입니다" in captured.out


def test_ask_question_prints_choices(capsys):
    with patch("builtins.input", return_value="1"):
        ask_question("질문", ["1. 선택A", "2. 선택B"], "1")
    captured = capsys.readouterr()
    assert "선택A" in captured.out
    assert "선택B" in captured.out
