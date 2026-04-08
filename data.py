# data.py
# 📚 학생 B 담당
# 배울 개념: 리스트, 딕셔너리, JSON 파일 읽기

import json


def load_questions():
    """
    questions.json 파일에서 문제 목록을 불러옵니다.
    반환값: 문제 딕셔너리들의 리스트
    """
    # TODO 1: with open()으로 "questions.json" 파일을 열어보세요
    #         힌트: with open("questions.json", "r", encoding="utf-8") as f:
    #               (with 블록 안에 TODO 2, 3이 들어가요 — 들여쓰기 주의!)

    # TODO 2: (with 블록 안에) json.load()로 파일 내용을 읽어보세요
    #         힌트: data = json.load(f)

    # TODO 3: (with 블록 안에) 읽어온 데이터를 반환하세요
    #         힌트: return data

    pass  # 이 줄을 지우고 코드를 채워보세요!


def get_question(questions, index):
    """
    questions 리스트에서 index번째 문제를 가져옵니다.
    반환값: 문제 딕셔너리 하나
    """
    # TODO 4: questions 리스트에서 index번째 항목을 꺼내서 반환하세요
    #         리스트에서 항목 꺼내는 법 → questions[index]
    #         함수가 값을 돌려주려면 return 키워드가 필요해요!
    #         힌트: return questions[index]
    pass  # 이 줄을 지우고 코드를 채워보세요!
