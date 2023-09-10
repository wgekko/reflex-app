import reflex as rx

#import navbar 
from reflex_app.components.navbar import navbar

def posts():
    return rx.container(
        rx.container(
            navbar(),
            rx.divider(border_color="black"),
            rx.responsive_grid(
                rx.center(
                    rx.box(
                        rx.heading('Soy Walter!!!', size='lg'),
                        rx.heading('Desarrollador Python', size='md'),                        
                        rx.text('------------------------------------'),
                        rx.text('video tutorial de Reflex'),
                        rx.link('Ir Video Reflex', margen_top='10rem' , href='https://www.youtube.com/watch?v=2u7JlBEavx0', button=True,),          
                    )
                ),
                rx.center(
                    rx.image(src='/python.png')
                ),
                columns=[1, 2]
            ),
            bg_color='#E8F8F5',
            borderRadius="15px",
            boxShadow="41px -41px 82px #0d0f15, -41px 41px 82px #2d374b",
        ),
        center_content=True,
        justifyContent="center",
        maxWidth="auto",
        height="100vh",
        bg="#FEF9E7",
    )