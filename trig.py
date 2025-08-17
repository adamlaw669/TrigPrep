import streamlit as st
import math
from random import choice
sine = { 0: 0,
        30: 1/2,
        45: 1/(2**(1/2)),
        60: (3**(1/2))/2,
        90: 1
        }

cosine = { 0: 1,
          30: (3**(1/2))/2,
          45: 1/(2**(1/2)),
          60: 1/2,
          90: 0
          }

tangent = {0: 0,
          30: 1/(3**(1/2)),
          45: 1,
          60: (3**(1/2)),
          90: 0.000000
          }

#defining an helper function to help with the rounding for comparism
def truncate_float(value, decimal):
    factor = 10**decimal
    return float(math.floor(value*factor)/factor)


def play_sine():
    keys = list(sine.keys())
    x = int(st.number_input('how many times do you want to practise sines ?', step = 1))
    st.sidebar.write('Practising sine', x, 'times')
    score = 0
    st.sidebar.write('Score:', score)
    for i in range(x):
        key = choice(keys)
        st.write(f'The sine of {key} is ?', end='')
        ans = st.number_input('',key = f'sine_input_{i}')
        decimal_places = len(str(ans).split('.')[1]) if '.' in str(ans) else 1
        
        try:
            user_answer = float(ans)
            if user_answer ==  truncate_float(float(sine[key]), decimal_places):
                score += 1
                st.info('Correct❕')
            else:
                st.info(f'Wrong❗ The correct answer is {sine[key]}')
        except ValueError:
            print('Invalid input. Please enter a numeric value.')
    
    st.sidebar.write(f'Your score: {score}/{x}')
    
    
def play_tan():
    keys = list(tangent.keys())
    x = int(st.number_input('how many times do you want to practise tangents ?', step = 1))
    st.sidebar.write('Practising tangents', x, 'times')
    score = 0
    st.sidebar.write('Score:', score)
    for i in range(x):
        key = choice(keys)
        st.write(f'The tangent of {key} is ?', end=' ')
        ans = st.number_input('', key = f'tan_input_{i}')
        st.write(ans, end= ' ')
        decimal_places = len(str(ans).split('.')[1]) if '.' in str(ans) else 1
        
        try:
            user_answer = float(ans)
            if user_answer == truncate_float(float(tangent[key]), decimal_places):
                score += 1
                st.info('Correct❕')
            else:
                st.info(f'Wrong❗ The correct answer is {tangent[key]}')
        except ValueError:
            print('Invalid input. Please enter a numeric value.')
    
    st.sidebar.write(f'Your score: {score}/{x}')
    
    
def play_cos():
    keys = list(cosine.keys())
    x = int(st.number_input('how many times do you want to practise cosines ?', step = 1))
    st.sidebar.write('Practising cosines', x, 'times')
    score = 0
    st.sidebar.write('Score:', score)
    for i in range(x):
        key = choice(keys)
        print(f'The cosine of {key} is ?', end=' ')
        ans = st.number_input('', key = f'cos_input_{i}')
        st.write(ans, end= ' ')
        decimal_places = len(str(ans).split('.')[1]) if '.' in str(ans) else 1
        
        try:
            user_answer = float(ans)
            if user_answer == truncate_float(float(cosine[key]), decimal_places):
                score += 1
                st.info('Correct❕')
            else:
                st.info(f'Wrong❗ The correct answer is {cosine[key]}') 
        except ValueError:
            print('Invalid input. Please enter a numeric value.')
    
    st.sidebar.write(f'Your score: {score}/{x}')
    


st.title('Trigonometry Practice')
st.button('Start Practice')
st.sidebar.title('Practice Options')
st.sidebar.markdown('How many times do you want to practice?')
progress_bar = st.sidebar.progress(0)
st.sidebar.markdown('Choose a trigonometric function to practice:')
practice_options = st.selectbox('Choose a trigonometric function to practice:',['Sine', 'Tangent', 'Cosine'])
if practice_options == 'Sine':
        play_sine()
        progress_bar.progress(100)
elif practice_options == 'Tangent':
        play_tan()
        progress_bar.progress(100)
elif practice_options == 'Cosine':
        play_cos()
        progress_bar.progress(100)


