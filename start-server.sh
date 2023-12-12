

export WORKER_CLASS="uvicorn.workers.UvicornWorker"
export WORKERS_NUM=1
export APP_MODULE="apgar_health.main:app"
exec gunicorn -k "$WORKER_CLASS" --workers $WORKERS_NUM $APP_MODULE