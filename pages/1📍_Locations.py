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
    st.sidebar.info("""
    ### License
    Atmospheric mesoscale modeling to simulate annual and seasonal wind speeds for wind energy production in Mexico - Dataset © 2024 by J.G. Hernández Yepes, O. Rodríguez-Hernández, C.A. López-Villalobos, O. Martínez-Alvarado is licensed under CC BY-SA 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/
    """)

    st.title("Atmospheric mesoscale modeling to simulate annual and seasonal wind speeds for wind energy production in Mexico")
    st.header('Stations and domains locations')

    st.image('imgs/regions.png', caption='Map of stations and domains', use_column_width='auto')

    st.markdown(
    """ffsd

    """)
if __name__ == "__main__":
    main()
