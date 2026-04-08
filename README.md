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

## 역할 분담

| 학생 | 담당 파일 | 역할 | 배울 개념 |
|------|----------|------|----------|
| 학생 A | `quiz.py` | 문제 출제 & 정답 확인 | 함수, if문, for문 |
| 학생 B | `data.py` | 문제 데이터 관리 | 리스트, 딕셔너리, JSON |
| 학생 C | `score.py` | 점수 저장 & 조회 | 파일 읽기/쓰기 |
| 학생 D | `main.py` | 메뉴 & 전체 흐름 | 모듈 import, while문 |

---

## 파일 구조

```
baekyang-highschool-circle-project/
├── main.py          # 학생 D — 메뉴 & 전체 흐름
├── quiz.py          # 학생 A — 문제 출제 & 정답 확인
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

### GitHub Codespaces (크롬북)

저장소 페이지에서 **Code → Open with Codespaces** 를 클릭하면 바로 시작할 수 있어요.

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
