import streamlit as st
import plotly.express as px
import pandas as pd
from scipy.cluster.hierarchy import complete, fcluster, single, ward, average
from scipy.spatial.distance import pdist
from PIL import Image

image = Image.open('second_floor.png')


def plot_data(df: pd.DataFrame) -> None:
    st.header("Data Points")
    df_sub = df[df["labels"] == 5].reset_index()
    fig = px.scatter_3d(df_sub, x='x', y='y', z='depth')
    st.plotly_chart(fig, use_container_width=True)


def plot_clustering(df: pd.DataFrame) -> None:
    st.header("Single Linkage Clustering")
    df_sub = df[df["labels"] == 5].reset_index()
    df_sub.drop(["labels"], inplace=True, axis=1)
    y = pdist(df_sub)
    Z = single(y)
    df_sub["labels"] = fcluster(Z, 47, criterion='distance')
    fig = px.scatter_3d(df_sub, x='x', y='y', z='depth', color="labels")
    st.plotly_chart(fig, use_container_width=True)


def plot_tragectory() -> None:
    st.header("Trajectories")
    st.image(image, use_column_width="auto")



class Secondfloor:

    # First page

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def secondfloor_app(self):
        st.header("First Floor Trajectories")

        column_1_0, column_1_1 = st.columns(2)
        with column_1_0:
            plot_data(st.session_state.df_clustering)

        with column_1_1:
            plot_clustering(st.session_state.df_clustering)

        st.markdown("___")

        plot_tragectory()
