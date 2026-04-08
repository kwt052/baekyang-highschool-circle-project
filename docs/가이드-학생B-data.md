# 학생 B 작업 가이드 — data.py

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
data.py  ←  학생 B(나!)가 만드는 "문제 창고"
  ↓ 문제 출제
quiz.py  ←  이동규가 만드는 "출제관"
  ↓ 점수 저장
score.py ←  학생 C가 만드는 "기록관"
```

### 내 역할

| 담당 파일 | 배울 개념 |
|----------|----------|
| `data.py` | 리스트, 딕셔너리, JSON 파일 읽기 |

**내가 만들 것:** `questions.json` 파일에서 퀴즈 문제를 불러오는 기능

`data.py` 가 완성돼야 퀴즈 문제들이 프로그램 안으로 들어올 수 있어요.  
내가 문제를 못 불러오면 퀴즈 자체가 시작이 안 돼요 — 중요한 역할이에요!

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
git checkout student-b-data
```

브랜치가 없으면 새로 만들기:

```
git checkout -b student-b-data
```

### VS Code에서 열기

```
code .
```

---

## 1단계: Codespaces에서 브랜치 만들기

> 개인 컴퓨터라면 위 섹션에서 이미 완료했어요. 2단계로 넘어가세요.

AI에게 이렇게 말해요:

> "내 브랜치 만들어줘. 이름은 `student-b-data` 로 해줘."

AI가 브랜치를 만들고, 지금 상황이 어떤지 설명해줄 거예요.

---

## 2단계: data.py 열기 전에 — questions.json 먼저 확인

왼쪽 파일 탐색기에서 `questions.json` 을 클릭해서 구조를 먼저 봐요.

```json
[
  {
    "question": "Python에서 리스트를 만들 때 사용하는 기호는?",
    "choices": ["1. ()", "2. {}", "3. []", "4. <>"],
    "answer": "3"
  },
  ...
]
```

이 파일이 바로 내가 읽어올 데이터예요:
- 전체는 `[]` 로 감싼 **리스트**
- 각 문제는 `{}` 로 감싼 **딕셔너리**
- 딕셔너리 안에 `"question"`, `"choices"`, `"answer"` 키가 있어요

이 구조를 눈에 익혀두면 코드 작성이 훨씬 쉬워져요!

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

### TODO 1~3: load_questions 함수

**이 함수가 할 일:**
- `questions.json` 파일을 열어서 내용을 읽고 돌려준다

**한국어로 먼저:**
1. 파일을 연다 (`with open(...)`)
2. JSON 형식으로 읽는다 (`json.load()`) — **이 줄은 with 블록 안에 있어야 해요**
3. 읽은 내용을 반환한다 (`return`) — **이 줄도 with 블록 안에 있어야 해요**

**들여쓰기 구조:**
```
with open(...) as f:   ← TODO 1
    읽기 (TODO 2)       ← with 안쪽, 스페이스 4칸
    반환 (TODO 3)       ← with 안쪽, 스페이스 4칸
```

`with open(...) as f:` 는 파일을 열고 작업이 끝나면 자동으로 닫아주는 문법이에요.

---

### TODO 4: get_question 함수

**이 함수가 할 일:**
- `questions` 리스트에서 `index` 번째 문제를 꺼내서 돌려준다

리스트에서 항목 꺼내는 법:
```python
my_list = ["사과", "바나나", "딸기"]
my_list[0]   # → "사과"   (0번째)
my_list[1]   # → "바나나" (1번째)
```

함수가 값을 돌려주려면 `return` 키워드가 필요하다는 것도 잊지 마세요!

---

## 4단계: 디버깅 — 내 코드가 맞는지 확인하기

### 터미널 여는 법

Codespaces 상단 메뉴 → **Terminal** → **New Terminal**  
(단축키: `` Ctrl + ` ``)

### 테스트 실행하기

```
pytest tests/test_data.py -v
```

**결과 읽는 법:**

```
PASSED tests/test_data.py::test_load_questions_returns_list   ← 성공!
FAILED tests/test_data.py::test_load_questions_not_empty      ← 아직 고쳐야 해요
```

초록불(PASSED)이 전부 나오면 완성이에요!

### 에러가 났을 때

에러 메시지를 AI에게 그대로 붙여넣으세요:

> "이런 에러가 났어요: [에러 메시지]"

**자주 나오는 에러:**

| 에러 | 뜻 | 확인할 것 |
|------|----|----------|
| `FileNotFoundError` | 파일을 못 찾았어요 | 터미널 위치가 프로젝트 최상위인지 확인 |
| `assert False` (test_load_questions_returns_list) | load_questions()가 리스트를 반환 안 해요 | return이 있는지 확인 |
| `TypeError: 'NoneType'` | 함수가 None을 반환했어요 | return 키워드가 빠진 건 아닌지 확인 |

---

## 5단계: 저장하고 GitHub에 올리기

**Codespaces라면** AI에게 말해요:
> "지금까지 작업한 거 저장해줘."

**개인 컴퓨터라면** 터미널에서:
```
git add data.py
git commit -m "feat: data.py 함수 구현"
git push origin student-b-data
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
| 들여쓰기 오류 | with 블록 안의 코드는 스페이스 4칸 들여써야 해요 |
| 저장을 안 함 | 편집 후 `Ctrl + S` 로 저장! |
| `return` 빠뜨림 | 함수가 값을 돌려주려면 `return` 이 있어야 해요 |
| `import json` 빠뜨림 | data.py 맨 위에 `import json` 이 있는지 확인 |

---

## 막혔을 때

1. 에러 메시지를 읽어봐요 — 어느 줄에서 무슨 문제인지 써있어요
2. AI에게 에러 메시지를 그대로 붙여넣어요
3. AI가 바로 답을 주지 않더라도 — 같이 생각하면서 찾아가요
4. 그래도 모르겠으면 옆 친구에게 물어봐요!
