import streamlit as st
from PIL import Image, ImageDraw, ImageFont


def text_on_image(image, text, color, font_size):
    img = Image.open(image)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", font_size)
    draw.text((0, 0), text, fill=color, font=font)
    #st.image(image, width=300)
    img.save("image.png")
    return img


image = st.file_uploader("Escolhe uma imagem", type=["png", "jpeg", "jpg"])

text = st.text_input("Escreve um texto")

color = st.selectbox("Escohe uma cor", ["red", "green", "blue", "purple"])
# st.write(color)
font_size = st.slider("Escolhe o tamanho da fonte", 10, 100, 20)

if image:
    # st.image(image, width=300)
    result = st.button(
    
        "Gerar uma marca dàgua",
        type='primary',
        help="Clique para gerar uma marca dàgua",
        on_click=text_on_image,
        args=(image, text, color, font_size),
    )
    st.write(result)
    if result:
        st.image("image.png", width=300)
        with open("image.png", "rb") as file:
            st.download_button("Baixar imagem", file.read(), mime="image/png")
