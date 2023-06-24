import flet as ft
from flet import *

def main(page: ft.Page):
    t = ft.Text(value="Hello!", color="green")
    page.controls.append(t)
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)