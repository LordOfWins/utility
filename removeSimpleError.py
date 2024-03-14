# 수정전 파일을 가져오기.
with open("c:/Users/Administrator/Downloads/drive-download-20240312T110153Z-001/final_eng_srt/9_5_OnYourOwn en short_240315.srt", "r", encoding='utf-8') as file:
    lines = file.readlines()

# 변경할 내용을 저장할 리스트를 준비합니다.
new_lines = []

# 각 줄을 순회하면서 조건에 맞는 줄의 첫 번째 문자가 공백인지 확인하고, 그렇다면 제거합니다.
for i, line in enumerate(lines, start=1):
    if (i % 4) == 3:  # 실제 자막(타임스탬프x)이 있는 부분의 등차 수열(각 행 번호의 차이로 생기는 규칙)을 활용하여 수정해주세요.
        if line.startswith(' '):  # 자막 앞이 공백으로 시작하는지 확인
            line = line[1:]  # 첫 번째 문자(공백)를 제거
        new_lines.append(line)
    else:
        new_lines.append(line)

# 빈 줄을 제거합니다.
new_lines = [line for i, line in enumerate(new_lines) if i == 0 or line.strip() or new_lines[i - 1].strip()]

# 각 줄을 순회하면서 개행문자 앞의 연속된 '.' 또는 ','를 제거합니다.
for i, line in enumerate(lines):
    while line.rstrip().endswith('.') or line.rstrip().endswith(','):
        line = line.rstrip()[:-1] + line[len(line.rstrip()):]
    lines[i] = new_lines


# 파일에 변경된 내용을 다시 씁니다.
with open("C:/Users/Administrator/Downloads/drive-download-20240312T110153Z-001/final_eng_srt/9_5_OnYourOwn en short_2403152.srt", "w", encoding='utf-8') as file:
    file.writelines(new_lines)
