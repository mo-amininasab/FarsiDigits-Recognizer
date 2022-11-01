import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np
import pickle


def rgba2grey(image):
  im = Image.fromarray(image).convert('L')
  im = np.array(im)
  return im


# @st.cache
def load_model(filename):
  with open(filename, 'rb') as file:
    model = pickle.load(file)

  return model


def main():
  st.header('Farsi Digit Recognizer 💯')
  st.subheader('SVC')
  st.text('Draw a Farsi number: ')

  DRAWING_MODE = 'freedraw'
  BG_COLOR = 'black'
  stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 2)

  canvas_result = st_canvas(stroke_color='white',
                            stroke_width=stroke_width,
                            background_color=BG_COLOR,
                            update_streamlit=True,
                            height=32,
                            width=32,
                            drawing_mode=DRAWING_MODE,
                            initial_drawing=None)

  data = canvas_result.image_data

  model = load_model('svc_model.pkl')

  if data is not None:
    data = rgba2grey(data)
    data = data.flatten()
    pred = model.predict([data])
    st.text(pred)


if __name__ == '__main__':
  main()
