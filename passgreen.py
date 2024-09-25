import flet as ft
import string
import random
def main(page:ft.Page):
    page.bgcolor=ft.colors.BLACK
    page.theme_mode=ft.ThemeMode.DARK
    page.padding=0
    page.theme=ft.Theme(
        color_scheme=ft.ColorScheme(
            primary='#192233',
            on_primary='#ffffff',
            background='#0d121c',
        )
    )
    options={}
    generate_buttom=ft.Ref[ft.Container]()
    text_password=ft.Ref[ft.Text]()
    characteres_count=ft.Ref[ft.Slider]()
    btn_clipboard=ft.Ref[ft.IconButton]()
    def copy(e):
        pwd= text_password.current.value
        if pwd:
            page.set_clipboard(pwd)
            btn_clipboard.current.selected=True
            btn_clipboard.current.update()
    def option(e):
        nonlocal options
        options.update({e.control.data:e.control.value})
        if any(options.values()):
            generate_buttom.current.disabled=False
            generate_buttom.current.opacity=1
        else:
            generate_buttom.current.disabled=True
            generate_buttom.current.opacity=0.3
        generate_buttom.current.update()
    def generate_password(e):
        pwd=''
        if options.get('uppercase'):
            pwd+=string.ascii_uppercase
        if options.get('lowercase'):
            pwd+=string.ascii_lowercase
        if options.get("digitis"):
            pwd+=string.digits
        if options.get('punctuation'):
            pwd+= string.punctuation
        cont = int(characteres_count.current.value)
        password=random.choices(pwd,k=cont)
        text_password.current.value=''.join(password)
        text_password.current.update()
        btn_clipboard.current.selected=False
        btn_clipboard.current.update()
    layout=ft.Container(
        expand=True,
        padding=ft.padding.only(top=60,left=20,right=20,bottom=30),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.colors.PRIMARY,ft.colors.BACKGROUND]
        ),
        content=ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Text(
                    value='GERADOR DE SENHAS',
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30,thickness=0.5),
                ft.Container(
                    bgcolor=ft.colors.with_opacity(0.3,ft.colors.BLACK),
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.all(10),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                selectable=True,
                                size=30,
                                height=40,
                                ref=text_password
                            ),
                            ft.IconButton(
                                icon=ft.icons.COPY,
                                icon_color=ft.colors.WHITE24,
                                selected_icon=ft.icons.CHECK,
                                selected_icon_color=ft.colors.INDIGO,
                                selected=False,
                                ref=btn_clipboard,
                                on_click=copy
                            )
                        ]
                    )
                ),
                ft.Text(
                   value='CARACTERES',
                    weight=ft.FontWeight.BOLD,
                    size=25
                ),
                 
                ft.Container(
                    bgcolor=ft.colors.with_opacity(0.3,ft.colors.BLACK),
                    border_radius=ft.border_radius.all(10),
                    content=ft.Slider(
                        value=10,
                        min=4,
                        max=20,
                        divisions=10,
                        label='{value}',
                        ref=characteres_count
                    )
                ),
                ft.Text(
                   value='PREFERÊNCIAS',
                    weight=ft.FontWeight.BOLD,
                    size=25
                ),
                ft.ListTile(
                    title=ft.Text(
                        value='letras maiusculas',
                        size=20
                    ),
                    trailing=ft.Switch(
                        active_color=ft.colors.INDIGO,
                        adaptive=True,
                        data='uppercase',
                        on_change=option
                    ),
                    toggle_inputs=True,
                ),
                ft.ListTile(
                    title=ft.Text(
                        value='letras minusculas',
                        size=20
                    ),
                    trailing=ft.Switch(
                        active_color=ft.colors.INDIGO,
                        adaptive=True,
                        data='lowercase',
                        on_change=option
                    ),
                    toggle_inputs=True,
                ),
                ft.ListTile(
                    title=ft.Text(
                        value='incluir números',
                        size=20
                    ),
                    trailing=ft.Switch(
                        active_color=ft.colors.INDIGO,
                        adaptive=True,
                        data='digitis',
                        on_change=option
                    ),
                    toggle_inputs=True,
                ),
                ft.ListTile(
                    title=ft.Text(
                        value='incluir símbolos',
                        size=20
                    ),
                    trailing=ft.Switch(
                        active_color=ft.colors.INDIGO,
                        adaptive=True,
                        data='punctuation',
                        on_change=option
                    ),
                    toggle_inputs=True,
                ),
                ft.Container(
                    content=ft.Text(
                        value='GERAR SENHA',
                        weight=ft.FontWeight.BOLD,
                        size=25
                    ),
                    gradient=ft.LinearGradient(
                        colors=[ft.colors.INDIGO_900,ft.colors.INDIGO_600]
                    ),
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(top=20,bottom=20),
                    border_radius=ft.border_radius.all(20),
                    on_click=generate_password,
                    disabled=True,
                    opacity=0.3,
                    animate_opacity=ft.Animation(duration=1000,curve=ft.AnimationCurve.DECELERATE),
                    ref=generate_buttom,
                )
            ]
        )
    )
    page.add(layout)

if __name__=="__main__":
    ft.app(target=main)