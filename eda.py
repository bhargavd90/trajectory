import streamlit as st
import plotly.express as px
import pandas as pd
from scipy.cluster.hierarchy import complete, fcluster, single, ward, average
from scipy.spatial.distance import pdist


def plot_data(df: pd.DataFrame) -> None:
    st.header("Data Points")
    df_clustering = df.drop("timestamp", axis=1)
    fig = px.scatter_3d(df_clustering, x='x', y='y', z='depth')
    fig.update_layout({
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
    })
    st.plotly_chart(fig, use_container_width=True)


def plot_clustering(df: pd.DataFrame) -> None:
    st.header("Clustering")
    df_clustering = df.drop("timestamp", axis=1)
    y = pdist(df_clustering)
    Z = single(y)
    df_clustering["labels"] = fcluster(Z, 50, criterion='distance')
    fig = px.scatter_3d(df_clustering, x='x', y='y', z='depth', color="labels")
    fig.update_layout({
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
    })
    st.plotly_chart(fig, use_container_width=True)
    if 'df_clustering' not in st.session_state:
        st.session_state.df_clustering = df_clustering


class EDA:

    # First page

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def eda_app(self):
        st.header("Crowd Analytics")

        column_0_0, column_0_1 = st.columns(2)
        with column_0_0:
            st.subheader("Rows : " + str(self.dataframe.shape[0]))

        with column_0_1:
            st.subheader("Columns : " + str(self.dataframe.shape[1]))

        st.markdown("___")
        column_1_0, column_1_1 = st.columns(2)
        with column_1_0:
            plot_data(self.dataframe)

        with column_1_1:
            plot_clustering(self.dataframe)

        st.markdown("___")

        st.subheader("Tabular data")
        st.markdown("##")
        st.dataframe(self.dataframe)
