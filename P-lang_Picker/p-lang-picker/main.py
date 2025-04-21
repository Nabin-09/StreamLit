import streamlit as st
st.title("Programming Language Picker !")
st.write("Choose your favourite programming language : ")

lang = st.selectbox("Your favourite language : ",
  ["Python",
  "JavaScript",
  "C++",
  "Java",
  "Ruby",
  "Go",
  "Swift",
  "PHP",
  "Rust",
  "Kotlin",
  "TypeScript",
  "C#",
  "R",
  "Perl",
  "Scala",
  "Lua",
  "Dart",
  "Haskell",
  "Shell",
  "SQL"])

if lang:
    st.success(f"Your favourite language is {lang}.")


