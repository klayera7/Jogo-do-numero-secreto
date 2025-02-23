import PySimpleGUI as sg
import random

sg.theme("DarkBlue")

numero_secreto = random.randint(1, 100)
tentativas = 10

layout = [
    [sg.Text("🎯 Adivinhe o número de 1 a 100!")],
    [sg.InputText(key="tentativa", size=(10, 1), focus=True, enable_events=True)],
    [sg.Button("Tentar", bind_return_key=True)],  # Aperte "Enter" para ativar o botão
    [sg.Text(f"Você tem {tentativas} tentativas.", key="status", size=(30, 1))],
    [sg.Button("Sair")]
]

janela = sg.Window("Jogo de Adivinhação", layout, finalize=True)

while True:
    evento, valores = janela.read()

    if evento == sg.WINDOW_CLOSED or evento == "Sair":
        break

    if evento == "Tentar":
        if not valores["tentativa"].isdigit():  # Verifica se é um número válido
            janela["status"].update("❌ Digite um número válido!")
            continue

        tentativa = int(valores["tentativa"])
        tentativas -= 1

        if tentativa == numero_secreto:
            sg.popup("🎉 Parabéns! Você acertou o número secreto!", title="Vitória")
            break
        elif tentativa < numero_secreto:
            msg = "🔼 O número secreto é maior!"
        else:
            msg = "🔽 O número secreto é menor!"

        if tentativas == 0:
            sg.popup(f"😢 Você perdeu! O número secreto era {numero_secreto}.", title="Fim de Jogo")
            break

        janela["status"].update(f"{msg} {tentativas} tentativas restantes.")
        janela["tentativa"].update("")  # Limpa a entrada para a próxima tentativa

janela.close()
