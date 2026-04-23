import os
import re
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError

def adicionar_titulo_por_nome_arquivo(caminho_pasta):
    # Listar arquivos .mp3 na pasta
    arquivos = [f for f in os.listdir(caminho_pasta) if f.lower().endswith('.mp3')]
    
    for arquivo in arquivos:
        caminho_completo = os.path.join(caminho_pasta, arquivo)
        
        # Remove extensão .mp3 para usar como título
        titulo = os.path.splitext(arquivo)[0]
        
        # Opcional: limpar o título (remover números, traços, etc.)
        # titulo = re.sub(r'^\d+[\s\-\._]*', '', titulo)  # Remove números iniciais
        # titulo = re.sub(r'[\-_\.]+', ' ', titulo)  # Substitui separadores por espaço
        
        try:
            # Tenta carregar ou criar tags ID3
            try:
                audio = EasyID3(caminho_completo)
            except ID3NoHeaderError:
                audio = MP3(caminho_completo)
                audio.add_tags()
                audio = EasyID3(caminho_completo)
            
            # Adiciona título
            audio['title'] = titulo
            
            # Salva as alterações
            audio.save()
            print(f"✓ Título adicionado: '{titulo}' em '{arquivo}'")
            
        except Exception as e:
            print(f"✗ Erro em '{arquivo}': {e}")

# Usar seu caminho
caminho = "/media/renato/ADE4-4B0E/A-Sertanejo-Forro-2021/"
adicionar_titulo_por_nome_arquivo(caminho)
