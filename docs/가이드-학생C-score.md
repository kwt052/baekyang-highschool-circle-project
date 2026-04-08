# 박성재 작업 가이드 — score.py

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
선택하세요: 2

홍길동: 3/5
김철수: 5/5
이영희: 4/5
```

### 전체 구조

프로그램은 4개 파일이 서로 연결돼서 동작해요:

```
main.py  ←  학생 D가 만드는 "사령탑"
  ↓ 문제 불러오기
data.py  ←  학생 B가 만드는 "문제 창고"
  ↓ 문제 출제
quiz.py  ←  이동규가 만드는 "출제관"
  ↓ 점수 저장
score.py ←  박성재(나!)가 만드는 "기록관"
```

### 내 역할

| 담당 파일 | 배울 개념 |
|----------|----------|
| `score.py` | 파일 읽기/쓰기, 문자열 처리, try-except(예외 처리) |

**내가 만들 것:** 퀴즈 점수를 파일에 저장하고, 저장된 기록을 불러와서 보여주는 기능

`score.py` 가 완성돼야 누가 몇 점을 받았는지 기록이 남아요.  
퀴즈가 끝날 때마다 자동으로 내 함수가 호출되고, "기록 보기" 메뉴도 내 함수로 동작해요.

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
git checkout student-c-score
```

브랜치가 없으면 새로 만들기:

```
git checkout -b student-c-score
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

> "내 브랜치 만들어줘. 이름은 `student-c-score` 로 해줘."

AI가 브랜치를 만들고, 지금 상황이 어떤지 설명해줄 거예요.

---

## 2단계: score.py 열기

왼쪽 파일 탐색기에서 `score.py` 를 클릭하면 편집기가 열려요.

- **`pass`** 는 "아직 아무것도 없음" 이라는 표시예요. 코드를 채우면 지워야 해요.
- 주석(`#`)에 힌트가 적혀 있어요. 힌트를 읽고 직접 코드를 써봐요.

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

### TODO 1~2: save_score 함수

**이 함수가 할 일:**
- 이름(`name`), 점수(`score`), 전체 문제 수(`total`)를 `scores.txt` 파일에 한 줄 추가한다

**한국어로 먼저:**
1. scores.txt 파일을 연다
2. "이름: 점수/전체" 형식으로 한 줄 쓴다

**파일 열기 모드를 먼저 생각해봐요:**

| 모드 | 설명 |
|------|------|
| `"r"` | 읽기 전용 |
| `"w"` | 덮어쓰기 (기존 내용이 지워져요!) |
| `"a"` | 이어쓰기 (기존 내용 유지하고 뒤에 추가) |

퀴즈를 여러 번 해도 기록이 쌓이려면 어떤 모드가 맞을까요?

---

### TODO 3~5: load_scores 함수

**잠깐, 이런 상황을 생각해봐요:**

처음 프로그램을 실행하면 `scores.txt` 파일이 없어요.  
없는 파일을 그냥 열려고 하면 어떻게 될까요?

```python
# scores.txt가 없을 때 이렇게 하면?
open("scores.txt", "r")   # → 프로그램이 에러로 멈춰버려요!
```

이런 상황을 대비하는 문법이 **try-except** 예요:

```
try:          → "이걸 먼저 해봐"
    ...
except ...:   → "이런 오류가 나면, 대신 이렇게 해"
    ...
```

**이 함수가 할 일:**
- 파일이 있으면 → 줄 목록을 읽어서 반환
- 파일이 없으면 → 빈 리스트 `[]` 를 반환

**들여쓰기 구조 (TODO 3, 4, 5의 관계):**
```
try:                           ← TODO 3 (try 블록 시작)
    파일 열기 (TODO 4)          ← try 안쪽
    readlines()로 반환 (TODO 5) ← try 안쪽
except FileNotFoundError:      ← TODO 3 (except 블록)
    return []                  ← except 안쪽
```

TODO 4와 5는 try 블록 안에 들어가야 해요. 들여쓰기에 주의하세요!

---

### TODO 6~8: display_scores 함수

**이 함수가 할 일:**
- 저장된 기록을 화면에 출력한다
- 기록이 없으면 "아직 기록이 없어요!" 를 출력한다

**한국어로 먼저:**
1. load_scores()로 기록을 불러온다
2. 기록이 없으면 안내 메시지를 출력한다
3. 기록이 있으면 for문으로 하나씩 출력한다

리스트가 비어있는지 확인하는 법은 뭘까요? `len()`을 써볼 수 있어요.

---

## 4단계: 디버깅 — 내 코드가 맞는지 확인하기

### 터미널 여는 법

Codespaces 상단 메뉴 → **Terminal** → **New Terminal**  
(단축키: `` Ctrl + ` ``)

### 테스트 실행하기

```
pytest tests/test_score.py -v
```

**결과 읽는 법:**

```
PASSED tests/test_score.py::test_save_score_creates_file   ← 성공!
FAILED tests/test_score.py::test_load_scores_returns_list  ← 아직 고쳐야 해요
```

초록불(PASSED)이 전부 나오면 완성이에요!

### 에러가 났을 때

에러 메시지를 AI에게 그대로 붙여넣으세요:

> "이런 에러가 났어요: [에러 메시지]"

**자주 나오는 에러:**

| 에러 | 뜻 | 확인할 것 |
|------|----|----------|
| `TypeError: 'NoneType'` | 함수가 None을 반환했어요 | `return` 이 빠진 건 아닌지 확인 |
| `object is not iterable` | for문에 반복 불가한 값이 들어왔어요 | load_scores가 리스트를 반환하는지 확인 |
| 기록이 계속 덮어써짐 | `"w"` 모드를 쓰고 있어요 | `"a"` 모드로 바꾸세요 |

---

## 5단계: 저장하고 GitHub에 올리기

**Codespaces라면** AI에게 말해요:
> "지금까지 작업한 거 저장해줘."

**개인 컴퓨터라면** 터미널에서:
```
git add score.py
git commit -m "feat: score.py 함수 구현"
git push origin student-c-score
```

---

## 6단계: PR 올리기

**Codespaces라면** AI에게 말해요:
> "PR 올려줘."

**개인 컴퓨터라면** GitHub 저장소 페이지에서 "Compare & pull request" 버튼을 클릭해요.

---

## 자주 하는 실수

| 실수 | 해결 방법 |
|------|----------|
| `pass` 를 안 지움 | 코드를 채운 후 `pass` 줄을 지워야 해요 |
| 들여쓰기 오류 | try 블록 안의 코드는 스페이스 4칸 들여써야 해요 |
| 저장을 안 함 | 편집 후 `Ctrl + S` 로 저장! |
| `"w"` 모드 사용 | save_score는 `"a"` 모드를 써야 기존 기록이 안 지워져요 |
| try-except 들여쓰기 | TODO 4, 5는 반드시 try: 블록 안쪽에 있어야 해요 |

---

## 막혔을 때

1. 에러 메시지를 읽어봐요 — 어느 줄에서 무슨 문제인지 써있어요
2. AI에게 에러 메시지를 그대로 붙여넣어요
3. AI가 바로 답을 주지 않더라도 — 같이 생각하면서 찾아가요
4. 그래도 모르겠으면 옆 친구에게 물어봐요!
