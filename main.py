import json
import requests
import flet as ft
from os import name
from httpx import request
from turtle import onclick
from functools import partial
from connect import get_books
from urllib.parse import urlparse, parse_qs


def main(page: ft.Page):
    page.title = 'App Register'
    page.window_width = 400

    def home_page():
        name_input = ft.TextField(label = "Product Name", text_align=ft.TextAlign.LEFT)

        streaming_select = ft.Dropdown(
            options=[
                ft.dropdown.Option("AK", text="Amazon Kindle"),
                ft.dropdown.Option("PB", text="Physical Book")
            ],
            label="Select the streaming"
        )

        def load_books():
            def redirect(e, book_id):
                page.go(f'/review?id={book_id}')
            books_list.controls.clear()
            for i in get_books():
                books_list.controls.append(
                    ft.Container(
                        ft.Text(i['name']),
                        bgcolor= ft.colors.BLACK12,
                        padding=15,
                        alignment=ft.alignment.center,
                        margin = 3,
                        border_radius= 10,
                        on_click= lambda e, book_id=i['id']: page.go(f'/review?id={book_id}')
                    )
                )
            page.update()

        def register(e):
            data = {
                'name': name_input.value,
                'streaming': streaming_select.value,
                'categories': []
            }
            requests.post('http://127.0.0.1:8000/api/books/', json=data)
            load_books()

        register_bttn = ft.ElevatedButton("Register", on_click=register)

        books_list = ft.ListView()

        load_books()
        page.views.append(
            ft.View(
                '/',
                controls=[
                    name_input,
                    streaming_select,
                    register_bttn,
                    books_list
                ]
            )
        )

    def review_page(book_id):
        grade_input = ft.TextField(label = "Grade it (between 1 and 5)", text_align=ft.TextAlign.LEFT, value='0')
        comment_input = ft.TextField(label='Comment', multiline=True, expand=True)

        def evaluate(e):
            data = {
                'grade': int(grade_input.value),
                'comments': comment_input.value
            }

            try:
                response = requests.put(f'http://127.0.0.1:8000/api/books/{book_id}', json=data)

                if response.status_code == 200:
                    page.snack_bar = ft.SnackBar(ft.Text('Comment sent successfully'))

                else: 
                    page.snack_bar=ft.SnackBar(ft.Text(F'Error when sending the comment'))


                page.snack_bar.open = True

            except Exception as e:
                page.snack_bar = ft. SnackBar(ft.Text(F'Connection error: {e}'))
                page.snack_bar.open = True

            page.update()


        evaluate_bttn = ft.ElevatedButton('Evaluate', on_click=evaluate)
        back_bttn = ft.ElevatedButton('Back', on_click = lambda _: page.go('/'))

        page.views.append(
            ft.View(
                '/review',
                controls=[
                    grade_input,
                    comment_input,
                    evaluate_bttn,
                    back_bttn
                ]
            )
        )

    def route_change(e):
        page.views.clear()

        if page.route == '/':
            home_page()
        elif page.route.startswith('/review'):
            parsed_url = urlparse(page.route)
            query_params = parse_qs(parsed_url.query)
            book_id = query_params['id'][0]
            review_page(book_id)

        page.update()

    page.on_route_change = route_change
    page.go('/')



ft.app(target=main)