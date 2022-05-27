from typing import List, Optional
from locust import HttpUser, task, between
import random
import json
from uuid import uuid4
from pydantic.main import BaseModel
from pydantic.networks import HttpUrl
import datetime


# TARGET_URL = "/api/v1/contents/evaluate"
# TARGET_URL = "https://dev-api-argos.emart.com/api/v1/contents/evaluate"
# API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiQVJHT1NfQVBJX0NMSUVOVCIsImV4cCI6MTY2ODg0NjMyOH0.7RMrMZ2AMHxJvcOub_4pvdFzwdYRAzFQ-ncLMaLh_Pk"

# TARGET_URL = "http://localhost:8000/api/v1/contents/evaluate?page_num=1&page_size=1&cond=a&review_type=a&admin_judge=a"
# API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiQVJHT1NfQVBJX0NMSUVOVCIsImV4cCI6MTY2ODg0NDM2Nn0.JRRghUP5DS04duolJDHIiFolttVslGlFGMD5dqBRchs"

# TARGET_URL = "https://dev-api-argos.emart.com/api/v1/contents/evaluate?page_num=1&page_size=1&cond=a&review_type=a&admin_judge=a"
# API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiQVJHT1NfQVBJX0NMSUVOVCIsImV4cCI6MTY2ODg0NjMyOH0.7RMrMZ2AMHxJvcOub_4pvdFzwdYRAzFQ-ncLMaLh_Pk"

# TARGET_URL = "https://stg-api-argos.emart.com/api/v1/contents/evaluate"
# API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiQVJHT1NfQVBJX0NMSUVOVCIsImV4cCI6MTY2ODg0ODE4NX0.uLgtacGLJRA7E948eoT1D-Yg7uPWeE6ij8iPJSNdDWo"


# TARGET_URL = "https://dev-api-argos.emart.com/api/v1/contents/evaluate/text"
# API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiQVJHT1NfQVBJX0NMSUVOVCIsImV4cCI6MTY2ODg0NjMyOH0.7RMrMZ2AMHxJvcOub_4pvdFzwdYRAzFQ-ncLMaLh_Pk"

# TARGET_URL = "http://localhost:8000/api/v1/contents/evaluate/1111"
# API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiQVJHT1NfQVBJX0NMSUVOVCIsImV4cCI6MTY2OTAxNzU0MH0.8UD2iS_DVQfz1XHn7L_jQo2P9aIThLHjSPCsg48X_98"


TARGET_URL = "https://dev-api-argos.emart.com/api/v1/contents/evaluate"
API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiQVJHT1NfQVBJX0NMSUVOVCIsImV4cCI6MTY2ODg0NjMyOH0.7RMrMZ2AMHxJvcOub_4pvdFzwdYRAzFQ-ncLMaLh_Pk"


# TARGET_URL = "http://localhost:8000/api/v1/contents/evaluate"
# API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiQVJHT1NfQVBJX0NMSUVOVCIsImV4cCI6MTY2OTAyMDA1OH0.ULTpz99WoAPbZcDgyBxx3dmL8U1I0h8mR4YxSX_w5qk"


# TARGET_URL = "https://dev-api-argos.emart.com/api/v1/contents/evaluate/8977245d"
# API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiQVJHT1NfQVBJX0NMSUVOVCIsImV4cCI6MTY2ODg0NjMyOH0.7RMrMZ2AMHxJvcOub_4pvdFzwdYRAzFQ-ncLMaLh_Pk"

# TARGET_URL = "http://localhost:8000/api/v1/contents/evaluate/82dfb54f"
# API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiQVJHT1NfQVBJX0NMSUVOVCIsImV4cCI6MTY2OTAyMDA1OH0.ULTpz99WoAPbZcDgyBxx3dmL8U1I0h8mR4YxSX_w5qk"


class HelloWorldUser(HttpUser):
    # wait_time = between(0.5, 2.5)
    # wait_time = between(0.0, 0.1)

    def on_start(self):
        print("start test")

    def on_stop(self):
        print("end test")

    @task
    def post_contents(self):
        auth_header = {"accept": "application/json", "api-token": API_TOKEN}

        json_data = {
            "content_id": uuid4().hex[:8],
            "prdt_cd": "704f7412",
            "prdt_nm": "상품명",
            "review_images": [
                # {
                #     "image_id": uuid4().hex[:8],
                #     "image_url": "https://prd-emartapp-upload.s3.ap-northeast-2.amazonaws.com/review/2022-05-16/2205161335391114/629ebd4e-96c2-4123-94d6-a25cbefce5ca.jpeg",
                # },
                # {
                #     "image_id": uuid4().hex[:8],
                #     "image_url": "https://prd-emartapp-upload.s3.ap-northeast-2.amazonaws.com/review/2022-05-16/2205161338049553/8405bc2b-1045-4343-b1d8-f41aa48c9381.jpg",
                # },
                # {
                #     "image_id": uuid4().hex[:8],
                #     "image_url": "https://picsum.photos/500/500?" + uuid4().hex[:8],
                # },
            ],
            "review_text": "DT본부10 댓글테스트 출발합니다. 한글 데이터 굿입니다. 짜잔 " + uuid4().hex[:8],
        }

        response = self.client.request(
            method="POST",
            url=TARGET_URL,
            headers=auth_header,
            json=json_data,
            timeout=30,
        )

        # response = self.client.request(
        #     method="GET",
        #     url=TARGET_URL,
        #     headers=auth_header,
        #     timeout=30,
        # )

        now = datetime.datetime.now()
        nowStr = now.strftime("%Y-%m-%d %H:%M:%S")

        # f"Registered background task, content_id: {str(item.content_id)}"
        # f"[{nowStr}] req_payload : {str(json_data)} res: {str(response.content)}"

        print(
            "["
            + str(nowStr)
            + "]"
            + str(json_data)
            + " "
            + str(response)
            + " "
            + str(response.content)
        )
