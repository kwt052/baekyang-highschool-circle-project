# main.py
# 📚 학생 D 담당
# 배울 개념: 모듈 import, 전체 흐름 설계, while문

import quiz
import data
import score

# 위 세 줄은 다른 파일에서 만든 함수를 가져오는 코드예요.
# quiz.py → quiz.ask_question() 처럼 "파일이름.함수이름()" 형태로 사용해요.

# ↓ 파일 맨 아래에 if __name__ == "__main__": 이 있어요.
#   이 부분은 건드리지 마세요. main()을 실행시켜주는 코드예요.


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

    # TODO 4: 맞은 문제 수를 셀 변수를 0으로 만드세요
    #         힌트: correct_count = 0

    # TODO 5: for문으로 각 문제를 출제하세요
    #         각 문제(q)는 딕셔너리예요. q["question"], q["choices"], q["answer"] 로 값을 꺼낼 수 있어요.
    #         quiz.ask_question()에 세 값을 넣어 호출하고, 맞으면 correct_count를 1 올려요.
    #         힌트: for q in questions:
    #                   result = quiz.ask_question(q["question"], q["choices"], q["answer"])
    #                   if result:
    #                       correct_count += 1

    # TODO 6: score.save_score()로 점수를 저장하세요
    #         힌트: score.save_score(name, correct_count, len(questions))

    # TODO 7: print()로 최종 점수를 출력하세요
    #         힌트: print(f"{correct_count}개 맞았어요!")
    pass  # 이 줄을 지우고 코드를 채워보세요!


def main():
    """
    프로그램의 메인 흐름입니다. 종료를 선택할 때까지 계속 실행됩니다.
    """
    # TODO 8: while True: 로 반복문을 시작하세요
    #         while True는 "계속 반복해"라는 뜻이에요. break를 만나면 멈춰요.

    # TODO 9: (while 블록 안에) show_menu()를 호출하세요

    # TODO 10: (while 블록 안에) input()으로 메뉴 선택을 입력받으세요
    #           힌트: choice = input("선택하세요: ")

    # TODO 11: (while 블록 안에) if문으로 선택에 따라 동작하게 하세요
    #           "1" → run_quiz()
    #           "2" → score.display_scores()
    #           "3" → print("잘 가요!") 후 break  ← break가 없으면 종료가 안 돼요!
    pass  # 이 줄을 지우고 코드를 채워보세요!


if __name__ == "__main__":
    main()
