# Story Blender

## 목차
[1. 프로젝트 개요](#intro) <br>
[2. 동작 방식](#flow) <br>
[3. 프로젝트 구조](#structure) <br>
[4. 실행 전 요구사항](#requirement) <br>
[5. 실행 방법](#usage) <br>
[6. 예시 실행 결과](#result) <br>

## <span id="intro">프로젝트 개요</span>
드라마, 영화 등 다양한 미디어 매체가 등장하면서 대중들은 단순히 작품을 즐기는 것에서 멈추지 않고 2차 창작을 생산하고 소비하는 팬층 또한 늘게 되었다.
따라서 해당 프로젝트는 ChatGPT를 이용하여 두 작픔을 조합하였을 때의 새로운 이야기를 유저가 즐길 수 있도록 하는 것을 주제로 하였다.

## <span id="flow">동작 방식</span>
1. 다음 세 가지의 입력 값을 받는다. <br>
   1-1. 스토리 A의 제목 <br>
   1-2. 스토리 A의 주인공 이름 <br>
   1-3. 스토리 B의 제목 <br>
2. 앞서 받은 입력 값을 토대로 내부적으로 프롬프트를 생성하여 ChatGPT에 주입
3. 생성한 프롬프트 요약 및 해당 내용을 바탕으로 어울리는 이미지 생성
4. 유저에게 책 페이지 형태로 그림 및 이야기 제공

## <span id="structure">프로젝트 구조</span>
<!-- 해당 부분은 프로젝트 파일 구조가 완전히 확정되면 추가 수정 예정 -->
```text
root
  ㄴ Story_Blender-html
    ㄴ MoverScore
    ㄴ static
    ㄴ templates
    ㄴ drawing_picture.py
    ㄴ movieData.py
    ㄴ new_result.html
  ㄴ README.md
```
- 설명
  - `MoverScore`: 텍스트 맥락 평가 Metric
  - `static`, `templates`: html, cs, js 관련 코드
  - `drawing_picture.py`: 이야기 생성 API 호출 코드
  - `movieData.py`: 영화 데이터 API 호출 코드
  - `new_result.html`: 테스트용 샘플 페이지

## <span id="requirement">실행 전 요구사항</span>
1. 프로젝트 특성 상 다수의 외부 API를 이용하기 때문에, 아래 API를 이용할 수 있도록 개인 키를 발급받아야 합니다. <br>
  - OpenAI API <br>
  - Stable Diffusion <br>
  - CLOVA <br>
  - Papago <br>
2. Python 코드 실행이 가능한 환경이어야 합니다. <br>

## <span id="usage">실행 방법</span>
1. 해당 레포지토리를 git clone을 통해 로컬 환경에 다운로드 <br>
2. 위에서 언급한 외부 API 키를 입력 <br>
3. index.html 실행 <br>

## <span id="result">예시 실행 결과</span>
![image](https://github.com/darkmochalover/GraduationProjectTeam2/assets/77332981/c91e2365-5941-4981-880e-458140b2f660)
