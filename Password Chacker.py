import streamlit as st
password=st.text_input("Enter your password")

if password:
    pass_len=len(password)

lower = False
upper=False
special=False
digit=False
reg_char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

for char in password:
    
    if char.islower():
            lower=True
    if char.isupper():
                upper=True
    if char.isdigit():
                digit=True
    if char not in reg_char:
                special=True
if lower and upper and digit and special and pass_len>=10:
        st.success("Strong")
elif (lower or upper) and (special or digit) and pass_len>=6:
        st.warning("Moderate")
else:
            st.error("Weak")
