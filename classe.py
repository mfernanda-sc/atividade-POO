class Notebook:
    def mostrar_marca(marca):
        print(f'Sua marca é: {marca}')

    def mostrar_modelo(modelo):
        print(f'seu modelo é: {modelo}')

    def mostrar_tudo(marca, modelo):
        print(f"seu Notebook é o {marca} {modelo}")


marc = "Lenovo"
model = "Ryzen 7"

Notebook.mostrar_marca(marc)

Notebook.mostrar_modelo(model)

Notebook.mostrar_tudo(marc,model)