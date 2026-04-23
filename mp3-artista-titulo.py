import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError

def adicionar_metadados_inteligente(caminho_pasta):
    arquivos = [f for f in os.listdir(caminho_pasta) if f.lower().endswith('.mp3')]
    
    for arquivo in arquivos:
        caminho_completo = os.path.join(caminho_pasta, arquivo)
        nome_sem_ext = os.path.splitext(arquivo)[0]
        
        # Tenta extrair artista se estiver no formato "Artista - Música.mp3"
        if ' - ' in nome_sem_ext:
            artista, titulo = nome_sem_ext.split(' - ', 1)
        else:
            artista = None
            titulo = nome_sem_ext
        
        try:
            # Carrega ou cria tags
            try:
                tags = EasyID3(caminho_completo)
            except ID3NoHeaderError:
                mp3 = MP3(caminho_completo)
                mp3.add_tags()
                tags = EasyID3(caminho_completo)
            
            # Adiciona tags
            tags['title'] = titulo
            if artista:
                tags['artist'] = artista
            
            tags.save()
            print(f"✓ {arquivo} -> Título: {titulo}" + (f" | Artista: {artista}" if artista else ""))
            
        except Exception as e:
            print(f"✗ Erro em {arquivo}: {e}")

caminho = "/media/renato/ADE4-4B0E/Isadora_Pompeo_2018/"
adicionar_metadados_inteligente(caminho)