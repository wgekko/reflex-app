
import reflex as rx


def posts():
    return rx.responsive_grid(
        rx.center(
            rx.box(
                rx.heading('Soy Walter!!!', size='xl'),
                rx.heading('Desarrollador Python', size='lg'),
                #rx.button('Click aqui', margin_top='2rem', 
                #on_click=MyState.get_quote),                
                #quote()
            )
        ),
        rx.center(
            rx.image(src='/python.png')
        ),       
        columns=[1,2]                
    )
    
