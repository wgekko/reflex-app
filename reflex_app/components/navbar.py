
import reflex as rx

def navbar():
    return rx.flex(
        rx.box(
            rx.link(
                rx.image(src='/python.png', width='60px'),
                href='/'
            )    
        ),
        rx.center(
            rx.menu(
                rx.menu_button('Menu'),
                rx.menu_list(
                    rx.menu_item(
                            rx.link('Reflex', href='/about')
                        ),
                    rx.menu_item(
                        rx.link('Tutorial', href='/posts')
                    ),
                    rx.menu_item(
                        rx.link('Gráficos DataScience', href='/datascience')
                    ),
                    rx.menu_item(
                        rx.link('Gráficos Mercados', href='/market')
                    )
                    
                )
            )
        ),
        justify_content='space-between'
        
    )
    