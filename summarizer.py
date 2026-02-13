import requests
from config import OPENROUTER_API_KEY, MODEL_NAME, OPENROUTER_URL

MAX_CHARS = 12000

def summarize_text(text: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    prompt = f"""
    Сделай общее саммари по содержимому папки.
    Определи:
    - Количество файлов 
    - О чем текст каждого файла
    - Дай названия каждому файлу в соответствии с их содержимым

    Вот содержимое:

    {text[:12000]}
    """

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "Ты помощник для анализа кода и документов."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.3,
    }

    response = requests.post(
        OPENROUTER_URL,
        headers=headers,
        json=payload,
    )

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
