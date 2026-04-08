# 백양고 퀴즈봇 — 구현 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 학생 4명이 역할 분담해서 채울 수 있도록, 쉐도우 코드 + 미리 작성된 테스트 + CI 환경을 준비한다.

**Architecture:** 선생님이 테스트를 먼저 작성해두고 학생이 통과시키는 TDD 구조. 학생 파일은 TODO 주석이 있는 빈 틀(쉐도우 코드)로 제공. 테스트는 처음엔 전부 실패(FAILED)하며, 학생이 코드를 채우면 통과(PASSED)된다.

**Tech Stack:** Python 3.11, pytest 8.3.4, JSON, GitHub Actions

---

## 파일 구조

| 파일 | 역할 | 작성자 |
|------|------|--------|
| `questions.json` | 퀴즈 문제 데이터 | 선생님 |
| `quiz.py` | 문제 출제 & 정답 확인 (쉐도우) | 학생 1이 채움 |
| `data.py` | JSON 파일 읽기 & 문제 관리 (쉐도우) | 학생 2가 채움 |
| `score.py` | 점수 저장 & 조회 (쉐도우) | 학생 3이 채움 |
| `main.py` | 메뉴 & 전체 흐름 (쉐도우) | 학생 4가 채움 |
| `tests/conftest.py` | pytest 경로 설정 | 선생님 |
| `tests/test_quiz.py` | quiz.py 테스트 | 선생님 |
| `tests/test_data.py` | data.py 테스트 | 선생님 |
| `tests/test_score.py` | score.py 테스트 | 선생님 |
| `.github/workflows/test.yml` | PR 자동 테스트 CI | 선생님 |

---

## Task 1: 퀴즈 데이터 파일 생성

**Files:**
- Create: `questions.json`

- [ ] **Step 1: questions.json 작성**

```json
[
  {
    "question": "Python에서 리스트를 만들 때 사용하는 기호는?",
    "choices": ["1. ()", "2. {}", "3. []", "4. <>"],
    "answer": "3"
  },
  {
    "question": "Python에서 화면에 출력할 때 쓰는 함수는?",
    "choices": ["1. input()", "2. print()", "3. write()", "4. show()"],
    "answer": "2"
  },
  {
    "question": "for문에서 리스트의 각 항목을 꺼낼 때 사용하는 키워드는?",
    "choices": ["1. from", "2. each", "3. in", "4. of"],
    "answer": "3"
  },
  {
    "question": "함수를 정의할 때 사용하는 키워드는?",
    "choices": ["1. function", "2. def", "3. func", "4. define"],
    "answer": "2"
  },
  {
    "question": "Python에서 주석을 달 때 사용하는 기호는?",
    "choices": ["1. //", "2. /* */", "3. #", "4. --"],
    "answer": "3"
  }
]
```

- [ ] **Step 2: 커밋**

```bash
git add questions.json
git commit -m "chore: 퀴즈 문제 데이터 추가"
```

---

## Task 2: quiz.py 쉐도우 코드

**Files:**
- Create: `quiz.py`

- [ ] **Step 1: quiz.py 쉐도우 코드 작성**

```python
# quiz.py
# 📚 학생 1 담당
# 배울 개념: 함수, if문, for문


def check_answer(user_input, answer):
    """
    사용자 입력과 정답을 비교합니다.
    반환값: 맞으면 True, 틀리면 False
    """
    # TODO 1: user_input과 answer를 비교해서
    #         같으면 True, 다르면 False를 반환하세요
    #         힌트: if문을 사용해요
    pass  # 이 줄을 지우고 코드를 채워보세요!


def ask_question(question, choices, answer):
    """
    문제를 출력하고 사용자 답을 받아 맞는지 확인합니다.
    반환값: 맞으면 True, 틀리면 False
    """
    # TODO 2: print()로 question을 출력하세요

    # TODO 3: for문으로 choices 리스트를 하나씩 출력하세요
    #         힌트: for choice in choices:
    #                   print(choice)

    # TODO 4: input()으로 사용자 답을 입력받으세요
    #         힌트: user_input = input("답을 입력하세요: ")

    # TODO 5: check_answer()를 사용해서 결과를 반환하세요
    pass  # 이 줄을 지우고 코드를 채워보세요!
```

