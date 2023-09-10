import reflex as rx

#import navbar 
from reflex_app.components.navbar import navbar

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
    