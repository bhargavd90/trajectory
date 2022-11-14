import streamlit as st
import plotly.express as px
import pandas as pd
from scipy.cluster.hierarchy import complete, fcluster, single, ward, average
from scipy.spatial.distance import pdist
from PIL import Image

image = Image.open('images/combined.png')


def plot_data(df: pd.DataFrame) -> None:
    st.header("Data Points")
    df_sub = df.reset_index()
    fig = px.scatter_3d(df_sub, x='x', y='y', z='depth')
    st.plotly_chart(fig, use_container_width=True)


def plot_clustering(df: pd.DataFrame, distance_threshold:int) -> None:
    st.header("Single Linkage Clustering")
    df_sub = df.reset_index()
    df_sub.drop(["labels"], inplace=True, axis=1)
    y = pdist(df_sub)
    Z = single(y)
    df_sub["labels"] = fcluster(Z, distance_threshold, criterion='distance')
    fig = px.scatter_3d(df_sub, x='x', y='y', z='depth', color="labels")
    st.plotly_chart(fig, use_container_width=True)


def plot_tragectory() -> None:
    st.header("Trajectories")
    st.image(image, use_column_width="auto")


class Combined:

    # Third page

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def combined_app(self):
        distance_threshold = st.slider('Distance Threshold', 0, 200, 47)

        column_1_0, column_1_1 = st.columns(2)
        with column_1_0:
            plot_data(st.session_state.df_clustering)

        with column_1_1:
            plot_clustering(st.session_state.df_clustering, distance_threshold)

        st.markdown("___")

        column_2_0, column_2_1 = st.columns(2)
        with column_2_0:
            plot_tragectory()

        with column_2_1:
            st.subheader(" ")
            st.subheader(" ")
            st.subheader(":point_right: Distance Threshold : 47")
            st.subheader(":point_right: Min 5 points in trajectory")
            st.subheader(":point_right: 10 Persons trajectories")

