# 🚀 Самый простой способ делать бесплатные видео через GitHub (WAN 2.2 → Hugging Face Space)

Это шаблон-репозиторий. После загрузки в GitHub у вас появится кнопка **Run workflow**, куда вы вбиваете промпт — и через публичный Hugging Face Space (демо) рендерится видео и сохраняется в папку `videos/` прямо в репозитории.

> Важно: нужен любой публичный Space с генерацией видео (например, с WAN 2.2). В workflow вы передаёте `space` — это *slug* Space вида `author/space-name`. Его можно взять из адресной строки страницы Space или из блока **Use via API** (там показан `Client("author/space-name")`).

## ⚡ Как пользоваться (прямо по шагам)

1. **Создайте новый репозиторий на GitHub.** Имя любое, например `video-bot`.
2. **Загрузите содержимое этого архива** в корень репозитория (папки `.github`, `scripts`, `docs`, `videos` и файлы из корня).
3. Зайдите во вкладку **Actions** → нажмите **I understand my workflows… Enable** (если GitHub спросит).
4. В левом списке выберите **Generate WAN2.2 Video (HF Space)** → **Run workflow**.
5. Заполните поля:
   - **space** — slug Space, например `author/space-name` (посмотрите URL страницы Space на Hugging Face).
   - **prompt** — ваш текст запроса (на английском/русском, как указывает Space).
   - **seconds** — длительность видео в секундах (например `5` или `8`). Не все Spaces поддерживают это поле — смотрите блок **Use via API** на странице Space. Если поле не поддерживается, просто оставьте значение по умолчанию или измените скрипт.
6. Нажмите **Run workflow**. Подождите, пока джоб станет **green** (Success).
7. Откройте вкладку **Code** → папку `videos/` → скачайте `output.mp4`.
8. (Опционально) Включите **Pages** в Settings → Pages → **Deploy from a branch**, *Branch*: `main`, *Folder*: `/docs`. Тогда страница `docs/index.html` позволит смотреть видео сразу в браузере (положите файл как `videos/output.mp4` — уже на месте).

## ❓ Где взять Space
1. Зайдите на huggingface.co и в поиске наберите `WAN 2.2` или `text-to-video`.
2. Откройте любой Space (обычно пометка **Spaces • gradio**).
3. Скопируйте **slug** из адресной строки (формат `author/space-name`) или нажмите **Use via API** — там показывают `Client("author/space-name")` и какие параметры принимает Space (prompt, seconds и т.д.).
4. Если очередь длинная или Space недоступен — просто попробуйте другой Space.

## 🧩 Папки и файлы
- `.github/workflows/generate.yaml` — GitHub Actions workflow (кнопка Run workflow).
- `scripts/hf_space_client.py` — скрипт, который обращается к Space по API и сохраняет видео.
- `videos/` — сюда падает `output.mp4` (хранится в вашем репозитории).
- `docs/index.html` — простая страница для GitHub Pages, чтобы проигрывать последнее видео.
- `requirements.txt` — зависимости для Actions.

## 🛠️ Кастомизация
- Если у Space другие имена инпутов (не просто `prompt`/`seconds`) — откройте на его странице блок **Use via API** и поправьте вызов в `hf_space_client.py` (параметр `api_name` и порядок аргументов).

Удачи и красивых роликов! ✨
