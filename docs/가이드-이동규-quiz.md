# 이동규 작업 가이드 — quiz.py

> 크롬북 + GitHub Codespaces 환경 기준입니다.  
> 개인 컴퓨터(Windows/Mac)를 쓴다면 → [개인 컴퓨터 설정](#개인-컴퓨터windowsmac에서-작업하기) 섹션을 먼저 읽어요.

---

## 우리가 만드는 프로그램

**백양고 퀴즈봇** — 터미널에서 실행하는 대화형 퀴즈 게임이에요.

```
===== 백양고 퀴즈봇 =====
1. 퀴즈 시작
2. 기록 보기
3. 종료
선택하세요: 1

이름을 입력하세요: 홍길동

Python에서 리스트를 만들 때 사용하는 기호는?
1. ()
2. {}
3. []
4. <>
답을 입력하세요: 3
정답이에요!

... (5문제 진행) ...

3개 맞았어요!
```

### 전체 구조

프로그램은 4개 파일이 서로 연결돼서 동작해요:

```
main.py  ←  학생 D가 만드는 "사령탑"
  ↓ 문제 불러오기
data.py  ←  학생 B가 만드는 "문제 창고"
  ↓ 문제 출제
quiz.py  ←  이동규(나!)가 만드는 "출제관"
  ↓ 점수 저장
score.py ←  박성재가 만드는 "기록관"
```

### 내 역할

| 담당 파일 | 배울 개념 |
|----------|----------|
| `quiz.py` | 함수, if문, for문 |

**내가 만들 것:** 문제를 화면에 출력하고, 사용자 답을 받아서, 맞는지 확인하는 기능

`quiz.py` 가 완성돼야 퀴즈 화면이 제대로 보이고, 정답 판정이 가능해져요.

---

## 개인 컴퓨터(Windows/Mac)에서 작업하기

> Codespaces를 쓴다면 이 섹션은 건너뛰어도 돼요.

### 사전 준비 (처음 한 번만)

| 프로그램 | 설치 확인 명령 |
|---------|--------------|
| Git | `git --version` |
| Python 3.11 이상 | `python --version` |
| VS Code (추천) | — |

- **Git:** https://git-scm.com/downloads
- **Python:** https://www.python.org/downloads (설치 시 "Add to PATH" 체크 필수)
- **VS Code:** https://code.visualstudio.com

### 저장소 클론하기 (처음 한 번만)

터미널(Windows: Git Bash 또는 PowerShell, Mac: Terminal)을 열고:

```
git clone https://github.com/kwt052/baekyang-highschool-circle-project.git
cd baekyang-highschool-circle-project
pip install -r requirements.txt
```

### 내 브랜치로 이동하기

```
git checkout student-a-quiz
```

브랜치가 없으면 새로 만들기:

```
git checkout -b student-a-quiz
```

### VS Code에서 열기

```
code .
```

---

## 1단계: 선생님 저장소 연결하기 (처음 한 번만)

Codespace 터미널에서 아래 명령어를 실행해요:

```bash
git remote add upstream https://github.com/kwt052/baekyang-highschool-circle-project.git
```

이후 선생님이 코드를 업데이트하면 이렇게 받아와요:

```bash
git pull upstream main
```

---

## 2단계: Codespaces에서 브랜치 만들기

> 개인 컴퓨터라면 위 섹션에서 이미 완료했어요. 3단계로 넘어가세요.

AI에게 이렇게 말해요:

> "내 브랜치 만들어줘. 이름은 `student-a-quiz` 로 해줘."

AI가 브랜치를 만들고, 지금 상황이 어떤지 설명해줄 거예요.

---

## 3단계: quiz.py 열기

왼쪽 파일 탐색기에서 `quiz.py` 를 클릭하면 편집기가 열려요.

파일을 보면 이렇게 생겼어요:

```python
def check_answer(user_input, answer):
    """
    사용자 입력과 정답을 비교합니다.
    반환값: 맞으면 True, 틀리면 False
    """
    # TODO 1: user_input과 answer를 비교해서 True 또는 False를 반환하세요
    #         두 값이 같은지 비교하는 방법: A == B
    #         ...
    pass  # 이 줄을 지우고 코드를 채워보세요!
```

- **`pass`** 는 "아직 아무것도 없음" 이라는 표시예요. 코드를 채우면 지워야 해요.
- 주석(`#`)에 힌트가 적혀 있어요. 힌트를 읽고 직접 코드를 써봐요.

---

## 4단계: 코드 채우기

### 코드 작성 전, 한국어로 먼저 생각해요

```
이 함수는 ___ 을 받아서,
___ 을 하고,
___ 을 돌려준다.
```

생각이 정리되면 그때 Python으로 옮겨요.

---

### TODO 1: check_answer 함수

**이 함수가 할 일:**
- 사용자가 입력한 답(`user_input`)과 정답(`answer`)을 비교한다
- 같으면 `True`, 다르면 `False` 를 돌려준다

**한국어로 먼저:**
1. user_input과 answer가 같은지 비교한다
2. 같으면 True를 돌려준다
3. 다르면 False를 돌려준다

비교 연산자 `==` 과 if문을 써봐요. 어떻게 조합할 수 있을까요?

---

### TODO 2~5: ask_question 함수

**이 함수가 할 일:**
1. 문제(`question`)를 화면에 출력한다
2. 선택지(`choices`) 리스트를 하나씩 출력한다
3. 사용자 답을 입력받는다
4. check_answer()로 맞는지 확인해서 결과를 돌려준다

**한국어로 먼저 정리해봐요:**
- for문으로 리스트를 하나씩 꺼내려면 어떻게 써야 할까요?
- 입력받은 값을 저장할 변수 이름은 무엇으로 할까요?
- check_answer에 무엇을 넣어야 할까요?

---

## 5단계: 디버깅 — 내 코드가 맞는지 확인하기

### 터미널 여는 법

Codespaces 상단 메뉴 → **Terminal** → **New Terminal**  
(단축키: `` Ctrl + ` ``)

### 테스트 실행하기

```
pytest tests/test_quiz.py -v
```

**결과 읽는 법:**

```
PASSED tests/test_quiz.py::test_correct_answer   ← 성공!
FAILED tests/test_quiz.py::test_wrong_answer     ← 아직 고쳐야 해요
```

초록불(PASSED)이 전부 나오면 완성이에요!

### 에러가 났을 때

에러 메시지를 AI에게 그대로 붙여넣으세요:

> "이런 에러가 났어요: [에러 메시지]"

---

## 6단계: 저장하고 GitHub에 올리기

**Codespaces라면** AI에게 말해요:
> "지금까지 작업한 거 저장해줘."

**개인 컴퓨터라면** 터미널에서:
```
git add quiz.py
git commit -m "feat: quiz.py 함수 구현"
git push origin student-a-quiz
```

---

## 7단계: PR 올리기

**Codespaces라면** AI에게 말해요:
> "PR 올려줘."

**개인 컴퓨터라면** GitHub 저장소 페이지에서 "Compare & pull request" 버튼을 클릭해요.

PR은 "내 작업을 메인에 합쳐도 될까요?" 라고 요청하는 거예요.

### ⚠️ 중요: PR 방향 확인하기

PR 생성 화면 상단에 이런 설정이 보여요. 반드시 확인하세요!

```
base repository: kwt052/baekyang-highschool-circle-project  ← 선생님 저장소여야 해요!
base: main

head repository: 내아이디/baekyang-highschool-circle-project  ← 내 포크
compare: student-a-quiz
```

**base repository가 내 포크로 되어 있으면** 선생님 저장소에 반영이 안 돼요.  
드롭다운을 눌러서 `kwt052/baekyang-highschool-circle-project`로 바꿔주세요.

---

## 자주 하는 실수

| 실수 | 해결 방법 |
|------|----------|
| `pass` 를 안 지움 | 코드를 채운 후 `pass` 줄을 지워야 해요 |
| 들여쓰기 오류 | Python은 들여쓰기가 중요해요. 스페이스 4칸이 기본이에요 |
| 저장을 안 함 | 편집 후 `Ctrl + S` 로 저장! |
| return을 빠뜨림 | 함수가 값을 돌려주려면 `return` 이 있어야 해요 |

---

## 막혔을 때

1. 에러 메시지를 읽어봐요 — 어느 줄에서 무슨 문제인지 써있어요
2. AI에게 에러 메시지를 그대로 붙여넣어요
3. AI가 바로 답을 주지 않더라도 — 같이 생각하면서 찾아가요
4. 그래도 모르겠으면 옆 친구에게 물어봐요!
