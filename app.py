import streamlit as st
from sympy import primerange, isprime
import pandas as pd

st.title("五十嵐問題ソルバー")

# 入力
n = st.number_input("n を入力", min_value=1, value=3)
max_prime = st.number_input("最大素数 (maxPrime)", min_value=3, value=50)

# 奇素数リスト
primes = [p for p in primerange(3, max_prime + 1)]

# 非減少列を生成（順序なし・重複OK）
def generate_sequences(primes, n, start=0):
    if n == 0:
        return [[]]
    sequences = []
    for i in range(start, len(primes)):
        for rest in generate_sequences(primes, n-1, i):
            sequences.append([primes[i]] + rest)
    return sequences

sequences = generate_sequences(primes, n)

# 素数条件でフィルタ
solutions = []
for seq in sequences:
    s = sum(seq)
    if isprime(s):
        solutions.append(seq + [s])

# 表示
st.write(f"解の個数: {len(solutions)}")

if solutions:
    columns = [f"N{i+1}" for i in range(n)] + ["S"]
    df = pd.DataFrame(solutions, columns=columns)
    st.dataframe(df)
