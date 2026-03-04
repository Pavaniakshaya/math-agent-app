import streamlit as st
import numpy as np
from numpy.linalg import matrix_rank, pinv

st.title("Math Agent App")

st.write("This app explains Rank and Pseudoinverse.")

rows = st.number_input("Number of rows", min_value=1, value=3)
cols = st.number_input("Number of columns", min_value=1, value=3)

st.write("Enter matrix values row by row (comma separated):")

matrix_input = []

for i in range(rows):
    row = st.text_input(f"Row {i+1}")
    if row:
        matrix_input.append([float(x) for x in row.split(",")])

if len(matrix_input) == rows:

    A = np.array(matrix_input)
    st.write("Matrix A:")
    st.write(A)

    r = matrix_rank(A)
    st.write("Rank =", r)

    A_pinv = pinv(A)
    st.write("Pseudoinverse:")
    st.write(A_pinv)

    P = A @ A_pinv
    st.write("Projection Matrix:")
    st.write(P)

    eigenvalues = np.linalg.eigvals(P)
    st.write("Eigenvalues:")
    st.write(eigenvalues)

    st.write("Zero eigenvalues:",
             np.sum(np.isclose(eigenvalues, 0)))

    st.write("One eigenvalues:",
             np.sum(np.isclose(eigenvalues, 1)))