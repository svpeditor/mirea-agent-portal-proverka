FROM python:3.12-slim

WORKDIR /agent

# Этот Dockerfile используется только для local-dev. Портал генерирует
# свой Dockerfile из manifest.yaml при сборке агента (apps/portal-worker/
# portal_worker/builder/dockerfile_gen.py), portal-sdk инжектится отдельно.

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY agent.py manifest.yaml ./

ENTRYPOINT ["python", "agent.py"]
