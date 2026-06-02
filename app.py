# My first app
# Here's our first attempt at using data to create a table:

import streamlit as st
import pandas as pd

# データフレームの作成
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

# データフレームを表示
st.write("Here's the table:")
st.dataframe(df)