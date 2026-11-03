🔐 Password Strength Checker

A  **Streamlit** web app that evaluates a typed password and classifies it as **Strong**, **Moderate**, or **Weak** based on length and character composition.

## 📌 Project Overview

This project demonstrates:

- Streamlit text input and conditional feedback (`st.success`, `st.warning`, `st.error`)
- String methods: `.islower()`, `.isupper()`, `.isdigit()`
- Character-by-character iteration
- Boolean flag aggregation
- Rule-based classification logic

## ⚙️ How It Works

1. Streamlit renders a single text input for the password.
2. If the password is non-empty, its length is computed.
3. Four boolean flags track whether the password contains:
   - a lowercase letter (`lower`)
   - an uppercase letter (`upper`)
   - a digit (`digit`)
   - a special character (`special`)
4. A rule engine classifies the password:
   - **Strong:** all four types present **and** length ≥ 10
   - **Moderate:** at least one letter **and** (special or digit) **and** length ≥ 6
   - **Weak:** anything else
5. Streamlit shows a coloured banner for the result.

## ▶️ How to Run

```bash
pip install streamlit
streamlit run "complete (2).py"
