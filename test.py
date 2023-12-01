! pip install -r requirements.txt

import streamlit as st
import xarray as xr

def main():
    st.title("NetCDF Visualization Example")

    # Path to your NetCDF file
    netcdf_path = "SanFernando_seasons.nc"  # Replace with the actual path to your NetCDF file

    # Load the NetCDF file using xarray
    ds = xr.open_dataset(netcdf_path)

    # Display dataset information
    st.write("NetCDF Dataset Information:")
    st.write(ds)

    # Allow the user to select a variable
    selected_variable = st.selectbox("Select a variable:", ds.variables.keys())

    # Display the selected variable as an image
    st.image(ds[selected_variable], caption=f"{selected_variable} Visualization", use_column_width=True)

if __name__ == "__main__":
    main()
