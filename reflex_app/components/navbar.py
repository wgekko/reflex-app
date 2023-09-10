
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
                            rx.link('About', href='/about')
                        ),
                    rx.menu_item(
                        rx.link('Posts', href='/posts')
                    )
                    
                )
            )
        ),
        justify_content='space-between'
        
    )
    