# Adicionar titulo em MP3 via nome do arquivo

```sh
sudo apt update

# Instala Python3 + pip (caso não tenha)
sudo apt install -y python3 python3-pip

# Instala a lib mutagen
pip3 install mutagen
python3 -m venv venv
source venv/bin/activate

pip install mutagen
python3 adicionar_titulo.py
```

## Use o Python com mutagen pois:

Mais confiável e cross-platform

Melhor manipulação de tags ID3

Não corrompe arquivos existentes

Pode preservar outras tags (artista, álbum, etc.)

Execute o script Python de dentro da pasta ou passe o caminho completo como argumento.
