from pathlib import Path

print(f'Current: ', Path(__file__).resolve())
print(f'Parent1: ', Path(__file__).resolve().parent)
print(f'Parent1: ', Path(__file__).resolve().parent.parent)
