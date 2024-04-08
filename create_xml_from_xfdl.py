import re
import xml.dom.minidom
from xml.etree.ElementTree import Element, ElementTree, SubElement


def extract_ids_and_create_xml(input_path, output_path, start_line):
    # 아이디 값을 저장할 리스트
    ids = []

    with open(input_path, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        # 사용자가 지정한 줄부터 시작하여 파일 끝까지 탐색
        for line in lines[start_line-1:]:
            # <Column id="아이디 값" ... /> 형태의 태그 찾기
            match = re.search(r'<Column id="([^"]+)"', line)
            if match:
                ids.append(match.group(1))
            # 다음 줄이 <Column으로 시작하지 않으면 멈춤
            if not line.strip().startswith('<Column'):
                break

    # Header가 아닌 RECIPE_INFO인 경우
    # root = Element('ROOT')
    # header = SubElement(root, 'RECIPE_INFO')  # HEADER를 SET의 자식으로 추가
    # body = SubElement(root, 'RECIPE_DETAIL_LIST')  # BODY를 SET의 자식으로 추가

    # XML 문서 생성 (Header인 경우)
    root = Element('ROOT')
    set_element = SubElement(root, 'SET')  # SET 태그를 ROOT의 자식으로 추가
    header = SubElement(set_element, 'HEADER')  # HEADER를 SET의 자식으로 추가
    body = SubElement(set_element, 'BODY')  # BODY를 SET의 자식으로 추가

    # 아이디 값으로 요소 추가 (닫히는 태그 포함) 헤더 부분
    # for id_val in ids:
    # id_element = SubElement(header, id_val)
    # id_element.text = None  # text 값을 None으로 설정
    header.text = None

    # 아이디 값으로 요소 추가 (닫히는 태그 포함)
    for id_val in ids:
        id_element = SubElement(body, id_val)
        # 태그 내용을 비워두되, 닫히는 태그를 유지하고 싶을 경우
        id_element.text = None  # text 값을 None으로 설정

    # XML 문서를 문자열로 변환
    rough_string = xml.etree.ElementTree.tostring(root, 'utf-8')

    # 예쁘게 출력하기 위한 처리 및 선언 추가
    reparsed = xml.dom.minidom.parseString(rough_string)
    pretty_xml_str = reparsed.toprettyxml(indent="  ", encoding="UTF-8")

    # 파일로 저장
    with open(output_path, 'wb') as output_file:  # 바이너리 모드로 파일 쓰기
        output_file.write(pretty_xml_str)


# 사용 예시
input_path = '파일경로.xfdl'
output_path = '파일경로.xml'
start_line = '시작라인'

extract_ids_and_create_xml(input_path, output_path, start_line)
