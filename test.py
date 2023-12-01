! pip install -r requirements.txt

import streamlit as st
import xarray as xr

def main():
        st.title("NetCDF Visualization Example")
    st.header('Test')

    filename = 'wind_global.nc'
    geojson = 'https://github.com/opengeos/leafmap/raw/master/examples/data/countries.geojson'
    m = leafmap.Map(layers_control=True)
    m.add_basemap('CartoDB.DarkMatter')
    #m.add_velocity(filename, zonal_speed='u_wind', meridional_speed='v_wind')
    m.add_netcdf(filename, variables=None, port='default', layer_name='NetCDF layer', shift_lon=True, lat='lat', lon='lon')
    m.to_streamlit()

if __name__ == "__main__":
    main()
