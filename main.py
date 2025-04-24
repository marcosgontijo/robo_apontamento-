import pyautogui
import time
import keyboard  # Biblioteca para detectar tecla F2

# Função para verificar se F2 foi pressionado
def verificar_parada():
    if keyboard.is_pressed('f2'):
        print("Parado pelo usuário (F2).")
        exit()

# Função para clicar no dia usando imagem + clicks extras
def clicar_dia(dia):
    verificar_parada()
    imagem = f"calendario/dia_{dia:02}.png"  # Ex: calendario/dia_01.png
    pos = pyautogui.locateCenterOnScreen(imagem, confidence=0.9)
    if pos:
        pyautogui.click(pos)
        time.sleep(0.5)
        print(f"Dia {dia} selecionado.")

        # Clique em "OK" do calendário
        pyautogui.click(1485, 996)
        time.sleep(0.5)

        # Clique em "Apontar horas"
        pyautogui.click(1027, 620)
        time.sleep(0.5)

    else:
        print(f"Dia {dia} NÃO encontrado.")

# Mensagem de início
print("Preparando para começar em 5 segundos... Pressione F2 para cancelar.")
time.sleep(5)

# Lista de cliques com coordenadas
passos = [
    (950, 650),    # Iniciar apontamento
    (979, 262),    # Seleciona o serviço
    (859, 460),    # Codex Utilities
    (923, 395),    # Atividade
    (975, 329),    # Departamento
    (1000, 546),   # Scroll departamento
    (776, 671),    # Departamento NDB - 0581
    (992, 401),    # Confirmar departamento
    (836, 843),    # Selecionar Desenvolvimento
    (1662, 629),   # Apontamento manual
    (1608, 580),   # Primeira hora
]

# Executa os cliques iniciais
for x, y in passos:
    verificar_parada()
    pyautogui.click(x, y)
    time.sleep(2)

# Escrever hora inicial
verificar_parada()
pyautogui.write('09')
time.sleep(0.5)

# Segundo minuto
verificar_parada()
pyautogui.click(1668, 570)
time.sleep(2)

verificar_parada()
pyautogui.write('00')
time.sleep(0.5)

# Abrir calendário pela primeira vez
verificar_parada()
pyautogui.click(1533, 564)
time.sleep(2)

# Loop para clicar nos dias do calendário (1 a 30)
for dia in range(1, 31):
    clicar_dia(dia)
    verificar_parada()

    # Reabre o calendário para o próximo dia
    pyautogui.click(1533, 564)
    time.sleep(1.5)

# Fim do script
print("Processo finalizado com sucesso.")
