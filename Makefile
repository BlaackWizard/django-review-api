DC = docker compose
STORAGE_NAME = postgres-db
APP_NAME = backend-app
APP_FILE = docker-compose/app.yaml
STORAGE_FILE = docker-compose/storages.yaml
ENV = --env-file .env
LOGS = docker logs
MANAGE_PY = python manage.py
EXEC = docker exec -it

.PHONY: storages
storages:
	${DC} -f ${STORAGE_FILE} ${ENV} up -d

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGE_FILE} down

.PHONY: storages-logs
storages-logs:
	${LOGS} ${STORAGE_NAME} -f

.PHONY: app
app:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} ${ENV} up --build -d

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} down

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_NAME} -f

.PHONY: migrate
migrate:
	${EXEC} ${APP_NAME} ${MANAGE_PY} migrate

.PHONY: migrations
migrations:
	${EXEC} ${APP_NAME} ${MANAGE_PY} makemigrations

.PHONY: superuser
superuser:
	${EXEC} ${APP_NAME} ${MANAGE_PY} createsuperuser

.PHONY: collectstatic
collectstatic:
	${EXEC} ${APP_NAME} ${MANAGE_PY} collectstatic

.PHONY: run-tests
run-tests:
	${EXEC} ${APP_NAME} pytest