from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled

video_id = "pAB1FyTtY7E"

try:
    api = YouTubeTranscriptApi()                         # instância
    ft = api.fetch(video_id, languages=["pt-BR", "pt"])  # FetchedTranscript

    # ----- forma simples: pega só o texto -----
    texto = "\n".join(snippet.text for snippet in ft)
    print(texto)

    # ----- forma alternativa: lista de dicionários -----
    # raw = ft.to_raw_data()              # ↩ devolve [{'text': ..., 'start': ...}, ...] :contentReference[oaicite:1]{index=1}
    # print("\n".join(item["text"] for item in raw))

except NoTranscriptFound:
    print("❌ Este vídeo não possui legendas nesses idiomas.")
except TranscriptsDisabled:
    print("❌ O autor do vídeo desativou as legendas.")
except Exception as e:
    print("❌ Erro inesperado:", e)
