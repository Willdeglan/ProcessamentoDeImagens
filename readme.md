### IFTO DE ARAGUATINS/TO
### LICENCIATURA EM COMPUTAÇÃO

# TRABALHO DE PROCESSAMENTO DE IMAGENS

### PROFESSOR / ORIENTADOR:
#### RAMASIO FERREIRA DE MELO

### Autores:
#### ALESSANDRA DE SOUSA BARROS
#### WILLDEGLAN GOMES DA SILVA
#### ELLEN CRISTINA VIEIRA SILVA

## TEMA:
    Detecção da Classe Pessoa em tempo real em um vídeo de
    entrada para auxiliar no monitoramento de ambiente restrito

## TRABALHO APRESENTADO EM SALA DE AULA NO DIA - 10 de junho de 2024.


## OBJETIVO DO PROJETO
    Este projeto visa desenvolver e validar um sistema de monitoramento por
    meio de câmeras de segurança em um ambiente restrito a pessoas não autorizadas.
    Essa solução se tornará uma ferramenta auxiliar na segurança contínua de
    ambientes. Para isso, a biblioteca Ultralytics, usando a ferramenta YOLOv8, será
    fundamental para alavancar o projeto e tornar a proposta de detecção de pessoas
    em vídeos de vigilância (como câmeras de segurança ou monitoramento de tráfego)
    uma realidade próxima. O objetivo é melhorar a segurança e identificar atividades
    suspeitas em tempo real.


## DESCRIÇÃO DO CONJUNTO DE DADOS
        O conjunto de dados utilizado no modelo YOLOv8 é o COCO (Common
    Objects in Context). O COCO é um conjunto de dados amplamente utilizado para
    treinar e avaliar modelos de detecção de objetos e segmentação de instâncias. Ele
    contém imagens de alta resolução com anotações detalhadas para várias classes
    de objetos, incluindo pessoas, animais, veículos, móveis e muito mais, atualmente
    com 80 classes já pré-treinadas.
        O YOLOv8 é pré-treinado no COCO, o que significa que ele aprende a
    detectar e localizar objetos em várias categorias. Essa base de conhecimento
    permite que o modelo se generalize bem para outras tarefas de detecção de
    objetos, mesmo quando aplicado a domínios diferentes.
    Este trabalho utilizou o modelo pré definido “yolov8n.pt” na documentação
    pública no repositório github como banco de dados para treinamento no repositório
    disponível do “coco8.yaml”, nesse repositório temos:
        ● 4 images para train
        ● 4 images para val

## O REPOSITÓRIO “coco.yaml”, ROOT DATASET CONTÉM:
    ● 118287 images para train
    ● 5000 images para val
    ● 20288 images para teste

## METODOLOGIA PROPOSTA
### A metodologia envolverá as seguintes etapas
        1. Definição do Escopo e Objetivos:
            ● Compreender os requisitos específicos do projeto, como o ambiente de
            captura de imagens, a taxa de quadros desejada e as restrições de
            hardware;
            ● Definir o objetivo principal para a detecção de pessoas em tempo real em
            um vídeo.
        2. Preparação do Ambiente:
            ● Instalar as bibliotecas necessárias, como o Ultralytics YOLOv8 e suas
            dependências;
            ● Configurar o ambiente de desenvolvimento (por exemplo, Python, Jupyter
            Notebook, Google Colab).
        3. Aquisição de Dados:
            ● Capturar imagens em tempo real usando câmeras ou outra fonte de
            vídeo;
            ● Converter as imagens para o formato adequado (por exemplo, RGB).
        4. Treinamento do Modelo (Opcional):
            ● Se necessário, treine o YOLOv8 em um conjunto de dados específico
            (por exemplo, imagens de pessoas). Obs.: Em específico a este caso,
            não será utilizado outro modelo.
            ● Ajustar os hiperparâmetros, como confiança mínima e limiar de não
            máxima supressão (NMS).
        5. Carregamento do Modelo Pré-Treinado:
            ● Carregar o modelo YOLOv8 pré-treinado (neste caso, “yolov8n.pt”);
            ● Certificar que o modelo esteja otimizado para detecção de pessoas.
        6. Processamento das Imagens em Tempo Real:
            ● Capturar as imagens em tempo real;
            ● Pré-processar as imagens conforme necessário (redimensionamento,
            normalização, etc.).
        7. Detecção de Pessoas:
            ● Fazer previsões usando o melhor modelo treinado pelo YOLOv8 nas
            imagens em tempo real;
            ● Extrair as detecções de pessoas com base nas classes atribuídas pelo
            modelo.
        8. Exibição dos Resultados:
            ● Desenhar caixas delimitadoras ao redor das pessoas detectadas nas
            imagens.
            ● Exibir as imagens processadas em tempo real.
        9. Avaliação e Otimização:
            ● Avaliar a precisão e a velocidade da detecção.
            ● Ajustar os parâmetros conforme necessário para otimizar o desempenho.
        10. Testes e Validação:
            ● Realizar testes rigorosos em diferentes cenários (variações de
            iluminação, ângulos, distâncias).
            ● Validar a precisão e a robustez do sistema.

