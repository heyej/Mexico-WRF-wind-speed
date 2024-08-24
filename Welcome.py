#!/usr/bin/env python3

import sys

import streamlit as st


def main():
    """ """
    #st.set_page_config(layout="wide")
    st.set_page_config(
        page_title="Hello",
        page_icon="👋🏽",
    )

    st.sidebar.info("""
    ### License
    Atmospheric mesoscale modeling to simulate annual and seasonal wind speeds for wind energy production in Mexico - Dataset © 2024 by J.G. Hernández Yepes, O. Rodríguez-Hernández, C.A. López-Villalobos, O. Martínez-Alvarado is licensed under CC BY-SA 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/
    """)

    st.title(
        "Atmospheric mesoscale modeling to simulate annual and seasonal wind speeds for wind energy production in Mexico"
    )

    st.markdown("""
    This work study the reproducibility of wind speed and wind power
    capacity factor by the WRF mesoscale model. Simulations are compared
    with 22 masts of observations with a uniform configuration
    and methodology for a nation-wide analysis.

    The maps present seasonal means of wind speed for the domain of WRF at 1 km resolution.
    
    If you need additional details about simulations or availability of data please reach us at josegus@outlook.com.
    
    ### Contents
    - Distribution of regions and stations.
    - Maps of seasonal wind speeds.
    - How to cite.
    """)


if __name__ == '__main__':
    sys.exit(main())
