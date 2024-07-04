import cv2
import numpy as np

# Nome dos arquivos de entrada e saída  
input_file = '3-RJS-0706-RJ_5333.60_x10_PP.jpg'
output_file = '0706_533.60.15.png'

# Limiar de crominância CB
threshold = 140

# Carrega a imagem e redimensiona para um tamanho menor
im = cv2.imread(input_file)

# Converte a imagem para o espaço de cores YCbCr
ycbcr = cv2.cvtColor(im, cv2.COLOR_BGR2YCrCb)

# Obtém as dimensões da imagem
s1, s2, _ = im.shape

# Inicializa uma matriz de zeros para armazenar a imagem binária
BW = np.zeros((s1, s2), dtype=np.uint8)

# Calcula a imagem binária com base no limiar de crominância CB
for I in range(s1):
    for J in range(s2):
        if ycbcr[I, J, 2] > threshold:
            BW[I, J] = 255  # Define pixels acima do limiar como brancos (porosos)
        # Imprime o valor de BW durante as iterações
        #print(f'Valor de BW[{I},{J}] = {BW[I, J]}')

# Calcula a porosidade
inverted_BW = cv2.bitwise_not(BW)
porosity = round(sum(sum(inverted_BW))/(s1*s2)*100)
# Salva a imagem binária
cv2.imwrite(output_file, inverted_BW)



# Exibe a porosidade
print(f'Porosidade Visual = {porosity} %')




