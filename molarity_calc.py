import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

from PIL import Image
from scipy.interpolate import PchipInterpolator
from scipy import integrate
from functools import reduce


st.set_page_config(page_title="Molarity calculator", page_icon=":lab_coat:")

st.write("""
# Molarity Calculator
Facilitates concentration calculations.
""")


tab_titles = [
    "Prepare solution",
    "Dilute/concentrate solution",
]
tabs = st.tabs(tab_titles)


with tabs[0]:
    col1_1, col1_2 = st.columns([2, 1], gap="small")
    with col1_1:
        freq = st.text_input(
            "Concentration", value="", help="Enter desired concentration"
        )
    with col1_2:
        freq_units = st.selectbox("", ("M", "%wt", "% v/v", "% w/v"), key="u_freq")

    col2_1, col2_2 = st.columns([2, 1])
    with col2_1:
        freq = st.selectbox("Compounds", ("sodium dodecyl sulfate", "x", "y", "z"), key="u_freq2")

    col3_1, col3_2 = st.columns([2, 1])
    with col3_1:
        freq = st.text_input(
            "Formula weight (molar  mass)", value="", help="Enter desired weight/molar mass"
        )

    col4_1, col4_2 = st.columns([2, 1])
    with col4_1:
        freq = st.text_input(
            "Density", value="", help="Enter desired density"
        )
    with col4_2:
        freq_units = st.selectbox("", ("g/cm^3", "kg/m^3"), key="u_freq3")

    st.markdown(f"$CSC_{{50mV/s}} = {50:.2f}\,uC$")
    st.markdown(f"$CSC_{{200mV/s}} = {50:.2f}\,uC$")


with tabs[1]:
    st.markdown(f"$CSC_{{50mV/s, \, area}} = {50:.2f}\,uC/cm^{2}$")
    st.markdown(f"$CSC_{{200mV/s, \, area}} = {50:.2f}\,uC/cm^{2}$")
