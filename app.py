import streamlit as st
import numpy as np
import pickle
from pathlib import Path
from PIL import Image

img = Image.open("boxing_winner.jpg")
load_model = pickle.load(open('model.pkl', 'rb'))


def predict_fight(draws, losses, wins, opponent_wins, opponent_losses, opponent_draws, Height_Difference):
    input = np.array([[draws, losses, wins, opponent_wins,
                     opponent_losses, opponent_draws, Height_Difference]]).astype(np.float64)
    prediction = load_model.predict(input)
    return prediction


def main():
    st.title("Predict the result for our fighter")

    wins = st.slider("Wins", 1, 70,10)
    losses = st.slider("Losses", 1, 70,10)
    draws = st.slider("Draws", 1, 70,10)
    height = st.slider("Height",150,220,175)
    opponent_wins = st.slider("Opponent wins", 1, 70,10)
    opponent_losses = st.slider("Opponent losses", 1, 70,10)
    opponent_draws = st.slider("Opponent draws", 1, 70,10)
    height_opponent = st.slider("Opponent height",150,220,175)
    ok = st.button("Predict result")
    if ok:
        output = predict_fight(draws, losses, wins,
                               opponent_wins, opponent_losses, opponent_draws, (height-height_opponent))
        st.subheader(
            f"The predicted result for our fighter is a {output[0].lower()}")

st.image(img)

if __name__ == '__main__':
    main()
