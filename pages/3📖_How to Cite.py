#!/usr/bin/env python3

import sys

import streamlit as st


def main():
    """
    Print information on how to cite this work.

    """
    st.sidebar.info("""
    ### License
    Atmospheric mesoscale modeling to simulate annual and seasonal wind speeds for wind energy production in Mexico - Dataset © 2024 by J.G. Hernández Yepes, O. Rodríguez-Hernández, C.A. López-Villalobos, O. Martínez-Alvarado is licensed under CC BY-SA 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/
    """)

    st.title(
        "Atmospheric mesoscale modeling to simulate annual and seasonal wind speeds for wind energy production in Mexico"
    )

    st.header('Reference')

    st.markdown('''
        Please cite the data and this webpage with the following reference:
    ''')
    st.markdown('''
        J.G. Hernandez-Yepes, O. Rodriguez-Hernandez, C.A. Lopez-Villalobos, O. Martínez-Alvarado, Atmospheric mesoscale modeling to simulate annual and seasonal wind speeds for wind energy production in Mexico, Sustainable Energy Technologies and Assessments, Volume 68, 2024, 103848, ISSN 2213-1388, https://doi.org/10.1016/j.seta.2024.103848.'''
    )


if __name__ == '__main__':
    sys.exit(main())
