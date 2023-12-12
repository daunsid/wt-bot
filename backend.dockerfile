FROM python:3.12

WORKDIR /app/

ENV PYTHONPATH=/app

#RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Install poetry version 1
# RUN pip install poetry fastapi uvicorn gunicorn
# RUN poetry config virtualenvs.create false


#COPY ./requirements.txt ./poetry.lock* /app/
#RUN poetry export -f requirements.txt --without-hashes --output /app/requirements.txt
RUN pip install -r requirements.txt

#COPY ./pyproject.toml ./poetry.lock /app/

COPY ./apgar_health .
CMD [ "bash", "/start-server.sh" ]


