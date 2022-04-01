import discord
import asyncio
import random
import openpyxl

from discord import Member
from discord.ext import commands
from urllib.request import urlopen, Request

import urllib
import urllib.request
import bs4
import os
import sys
import json
import time

client = discord.Client()

@client.event
async def on_member_join(member):
    role = ""
    for i in member.server.roles:
        if i.name == "USER":
            role = i
            break
    await client.add_roles(member, role)

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='test', type=1))

@client.event
async def on_message(message):
    if message.content.startswith('!안녕'):
        await client.send_message(message.channel, "안녕하세요")

    if message.content.startswith('!이미지'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]
        print(Text.strip())  # 입력한 명령어

        randomNum = random.randrange(0, 40)  # 랜덤 이미지 숫자

        location = Text
        enc_location = urllib.parse.quote(location)  # 한글을 url에 사용하게끔 형식을 바꿔줍니다. 그냥 한글로 쓰면 실행이 안됩니다.
        hdr = {'User-Agent': 'Mozilla/5.0'}
        # 크롤링 하는데 있어서 가끔씩 안되는 사이트가 있습니다.
        # 그 이유는 사이트가 접속하는 상대를 봇으로 인식하였기 때문인데
        # 이 코드는 자신이 봇이 아닌것을 증명하여 사이트에 접속이 가능해집니다!
        url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=' + enc_location  # 이미지 검색링크+검색할 키워드
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")  # 전체 html 코드를 가져옵니다.
        # print(bsObj)
        imgfind1 = bsObj.find('div', {'class': 'photo_grid _box'})  # bsjObj에서 div class : photo_grid_box 의 코드를 가져옵니다.
        # print(imgfind1)
        imgfind2 = imgfind1.findAll('a', {'class': 'thumb _thumb'})  # imgfind1 에서 모든 a태그 코드를 가져옵니다.
        imgfind3 = imgfind2[randomNum]  # 0이면 1번째사진 1이면 2번째사진 형식으로 하나의 사진 코드만 가져옵니다.
        imgfind4 = imgfind3.find('img')  # imgfind3 에서 img코드만 가져옵니다.
        imgsrc = imgfind4.get('data-source')  # imgfind4 에서 data-source(사진링크) 의 값만 가져옵니다.
        print(imgsrc)
        embed = discord.Embed(
            colour=discord.Colour.green()
        )
        embed.set_image(url=imgsrc)  # 이미지의 링크를 지정해 이미지를 설정합니다.
        await client.send_message(message.channel, embed=embed)  # 메시지를 보냅니다.

    if message.content.startswith('!제비뽑기'):

        channel = message.channel

        embed = discord.Embed(

            title='제비뽑기',

            description='각 번호별로 번호를 지정합니다.',

            colour=discord.Colour.blue()

        )

        embed.set_footer(text='끗')

        Text = ""

        learn = message.content.split(" ")

        vrsize = len(learn)  # 배열크기

        vrsize = int(vrsize)

        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함

            Text = Text + " " + learn[i]

        print(Text.strip())  # 입력한 명령어

        number = int(Text)

        List = []

        num = random.randrange(0, number)

        for i in range(number):

            while num in List:  # 중복일때만

                num = random.randrange(0, number)  # 다시 랜덤수 생성

            List.append(num)  # 중복 아닐때만 리스트에 추가

            embed.add_field(name=str(i + 1) + '번째', value=str(num + 1), inline=True)

        print(List)

        await client.send_message(channel, embed=embed)

    if message.content.startswith('!타이머'):

        Text = ""

        learn = message.content.split(" ")

        vrsize = len(learn)  # 배열크기

        vrsize = int(vrsize)

        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함

            Text = Text + " " + learn[i]

        secint = int(Text)

        sec = secint

        for i in range(sec, 0, -1):

            print(i)

            await client.send_message(message.channel, embed=discord.Embed(description='타이머 작동중 : ' + str(i) + '초'))

            time.sleep(1)



        else:

            print("땡")

            await client.send_message(message.channel, embed=discord.Embed(description='타이머 종료'))

    if message.content.startswith('!실시간검색어') or message.content.startswith('!실검'):

        url = "https://www.naver.com/"

        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")

        realTimeSerach1 = bsObj.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})

        realTimeSerach2 = realTimeSerach1.find('ul', {'class': 'ah_l'})

        realTimeSerach3 = realTimeSerach2.find_all('li')

        embed = discord.Embed(

            title='네이버 실시간 검색어',

            description='실시간검색어',

            colour=discord.Colour.green()

        )

        for i in range(0, 20):
            realTimeSerach4 = realTimeSerach3[i]

            realTimeSerach5 = realTimeSerach4.find('span', {'class': 'ah_k'})

            realTimeSerach = realTimeSerach5.text.replace(' ', '')

            realURL = 'https://search.naver.com/search.naver?ie=utf8&query=' + realTimeSerach

            print(realTimeSerach)

            embed.add_field(name=str(i + 1) + '위', value='\n' + '[%s](<%s>)' % (realTimeSerach, realURL),
                            inline=False)  # [텍스트](<링크>) 형식으로 적으면 텍스트 하이퍼링크 만들어집니다

        await client.send_message(message.channel, embed=embed)

    if message.content.startswith("!날씨"):
        learn= message.content.split(" ")

        location = learn[1]

        enc_location = urllib.parse.quote(location + '날씨')

        hdr = {'User-Agent': 'Mozilla/5.0'}

        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location

        print(url)

        req = Request(url, headers=hdr)

        html = urllib.request.urlopen(req)

        bsObj = bs4.BeautifulSoup(html, "html.parser")

        todayBase = bsObj.find('div', {'class': 'main_info'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})

        todayTemp = todayTemp1.text.strip()  # 온도

        print(todayTemp)

        todayValueBase = todayBase.find('ul', {'class': 'info_list'})

        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})

        todayValue = todayValue2.text.strip()  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌

        print(todayValue)

        todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})

        todayFeelingTemp = todayFeelingTemp1.text.strip()  # 체감온도

        print(todayFeelingTemp)

        todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})

        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})

        todayMiseaMongi3 = todayMiseaMongi2.find('dd')

        todayMiseaMongi = todayMiseaMongi3.text  # 미세먼지

        print(todayMiseaMongi)

        tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})

        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})

        tomorrowTemp2 = tomorrowTemp1.find('dl')

        tomorrowTemp3 = tomorrowTemp2.find('dd')

        tomorrowTemp = tomorrowTemp3.text.strip()  # 오늘 오전,오후온도

        print(tomorrowTemp)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})

        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})

        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})

        tomorrowMoring = tomorrowMoring2.text.strip()  # 내일 오전 온도

        print(tomorrowMoring)

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})

        tomorrowValue = tomorrowValue1.text.strip()  # 내일 오전 날씨상태, 미세먼지 상태

        print(tomorrowValue)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})

        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})

        tomorrowAfter1 = tomorrowAllFind[1]

        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})

        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})

        tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 내일 오후 온도

        print(tomorrowAfterTemp)

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})

        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        print(tomorrowAfterValue)  # 내일 오후 날씨상태,미세먼지

        embed = discord.Embed(

            title=learn[1] + ' 날씨 정보',

            description=learn[1] + '날씨 정보입니다.',

            colour=discord.Colour.gold()

        )

        embed.add_field(name='현재온도', value=todayTemp + '˚', inline=False)  # 현재온도

        embed.add_field(name='체감온도', value=todayFeelingTemp, inline=False)  # 체감온도

        embed.add_field(name='현재상태', value=todayValue, inline=False)  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌

        embed.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)  # 오늘 미세먼지

        embed.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False)  # 오늘날씨 # color=discord.Color.blue()

        embed.add_field(name='**----------------------------------**', value='**----------------------------------**',
                        inline=False)  # 구분선

        embed.add_field(name='내일 오전온도', value=tomorrowMoring + '˚', inline=False)  # 내일오전날씨

        embed.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)  # 내일오전 날씨상태

        embed.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)  # 내일오후날씨

        embed.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False)  # 내일오후 날씨상태

        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!영화순위'):

        # http://ticket2.movie.daum.net/movie/movieranklist.aspx

        i1 = 0  # 랭킹 string값

        embed = discord.Embed(

            title="영화순위",

            description="영화순위입니다.",

            colour=discord.Color.red()

        )

        hdr = {'User-Agent': 'Mozilla/5.0'}

        url = 'http://ticket2.movie.daum.net/movie/movieranklist.aspx'

        print(url)

        req = Request(url, headers=hdr)

        html = urllib.request.urlopen(req)

        bsObj = bs4.BeautifulSoup(html, "html.parser")

        moviechartBase = bsObj.find('div', {'class': 'main_detail'})

        moviechart1 = moviechartBase.find('ul', {'class': 'list_boxthumb'})

        moviechart2 = moviechart1.find_all('li')

        for i in range(0, 20):
            i1 = i1 + 1

            stri1 = str(i1)  # i1은 영화랭킹을 나타내는데 사용됩니다

            print()

            print(i)

            print()

            moviechartLi1 = moviechart2[i]  # ------------------------- 1등랭킹 영화---------------------------

            moviechartLi1Div = moviechartLi1.find('div', {'class': 'desc_boxthumb'})  # 영화박스 나타내는 Div

            moviechartLi1MovieName1 = moviechartLi1Div.find('strong', {'class': 'tit_join'})

            moviechartLi1MovieName = moviechartLi1MovieName1.text.strip()  # 영화 제목

            print(moviechartLi1MovieName)

            moviechartLi1Ratting1 = moviechartLi1Div.find('div', {'class': 'raking_grade'})

            moviechartLi1Ratting2 = moviechartLi1Ratting1.find('em', {'class': 'emph_grade'})

            moviechartLi1Ratting = moviechartLi1Ratting2.text.strip()  # 영화 평점

            print(moviechartLi1Ratting)

            moviechartLi1openDay1 = moviechartLi1Div.find('dl', {'class': 'list_state'})

            moviechartLi1openDay2 = moviechartLi1openDay1.find_all('dd')  # 개봉날짜, 예매율 두개포함한 dd임

            moviechartLi1openDay3 = moviechartLi1openDay2[0]

            moviechartLi1Yerating1 = moviechartLi1openDay2[1]

            moviechartLi1openDay = moviechartLi1openDay3.text.strip()  # 개봉날짜

            print(moviechartLi1openDay)

            moviechartLi1Yerating = moviechartLi1Yerating1.text.strip()  # 예매율 ,랭킹변동

            print(moviechartLi1Yerating)  # ------------------------- 1등랭킹 영화---------------------------

            print()

            embed.add_field(name='---------------랭킹' + stri1 + '위---------------',
                            value='\n영화제목 : ' + moviechartLi1MovieName + '\n영화평점 : ' + moviechartLi1Ratting + '점' + '\n개봉날짜 : ' + moviechartLi1openDay + '\n예매율,랭킹변동 : ' + moviechartLi1Yerating,
                            inline=False)  # 영화랭킹

        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!오늘배그'):

        randomNum = random.randrange(1, 3)

        if randomNum == 1:

            await client.send_message(message.channel, embed=discord.Embed(title="배그각입니다.", color=discord.Color.blue()))

        else:

            await client.send_message(message.channel,
                                      embed=discord.Embed(title="자러갑시다....", color=discord.Color.red()))


    if message.content.startswith('!초대'):
        msg = '{0.author.mention}'.format(message)

        await client.send_message(message.channel, msg)

        channel = message.channel

        embed = discord.Embed(title="서버 들어가기", url="https://discord.gg/BFWDUQe", description="↑서버들어가기", color=0x25a76a)

        embed.set_author(name="SAINC Bot 입니다", icon_url="https://cdn.discordapp.com/attachments/536048659784007711/536070315915214850/Hot_Concrete_Text_Effect_preview.jpg")

        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/536048659784007711/536070315915214850/Hot_Concrete_Text_Effect_preview.jpg")

        await client.send_message(channel, embed=embed)

        await client.send_message(message.channel, "https://discord.gg/BFWDUQe")

    if message.content.startswith('!명령어'):
        channel = message.channel

        embed = discord.Embed(title="ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ", color=0x2d0606)

        embed.set_author(name="SAINC Bot 전용", icon_url = "https://images-ext-1.discordapp.net/external/7bopmZQ6jonvlN90L05AeKE_sX9KG61JR-Uv4sKVSeU/https/cdn.discordapp.com/attachments/536048659784007711/536070315915214850/Hot_Concrete_Text_Effect_preview.jpg")

        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/7bopmZQ6jonvlN90L05AeKE_sX9KG61JR-Uv4sKVSeU/https/cdn.discordapp.com/attachments/536048659784007711/536070315915214850/Hot_Concrete_Text_Effect_preview.jpg")

        embed.add_field(name='!안녕', value='인사를 받아줍니다.', inline=False)

        embed.add_field(name='!날씨 (지역)', value='그 지역의 날씨정보를 제공합니다.', inline=False)

        embed.add_field(name='!초대', value='서버초대 링크를 올려줍니다.', inline=False)

        embed.add_field(name='!오늘배그', value='오늘배그각을 알려줍니다.', inline=False)

        embed.add_field(name='!전적메뉴', value='전적메뉴를 불러옵니다.', inline=False)

        embed.add_field(name='!이미지 (제시어)', value='제시어와관련된 이미지를 올려줍니다.', inline=False)

        embed.add_field(name='!타이머 (초)', value='타이머로 시간을재줍니다.', inline=False)

        embed.add_field(name='!영화순위', value='실시간 영화순위를 올려줍니다.', inline=False)

        embed.add_field(name='!제비뽑기', value='제비뽑기로 순서를 정해줍니다.', inline=False)

        embed.add_field(name='!실시간검색어,!실검', value='실시간검색어를 알려줍니다.', inline=False)

        await client.send_message(channel, embed=embed)

    if message.content.startswith('!실행중'):
        learn = message.content.split(" ")
        text = learn[1]
        await client.change_presence(game=discord.Game(name=text, type=1))
        await client.send_message(message.channel,
                                  embed=discord.Embed(title=text + " 플레이 중으로 변경되었습니다.", color=discord.Color.dark_gold()))


    if message.content.startswith("!전적메뉴"):
        channel = message.channel

        embed = discord.Embed(

            title='SAINC 명령어입니다.',

            description='[도배금지]',

            colour=discord.Colour.purple()

        )

        embed.set_footer(text='모든 전적은 dak.gg 기준입니다.')

        embed.add_field(name='!롤', value='!롤 닉네임 형식으로 적으면 그 닉네임에대한 정보를 알려줍니다..', inline=False)

        embed.add_field(name='!배그솔로', value='!배그솔로 닉네임 형식으로 적으면 그 닉네임에대한 정보를 알려줍니다..', inline=False)

        embed.add_field(name='!배그듀오', value='!배그듀오 닉네임 형식으로 적으면 그 닉네임에대한 정보를 알려줍니다..', inline=False)

        embed.add_field(name='!배그스쿼드', value='!배그스쿼드 닉네임 형식으로 적으면 그 닉네임에대한 정보를 알려줍니다..', inline=False)

        embed.add_field(name='아래파란버튼을 누르면 dak.gg에 들어가집니다.', value='[dak.gg들어가기](https://www.dak.gg/)', inline=False)

        await client.send_message(channel, embed=embed)



    if message.content.startswith("!롤"):

        learn = message.content.split(" ")

        location = learn[1]

        enc_location = urllib.parse.quote(location)

        url = "http://www.op.gg/summoner/userName=" + enc_location

        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")

        rank1 = bsObj.find("div", {"class": "TierRankInfo"})

        rank2 = rank1.find("div", {"class": "TierRank"})

        rank3 = rank2.find("span", {"class": "tierRank"})

        rank4 = rank3.text  # 티어표시 (브론즈1,2,3,4,5 등등)

        print(rank4)

        if rank4 != 'Unranked':
            jumsu1 = rank1.find("div", {"class": "TierInfo"})

            jumsu2 = jumsu1.find("span", {"class": "LeaguePoints"})

            jumsu3 = jumsu2.text

            jumsu4 = jumsu3.strip()  # 점수표시 (11LP등등)

            print(jumsu4)

            winlose1 = jumsu1.find("span", {"class": "WinLose"})

            winlose2 = winlose1.find("span", {"class": "wins"})

            winlose2_1 = winlose1.find("span", {"class": "losses"})

            winlose2_2 = winlose1.find("span", {"class": "winratio"})

            winlose2txt = winlose2.text

            winlose2_1txt = winlose2_1.text

            winlose2_2txt = winlose2_2.text  # 승,패,승률 나타냄  200W 150L Win Ratio 55% 등등

            print(winlose2txt + " " + winlose2_1txt + " " + winlose2_2txt)

        channel = message.channel

        embed = discord.Embed(

            title='롤 정보',

            description='롤 정보입니다.',

            colour=discord.Colour.purple()

        )

        if rank4 == 'Unranked':

            embed.add_field(name='당신의 티어', value=rank4, inline=False)

            embed.add_field(name='-당신은 언랭-', value="언랭은 더이상의 정보는 제공하지 않습니다.", inline=False)

            await client.send_message(channel, embed=embed)



        else:

            embed.add_field(name='당신의 티어', value=rank4, inline=False)

            embed.add_field(name='당신의 LP(점수)', value=jumsu4, inline=False)

            embed.add_field(name='당신의 승,패 정보', value=winlose2txt + " " + winlose2_1txt, inline=False)

            embed.add_field(name='당신의 승률', value=winlose2_2txt, inline=False)

            await client.send_message(channel, embed=embed)



    if message.content.startswith("!배그솔로"):

        learn = message.content.split(" ")

        location = learn[1]

        enc_location = urllib.parse.quote(location)

        url = "https://dak.gg/profile/" + enc_location

        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")

        solo1 = bsObj.find("div", {"class": "overview"})

        solo2 = solo1.text

        solo3 = solo2.strip()

        channel = message.channel

        embed = discord.Embed(

            title='배그솔로 정보',

            description='배그솔로 정보입니다.',

            colour=discord.Colour.purple())

        if solo3 == "No record":

            print("솔로 경기가 없습니다.")

            embed.add_field(name='배그를 한판이라도 해주세요', value='솔로 경기 전적이 없습니다..', inline=False)

            await client.send_message(channel, embed=embed)





        else:

            solo4 = solo1.find("span", {"class": "value"})

            soloratting = solo4.text  # -------솔로레이팅---------

            solorank0_1 = solo1.find("div", {"class": "grade-info"})

            solorank0_2 = solorank0_1.text

            solorank = solorank0_2.strip()  # -------랭크(그마,브론즈)---------

            print("레이팅 : " + soloratting)

            print("등급 : " + solorank)

            print("")

            embed.add_field(name='레이팅', value=soloratting, inline=False)

            embed.add_field(name='등급', value=solorank, inline=False)

            soloKD1 = bsObj.find("div", {"class": "kd stats-item stats-top-graph"})

            soloKD2 = soloKD1.find("p", {"class": "value"})

            soloKD3 = soloKD2.text

            soloKD = soloKD3.strip()  # -------킬뎃(2.0---------

            soloSky1 = soloKD1.find("span", {"class": "top"})

            soloSky2 = soloSky1.text  # -------상위10.24%---------

            print("킬뎃 : " + soloKD)

            print("킬뎃상위 : " + soloSky2)

            print("")

            embed.add_field(name='킬뎃,킬뎃상위', value=soloKD + " " + soloSky2, inline=False)

            # embed.add_field(name='킬뎃상위', value=soloSky2, inline=False)

            soloWinRat1 = bsObj.find("div", {"class": "stats"})  # 박스

            soloWinRat2 = soloWinRat1.find("div", {"class": "winratio stats-item stats-top-graph"})

            soloWinRat3 = soloWinRat2.find("p", {"class": "value"})

            soloWinRat = soloWinRat3.text.strip()  # -------승률---------

            soloWinRatSky1 = soloWinRat2.find("span", {"class": "top"})

            soloWinRatSky = soloWinRatSky1.text.strip()  # -------상위?%---------

            print("승률 : " + soloWinRat)

            print("승률상위 : " + soloWinRatSky)

            print("")

            embed.add_field(name='승률,승률상위', value=soloWinRat + " " + soloWinRatSky, inline=False)

            # embed.add_field(name='승률상위', value=soloWinRatSky, inline=False)

            soloHead1 = soloWinRat1.find("div", {"class": "headshots stats-item stats-top-graph"})

            soloHead2 = soloHead1.find("p", {"class": "value"})

            soloHead = soloHead2.text.strip()  # -------헤드샷---------

            soloHeadSky1 = soloHead1.find("span", {"class": "top"})

            soloHeadSky = soloHeadSky1.text.strip()  # # -------상위?%---------

            print("헤드샷 : " + soloHead)

            print("헤드샷상위 : " + soloHeadSky)

            print("")

            embed.add_field(name='헤드샷,헤드샷상위', value=soloHead + " " + soloHeadSky, inline=False)

            # embed.add_field(name='헤드샷상위', value=soloHeadSky, inline=False)

            await client.send_message(channel, embed=embed)


    if message.content.startswith("!배그듀오"):

        learn = message.content.split(" ")

        location = learn[1]

        enc_location = urllib.parse.quote(location)

        url = "https://dak.gg/profile/" + enc_location

        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")

        duoCenter1 = bsObj.find("section", {"class": "duo modeItem"})

        duoRecord1 = duoCenter1.find("div", {"class": "overview"})

        duoRecord = duoRecord1.text.strip()  # ----기록이없습니다 문구----

        print(duoRecord)

        channel = message.channel

        embed = discord.Embed(

            title='배그듀오 정보',

            description='배그듀오 정보입니다.',

            colour=discord.Colour.purple())

        if duoRecord == 'No record':

            print('듀오 경기가 없습니다.')

            embed.add_field(name='배그를 한판이라도 해주세요', value='듀오 경기 전적이 없습니다..', inline=False)

            await client.send_message(channel, embed=embed)





        else:

            duoRat1 = duoRecord1.find("span", {"class": "value"})

            duoRat = duoRat1.text.strip()  # ----레이팅----

            duoRank1 = duoRecord1.find("p", {"class": "grade-name"})

            duoRank = duoRank1.text.strip()  # ----등급----

            print(duoRank)

            embed.add_field(name='레이팅', value=duoRat, inline=False)

            embed.add_field(name='등급', value=duoRank, inline=False)

            duoStat = duoCenter1.find("div", {"class": "stats"})

            duoKD1 = duoStat.find("div", {"class": "kd stats-item stats-top-graph"})

            duoKD2 = duoKD1.find("p", {"class": "value"})

            duoKD = duoKD2.text.strip()  # ----킬뎃----

            duoKdSky1 = duoStat.find("span", {"class": "top"})

            duoKdSky = duoKdSky1.text.strip()  # ----킬뎃 상위?%----

            print(duoKD)

            print(duoKdSky)

            embed.add_field(name='킬뎃,킬뎃상위', value=duoKD + " " + duoKdSky, inline=False)

            duoWinRat1 = duoStat.find("div", {"class": "winratio stats-item stats-top-graph"})

            duoWinRat2 = duoWinRat1.find("p", {"class": "value"})

            duoWinRat = duoWinRat2.text.strip()  # ----승률----

            duoWinRatSky1 = duoWinRat1.find("span", {"class": "top"})

            duoWinRatSky = duoWinRatSky1.text.strip()  # ----승률 상위?%----

            print(duoWinRat)

            print(duoWinRatSky)

            embed.add_field(name='승률,승률상위', value=duoWinRat + " " + duoWinRatSky, inline=False)

            duoHead1 = duoStat.find("div", {"class": "headshots"})

            duoHead2 = duoHead1.find("p", {"class": "value"})

            duoHead = duoHead2.text.strip()  # ----헤드샷----

            duoHeadSky1 = duoHead1.find("span", {"class": "top"})

            duoHeadSky = duoHeadSky1.text.strip()  # ----헤드샷 상위?%----

            print(duoHead)

            print(duoHeadSky)

            embed.add_field(name='헤드샷,헤드샷상위', value=duoHead + " " + duoHeadSky, inline=False)

            await client.send_message(channel, embed=embed)


    if message.content.startswith("!배그스쿼드"):

        learn = message.content.split(" ")

        location = learn[1]

        enc_location = urllib.parse.quote(location)

        url = "https://dak.gg/profile/" + enc_location

        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")

        duoCenter1 = bsObj.find("section", {"class": "squad modeItem"})

        duoRecord1 = duoCenter1.find("div", {"class": "overview"})

        duoRecord = duoRecord1.text.strip()  # ----기록이없습니다 문구----

        print(duoRecord)

        channel = message.channel

        embed = discord.Embed(

            title='배그스쿼드 정보',

            description='배그스쿼드 정보입니다.',

            colour=discord.Colour.purple())

        if duoRecord == 'No record':

            print('스쿼드 경기가 없습니다.')

            embed.add_field(name='배그를 한판이라도 해주세요', value='스쿼드 경기 전적이 없습니다..', inline=False)

            await client.send_message(channel, embed=embed)



        else:

            duoRat1 = duoRecord1.find("span", {"class": "value"})

            duoRat = duoRat1.text.strip()  # ----레이팅----

            duoRank1 = duoRecord1.find("p", {"class": "grade-name"})

            duoRank = duoRank1.text.strip()  # ----등급----

            print(duoRank)

            embed.add_field(name='레이팅', value=duoRat, inline=False)

            embed.add_field(name='등급', value=duoRank, inline=False)

            duoStat = duoCenter1.find("div", {"class": "stats"})

            duoKD1 = duoStat.find("div", {"class": "kd stats-item stats-top-graph"})

            duoKD2 = duoKD1.find("p", {"class": "value"})

            duoKD = duoKD2.text.strip()  # ----킬뎃----

            duoKdSky1 = duoStat.find("span", {"class": "top"})

            duoKdSky = duoKdSky1.text.strip()  # ----킬뎃 상위?%----

            print(duoKD)

            print(duoKdSky)

            embed.add_field(name='킬뎃,킬뎃상위', value=duoKD + " " + duoKdSky, inline=False)

            duoWinRat1 = duoStat.find("div", {"class": "winratio stats-item stats-top-graph"})

            duoWinRat2 = duoWinRat1.find("p", {"class": "value"})

            duoWinRat = duoWinRat2.text.strip()  # ----승률----

            duoWinRatSky1 = duoWinRat1.find("span", {"class": "top"})

            duoWinRatSky = duoWinRatSky1.text.strip()  # ----승률 상위?%----

            print(duoWinRat)

            print(duoWinRatSky)

            embed.add_field(name='승률,승률상위', value=duoWinRat + " " + duoWinRatSky, inline=False)

            duoHead1 = duoStat.find("div", {"class": "headshots"})

            duoHead2 = duoHead1.find("p", {"class": "value"})

            duoHead = duoHead2.text.strip()  # ----헤드샷----

            duoHeadSky1 = duoHead1.find("span", {"class": "top"})

            duoHeadSky = duoHeadSky1.text.strip()  # ----헤드샷 상위?%----

            print(duoHead)

            print(duoHeadSky)

            embed.add_field(name='헤드샷,헤드샷상위', value=duoHead + " " + duoHeadSky, inline=False)

            await client.send_message(channel, embed=embed)

access_tonken = os.environ["BOT_TOKEN"]           
client.run(access_token)
