import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Fabのレコメンドアプリ')
st.caption('これはあなたのアプリです')
st.subheader('自己紹介')
st.text('こんにちは！松井渓です')

with st.form(key='profile_form'):

    #テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')

    #　セレクトボックス
    age_category = st.selectbox(
        '年齢層',
        ('子供(18才未満)','大人(18才以上'))
    
    # fab用
    hero = st.selectbox(
        '年齢層',
        ('Arakni','Arakni, Sol','Azalea','Benji, the...','Boltyn','Bravo','Brevant, Ci...','Briar','Dash','Dash, Database','Data Doll MKII'))
    
    # ラジオボタン
    work_category = st.radio(
        '職業',
        ('営業職','企画職','研究職',))
    
    hobby = st.multiselect(
       '趣味',
       ('スポーツ','読書','プログラミング'))

    # ボタン
    submit_btn =st.form_submit_button('送信')
    if submit_btn:
        st.text(f'ようこそ{name}さん！{address}に書籍を送りました！')
        st.text(f'年齢層：{age_category}')
        st.text(f'趣味：{",".join(hobby)}')

# データ分析関連
#df = pd.read_csv('平均気温.csv',index='月')
#st.line_chart(df)
#st.bar_chart(df['2021年'])

#データフレームの表示
df = pd.DataFrame({'col1': [1,2,3]})
df

# グラフの表示
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig