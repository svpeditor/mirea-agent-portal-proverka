# mirea-agent-portal-proverka

Агент для платформы [mirea-agent-portal](https://github.com/svpeditor/mirea-agent-portal).

## Что делает

Принимает папку с работами школьников (PDF/DOCX), извлекает текст и отправляет в **DeepSeek-R1** через **OpenRouter** на разбор по чек-листу научной экспертизы:

- Соответствие теме
- Научная новизна
- Качество методологии и эксперимента
- Чёткость и обоснованность результатов
- Оформление и грамотность

На выходе:
- `report.docx` — сводная таблица оценок + топ-3 работы
- `per_work.zip` — отдельное заключение Word по каждой работе

## Параметры

| Поле | Тип | Описание |
|------|-----|----------|
| `competition` | text | Название конкурса (пишется в шапку заключения) |
| `grade_level` | select | Класс участников: 5-7 / 8-9 / 10-11 |
| `works` | folder | Папка с работами (`.pdf`, `.docx`) |

## Раскладка папки `works`

Два варианта:
```
works/Иванов_И/работа.pdf
works/Петров_П/доклад.docx
```
или
```
works/Иванов_И.pdf
works/Петров_П.docx
```

## LLM

Использует ephemeral-токен `OPENROUTER_API_KEY`, который инжектит портал в контейнер агента на запуске. Модель: `deepseek/deepseek-r1` (можно переопределить через env `LLM_MODEL`).

## Локальный запуск

```bash
pip install -r requirements.txt
export OPENROUTER_API_KEY="sk-or-v1-..."
export INPUT_DIR=/tmp/in OUTPUT_DIR=/tmp/out
mkdir -p $INPUT_DIR/works/test1
cp ~/Downloads/work.pdf $INPUT_DIR/works/test1/
python agent.py < params.json
```

## Подключение к порталу

```bash
curl -X POST https://your-portal/api/admin/agents \
  -H 'Cookie: session=...' \
  -d '{"git_url":"https://github.com/svpeditor/mirea-agent-portal-proverka","git_ref":"main"}'
```
