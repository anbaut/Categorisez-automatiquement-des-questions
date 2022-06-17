import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
import ast


def main():

    #Import dataset
    df = pd.read_csv("df.csv", sep=',')
    df = df.sample(frac=0.1,random_state=1)
    df = df.reset_index()
    df = df.drop(['index'], axis=1)
    full_text = df["Title"].values + " " + df["Body"].values
    df["full_text"] = df["Title"] + df["Body"]

    

    st.title("Tags prediction")
    menu = ["Content Based prediction"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Content Based prediction":
        st.subheader("Content Based prediction")
        title = st.text_area("Title")
        body = st.text_area("Body")
        if st.button("Predict Tags"):
            full_text = title + " " + body
            print(df)
            df.loc[df.shape[0]] = [title, body,'None','None','None','None','None','None',full_text]

            st.write(full_text)

            post = recommend_tags(df,title,100)
            tags = post.index.tolist()
            st.write(tags[:5])

    else:
        st.subheader("About")

def post_recommend(df,original_title):
    df["full_text"] = df["Title"] + df["Body"]
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
    matrix = tf.fit_transform(df['full_text'])
    cosine_similarities = linear_kernel(matrix,matrix)
    post_title = df['Title']
    indices = pd.Series(df.index, index=df['Title'])
    
    idx = indices[original_title]

    sim_scores = list(enumerate(cosine_similarities[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:31]

    movie_indices = [i[0] for i in sim_scores]

    return df.iloc[movie_indices]

def recommend_tags(df,original_title, sample_size):
    posts = post_recommend(df,original_title).head(sample_size)

    tags = posts["Tags"].apply(ast.literal_eval).apply(lambda x: pd.Series(x)).stack().value_counts()
    return tags

if __name__ == '__main__':
    main()