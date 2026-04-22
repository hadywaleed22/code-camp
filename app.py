# 1.import streamlit
import streamlit as st 

# 2.converting the files 
home_page = st.Page(page='home.py',title='Home Page',icon='🏡',default=True)
signup_page = st.Page(page='signup.py',title='Sign Up',icon='🔒')
signin_page =st.Page(page='signin.py',title='Sign In',icon='🔑')
menu_page = st.Page(page='menu.py',title='Explore Menu',icon='📝')
chatbot_page = st.Page(page='chatbot.py',title='Talk whith AI ',icon='🙋')

# 3.creating the navbar
all_pages = st.navigation(
pages=[ home_page , signin_page , signup_page , 
       menu_page ,chatbot_page], 
position='top'
)
#4.Run all pages 
all_pages.run()