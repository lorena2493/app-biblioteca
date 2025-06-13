import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors
from flet.core.elevated_button import ElevatedButton


def main(page: ft.Page):
    # Configuração da página
    page.title = 'Mecânica Hephaestus'
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667
    page.auto_scroll = True

    # Definição de funções
    lista = []
    clientes = []
    campos_clientes = []

    def main_view():
        return ft.Column(
            controls=[
                img,

                ElevatedButton(text="Clientes", width=355, style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10)), color=Colors.BLACK, bgcolor=Colors.YELLOW_600,
                               on_click=lambda _: page.go("/clientes")),
                ElevatedButton(text="Veiculos", width=355, style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10)), color=Colors.BLACK, bgcolor=Colors.YELLOW_600,
                               on_click=lambda _: page.go("/veiculos")),
                ElevatedButton(text="Ordens", width=355, style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10)), color=Colors.BLACK, bgcolor=Colors.YELLOW_600,
                               on_click=lambda _: page.go("/ordens"))
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,  # Adicionado espaçamento entre os campos
        )

    def gerencia_rotas(route):
        # Construir layout
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [
                        main_view(),
                    ],
                )
            )

        elif page.route == "/clientes":
            page.views.append(
                View(
                    "clientes",
                    [
                        input_nome,
                        input_cpf,
                        input_telefone,
                        input_endereco,
                        ft.ElevatedButton("Salvar", on_click=salvar_cliente, bgcolor=Colors.RED_700,
                                          color=Colors.WHITE),

                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,  # Adicionado espaçamento entre os campos
                )
            )
        elif page.route == "/veiculos":
            page.views.append(
                View(
                    "veiculos",
                    [
                        input_marca,
                        input_modelo,
                        input_placa,
                        input_ano_fabricacao,
                        ft.ElevatedButton("Salvar", on_click=salvar_cliente, bgcolor=Colors.RED_700,
                                          color=Colors.WHITE),

                    ],
                    scroll=scroll.mode.always,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,  # Adicionado espaçamento entre os campos
                )
            )
        elif page.route == "/ordens":
            page.views.append(
                View(
                    "ordens",
                    [
                        input_data_abertura,
                        input_descricao_servico,
                        input_status,
                        input_valor_estimado,
                        ft.ElevatedButton("Salvar", on_click=salvar_cliente, bgcolor=Colors.RED_700,
                                          color=Colors.WHITE),

                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,  # Adicionado espaçamento entre os campos
                )
            )

        page.update()


    def salvar_cliente(e):
        if input_nome.value == "":
            page.overlay.append(msg_erro)
            msg_erro = True
            page.update()
        else:
            lista.append(input_nome.value)
            input_nome.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()
            return

        cliente = {
            "nome": input_nome.value,
            "cpf": input_cpf.value,
            "telefone": input_telefone.value,
            "endereco": input_endereco.value,
            "marca": input_marca.value,
            "modelo": input_modelo.value,
            "placa": input_placa.value,
            "ano_fabricacao": input_ano_fabricacao.value,
            "data_abertura": input_data_abertura.value,
            "descricao_servico": input_descricao_servico.value,
            "status": input_status.value,
            "valor_estimado": input_valor_estimado.value
        }
        clientes.append(cliente)

        for campo in campos_cliente.values():
            campo.value = ""

    def voltar(e):
        page.go("/")

    # Criação de componentes

    img = ft.Image(
        src="assets/mech_ft.svg"
    )

    input_nome = ft.TextField(label='Nome:', hint_text='EX: Fernanda')

    input_cpf = ft.TextField(label='CPF:', hint_text='EX: 12345678910')

    input_telefone = ft.TextField(label='Telefone:', hint_text='EX: 12345678910')

    input_endereco = ft.TextField(label='Endereço:', hint_text='EX: Rua da alegria, 123')

    input_marca = ft.TextField(label='Marca:', hint_text='EX: Ford')

    input_modelo = ft.TextField(label='Modelo:', hint_text='EX: Fusca')

    input_placa = ft.TextField(label='Placa:', hint_text='EX: A1B23C')

    input_ano_fabricacao = ft.TextField(label='Ano de fabricação:', hint_text='EX: 2007')

    input_data_abertura = ft.TextField(label='Data da abertura:', hint_text='EX: 04-10-2024')

    input_descricao_servico = ft.TextField(label='Descrição do serviço:', hint_text='EX: Troca de óleo')

    input_status = ft.TextField(label='Status:', hint_text='EX: Completo')

    input_valor_estimado = ft.TextField(label='Valor estimado:', hint_text='EX: 1400')

    campos_cliente = {
        "nome": input_nome,
        "cpf": input_cpf,
        "telefone": input_telefone,
        "endereco": input_endereco,
        "marca": input_marca,
        "modelo": input_modelo,
        "placa": input_placa,
        "ano_fabricacao": input_ano_fabricacao,
        "data_abertura": input_data_abertura,
        "descricao_servico": input_descricao_servico,
        "status": input_status,
        "valor_estimado": input_valor_estimado
    }

    msg_sucesso = ft.SnackBar(
        content=ft.Text("Salvo com sucesso"),
        bgcolor=Colors.GREEN
    )

    msg_erro = ft.SnackBar(
        content=ft.Text("Preencha todos os campos"),
        bgcolor=Colors.RED
    )

    lv_nome = ft.ListView(
        height=500
    )

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.go(page.route)


# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)
