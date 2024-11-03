from youtube_transcript_api import YouTubeTranscriptApi

# ID do vídeo do YouTube (após 'v=' na URL ou último segmento da URL encurtada)
video_id = '4lzD17wWPjE'

try:
    # Obtém a transcrição automática em português
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt', 'pt-BR'])

    # Exibe as legendas em formato de texto
    for entry in transcript:
        print(f"{entry['text']}")
        #print(f"{entry['start']:.2f}s: {entry['text']}")
except Exception as e:
    print("Não foi possível obter as legendas:", str(e))
