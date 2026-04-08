# tests/test_main.py
# 선생님이 미리 작성한 테스트 — 학생 D가 main.py를 완성하면 통과됩니다
import pytest
from unittest.mock import patch
from main import show_menu, main


def test_show_menu_prints_something(capsys):
    show_menu()
    captured = capsys.readouterr()
    assert len(captured.out) > 0, "show_menu()가 아무것도 출력하지 않았어요"


def test_show_menu_contains_menu_items(capsys):
    show_menu()
    captured = capsys.readouterr()
    assert "1" in captured.out, "메뉴에 '1'이 없어요"
    assert "2" in captured.out, "메뉴에 '2'가 없어요"
    assert "3" in captured.out, "메뉴에 '3'이 없어요"


def test_main_exits_on_3(capsys):
    # "3"을 입력하면 프로그램이 종료되어야 해요
    with patch("builtins.input", return_value="3"):
        main()
    captured = capsys.readouterr()
    assert len(captured.out) > 0, "종료 메시지가 출력되지 않았어요"


def test_main_shows_menu_before_exit(capsys):
    # 종료하기 전에 메뉴가 출력되어야 해요
    with patch("builtins.input", return_value="3"):
        main()
    captured = capsys.readouterr()
    assert "1" in captured.out or "2" in captured.out or "3" in captured.out
