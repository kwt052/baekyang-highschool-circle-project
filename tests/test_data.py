# tests/test_data.py
# 선생님이 미리 작성한 테스트 — 학생 2가 data.py를 완성하면 통과됩니다
import pytest
from data import load_questions, get_question


def test_load_questions_returns_list():
    questions = load_questions()
    assert isinstance(questions, list)


def test_load_questions_not_empty():
    questions = load_questions()
    assert len(questions) > 0


def test_question_has_required_fields():
    questions = load_questions()
    q = questions[0]
    assert "question" in q
    assert "choices" in q
    assert "answer" in q


def test_choices_is_list():
    questions = load_questions()
    q = questions[0]
    assert isinstance(q["choices"], list)


def test_get_question_returns_dict():
    questions = load_questions()
    q = get_question(questions, 0)
    assert isinstance(q, dict)


def test_get_question_correct_index():
    questions = load_questions()
    q = get_question(questions, 0)
    assert q == questions[0]
