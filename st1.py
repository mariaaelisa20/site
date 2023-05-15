import streamlit as st 

st.title("Hello World")

st.write("Aqui é um texto normal")

st.markdown(
  """    
  $$f(x) = x ^2 +1$$
  :smile:
:heart:
"""            
)

arq = st.file_uploader("Escolher um arquivo", type=["png", "jpeg", "mp3"])
if arq:
    st.write(arq.type)
    if arq.type.split("/")[0] == "image":
        st.image(arq, width=300)
    elif arq.type.split("/")[0] == "audio":
        st.audio(arq)
else:
    st.write("Não tem arquivo")