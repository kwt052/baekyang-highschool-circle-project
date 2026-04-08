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
