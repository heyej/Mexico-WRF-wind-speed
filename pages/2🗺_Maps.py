#!/usr/bin/env python3
#
#  streamlit.py
#

import sys

import matplotlib.pyplot as plt
import streamlit as st
import iris
import iris.quickplot as qplt
import cartopy.crs as ccrs
import cartopy.feature as cfeat
import cartopy.io.img_tiles as cimgt

@st.cache_data
def load_cube(cube_name):
    cube = iris.load_cube('data/'+cube_name+'_seasons.nc')
    return cube

#@st.cache_data(experimental_allow_widgets=True)
def select_season(_cube, idd):
    season_coord = _cube.coord("season")
    met_seasons = [str(value) for value in season_coord.points]

    seasons = {'djf': 'Winter', 'mam': 'Spring', 'jja': 'Summer', 'son': 'Autumn'}

    st.markdown("##### 3. Select a season:")
    season_name = st.select_slider('label', options=list(map(seasons.get, met_seasons)),
        label_visibility='hidden', key=idd)

    value = [i for i in seasons if seasons[i]==season_name]
    loc_n_season = _cube.extract(iris.Constraint(season=value))

    lats = _cube.coord("latitude").points
    lons = _cube.coord("longitude").points
    return lats, lons, loc_n_season, value

@st.cache_data
def plot_map(lats, lons, _location, season_value):
    fig = plt.figure(figsize=(10,15))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent([lons[0]-1, lons[-1]+1, lats[0]-1, lats[-1]+1])

    #stamen_terrain = cimgt.Stamen(style='terrain')
    #ax.add_image(stamen_terrain, 10)

    gl = ax.gridlines(draw_labels=True, linewidth=1,
        color='gray', alpha=0.5, linestyle='--')
    gl.top_labels = False
    gl.left_labels = False

    ax.add_feature(cfeat.LAKES, alpha=0.5, zorder=-100)
    ax.add_feature(cfeat.COASTLINE, linewidth=0.3)
    ax.add_feature(cfeat.BORDERS, linestyle=':',linewidth=0.3, zorder=100)
    ax.add_feature(cfeat.RIVERS, alpha=0.5)
    ax.add_feature(cfeat.OCEAN, facecolor='lightblue')
    ax.add_feature(cfeat.LAND, facecolor='#CAE4C7')

    qplt.contourf(_location, 10)

    if season_value[0] == 'djf':
        titulo = 'Winter'
    elif season_value[0] == 'mam':
        titulo = 'Spring'
    elif season_value[0] == 'jja':
        titulo = 'Summer'
    else:
        titulo = 'Autumn'
    ax.set_title(titulo)
    st.pyplot(fig, dpi=90)
    plt.close()

def main():
    st.sidebar.title("Navigation")

    st.title("Atmospheric mesoscale modeling to simulate annual and seasonal wind speeds for wind energy production in Mexico")

    st.markdown("##### 1. Select a region:")
    NW, N, NE, C, TVB, T, Y = st.tabs(["Northwest", "North", "Northeast", "Central", "Transvolcanic Belt", "Tehuantepec", "Yucatan"])

    with NW:
        st.markdown("##### 2. Select a station:")
        st_1NW, st_2NW, st_3NW4NW, st_5NW = st.tabs(['1NW', '2NW', '3NW / 4NW', '5NW'])
    with N:
        st.markdown("##### 2. Select a station:")
        st_6N, st_7N, st_8N = st.tabs(['6N', '7N', '8N'])
    with NE:
        st.markdown("##### 2. Select a station:")
        st_9NE, st_10NE = st.tabs(['9NE', '10NE'])
    with C:
        st.markdown("##### 2. Select a station:")
        st_11C, st_12C = st.tabs(['11C', '12C'])
    with TVB:
        st.markdown("##### 2. Select a station:")
        st_13TVB, st_14TVB, st_15TVB, st_16TVB, st_17TVB = st.tabs(['13TVB', '14TVB', '15TVB', '16TVB', '17TVB'])
    with T:
        st.markdown("##### 2. Select a station:")
        st_18T, st_19T, st_20T = st.tabs(['18T', '19T', '20T'])
    with Y:
        st.markdown("##### 2. Select a station:")
        st_21Y, st_22Y = st.tabs(['21Y', '22Y'])



    with st_1NW:
        cube_name = '1NW'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_2NW:
        cube_name = '2NW'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_3NW4NW:
        cube_name = '3NW4NW'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_5NW:
        cube_name = '5NW'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_6N:
        cube_name = '6N'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_7N:
        cube_name = '7N'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_8N:
        cube_name = '8N'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_9NE:
        cube_name = '9NE'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_10NE:
        cube_name = '10NE'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_11C:
        cube_name = '11C'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_12C:
        cube_name = '12C'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_13TVB:
        cube_name = '13TVB'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_14TVB:
        cube_name = '14TVB'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_15TVB:
        cube_name = '15TVB'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_16TVB:
        cube_name = '16TVB'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_17TVB:
        cube_name = '17TVB'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_18T:
        cube_name = '18T'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_19T:
        cube_name = '19T'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_20T:
        cube_name = '20T'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_21Y:
        cube_name = '21Y'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)
    with st_22Y:
        cube_name = '22Y'
        cube = load_cube(cube_name)
        lats, lons, loc_n_season, value = select_season(cube, idd=cube_name)
        plot_map(lats, lons, loc_n_season, value)








if __name__ == "__main__":
    main()
