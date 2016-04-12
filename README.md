# Board Image Downloader
## Faça download de imagens e vídeos de uma image board!

### Descrição:

###### Este é um simples programa escrito em Python que permite o download de imagens (.jpg, .png e .gif) e vídeos (.webm) de um tópico em uma image board específica.

###### Ao escolher a board e o tópico desejado, o programa irá fazer uma varredura para determinar a quantidade de imagens e vídeos disponíveis. Ele então irá fazer o download de todos os arquivos do tópico. 

###### Caso faça o download novamente do mesmo tópico no mesmo diretório escolhido, o programa irá baixar apenas os arquivos mais novos, que ainda não estão presentes no diretório.

###### Se não for especificado o uso de um diretório, o programa irá criar uma pasta genérica no mesmo diretório do programa para armazenar os arquivos baixados.

<br />

###### A quem estiver interessado em usar este programa, poderá baixá-lo e modificá-lo, adicionando novas funções, portando para outras linguagens e modificando funções já existentes no programa.

### Requisitos:

- Python 2.x

### Download e Execução:

    wget https://raw.github.com/Wolfterro/Board-Image-Downloader/master/Board-Image-Downloader.py
    chmod +x Board-Image-Downloader.py
    ./Board-Image-Downloader.py

### Uso:
    
    Ajuda:
    '-h' ou '--help': Mostra a tela de ajuda
    
    Argumentos:
    '-d' ou '--directory': Escolhe e cria (se não existir) um diretório para armazenar as imagens e vídeos
    '-b' ou '--boards': Escolhe inicialmente a board desejada
