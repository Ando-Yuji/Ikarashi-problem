import streamlit as st
from sympy import isprime

st.title("安藤問題ソルバー")

k = st.number_input("kを入力", min_value=0, value=5)

results = []
for m in range(2*k+2):
    l = 2*k+1-m
    s = 3*l + 5*m
    if isprime(s):
        results.append((l, m, s))

st.write(f"解の個数: {len(results)}")

for l, m, s in results:
    st.write(f"l={l}, m={m}, S={s}")
