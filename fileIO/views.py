from django.http import HttpResponse
from django.shortcuts import render
from urllib.parse import quote
import os
import pandas as pd
import requests
from io import BytesIO 
from PIL import Image, ImageDraw, ImageFont

# 로컬에 저장된 엑셀 파일 다운로드
def response_excel(request):
    filepath = 'c:/dev/django/hh/file_data/excel.xls'
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse (f, content_type = 'application/vnd.ms-excel')
        encoded_filename = quote(filename)
        response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format (encoded_filename)

    return response

# 엑셀 파일 생성 후 다운로드
def response_excel2(request):
    df = pd.DataFrame([
        [100, 110, 120],
        ['A', 'B', 'C'],
    ])

    io = BytesIO() # 메모리 기반의 파일 객체 지정
    df.to_excel(io) # 파일 카서가 맨 아래에 위치하게 됨
    io.seek(0) # 파일 위치를 처음으로 이동

    encoded_filename = quote('pandas.xlsx')
    response = HttpResponse(io, content_type = 'application/vnd.ms-excel')
    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format (encoded_filename)
    return response

# Pillow 활용하여 이미지 응답 생성하기
def response_pillow_image(request):
    ttf_path = 'c:/Windows/Fonts/malgun.ttf'

    image_url = "https://www.kmart.com.au/wcsstore/Kmart/images/ncatalog/f/8/42269878-1-f.jpg"
    res = requests.get(image_url)
    io = BytesIO(res.content)
    io.seek(0)

    canvas = Image.open(io).convert('RGBA')
    font = ImageFont.truetype(ttf_path, 40)
    draw = ImageDraw.Draw(canvas)

    text = "Duck's Good"
    left, top = 10, 10
    margin = 10
    width,height = font. getsize(text)
    right = left + width + margin
    bottom = top + width + margin
    draw.rectangle((left, top, right, bottom), (255, 255, 224))
    draw.text((15,15), text, font=font, fill=(20, 20, 20))

    response = HttpResponse(content_type= 'image/png') 
    canvas.save(response, format = 'PNG')
    
    return response
    
