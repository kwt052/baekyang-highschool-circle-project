# tests/test_score.py
# 선생님이 미리 작성한 테스트 — 학생 3이 score.py를 완성하면 통과됩니다
import pytest
import os
from score import save_score, load_scores, display_scores


@pytest.fixture(autouse=True)
def cleanup_scores_file():
    """각 테스트 전후로 scores.txt를 정리합니다."""
    if os.path.exists("scores.txt"):
        os.remove("scores.txt")
    yield
    if os.path.exists("scores.txt"):
        os.remove("scores.txt")


def test_save_score_creates_file():
    save_score("홍길동", 3, 5)
    assert os.path.exists("scores.txt")


def test_save_score_contains_name():
    save_score("홍길동", 3, 5)
    scores = load_scores()
    assert any("홍길동" in line for line in scores)


def test_save_score_contains_score():
    save_score("홍길동", 3, 5)
    scores = load_scores()
    assert any("3/5" in line for line in scores)


def test_load_scores_returns_empty_when_no_file():
    scores = load_scores()
    assert scores == []


def test_load_scores_returns_list():
    save_score("테스트", 4, 5)
    scores = load_scores()
    assert isinstance(scores, list)


def test_multiple_scores_saved():
    save_score("학생A", 3, 5)
    save_score("학생B", 5, 5)
    scores = load_scores()
    assert len(scores) == 2


def test_display_scores_no_file(capsys):
    display_scores()
    captured = capsys.readouterr()
    assert "없" in captured.out
