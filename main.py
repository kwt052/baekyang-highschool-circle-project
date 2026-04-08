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
