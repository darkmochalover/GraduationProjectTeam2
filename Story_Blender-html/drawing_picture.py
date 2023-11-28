import json
import requests
import torch
from diffusers import StableDiffusionPipeline

def get_translate(text):
    client_id = ""
    client_secret = ""

    data = {'text': text,
            'source': 'ko',
            'target': 'en'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id": client_id,
              "X-Naver-Client-Secret": client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if (rescode == 200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        print("Error Code:", rescode)


def summary(text):
    client_id = ""
    client_secret = ""
    url = 'https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize'

    headers = {
        'Accept': 'application/json;UTF-8',
        'Content-Type': 'application/json;UTF-8',
        'X-NCP-APIGW-API-KEY-ID': client_id,
        'X-NCP-APIGW-API-KEY': client_secret
    }

    data = {
        "document": {
            "content": text
        },
        "option": {
            "language": "ko",
            "model": "general",
            "tone": 0,
            "summaryCount": 1
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data).encode('UTF-8'))
    rescode = response.status_code
    if (rescode == 200):
        print(response.text)
        return response.text
    else:
        print("Error : " + response.text)
        return "Error"


text = "한 번은 슈퍼마리오의 세계에서 놀던 백설공주가 있었습니다. 그녀는 화려한 성에서 함께 사는 일곱 난장이와 행복한 일상을 보내고 있었습니다. 어느 날, 마리오와 루이지는 백설공주의 세계로 떠나게 " \
       "되었습니다. 처음엔 낯선 세계에 어색함을 느낀 백설공주였지만, 함께 뛰어노는 슈퍼마리오와 루이지의 모습에 빨리 적응하게 되었습니다. 그녀도 슈퍼 파워를 얻어 매우 높이 점프하고 벽을 올라가며 " \
       "재미있게 놀았습니다. 하지만 한가운데 덕분에 걸린 악당이 나타났습니다. 그는 백설공주의 세계를 어지럽히고 평화를 무너뜨리려는 교활한 브라더스입니다. 백설공주와 슈퍼마리오는 힘을 합쳐 이 두 사람의 " \
       "악한 계획을 막기로 결심했습니다. 일곱 난장이들은 각자의 특별한 능력을 발휘하여 슈퍼마리오와 백설공주를 도왔습니다. 화려한 아이템과 슈퍼 파워의 조합으로 브라더스의 함정을 피하고 어려운 미션을 " \
       "해결해 나갔습니다. 계속된 모험 끝에 백설공주와 슈퍼마리오는 브라더스의 악한 계획을 무산시켰습니다. 세계는 다시 한 번 평화롭게 되었고, 백설공주는 일곱 난장이와 함께 새로운 친구들을 얻어 더욱 " \
       "풍요로운 일상을 즐기게 되었습니다. 마리오와 루이지는 돌아가기 전에 백설공주에게 슈퍼마리오 세계의 기술과 문화를 가르쳐주었습니다. 그리고 이제 두 세계의 사람들은 서로를 이해하고 협력하여 새로운 " \
       "세계를 만들어가게 되었습니다. 이후로 백설공주는 슈퍼마리오 세계와 자신의 세계를 오가며 친구들과 함께 모험을 즐기고, 브라더스와 같은 악당들을 상대로 싸우며 두 세계의 평화를 함께 지켜나갔습니다. " \
       "그녀의 용기와 친절한 마음은 어느 세계에서나 사람들에게 희망과 영감을 주었습니다."

if len(text) > 70:
    text = summary(text)

text = get_translate(text)
print(text)


# mac
# pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", revision="fp16", torch_dtype=torch.float16).to("mps")

# window
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", revision="fp16", torch_dtype=torch.float16).to("cpu")

pipe(text).images[0].show()
