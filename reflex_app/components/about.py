import reflex as rx

#import navbar 
from reflex_app.components.navbar import navbar

def about():
    return rx.container(
        rx.container(
            navbar(),
            rx.divider(border_color="black"),
            rx.responsive_grid(
                rx.center(
                    rx.box(
                        rx.heading('Soy Walter!!!', size='xl'),
                        rx.heading('Desarrollador Python', size='lg'),
                        rx.text('------------------------------------'),
                        rx.text('Página Web de Reflex, documentación'),
                        rx.link('Ir Página Reflex', margen_top='10rem' , href='https://reflex.dev/', button=True,),          
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