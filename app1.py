import streamlit as st
import pandas as pd

view = [100,150,30]
st.write('# Youtube view')
st.write('## Bar chart')
st.bar_chart(view)

sview = pd.Series(view)
sview