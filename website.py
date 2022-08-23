import streamlit as st
import pickle

info = pickle.load(open('info.pkl', 'rb'))
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_list['Series_Title'].values
overview = info['Overview'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommendation")

options = st.selectbox('What would you like to watch', movies_list)
st.write(options)

def overview(text):
    for i in text:
        if i==options:
            index = info[info['Series_Title'] == options].index[0]
            return str(info['Overview'][index])

def recommend(movies):
    movie_index = info[info['Series_Title'] == movies].index[0]
    distances = similarity[movie_index]
    movies_li = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_list = []
    for i in movies_li:
        recommend_list.append(info.iloc[i[0]].Series_Title)
    return recommend_list

if st.button('Info'):
    st.write(overview(info['Series_Title']))
elif st.button('Recommend'):
    re=recommend(options)
    for i in re:
        st.write(i)