- [ ] **Step 2: 커밋**

```bash
git add quiz.py
git commit -m "chore: quiz.py 쉐도우 코드 추가 (학생 1용)"
```

---

## Task 3: data.py 쉐도우 코드

**Files:**
- Create: `data.py`

- [ ] **Step 1: data.py 쉐도우 코드 작성**

```python
# data.py
# 📚 학생 2 담당
# 배울 개념: 리스트, 딕셔너리, JSON 파일 읽기

import json


def load_questions():
    """
    questions.json 파일에서 문제 목록을 불러옵니다.
    반환값: 문제 딕셔너리들의 리스트
    """
    # TODO 1: open()으로 "questions.json" 파일을 열어보세요
    #         힌트: with open("questions.json", "r", encoding="utf-8") as f:

    # TODO 2: json.load()로 파일 내용을 읽어보세요
    #         힌트: data = json.load(f)

    # TODO 3: 읽어온 데이터를 반환하세요
    pass  # 이 줄을 지우고 코드를 채워보세요!


def get_question(questions, index):
    """
    questions 리스트에서 index번째 문제를 가져옵니다.
    반환값: 문제 딕셔너리 하나
    """
    # TODO 4: questions 리스트에서 index번째 항목을 반환하세요
    #         힌트: 리스트에서 항목 꺼내는 법 → questions[index]
    pass  # 이 줄을 지우고 코드를 채워보세요!
```

- [ ] **Step 2: 커밋**

```bash
git add data.py
git commit -m "chore: data.py 쉐도우 코드 추가 (학생 2용)"
```

---

## Task 4: score.py 쉐도우 코드

**Files:**
- Create: `score.py`

- [ ] **Step 1: score.py 쉐도우 코드 작성**

```python
# score.py
# 📚 학생 3 담당
# 배울 개념: 파일 I/O, 문자열 처리

SCORES_FILE = "scores.txt"


def save_score(name, score, total):
    """
    이름, 점수, 전체 문제 수를 scores.txt에 저장합니다.
    """
    # TODO 1: open()으로 SCORES_FILE을 추가 모드("a")로 열어보세요
    #         힌트: with open(SCORES_FILE, "a", encoding="utf-8") as f:

    # TODO 2: f.write()로 결과를 저장하세요
    #         형식: "이름: 점수/전체\n"
    #         힌트: f.write(f"{name}: {score}/{total}\n")
    pass  # 이 줄을 지우고 코드를 채워보세요!


def load_scores():
    """
    scores.txt에서 저장된 기록을 읽어옵니다.
    반환값: 기록 문자열 리스트 (파일이 없으면 빈 리스트)
    """
    # TODO 3: 파일이 없을 수도 있어요. try-except를 사용해봐요
    #         힌트: try:
    #                   ...
    #               except FileNotFoundError:
    #                   return []

    # TODO 4: open()으로 파일을 읽기 모드("r")로 열어보세요

    # TODO 5: readlines()로 내용을 읽어 반환하세요
    pass  # 이 줄을 지우고 코드를 채워보세요!


def display_scores():
    """
    저장된 모든 기록을 출력합니다.
    """
    # TODO 6: load_scores()로 기록을 불러오세요

    # TODO 7: 기록이 없으면 "아직 기록이 없어요!" 를 출력하세요

    # TODO 8: 기록이 있으면 for문으로 하나씩 출력하세요
    #         힌트: for line in scores:
    #                   print(line, end="")
    pass  # 이 줄을 지우고 코드를 채워보세요!
```

- [ ] **Step 2: 커밋**

```bash
git add score.py
git commit -m "chore: score.py 쉐도우 코드 추가 (학생 3용)"
```

---

## Task 5: main.py 쉐도우 코드

**Files:**
- Create: `main.py`

- [ ] **Step 1: main.py 쉐도우 코드 작성**

```python
# main.py
# 📚 학생 4 담당
# 배울 개념: 모듈 import, 전체 흐름 설계

import quiz
import data
import score


def show_menu():
    """
    메인 메뉴를 출력합니다.
    """
    # TODO 1: print()로 메뉴를 출력해보세요
    #         예시:
    #         print("===== 백양고 퀴즈봇 =====")
    #         print("1. 퀴즈 시작")
    #         print("2. 기록 보기")
    #         print("3. 종료")
    pass  # 이 줄을 지우고 코드를 채워보세요!


def run_quiz():
    """
    퀴즈를 진행합니다.
    """
    # TODO 2: data.load_questions()로 문제 목록을 불러오세요
    #         힌트: questions = data.load_questions()

    # TODO 3: input()으로 이름을 입력받으세요
    #         힌트: name = input("이름을 입력하세요: ")

    # TODO 4: 맞은 문제 수를 셀 변수를 만드세요
    #         힌트: correct_count = 0

    # TODO 5: for문으로 각 문제를 quiz.ask_question()으로 출제하세요
    #         맞으면 correct_count를 1 올려요
    #         힌트: for q in questions:
    #                   result = quiz.ask_question(q["question"], q["choices"], q["answer"])
    #                   if result:
    #                       correct_count += 1

    # TODO 6: score.save_score()로 점수를 저장하세요

    # TODO 7: print()로 최종 점수를 출력하세요
    pass  # 이 줄을 지우고 코드를 채워보세요!


def main():
    """
    프로그램의 메인 흐름입니다. 종료를 선택할 때까지 계속 실행됩니다.
    """
    # TODO 8: while True 반복문으로 프로그램이 계속 실행되게 하세요

    # TODO 9: show_menu()를 호출하세요

    # TODO 10: input()으로 메뉴 선택을 입력받으세요
    #          힌트: choice = input("선택하세요: ")

    # TODO 11: if문으로 선택에 따라 동작하게 하세요
    #          "1" → run_quiz()
    #          "2" → score.display_scores()
    #          "3" → print("잘 가요!") 후 break
    pass  # 이 줄을 지우고 코드를 채워보세요!


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: 커밋**

```bash
git add main.py
git commit -m "chore: main.py 쉐도우 코드 추가 (학생 4용)"
```

---

## Task 6: pytest 설정 및 테스트 파일

**Files:**
- Create: `tests/conftest.py`
- Create: `tests/test_quiz.py`
- Create: `tests/test_data.py`
- Create: `tests/test_score.py`

- [ ] **Step 1: tests/conftest.py 작성 (경로 설정)**

```python
# tests/conftest.py
import os
import sys

# 프로젝트 루트를 Python 경로에 추가 (quiz, data, score import 가능하게)
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# 테스트가 항상 프로젝트 루트에서 실행되도록 설정
# (questions.json, scores.txt 상대경로가 올바르게 동작하게)
os.chdir(os.path.dirname(os.path.dirname(__file__)))
```

- [ ] **Step 2: tests/test_quiz.py 작성**

```python
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
```

- [ ] **Step 3: tests/test_data.py 작성**

```python
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
```

- [ ] **Step 4: tests/test_score.py 작성**

```python
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
```

- [ ] **Step 5: 커밋**

```bash
git add tests/
git commit -m "test: 선생님 테스트 코드 추가 (학생이 통과시킬 목표)"
```

---

## Task 7: GitHub Actions CI

**Files:**
- Create: `.github/workflows/test.yml`

- [ ] **Step 1: .github/workflows/test.yml 작성**

```yaml
name: Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Python 설정
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: 패키지 설치
        run: pip install -r requirements.txt

      - name: 테스트 실행
        run: pytest tests/ -v
```

- [ ] **Step 2: 커밋**

```bash
git add .github/
git commit -m "ci: GitHub Actions 자동 테스트 설정"
```

---

## 검증

모든 파일이 준비되면 다음을 확인:

```bash
# 테스트 실행 — 학생이 코드를 아직 안 채웠으니 전부 FAILED가 나와야 정상
pytest tests/ -v
```

예상 출력:
```
FAILED tests/test_quiz.py::test_correct_answer
FAILED tests/test_data.py::test_load_questions_returns_list
FAILED tests/test_score.py::test_save_score_creates_file
...
```

이것이 정상입니다. 학생들이 TODO를 채우면 초록불(PASSED)로 바뀝니다.
