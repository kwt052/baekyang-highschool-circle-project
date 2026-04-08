# score.py
# 📚 박성재 담당
# 배울 개념: 파일 I/O, 문자열 처리, try-except(예외 처리)

SCORES_FILE = "scores.txt"


def save_score(name, score, total):
    """
    이름, 점수, 전체 문제 수를 scores.txt에 저장합니다.
    """
    # TODO 1: open()으로 SCORES_FILE을 추가 모드로 열어보세요
    #         파일 열기 모드: "r"=읽기, "w"=덮어쓰기, "a"=이어쓰기(기존 내용 유지)
    #         퀴즈를 여러 번 해도 기록이 쌓이려면 어떤 모드가 맞을까요?
    #         힌트: with open(SCORES_FILE, ???, encoding="utf-8") as f:

    # TODO 2: (with 블록 안에) f.write()로 한 줄을 저장하세요
    #         저장 형식: "이름: 점수/전체\n"   ← \n 은 줄바꿈 기호예요
    #         예) "홍길동: 3/5\n"
    #         힌트: f-string을 사용해요 → f"{변수}: {변수}/{변수}\n"
    pass  # 이 줄을 지우고 코드를 채워보세요!


def load_scores():
    """
    scores.txt에서 저장된 기록을 읽어옵니다.
    반환값: 기록 문자열 리스트 (파일이 없으면 빈 리스트)
    """
    # 생각해봐요: scores.txt가 아직 없다면 어떻게 될까요?
    # 그냥 open()을 쓰면 프로그램이 에러로 멈춰버려요.
    # 이런 상황을 대비하는 문법이 try-except 예요.
    # "이걸 해봐. 만약 이런 오류가 나면, 대신 이렇게 해."

    # TODO 3: try-except 블록을 만드세요
    #         try:              ← 이걸 먼저 시도해요
    #             ...           ← TODO 4, 5가 여기 안에 들어가요
    #         except FileNotFoundError:   ← 파일이 없을 때 실행돼요
    #             return []     ← 빈 리스트를 반환해요

    # TODO 4: (try 블록 안에) open()으로 파일을 읽기 모드("r")로 열어보세요

    # TODO 5: (try 블록 안에) readlines()로 모든 줄을 읽어서 반환하세요
    #         힌트: readlines()는 줄 목록을 리스트로 돌려줘요

    pass  # 이 줄을 지우고 코드를 채워보세요!


def display_scores():
    """
    저장된 모든 기록을 출력합니다.
    """
    # TODO 6: load_scores()로 기록을 불러오세요
    #         힌트: scores = load_scores()

    # TODO 7: 기록이 없으면 "아직 기록이 없어요!" 를 출력하세요
    #         힌트: 리스트가 비어있는지 확인하는 법 → if len(scores) == 0:

    # TODO 8: (else 블록에) 기록이 있으면 for문으로 하나씩 출력하세요
    #         힌트: for line in scores:
    #                   print(line, end="")   ← end=""는 줄바꿈을 한 번만 하기 위해서예요
    pass  # 이 줄을 지우고 코드를 채워보세요!
