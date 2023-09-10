import random
import reflex as rx
import requests

class MyState(rx.State):
    quote = ''
    author = ''
    def get_quote(self):
        url = 'https://type.fit/api/quotes'
        res = requests.get(url)
        data = res.json()
        rand_num = random.randrange(0,len(data))
        self.quote = data[rand_num]['text']
        self.author = data[rand_num]['author']
        

def header():
    return rx.responsive_grid(
        rx.center(
            rx.box(
                rx.heading('Soy Walter!!!', size='xl'),
                rx.heading('Desarrollador Python', size='lg'),                
            )
        ),
        rx.center(
            rx.image(src='/python.png')
        ),
        rx.center(
            rx.box(
                rx.text('frases', margin_top='1rem', font_size='1.5rem'),
                rx.button('Click aqui', margin_top='2rem', bg_color='aqua',
                on_click=MyState.get_quote),                
                quote()
            )
        ),
        rx.center(
            rx.image(src='/text.png',  margin_top='5rem')
        ),
        columns=[1,2]                
    )
    
def quote():
    return rx.box(
        rx.text(MyState.quote, as_='b'),
        rx.text('   '),
        rx.text(MyState.author, as_='b'),
    )