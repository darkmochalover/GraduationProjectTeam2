import requests
from bs4 import BeautifulSoup
import openai
import json
import pandas as pd
from flask import Flask,render_template,request,redirect, url_for


# OpenAI API 인증
openai.api_key = ''

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('demo.html')

@app.route('/process', methods=['POST'])
def process():
    user_input_1=request.form['input1']
    user_input_2=request.form['input2']
    user_input_3=request.form['input3']
    processed_result = process_input(user_input_1,user_input_2,user_input_3)
    return redirect(url_for('show_result', input1=user_input_1, input2=user_input_2,input3=user_input_3, processed_result=processed_result))

@app.route('/result')
def show_result():
    input1 = request.args.get('input1')
    input2 = request.args.get('input2')
    input3 = request.args.get('input3')
    processed_result = process_input(input1,input2,input3)
    return render_template('new_result.html', input1=input1, input2=input2,input3=input3, processed_result=processed_result)


def process_input(input_data_1,input_data_2,input_data_3):
    # 사용자로부터 입력 받기
    #user_input=input("들어가는 영화 첫번째 제목")
    #user_input_2=input("그 영화에 등장하는 인물")
    #user_input_3=input("배경이 되는 영화")

    #영화 정보 불러오기
    movie_info_1=movieData(input_data_1)
    movie_info_2=movieData(input_data_3)
    print(input_data_1)
    print(input_data_2)
    print(input_data_3)

    # 가져온 정보를 기반으로 챗지피티에게 문장 전달 및 답변 받기
    chat_input = f"{input_data_1}"+"에 등장하는 "+f"{input_data_2}"+"가 "+f"{input_data_3}"+"세계에 들어가면 어떻게 될지에 관한 소설을 적어줘. "+f"{input_data_1}"+"의 줄거리는 "+f"{movie_info_1}"+"이고 "+f"{input_data_3}"+"의 줄거리는 "+f"{movie_info_2}"+"야.\n"
    print(chat_input)
    chat_response = chat_with_gpt3(chat_input)

    # 챗지피티의 답변 출력
    print("챗지피티: ", chat_response)
    return chat_response

def movieData(query):
    key=''
    
    url='http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json.jsp?collection=kmdb_new&detail=Y'
    r=requests.post(url,data={'title':query,'ServiceKey':key,'createDts':'2018','createDts':'2018','val001':'2023','val002':'01'})
    
    movie_data = r.json()
    print(movie_data)
    
    
    max=-1
    
    for h in movie_data['Data'][0]['Result']:
        if max<int(h['runtime']):
            result=h['plot']
            max=int(h['runtime'])
    print(result)
    return result

def chat_with_gpt3(query):
    
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": query}]
)
    return response.choices[0].message.content

def main():
    # 사용자로부터 입력 받기
    user_input=input("들어가는 영화 첫번째 제목")
    user_input_2=input("그 영화에 등장하는 인물")
    user_input_3=input("배경이 되는 영화")

    #영화 정보 불러오기
    movie_info_1=movieData(user_input)
    movie_info_2=movieData(user_input_3)
    

    # 가져온 정보를 기반으로 챗지피티에게 문장 전달 및 답변 받기
    chat_input = f"{user_input}"+"에 등장하는 "+f"{user_input_2}"+"가 "+f"{user_input_3}"+"세계에 들어가면 어떻게 될지에 관한 소설을 적어줘. "+f"{user_input}"+"의 줄거리는 "+f"{movie_info_1}"+"이고 "+f"{user_input_3}"+"의 줄거리는 "+f"{movie_info_2}"+"야.\n"
    chat_response = chat_with_gpt3(chat_input)

    # 챗지피티의 답변 출력
    print("챗지피티: ", chat_response)

if __name__ == "__main__":
    app.run(debug=True)