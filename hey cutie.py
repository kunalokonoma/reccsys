
import streamlit as st
import pickle
import pandas as pd


movie_list=pickle.load(open('movie_list.pkl', 'rb'))
movie=pd.DataFrame(movie_list)
st.title("watch what i tell you to")

#option=st.selectbox('just tell me what movie you liked earlier', 'a','b','c', index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")


options=st.selectbox(
    'just tell me what movie you like',
    movie['title'].values
)

similarity=pickle.load(open('similarity.pkl', 'rb'))


def recommend(options):
    def recommend(movie):
        movie_index = movie[movie['title'] == movie].index[0]
        distances = similarity[movie_index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended=[]
        for i in movie_list:
            recommended.append(new.iloc[i[0]].title)
        return recommended


if st.button('Recommend'):
    recommend(options)
    op=recommend(options)
    for i in op:
        st.write(i)