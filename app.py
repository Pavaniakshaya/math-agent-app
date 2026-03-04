import streamlit as st
import numpy as np
from numpy.linalg import matrix_rank, pinv

st.set_page_config(page_title="Math Agent App", layout="wide")

st.title("🚀 Math Agent App")
st.subheader("Rank + Pseudoinverse + Projection Explorer")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    rows = st.number_input("Number of Rows", min_value=1, value=3)

with col2:
    cols = st.number_input("Number of Columns", min_value=1, value=3)

st.write("### Enter Matrix Values (comma separated)")

matrix_input = []

for i in range(rows):
    row = st.text_input(f"Row {i+1}")
    if row:
        matrix_input.append([float(x) for x in row.split(",")])

if len(matrix_input) == rows:

    A = np.array(matrix_input)

    st.markdown("## 📊 Matrix")
    st.dataframe(A)

    rank = matrix_rank(A)
    st.success(f"✅ Rank = {rank}")

    A_pinv = pinv(A)

    st.markdown("## 🔄 Pseudoinverse")
    st.dataframe(A_pinv)

    P = A @ A_pinv

    st.markdown("## 🎯 Projection Matrix")
    st.dataframe(P)

    eigenvalues = np.linalg.eigvals(P)

    st.markdown("## 📈 Eigenvalues")
    st.write(eigenvalues)

    st.write("Zero Eigenvalues:",
             np.sum(np.isclose(eigenvalues, 0)))

    st.write("One Eigenvalues:",
             np.sum(np.isclose(eigenvalues, 1)))