import pickle
import streamlit as st
import requests
import bz2file as bz2

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=aef03f80b5cf97bfe329fbc07cba5171&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    movie = movie.lower()
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    cast = []
    overview = []
    crew = []
    genres = []
    vote = []


    for i in distances[0:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        cast.append(movies.iloc[i[0]].cast)
        overview.append(movies.iloc[i[0]].overview)
        crew.append(movies.iloc[i[0]].crew)
        genres.append(movies.iloc[i[0]].genres)
        vote.append(movies.iloc[i[0]].vote_average)


    return recommended_movie_names,recommended_movie_posters,cast,overview,crew,genres,vote

st. set_page_config(layout="wide")
st.header('Movie Recommender System')
#movies = pickle.load(open('movie_list.pkl','rb'))
#similarity = pickle.load(open('similarity.pkl','rb'))
def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = pickle.load(data)
    return data
movies = decompress_pickle('movie_list.pbz2')

similarity = decompress_pickle('similarity.pbz2')



movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)
import base64
def backgroundImage(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
backgroundImage('image.jpg')


if st.button('Search'):
    recommended_movie_names,recommended_movie_posters,cast,overview,crew,genres,vote = recommend(selected_movie)

    col0, col1 = st.columns(2,gap='medium')
    with col0:
        st.image(recommended_movie_posters[0],use_column_width='auto')
    with col1:
        st.header(f'Title: {recommended_movie_names[0].title()}')
        st.subheader(f'Overview : {overview[0]}')
        st.subheader(f'Cast: {",  ".join(map(str,cast[0]))}')
        st.subheader(f'Director: {" ".join(map(str,crew[0]))}')
        st.subheader(f'Genres:  {", ".join(map(str,genres[0]))}')
        st.subheader(f'Vote: {vote[0]}/10')
    col33, col44, col55 = st.columns(3,gap='medium')
    with col33:
        pass
    with col44:
        st.header("Recommended Movies")
    with col55:
        pass

    col2, col3, col4, col5,col6= st.columns(5,gap='medium')
    col7, col8, col9, col10, col11 = st.columns(5,gap='medium')

    with col2:
        st.image(recommended_movie_posters[1],width=200)
        st.subheader(recommended_movie_names[1].title())

    with col3:
        st.image(recommended_movie_posters[2],width=200)
        st.subheader(recommended_movie_names[2].title())
    with col4:
        st.image(recommended_movie_posters[3],width=200)
        st.subheader(recommended_movie_names[3].title())
    with col5:
        st.image(recommended_movie_posters[4],width=200)
        st.subheader(recommended_movie_names[4].title())
    with col6:
        st.image(recommended_movie_posters[5],width=200)
        st.subheader(recommended_movie_names[5].title())

    with col7:
        st.image(recommended_movie_posters[6],width=200)
        st.subheader(recommended_movie_names[6].title())

    with col8:
        st.image(recommended_movie_posters[7],width=200)
        st.subheader(recommended_movie_names[7].title())
    with col9:
        st.image(recommended_movie_posters[8],width=200)
        st.subheader(recommended_movie_names[8].title())
    with col10:
        st.image(recommended_movie_posters[9],width=200)
        st.subheader(recommended_movie_names[9].title())
    with col11:
        st.image(recommended_movie_posters[10],width=200)
        st.subheader(recommended_movie_names[10].title())








