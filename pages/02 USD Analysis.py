import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="GSB", page_icon="16.png")
st.image("GSB Medium.png", width=120,)


st.title("GSB USD Analysis System")
components.iframe("https://app.powerbi.com/view?r=eyJrIjoiMWI3YWM1MjUtYjU0Yi00NzVkLWFmNDctNWMxNzVhMTUwZjZhIiwidCI6ImE0NzRkYzY0LTQ1ZDEtNDNkOS05N2FjLWM4NWY0ZDMyZmUwMCIsImMiOjl9", width=800, height=600)