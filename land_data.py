# import streamlit as st
# import requests
# import pandas as pd

# # 세션 상태에서 데이터 관리 (데이터를 여러 번 새로고침해도 유지할 수 있도록)
# if "articles" not in st.session_state:
#     st.session_state["articles"] = []

# # 쿠키 및 헤더 설정
# cookies = {
#     'NNB': 'NFPCMMVQY6YGM',
#     'NFS': '2',
#     'NID_AUT': 'd3l4gUH1rLkXEaOhWjZEzCVUHnQ0eq+8z3N7HQwNjhapXzKFfdxFxecyhKjtORpm',
#     'NID_JKL': 'LThkbDDeK8VJUDaFoaJZrA9fSf6mmSm/hR7+THUGUzk=',
#     'NAC': 'GDfuDwg5LkY4A',
#     '_fwb': '248RSCYlRjzaAgBuZrAOuGR.1735994273417',
#     'landHomeFlashUseYn': 'Y',
#     '_fwb': '248RSCYlRjzaAgBuZrAOuGR.1735994273417',
#     'NACT': '1',
#     'NID_SES': 'AAABnAvn/nUKYdGeBWOT1wK4CSepokl8krNb1SNiTi7RE+FuTkyaz+E6C3S5uVY2FpMIV5hW0SnyMF1rj1hJdRhyqqjVF0SvLyESK7Rl+DwmjcjziKn/JwEXGtPkuvRZBDAE14cQ0jp5/D5wjA79riek61gDXx/R/4JP2/Eqov6HPS/gdHyItOufcXRLJOqNY/fKtVcF1fzafdU+nYo9DHnldDEAD1xVx5iENgdKzy2B7uCQDUBXa75ApuxtOIsbi401zfiKRumyJFvquEim6P+1hAsyeiYQ05r6bRSE0LZX3e7pybE2Lx1+FFdHtVNugCGucPp979agK4ixSL8nEqpg555nqP/ZyAenYkBZW0nF8ERk35rcct57aA5WCC4GwV5kMVn5mGjXCw1iMFt67ltDNCFbVdm4fquFn1hMZyboRpmeuwl2yafjI/rAan46ylufL9Vd97TXyjPuRXSzlTSqwTwZ7EJvqpC1+mLtxM8Rqq1j3KyzdgQu31YSriRkhar/DyxKeS0+kWTxm3Q8TCKBC8L7vAwJl7MYD0vraCkj/HKb',
#     'nhn.realestate.article.rlet_type_cd': 'A01',
#     'nhn.realestate.article.trade_type_cd': '""',
#     'SRT30': '1736914896',
#     'SRT5': '1736914896',
#     'REALESTATE': 'Wed%20Jan%2015%202025%2013%3A21%3A55%20GMT%2B0900%20(Korean%20Standard%20Time)',
#     'BUC': 'h9AhtLFq4q5RHYh5CKQeHxv-lNQPs9jQ8EsYcolPAp4=',
# }

# headers = {
#     'accept': '*/*',
#     'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh;q=0.5,zh-CN;q=0.4,zh-TW;q=0.3,zh-HK;q=0.2',
#     'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3MzY5MTQ5MTUsImV4cCI6MTczNjkyNTcxNX0.IXqL3q0NucHHms1INKoMimJXeFW93gPq3t-Gs-ypCBg',
#     'priority': 'u=1, i',
#     'referer': 'https://new.land.naver.com/complexes/117329?ms=37.5156552,126.8392419,16&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&h=99&i=132&ad=true',
#     'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
# }

# def fetch_data():
#     """1~10 페이지 데이터를 수집하여 리스트로 반환"""
#     all_articles = []
#     for page in range(1, 11):
#         url = (
#             'https://new.land.naver.com/api/articles/complex/117329'
#             '?realEstateType=APT%3AABYG%3AJGC%3APRE'
#             '&tradeType=A1'
#             '&tag=%3A%3A%3A%3A%3A%3A%3A%3A'
#             '&rentPriceMin=0'
#             '&rentPriceMax=900000000'
#             '&priceMin=0'
#             '&priceMax=900000000'
#             '&areaMin=0'
#             '&areaMax=900000000'
#             '&oldBuildYears'
#             '&recentlyBuildYears'
#             '&minHouseHoldCount'
#             '&maxHouseHoldCount'
#             '&showArticle=false'
#             '&sameAddressGroup=true'
#             '&minMaintenanceCost'
#             '&maxMaintenanceCost'
#             '&priceType=RETAIL'
#             '&directions='
#             f'&page={page}'
#             '&complexNo=117329'
#             '&buildingNos='
#             '&areaNos=15%3A17%3A16%3A18%3A21%3A20%3A19%3A23%3A24%3A22%3A28%3A29%3A25%3A26%3A27%3A30'
#             '&type=list'
#             '&order=rank'
#         )

