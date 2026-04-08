# 학생 D 작업 가이드 — main.py

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

... (5문제 진행) ...

3개 맞았어요!
```

### 전체 구조

프로그램은 4개 파일이 서로 연결돼서 동작해요:

```
main.py  ←  학생 D(나!)가 만드는 "사령탑"
  ↓ 문제 불러오기
data.py  ←  학생 B가 만드는 "문제 창고"
  ↓ 문제 출제
quiz.py  ←  이동규가 만드는 "출제관"
  ↓ 점수 저장
score.py ←  박성재가 만드는 "기록관"
```

### 내 역할

| 담당 파일 | 배울 개념 |
|----------|----------|
| `main.py` | 모듈 import, while문, 전체 흐름 설계 |

**내가 만들 것:** 메뉴를 보여주고, 이동규·B·C가 만든 기능들을 연결해서 전체 프로그램을 완성하는 기능

`main.py` 는 다른 세 파일을 모두 가져다 쓰는 "사령탑" 이에요.  
내 파일이 완성되면 `python main.py` 한 줄로 전체 퀴즈봇이 실행돼요!

> **참고:** 이동규·B·C의 작업이 어느 정도 완성돼야 전체 실행이 가능해요.  
> 먼저 `show_menu()`와 `main()` 함수부터 만들어봐요. 테스트도 할 수 있어요!

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
git checkout student-d-main
```

브랜치가 없으면 새로 만들기:

```
git checkout -b student-d-main
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

> "내 브랜치 만들어줘. 이름은 `student-d-main` 으로 해줘."

AI가 브랜치를 만들고, 지금 상황이 어떤지 설명해줄 거예요.

---

## 2단계: main.py 열기

왼쪽 파일 탐색기에서 `main.py` 를 클릭하면 편집기가 열려요.

파일 맨 위에 이런 줄이 있어요:

```python
import quiz
import data
import score
```

이게 바로 **모듈 import** 예요.  
다른 파일(quiz.py, data.py, score.py)에서 만든 함수들을 가져다 쓰는 선언이에요.  
`data.load_questions()` 처럼 `파일이름.함수이름()` 형식으로 사용해요.

그리고 파일 맨 아래에 이런 줄이 있어요:

```python
if __name__ == "__main__":
    main()
```

이 부분은 건드리지 마세요. `python main.py` 로 실행했을 때 `main()` 함수를 자동으로 실행시켜주는 코드예요. 지금은 이 정도만 알면 충분해요.

---

## 3단계: 코드 채우기

### 코드 작성 전, 한국어로 먼저 생각해요

```
이 함수는 ___ 을 받아서,
___ 을 하고,
___ 을 돌려준다.
```

생각이 정리되면 그때 Python으로 옮겨요.

---

### TODO 1: show_menu 함수 (여기서부터 시작해요!)

**이 함수가 할 일:**
- 메뉴를 화면에 출력한다

단순하게 `print()` 여러 번이에요. 먼저 이것부터 완성하고 테스트해봐요!

---

### TODO 2~7: run_quiz 함수

**이 함수가 할 일:**
1. 문제 목록을 불러온다
2. 이름을 입력받는다
3. 맞은 수를 셀 변수를 만든다
4. 문제를 하나씩 출제하고 맞으면 카운트를 올린다
5. 점수를 저장한다
6. 최종 점수를 출력한다

**한국어로 단계별로 정리해봐요:**

각 문제(`q`)는 딕셔너리예요.  
`q["question"]`, `q["choices"]`, `q["answer"]` 처럼 키로 값을 꺼낼 수 있어요.  
for문으로 questions를 돌면서 quiz.ask_question()을 호출하면 돼요.

---

### TODO 8~11: main 함수

**이 함수가 할 일:**
- 프로그램이 종료를 선택할 때까지 계속 실행된다
- 메뉴를 보여주고, 선택에 따라 동작한다

**`while True:`** 는 "조건 없이 계속 반복해" 라는 뜻이에요.  
`break` 를 만나면 반복이 멈춰요.

**한국어로 먼저:**
1. 계속 반복한다 (while True)
2. 메뉴를 보여준다
3. 선택을 입력받는다
4. 1이면 퀴즈, 2이면 기록 보기, 3이면 종료(break)

---

## 4단계: 디버깅 — 내 코드가 맞는지 확인하기

### 터미널 여는 법

Codespaces 상단 메뉴 → **Terminal** → **New Terminal**  
(단축키: `` Ctrl + ` ``)

### show_menu 먼저 테스트하기

show_menu를 완성하면 바로 테스트할 수 있어요:

```
pytest tests/test_main.py -v
```

**결과 읽는 법:**

```
PASSED tests/test_main.py::test_show_menu_prints_something   ← 성공!
FAILED tests/test_main.py::test_main_exits_on_3              ← 아직 고쳐야 해요
```

### 전체 실행해보기

이동규·B·C 작업이 완성된 후:

```
python main.py
```

실제로 퀴즈를 풀어볼 수 있어요!

### 에러가 났을 때

에러 메시지를 AI에게 그대로 붙여넣으세요:

> "이런 에러가 났어요: [에러 메시지]"

**자주 나오는 에러:**

| 에러 | 뜻 | 확인할 것 |
|------|----|----------|
| `ModuleNotFoundError` | 모듈을 못 찾았어요 | quiz.py, data.py, score.py 파일이 있는지 확인 |
| `AttributeError` | 없는 함수를 호출했어요 | `data.load_questions()` 철자 확인 |
| 프로그램이 안 꺼짐 | break가 없어요 | "3" 선택 시 break가 있는지 확인 |

---

## 5단계: 저장하고 GitHub에 올리기

**Codespaces라면** AI에게 말해요:
> "지금까지 작업한 거 저장해줘."

**개인 컴퓨터라면** 터미널에서:
```
git add main.py
git commit -m "feat: main.py 함수 구현"
git push origin student-d-main
```

---

## 6단계: PR 올리기

**Codespaces라면** AI에게 말해요:
> "PR 올려줘."

**개인 컴퓨터라면** GitHub 저장소 페이지에서 "Compare & pull request" 버튼을 클릭해요.

> **학생 D의 main.py는 마지막에 합쳐져요.**  
> 다른 친구들의 PR이 먼저 merge되면 `python main.py` 로 전체 프로그램을 실행해볼 수 있어요!

---

## 자주 하는 실수

| 실수 | 해결 방법 |
|------|----------|
| `pass` 를 안 지움 | 코드를 채운 후 `pass` 줄을 지워야 해요 |
| 들여쓰기 오류 | while 블록 안의 코드는 스페이스 4칸 들여써야 해요 |
| 저장을 안 함 | 편집 후 `Ctrl + S` 로 저장! |
| `break` 빠뜨림 | while True는 break 없으면 영원히 안 꺼져요 |
| `data.` 빠뜨림 | 다른 파일 함수는 `data.load_questions()` 처럼 파일 이름을 붙여야 해요 |

---

## 막혔을 때

1. 에러 메시지를 읽어봐요 — 어느 줄에서 무슨 문제인지 써있어요
2. AI에게 에러 메시지를 그대로 붙여넣어요
3. AI가 바로 답을 주지 않더라도 — 같이 생각하면서 찾아가요
4. 그래도 모르겠으면 옆 친구에게 물어봐요!
