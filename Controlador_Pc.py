import pyautogui as posicaoMouse
import time

posicaoMouse.sleep(3.3) # Tempo de spera para execução
print(posicaoMouse.position()) # valor de posição 
# posicaoMouse.moveTo(x=9, y=763) # movimento do ponto para o local
posicaoMouse.click(x=9, y=763) # click da operação
time.sleep(1.7)
posicaoMouse.typewrite('Edge')
time.sleep(2.3)
posicaoMouse.press('Enter')
time.sleep(3.15)
posicaoMouse.typewrite('Valor do dolar')
time.sleep(2.35)
posicaoMouse.press('Enter')
