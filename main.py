import pandas as pd
import streamlit as st
from PIL import Image
from eda import EDA
from firstfloor import Firstfloor
from secondfloor import Secondfloor
from combined import Combined
from datetime import datetime
image = Image.open('Ariadne-Maps-GmbH.jpeg')


# https://www.webfx.com/tools/emoji-cheat-sheet/


def do_stuff_on_page_load():
    # To set the page layout to wide on page load
    st.set_page_config(layout="wide")


@st.cache
def get_data(path: str) -> pd.DataFrame:
    # Fetches the data from the given url and returns a dataframe
    dataframe = pd.read_csv(path, header=None)
    dataframe[3] = [datetime.fromtimestamp(x) for x in dataframe[3]]
    dataframe.columns = ["x", "y", "depth", "timestamp"]
    return dataframe


do_stuff_on_page_load()
# st.sidebar.title(":mailbox_closed: Metyis :mailbox_closed:")
st.sidebar.markdown("##")

file_path_main = "centres.csv"

df = get_data(file_path_main)

st.sidebar.image(image, width=200)
plot_type = st.sidebar.radio(
    " ",
    ('EDA', 'First Floor', "Second Floor", "Combined")
)

if plot_type == 'EDA':
    eda = EDA(df)
    eda.eda_app()
elif plot_type == "First Floor":
    first_floor = Firstfloor(df)
    first_floor.firstfloor_app()
elif plot_type == "Second Floor":
    second_floor = Secondfloor(df)
    second_floor.secondfloor_app()
elif plot_type == "Combined":
    combined = Combined(df)
    combined.combined_app()

