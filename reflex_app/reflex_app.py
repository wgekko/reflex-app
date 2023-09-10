# from rxconfig import config

import reflex as rx
from .components.navbar import navbar
from .components.header import header
from .components.about import about
from .components.posts import posts
from .components.datascience import datascience
from .components.market import market



def index():
    return rx.container(
        rx.container(
            navbar(),
            rx.divider(border_color="black"),
            header(),
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


# Add state and page to the app.
app=rx.App()
app.add_page(index)
app.add_page(about, route="/about")
app.add_page(posts, route="/posts")
app.add_page(datascience, route='/datascience')
app.add_page(market, route='/market')
app.compile()




"""
# desarrollo de codigo alternativo
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

def datascience():
    return rx.container(
        rx.container(
            navbar(),
            rx.divider(border_color="black"),
            rx.responsive_grid(
                rx.center(
                    rx.box(
                        rx.heading('Soy Walter!!!', size='lg'),
                        rx.heading('Desarrollador Python', size='md'),
                        rx.text('Gráfico de DataScience (max, min, mediana)'),                                 
                                                         
                    )
                ),
                rx.center(
                    rx.image(src='/python.png')
                ),
                #rx.text('------------------------------------'),
                rx.text('Gráfico de ventas trimestrales 2022 (en millones de pesos), la mediana está representada en color verde'),
                
                rx.chart(
                    rx.box_plot(
                        data=rx.data(
                            "box_plot",
                            x=[1, 2, 3, 4, 5],
                            y=[
                                [1, 2, 3, 4, 10],
                                [5, 12, 4, 6, 1],
                                [1, 2, 3, 4, 10],
                                [5, 12, 4, 6, 1],
                                [1, 2, 3, 4, 10],
                            ],
                        ),
                        style={
                            "min": {"stroke": "Salmon"},
                            "max": {"stroke": "IndianRed"},
                            "q1": {"fill": "Salmon"},
                            "q3": {"fill": "IndianRed"},
                            "median": {"stroke": "Teal", "strokeWidth": 5},
                        }, 
                    ),
                    domain_padding={"x": 15, "y": 5},
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
"""