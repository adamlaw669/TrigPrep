import streamlit as st
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

def play_sine():
    keys = list(sine.keys())
    x = int(st.number_input('how many times do you want to practise sines ?', step = 1))
    st.sidebar.write('Practising sine', x, 'times')
    score = 0
    st.sidebar.write('Score:', score)
    for i in range(x):
        key = choice(keys)
        st.write(f'The sine of {key} is ?', end='')
        ans = st.number_input('--->')
        st.write(ans, end= ' ')
        decimal_places = len(ans.split('.')[1]) if '.' in ans else 0
        
        try:
            user_answer = float(ans)
            if user_answer == round(float(sine[key]), decimal_places):
                score += 1
                st.write('✅')
            else:
                st.write('❌') 
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
        ans = st.number_input('--->')
        st.write(ans, end= ' ')
        decimal_places = len(ans.split('.')[1]) if '.' in ans else 0
        
        try:
            user_answer = float(ans)
            if user_answer == round(float(tangent[key]), decimal_places):
                score += 1
                st.write('✅')
            else:
                st.write('❌') 
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
        ans = st.number_input('--->')
        st.write(ans, end= ' ')
        decimal_places = len(ans.split('.')[1]) if '.' in ans else 0
        
        try:
            user_answer = float(ans)
            if user_answer == round(float(cosine[key]), decimal_places):
                score += 1
                st.write('✅')
            else:
                st.write('❌')  
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
