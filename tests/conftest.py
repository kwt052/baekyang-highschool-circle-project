# tests/conftest.py
import os
import sys

# 프로젝트 루트를 Python 경로에 추가 (quiz, data, score import 가능하게)
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# 테스트가 항상 프로젝트 루트에서 실행되도록 설정
# (questions.json, scores.txt 상대경로가 올바르게 동작하게)
os.chdir(os.path.dirname(os.path.dirname(__file__)))
