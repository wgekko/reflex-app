# from rxconfig import config

import reflex as rx
from .components.navbar import navbar
from .components.header import header
from .components.about import  about 
from .components.posts import posts


def index():

    return rx.container(
        rx.container(
            navbar(),
            rx.divider(),
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

def about():
    return rx.container(
        rx.container(
            navbar(),
            rx.divider(),
            rx.text('pagina about'),
            #about(),
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
            rx.divider(),
            rx.text('pagina posts'),
            #posts(),
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
app = rx.App()
app.add_page(index)
app.add_page(about, route="/about")
app.add_page(posts, route="/posts")
app.compile()