## CRITÉRIOS DE DESEMPENHO
        O projeto precisa alcançar o mínimo de 70% na detecção para ser
    considerada uma amostra viável, alcançável e promissor em relação a uma possível
    implementação em grande escala no mercado, desta forma, podemos analisar o
    projeto por quatro eixos que se mostraram excelentes, são eles:
        Tempo Real e Responsividade: O uso do YOLOv8 permite a detecção de
    pessoas em tempo real, garantindo respostas rápidas e análise instantânea de
    imagens de vídeo; Esse desempenho ágil é essencial para aplicações no campo da
    segurança, monitoramento de multidões e condução autônoma.
        Precisão e Eficiência: O YOLOv8 combina alta precisão com eficiência
    computacional, tornando-o ideal para sistemas que exigem detecção confiável de
    pessoas; A capacidade de equilibrar esses dois fatores é crucial para otimizar o
    desempenho geral do projeto.
        Escalabilidade e Implementação: O YOLOv8 é escalável e pode ser
    implantado em várias câmeras simultaneamente; Isso permite monitorar grandes
    áreas ou múltiplos locais de forma eficiente, mantendo a detecção de pessoas em
    tempo real.
        Adaptação a Diferentes Cenários: O YOLOv8 é versátil e pode ser ajustado
    para diferentes ambientes, iluminação e ângulos de câmera; Essa adaptabilidade é
    fundamental para garantir a detecção precisa de pessoas em variadas situações de
    vídeo.

## RESULTADOS ESPERADOS E IMPACTO
        Conclui-se que o sistema de detecção de pessoa em vídeo em tempo real
    pode aumentar a precisão e a intervenção em tempo hábil nos locais que pessoas
    não autorizadas/proibidas entraram no ambiente monitorado.
        O projeto de detecção de pessoas em tempo real usando o YOLOv8 é uma
    solução altamente eficaz para melhorar a segurança e a eficiência em diversos
    cenários. Com sua capacidade de detectar pessoas com alta precisão e velocidade,
    o YOLOv8 permite monitorar multidões, prevenir incidentes e identificar atividades
    suspeitas em tempo real. Além disso, sua flexibilidade e escalabilidade tornam-no
    ideal para integração em sistemas de vigilância, controle de acesso e
    gerenciamento de fluxo de pessoas.
        Em resumo, o YOLOv8 é uma ferramenta essencial para garantir a
    tranquilidade e a proteção em ambientes diversos.



# REQUISITOS TÉCNICOS

Para instalação em ambas as platoformas: Windows ou Linux

- Bibliotecas Python:
- - pip install pillow
- - pip install opencv-python
- - pip install ultralytics

- - pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
ou
- - pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

## OBSERVAÇÃO:
No caso do Linux, você deverá observar se sua distro contem uma ferramenta gráfica a mais para operar em conjunto com a Lib Pillow.
Um exemplo seria o ambiente X11 que é um sistema de janelas que permite aos usuários interagir com o Linux através de uma interface gráfica. Quando configurado e funcionando corretamente, o X11 facilita a execução de aplicativos gráficos e a utilização de uma interface de usuário amigável.

