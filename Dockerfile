ARG PYTHON_BASE=3.12.0-slim

# Build stage
FROM python:$PYTHON_BASE AS build

COPY pyproject.toml pdm.lock README.md ./

# Install pdm
RUN python -m pip install --upgrade pip setuptools wheel &&\
    pip install pdm

# Install dependencies
RUN pdm install --no-lock --no-editable

# Run stage
FROM python:$PYTHON_BASE

# Copy application files
COPY adapters /adapters
COPY core /core

COPY --from=build /.venv /.venv
ENV PATH="/.venv/bin:{$PATH}"

EXPOSE $PORT

CMD ["sh", "-c", "uvicorn adapters.handlers.rest.app:create_app --factory --host 0.0.0.0 --port $PORT"]