#         response = requests.get(url, cookies=cookies, headers=headers)
#         if response.status_code == 200:
#             data = response.json()
#             if 'articleList' in data:
#                 article_list = data['articleList']
#                 for article in article_list:
#                     row_data = {
#                         "articleNo": article.get("articleNo", ""),
#                         "articleName": article.get("articleName", ""),
#                         "tradeTypeName": article.get("tradeTypeName", ""),
#                         "dealOrWarrantPrc": article.get("dealOrWarrantPrc", ""),
#                         "areaName": article.get("areaName", ""),
#                         "area1": article.get("area1", ""),
#                         "area2": article.get("area2", ""),
#                         "articleFeatureDesc": article.get("articleFeatureDesc", ""),
#                         "buildingName": article.get("buildingName", ""),
#                         "sameAddrCnt": article.get("sameAddrCnt", ""),
#                         "sameAddrMaxPrc": article.get("sameAddrMaxPrc", ""),
#                         "sameAddrMinPrc": article.get("sameAddrMinPrc", ""),
#                         "direction": article.get("direction", ""),
#                         "realtorName": article.get("realtorName", ""),
#                     }
#                     all_articles.append(row_data)
#         else:
#             st.warning(f"{page}페이지 요청 실패 (status code: {response.status_code})")
#     return all_articles

# # ----------------------
# # Streamlit 웹페이지 구성
# # ----------------------

# st.title("부동산 매물 조회 (Streamlit)")
# st.write("1~10페이지 매물 정보를 수집하여 화면에 표시하고, CSV 다운로드 기능을 제공합니다.")

# # "데이터 수집" 버튼
# if st.button("데이터 수집"):
#     st.session_state["articles"] = fetch_data()
#     st.success("데이터 수집이 완료되었습니다!")

# # 데이터가 있을 경우 테이블 표시 및 CSV 다운로드
# if st.session_state["articles"]:
#     df = pd.DataFrame(st.session_state["articles"])
    
#     st.subheader("매물 정보 테이블")
#     st.dataframe(df, use_container_width=True)
    
#     # CSV로 변환
#     csv_data = df.to_csv(index=False, encoding="utf-8-sig")
    
#     # 다운로드 버튼
#     st.download_button(
#         label="CSV 다운로드",
#         data=csv_data,
#         file_name="land_data.csv",
#         mime="text/csv"
#     )


import streamlit as st
import requests
import pandas as pd

# Streamlit 세션 상태에서 데이터를 보관
if "article_data" not in st.session_state:
    st.session_state["article_data"] = []

