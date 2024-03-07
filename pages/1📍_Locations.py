#!/usr/bin/env python3
#
#  streamlit.py
#

import sys

import matplotlib.pyplot as plt
import numpy as np
import time
import streamlit as st

def main():
    #st.set_page_config(layout="wide")
    st.sidebar.info("Select a page above.")

    st.title("Atmospheric mesoscale modeling to simulate annual and seasonal wind speeds for wind energy production in Mexico")
    st.header('Stations and domains locations')

    st.image('imgs/regions.png', caption='Map of stations and domains', use_column_width='auto')

    st.markdown(
    """ffsd

    """)
if __name__ == "__main__":
    main()
