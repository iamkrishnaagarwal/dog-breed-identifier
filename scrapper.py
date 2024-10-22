import random
import requests
from bs4 import BeautifulSoup
import streamlit as st

def info(breed):
    url = f"https://www.akc.org/dog-breeds/{breed}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    paragraphs = soup.find(class_="share-modal__content-inner mt3")
    return(paragraphs.text)

def name(gender):
    if gender == "Male":
        url = "https://www.akc.org/expert-advice/lifestyle/top-100-boy-dog-names"
    if gender == "Female":
        url = "https://www.akc.org/expert-advice/lifestyle/top-100-girl-dog-names"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    names = soup.find('tbody').get_text()
    temp = names.strip().split("\n\n")
    temp = "".join(temp)
    temp = temp.split("\n")
    lst = list(temp)
    return random.choices(lst, k=10)


def stats(breed):
    info = []
    url = f"https://dogtime.com/dog-breeds/{breed}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs1 = soup.find_all('h6', class_="breed-statistics-title")
    paragraphs2 = soup.find_all('h5', class_="breed-statistics-description")
    for i, j in zip(paragraphs1[1:], paragraphs2[1:]):
        st.write(f"*{i.text}*:")
        st.write(j.text)

# def stats(breed):
#     info = []
#     url = f"https://dogtime.com/dog-breeds/{breed}"
#     st.write(url)
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     paragraphs = soup.find('div', class_="breed-vital-stats-wrapper")
#     para = str(paragraphs).split('</div>')
#     for i in range(1,8,2):
#         info.append(para[i])
#     return info