# 백양고 퀴즈봇

백양고 동아리 학생 4명이 함께 만드는 터미널 퀴즈 게임이에요.  
Python 기초 개념을 배우면서, 협업으로 하나의 프로그램을 완성하는 프로젝트입니다.

---

## 실행 화면

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

---

## 내 가이드 바로 가기

| 나는... | 내 가이드 |
|---------|---------|
| 이동규 (quiz.py 담당) | [가이드-학생A-quiz.md](docs/가이드-학생A-quiz.md) |
| 학생 B (data.py 담당) | [가이드-학생B-data.md](docs/가이드-학생B-data.md) |
| 학생 C (score.py 담당) | [가이드-학생C-score.md](docs/가이드-학생C-score.md) |
| 학생 D (main.py 담당) | [가이드-학생D-main.md](docs/가이드-학생D-main.md) |

---

## 역할 분담

| 학생 | 담당 파일 | 역할 | 배울 개념 |
|------|----------|------|----------|
| 이동규 | `quiz.py` | 문제 출제 & 정답 확인 | 함수, if문, for문 |
| 학생 B | `data.py` | 문제 데이터 관리 | 리스트, 딕셔너리, JSON |
| 학생 C | `score.py` | 점수 저장 & 조회 | 파일 읽기/쓰기 |
| 학생 D | `main.py` | 메뉴 & 전체 흐름 | 모듈 import, while문 |

---

## 파일 구조

```
baekyang-highschool-circle-project/
├── main.py          # 학생 D — 메뉴 & 전체 흐름
├── quiz.py          # 이동규 — 문제 출제 & 정답 확인
├── data.py          # 학생 B — 문제 데이터 관리
├── score.py         # 학생 C — 점수 저장 & 조회
├── questions.json   # 퀴즈 문제 데이터
├── requirements.txt # 필요한 패키지 목록
├── tests/
│   ├── conftest.py
│   ├── test_quiz.py
│   ├── test_data.py
│   └── test_score.py
└── docs/
    ├── 가이드-학생A-quiz.md
    ├── 가이드-학생B-data.md
    ├── 가이드-학생C-score.md
    └── 가이드-학생D-main.md
```

---

## 시작하기

### 1단계 — 저장소 포크 (Fork)

> 포크 = 선생님 저장소를 내 GitHub 계정으로 복사하는 것

1. 선생님이 공유한 저장소 링크를 크롬에서 열어요
2. 오른쪽 위 **Fork** 버튼 클릭
3. **Create fork** 버튼 클릭
4. 잠시 기다리면 `내아이디/baekyang-highschool-circle-project` 저장소가 생겨요

---

### 2단계 — Codespace 열기

> Codespace = 크롬북에서 바로 쓰는 온라인 개발 환경

1. 포크된 **내 저장소** 페이지에서 초록색 **`<> Code`** 버튼 클릭
2. **Codespaces** 탭 클릭
3. **Create codespace on main** 클릭
4. 새 탭에서 VS Code가 열리고 환경이 자동으로 설정돼요 (1~2분 소요)
5. 하단 터미널에서 아래 명령어로 Claude가 설치됐는지 확인해요:

```bash
claude --version
```

---

### 3단계 — Claude 로그인

터미널에 아래 명령어를 입력하고 안내에 따라 로그인해요:

```bash
claude
```

---

### 개인 컴퓨터 (Windows / Mac)

```bash
git clone https://github.com/kwt052/baekyang-highschool-circle-project.git
cd baekyang-highschool-circle-project
pip install -r requirements.txt
python main.py
```

---

## 테스트 실행

```bash
pytest tests/ -v
```

학생이 각자 파일을 완성할수록 빨간불(FAILED)이 초록불(PASSED)로 바뀌어요.

---

## 작업 방법

1. 내 담당 `docs/가이드-학생X-xxx.md` 파일을 읽어요
2. 내 브랜치를 만들어요
3. 담당 파일의 TODO를 채워요
4. `pytest` 로 테스트를 통과시켜요
5. PR을 올려요

---

## 기술 스택

- Python 3.11
- pytest 8.3.4
- GitHub Codespaces
