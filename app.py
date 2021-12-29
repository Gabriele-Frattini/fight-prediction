import streamlit as st
import numpy as np
import pickle
from pathlib import Path

load_model = pickle.load(open('model.pkl', 'rb'))


def predict_fight(wins, losses, draws, opponent_wins, opponent_losses, opponent_draws):
    input = np.array([[wins, losses, draws, opponent_wins,
                     opponent_losses, opponent_draws]]).astype(np.float64)
    prediction = load_model.predict(input)
    return prediction


def main():
    st.title("Predict the result for our fighter")

    wins = st.slider("wins", 1, 70)
    losses = st.slider("losses", 1, 70)
    draws = st.slider("draws", 1, 70)
    opponent_wins = st.slider("opponent wins", 1, 70)
    opponent_losses = st.slider("opponent losses", 1, 70)
    opponent_draws = st.slider("opponent draws", 1, 70)
    ok = st.button("predict")
    if ok:
        output = predict_fight(wins, losses, draws,
                               opponent_wins, opponent_losses, opponent_draws)
        st.subheader(
            f"The predicted result for our fighter is a {output[0].lower()}")


if __name__ == '__main__':
    main()
