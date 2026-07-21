import streamlit as st
import random

# Center the title
st.markdown("<h2 style='text-align: center;'>------------- GUESSING THE NUMBER -------------</h2>", unsafe_allow_html=True)

# Initialize the game variables only once per session
if 'bot' not in st.session_state:
    st.session_state.bot = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.win = False
    st.session_state.game_over = False

st.markdown("**RULES:**\n* There are only five attempts\n* Guessing is between 1 to 100")

# If game is still active
if not st.session_state.game_over:
    user_guess = st.number_input("You:", min_value=1, max_value=100, step=1)
    
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        
        if user_guess == st.session_state.bot:
            st.success("--------------- BINGO --------------\n\n\"YOU WIN\"")
            st.session_state.win = True
            st.session_state.game_over = True
        elif st.session_state.attempts >= 5:
            st.error(f"----- THE GAME IS OVER ------\nTry again\nBOT Guessing---{st.session_state.bot}")
            st.session_state.game_over = True
        elif user_guess < st.session_state.bot:
            st.warning("Guessing is less. Try greater no.")
        else:
            st.warning("Guessing is too high. Try some low.")
            
        # Display attempts left
        if not st.session_state.game_over:
            st.info(f"Attempts used: {st.session_state.attempts} / 5")

# If game is over, show the Try Again button
if st.session_state.game_over:
    if st.button("_____Want to play again? Click Here_____"):
        # Reset the game state
        st.session_state.bot = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.win = False
        st.session_state.game_over = False
        st.rerun()