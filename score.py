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
