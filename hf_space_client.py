# scripts/hf_space_client.py
# Мини-клиент к публичному Hugging Face Space (Gradio).
# Умеет отправлять prompt (и, при наличии, длительность) и скачивать видео.
# Зависимости: gradio_client, requests

import argparse, pathlib
from gradio_client import Client
import requests

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--space", required=True, help="Slug Space: author/space-name")
    p.add_argument("--prompt", required=True, help="Текстовый промпт для видео")
    p.add_argument("--seconds", type=int, default=5, help="Длительность (если поддерживается Space)")
    p.add_argument("--out", default="videos/output.mp4", help="Куда сохранить видео")
    p.add_argument("--api-name", default="/predict", help="Имя эндпойнта (смотрите Use via API у Space)")
    args = p.parse_args()

    client = Client(args.space)

    # Попытка универсального вызова: сначала пробуем (prompt, seconds), потом — только prompt
    result = None
    try:
        job = client.submit(args.prompt, args.seconds, api_name=args.api_name)
        result = job.result()
    except Exception:
        # fallback: только prompt
        job = client.submit(args.prompt, api_name=args.api_name)
        result = job.result()

    # Достаём ссылку на видео из результата
    url = None
    if isinstance(result, str) and result.endswith((".mp4", ".webm", ".gif")):
        url = result
    elif isinstance(result, (list, tuple)):
        for x in result:
            if isinstance(x, str) and x.endswith((".mp4", ".webm", ".gif")):
                url = x
                break
    if not url:
        raise SystemExit(f"Не удалось найти видео в ответе Space: {result}")

    # Скачиваем
    r = requests.get(url)
    r.raise_for_status()
    pathlib.Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(args.out).write_bytes(r.content)
    print("Saved:", args.out)

if __name__ == "__main__":
    main()
