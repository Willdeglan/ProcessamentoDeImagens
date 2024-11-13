'''
IFTO DE ARAGUATINS/TO
LICENCIATURA EM COMPUTAÇÃO

TRABALHO DE PROCESSAMENTO DE IMAGENS

Trabalho apresentado em sala de aula no dia 10 de junho de 2024.
'''

#pip install pillow
#pip install opencv-python
#pip install ultralytics
#pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
#pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu


# Para capturar um espaço ou print da tela
from PIL import ImageGrab
# Para maniputação da imagem capturada
import cv2
# Para calculos e conveções dos dados da imagem
import numpy as np
# Para baixar e utilizar a biblioteca Yolo
from ultralytics import YOLO
# Para usar comandos internos do sistema operacional
import os
# Para usar os comandos do sistema operacional com especificações do comando
import shutil


# Verifica se existe a pasta, se existir, exclui
def excluir_pasta(caminho_pasta):
    if os.path.exists(caminho_pasta):
        try:
            shutil.rmtree(caminho_pasta)
            print(f"Pasta {caminho_pasta} excluída com sucesso!")
        except Exception as e:
            print(f"Erro ao excluir a pasta {caminho_pasta}: {str(e)}")
    else:
        print(f"A pasta {caminho_pasta} não existe. Continuando...")


# Define as coordenadas da região que você deseja capturar
left, top, right, bottom = 800, 100, 1300, 700


'''
##################################
# TRAIN
# Load a model
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="coco8.yaml", epochs=1000, imgsz=640)
'''


##################################
# Carrega o melhor modelo treinado
model = YOLO("./runs/detect/train/weights/best.pt")


# Chama a função para verificação de existencia da pasta
excluir_pasta("./runs/detect/predict")


# Loop de captura de tela e detecção de pessoa
while True:

    # Captura a região especificada
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    # Converte a imagem para um array de numpy
    frame = np.array(screenshot)
    # Converte o array BGR para RGB
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


    # Salva a captura em um arquivo
    #img.save("./print/screenshot_region.png")


    # Faz a predicção da imagem
    detection_output = model.predict(source=img, conf=0.55, save=True, classes=0)

    # Lê o caminho da imagem com predicção e entregas para a biblioteca cv2
    local_img = "./runs/detect/predict/image0.jpg"
    detectado = cv2.imread(local_img)

    # Exibe a imagem
    cv2.imshow('Imagem RGB', detectado)

    # Espera 1 milessegundo e também o clik na tecla 27/ESC para sair do loop
    if cv2.waitKey(1) == 27:
        break


# Garante que todo o sistemas do cv2 aberto sejam finalizados
cv2.destroyAllWindows()