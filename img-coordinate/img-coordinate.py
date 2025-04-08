import cv2
import matplotlib.pyplot as plt

# Função de callback que registra o início e o fim do clique do mouse
def select_area(event, x, y, flags, param):
    global x_initial, y_initial, drawing, rect
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x_initial, y_initial = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_copy = img.copy()
            cv2.rectangle(img_copy, (x_initial, y_initial), (x, y), (0, 255, 0), 2)
            cv2.imshow('Image', img_copy)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        rect = (x_initial, y_initial, x, y)

# Carregar a imagem e inicializar variáveis
img = cv2.imread('imagem.png')  # Substitua pelo caminho da sua imagem
cv2.imshow('Image', img)
drawing = False
rect = None

# Exibir a imagem e registrar o evento do mouse
cv2.setMouseCallback('Image', select_area)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Se uma área foi selecionada, exibir coordenadas
if rect:
    x1, y1, x2, y2 = rect
    print(f"Coordenadas do retângulo: ({x1}, {y1}) -> ({x2}, {y2})")
    # Exibir a área demarcada
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.gca().add_patch(plt.Rectangle((x1, y1), x2-x1, y2-y1, linewidth=2, edgecolor='r', facecolor='none'))
    plt.show()
else:
    print("Nenhuma área foi demarcada.")

