import streamlit as st
import pickle
import requests

similarity = pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    movie_index = movie_list_df[movie_list_df['title'] == movie].index[0]
    movie_listed = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_listed:
        #movie_id = movie_list_df.iloc[i[0]].movie_id
        #fetch poster from API
        recommended_movies.append(movie_list_df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_list_df.iloc[i[0]].id))
    return recommended_movies,recommended_movies_posters

def fetch_poster(movie_id):
    response =  requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=6d5022fe0b9fa490c7b004884c7a66b5&language=en-US')
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']


movie_list_df = pickle.load(open('movies.pkl','rb'))
movie_list = movie_list_df['title'].values
st.title("Movie Recommender System")
selected_movie_name = st.selectbox(
    "which movie would you like to select?",
    movie_list
)

if st.button('Recommend') :
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])