# 쿠키 / 헤더 설정 (질문에서 주어진 예시값)
cookies = {
    'NNB': 'NFPCMMVQY6YGM',
    'NFS': '2',
    'NID_AUT': 'd3l4gUH1rLkXEaOhWjZEzCVUHnQ0eq+8z3N7HQwNjhapXzKFfdxFxecyhKjtORpm',
    'NID_JKL': 'LThkbDDeK8VJUDaFoaJZrA9fSf6mmSm/hR7+THUGUzk=',
    'NAC': 'GDfuDwg5LkY4A',
    '_fwb': '248RSCYlRjzaAgBuZrAOuGR.1735994273417',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '248RSCYlRjzaAgBuZrAOuGR.1735994273417',
    'NACT': '1',
    'NID_SES': 'AAABnAvn/nUKYdGeBWOT1wK4CSepokl8krNb1SNiTi7RE+FuTkyaz+E6C3S5uVY2FpMIV5hW0SnyMF1rj1hJdRhyqqjVF0SvLyESK7Rl+DwmjcjziKn/JwEXGtPkuvRZBDAE14cQ0jp5/D5wjA79riek61gDXx/R/4JP2/Eqov6HPS/gdHyItOufcXRLJOqNY/fKtVcF1fzafdU+nYo9DHnldDEAD1xVx5iENgdKzy2B7uCQDUBXa75ApuxtOIsbi401zfiKRumyJFvquEim6P+1hAsyeiYQ05r6bRSE0LZX3e7pybE2Lx1+FFdHtVNugCGucPp979agK4ixSL8nEqpg555nqP/ZyAenYkBZW0nF8ERk35rcct57aA5WCC4GwV5kMVn5mGjXCw1iMFt67ltDNCFbVdm4fquFn1hMZyboRpmeuwl2yafjI/rAan46ylufL9Vd97TXyjPuRXSzlTSqwTwZ7EJvqpC1+mLtxM8Rqq1j3KyzdgQu31YSriRkhar/DyxKeS0+kWTxm3Q8TCKBC8L7vAwJl7MYD0vraCkj/HKb',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'SRT30': '1736914896',
    'SRT5': '1736914896',
    'REALESTATE': 'Wed%20Jan%2015%202025%2013%3A21%3A55%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'BUC': 'h9AhtLFq4q5RHYh5CKQeHxv-lNQPs9jQ8EsYcolPAp4=',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh;q=0.5,zh-CN;q=0.4,zh-TW;q=0.3,zh-HK;q=0.2',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3MzY5MTQ5MTUsImV4cCI6MTczNjkyNTcxNX0.IXqL3q0NucHHms1INKoMimJXeFW93gPq3t-Gs-ypCBg',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/117329?ms=37.5156552,126.8392419,16&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&h=99&i=132&ad=true',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}


def fetch_article_data(page: int):
    """
    해당 page 번호에 맞춰 네이버 부동산 API를 호출, JSON 응답을 반환합니다.
    """
    url = (
        "https://new.land.naver.com/api/articles/complex/117329"
        "?realEstateType=APT%3AABYG%3AJGC%3APRE"
        "&tradeType=A1"
        "&tag=%3A%3A%3A%3A%3A%3A%3A%3A"
        "&rentPriceMin=0"
        "&rentPriceMax=900000000"
        "&priceMin=0"
        "&priceMax=900000000"
        "&areaMin=0"
        "&areaMax=900000000"
        "&oldBuildYears"
        "&recentlyBuildYears"
        "&minHouseHoldCount"
        "&maxHouseHoldCount"
        "&showArticle=false"
        "&sameAddressGroup=true"
        "&minMaintenanceCost"
        "&maxMaintenanceCost"
        "&priceType=RETAIL"
        "&directions="
        f"&page={page}"  # 페이지 번호 삽입
        "&complexNo=117329"
        "&buildingNos="
        "&areaNos=15%3A17%3A16%3A18%3A21%3A20%3A19%3A23%3A24%3A22%3A28%3A29%3A25%3A26%3A27%3A30"
        "&type=list"
        "&order=rank"
    )
    resp = requests.get(url, headers=headers, cookies=cookies)
    if resp.status_code == 200:
        return resp.json()
    else:
        st.error(f"요청 실패(HTTP {resp.status_code}) / page={page}")
        return None


st.title("네이버 부동산 1~10페이지 매물 조회 (Streamlit)")

if st.button("데이터 수집하기"):
    all_articles = []
    for page_num in range(1, 11):
        data = fetch_article_data(page_num)
        if data and "articleList" in data:
            all_articles.extend(data["articleList"])
        else:
            st.warning(f"{page_num}페이지: articleList 없음 또는 응답 실패")

    st.session_state["article_data"] = all_articles
    st.success(f"총 {len(all_articles)}건의 매물을 수집했습니다.")

# 수집된 데이터가 있다면 화면에 표시
if st.session_state["article_data"]:
    df = pd.DataFrame(st.session_state["article_data"])
    
    st.subheader("매물 정보 (1~10페이지 취합)")
    st.dataframe(df, use_container_width=True)

    # CSV 변환 및 다운로드 버튼
    csv_data = df.to_csv(index=False, encoding="utf-8-sig")
    st.download_button(
        label="CSV 다운로드",
        data=csv_data,
        file_name="real_estate_all_pages.csv",
        mime="text/csv"
    )
