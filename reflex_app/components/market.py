import reflex as rx

#import navbar
from reflex_app.components.navbar import navbar

def market():
    return rx.container(
        rx.container(
            navbar(),
            rx.divider(border_color="black"),
            rx.responsive_grid(
                rx.center(
                    rx.box(
                        rx.heading('Soy Walter!!!', size='lg'),
                        rx.heading('Desarrollador Python', size='md'),                                                        
                    )
                ),
                rx.center(
                    rx.image(src='/python.png',heigth='50%', width='50%')
                ),
                rx.text('------------------------------------'),  
                rx.text('Gráfico de cotizaciones de acciones (precios en USD) Set/2023'),
                rx.chart(
                    rx.candlestick(
                        data=rx.data(
                            "candlestick",
                            x=['4/9', '5/9', '6/9', '7/9', '8/9'],
                            open=[1, 3, 6, 7, 15],
                            close=[1, 11, 3, 4, 10],
                            high=[3, 14, 6, 7, 16],
                            low=[1, 2, 3, 4, 10],
                        ),
                        candle_colors={
                            "positive": "green",
                            "negative": "red",
                        },
                        candle_width=8.0,
                        candle_ratio=0.5,
                    ),
                ),heigth='5em', width='20em'                
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
