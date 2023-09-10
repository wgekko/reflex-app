import reflex as rx

def about():
    return rx.responsive_grid(
        rx.center(
            rx.box(
                rx.heading('Soy Walter!!!', size='xl'),
                rx.heading('Desarrollador Python', size='lg'),
                rx.text('pagina about')                
                
            )
        ),
        rx.center(
            rx.image(src='/python.png')
        ),       
        columns=[1,2]                
    )
    
