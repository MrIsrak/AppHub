import flet as ft
import keyboard
from cnvrt_fnc import convert, update_result, update_type, check_keys

res = 0
UserInputValue = 0
def main(page):
    page.window_width = 600        # window's width is 200 px
    page.window_height = 400       # window's height is 200 px
    page.window_resizable = False  # window is not resizable
    page.update()

    page.title = "Calc App"
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter number."
            page.update()
        else:
            num = txt_name.value
            page.clean()
            page.add(ft.Text(num))
    def row_with_alignment(align: ft.MainAxisAlignment):

        page.add(ft.Column(
            width=500,
            controls=[
                ft.Text(str(align), size=16),
                ft.Container(
                    content=ft.Row(options1,options2),
                    
                ),
            ]
            )
        )
    # Объявление выпадающих списков
    menu = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Lenght"),
            ft.dropdown.Option("Time"),
            ft.dropdown.Option("Mass"),
        ],
    )
    options1 = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Kilometers"),
            ft.dropdown.Option("Meters"),
            ft.dropdown.Option("Centimeters"),
        ],
    )
    options2 = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Kilometers"),
            ft.dropdown.Option("Meters"),
            ft.dropdown.Option("Centimeters"),
        ],
    )
    txt_name = ft.TextField(label="Your number", autofocus=True)
    
    # Размещение
    page.add(txt_name)
    page.add(
        ft.Row(
            controls=[
                menu
            ]
        ),
    page.add(ft.Column(
        controls=[
            options1,options2
                
        ]
        )
        )
    )

ft.app(target=main)