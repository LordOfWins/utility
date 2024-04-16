import xml.etree.ElementTree as ET
import re
import xml.dom.minidom

"""
xfdl 파일에서 head 밴드에 있는 아이디 값을 추출하여 txt로 저장하는 코드입니다.
"""
# 레포트가 모여있는 파일 경로
report_path = "C:\\Users\\Administrator\\Desktop\\utility"

# raw_path 이 부분만 Copy Full Path 후 입력해주시면 됩니다.
raw_path = r"C:\eSmartFrameDev-1.0-64bit\workspace\eSMART_ERP_TASK_V1.0\src\main\nxui\pgms\pgmsDyeSendDyestuffsWorkP01.xfdl"

# 파일 경로에서 확장자를 제외한 파일명 추출
file_name = re.search(r"[^\\]*(?=\.\w+$)", raw_path).group()
# 파일 경로에서 패키지명 추출
package_name = re.search(r"[^\\]*(?=\\[^\\]*$)", raw_path).group()
# 파일 경로에서 패키지명을 제외한 나머지 경로 추출
xfdl_path = raw_path.rsplit("\\", 2)[0]

# 입력 경로는 넥사크로 파일 경로
input_path = f"{xfdl_path}\\{package_name}\\{file_name}.xfdl"
# 출력 경로는 레포트 경로에 패키지명과 파일명을 추가하여 생성
output_path = f"{report_path}\\{file_name}.txt"

def extract_ids_and_create_xml(input_path, output_path):
    ids = []

    with open(input_path, 'r', encoding='UTF-8') as file:
        content = file.read()

        # <Band id="head"> 부분 찾기
        body_band_matches = re.finditer(
            r'<Band id="head">([\s\S]*?)</Band>', content)
        for body_band_match in body_band_matches:
            body_band_content = body_band_match.group(1)

        # text="bind:아이디 값"에서 아이디 값 추출
            for match in re.finditer(r'text="([^"]+)"', body_band_content):
                changed_id = match.group(1).replace('&#13;&#10;', ' ')
                ids.append(changed_id)

    # txt문서로 저장
    with open(output_path, 'w', encoding='UTF-8') as file:
        file.write("\n".join(ids))


print(f"output path is {output_path}")

extract_ids_and_create_xml(input_path, output_path)