## PASSO A PASSO NA EXECUÇÃO DO CÓDIGO
- Para uma primeira execução você deverá retirar o 'comentário de bloco' do arquivo chave para que o sistema possa carregar o arquivo .yaml da plataforma COCO, onde estão guardados todos os bancos de dados do sistema;
- Em seguida o sistema carregará e criarar pastas e arquivos necessários que ele vai precisar para fazer as previsões, caso exista uma pasta específica onde guarda as previsões, o sistema vai excluir e criar uma nova vazia;
- Por fim, utilizando a Lib Pillow o sistema vai capturar um espaço do home screen para entregar ao sistema e para que ele faça as previsões e ja entregando as precisões ao operador em sua tela.

## VALE LEMBRAR
- Esse programa utiliza um bando de dados público disponível e conhecido como COCODATASET.ORG, nela existe atualmente 80 clases bem definidas e que pode definir o foco da predicção do sistema utilizado um parâmetro bem simples chamdo de 'classes=0' ou 'classe pessoa' no momento da linha de comando de predicção.
- Passos de verificação e instalação dessa ferramenta x11 no terminal:
    - Verificar se ja existe e instalado:
        - dpkg -l xserver-xorg
    - Instalando o x11:
        - sudo apt-get install xserver-xorg
    - Configurando o x11:
        - sudo nano /etc/X11/xorg.conf
    - Restart do servidor gráficos
        - sudo systemctl restart gdm

Após reiniciar, verifique se a interface gráfica está funcionando corretamente.

## CLASSES DISPONÍVEIS
  cod:    clase
-  0: person
-  1: bicycle
-  2: car
-  3: motorcycle
-  4: airplane
-  5: bus
-  6: train
-  7: truck
-  8: boat
-  9: traffic light
-  10: fire hydrant
-  11: stop sign
-  12: parking meter
-  13: bench
-  14: bird
-  15: cat
-  16: dog
-  17: horse
-  18: sheep
-  19: cow
-  20: elephant
-  21: bear
-  22: zebra
-  23: giraffe
-  24: backpack
-  25: umbrella
-  26: handbag
-  27: tie
-  28: suitcase
-  29: frisbee
-  30: skis
-  31: snowboard
-  32: sports ball
-  33: kite
-  34: baseball bat
-  35: baseball glove
-  36: skateboard
-  37: surfboard
-  38: tennis racket
-  39: bottle
-  40: wine glass
-  41: cup
-  42: fork
-  43: knife
-  44: spoon
-  45: bowl
-  46: banana
-  47: apple
-  48: sandwich
-  49: orange
-  50: broccoli
-  51: carrot
-  52: hot dog
-  53: pizza
-  54: donut
-  55: cake
-  56: chair
-  57: couch
-  58: potted plant
-  59: bed
-  60: dining table
-  61: toilet
-  62: tv
-  63: laptop
-  64: mouse
-  65: remote
-  66: keyboard
-  67: cell phone
-  68: microwave
-  69: oven
-  70: toaster
-  71: sink
-  72: refrigerator
-  73: book
-  74: clock
-  75: vase
-  76: scissors
-  77: teddy bear
-  78: hair drier
-  79: toothbrush

## CODIGO ADAPTÁVEL
Vale lebrar que esse código foi criado para detecção uma classe, mas ele pode sofrer leves alterações em seu comando e realizar mais outras funções muito interessantes, como:
- Classificação;
- Detecção;
- Segmentação;
- Track;
- Pose.

## CRESCIMENTO
Utilizando esse mesmo código, adaptando o bando de dados para a segmentação ou você pode criar seu banco de dados específico, em seguida, executar esse programa com o banco de dados específico para identificar uma segmentação, podendo ser uma cor, um objeto, uma doença ou fungo. Eis que abre um leque muito grande de possibilidades.



### REFERÊNCIAS
Todos os créditos são dados a essa biliotecas públicas na plataforma GITHUB
- https://github.com/ultralytics/ultralytics
- https://docs.ultralytics.com/datasets/detect/coco/
- https://dataset.org