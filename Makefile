VENV_NAME=venv

.PHONY: install
install:
	@echo "Installing requirements..."
	@. $(VENV_NAME)/bin/activate && pip install -r requirements.txt

.PHONY: createsuperuser
createsuperuser:
	@echo "Creating superuser..."
	@. $(VENV_NAME)/bin/activate && python manage.py createsuperuser --email admin@example.com --username admin

.PHONY: migrate
migrate:
	@echo "Applying migrations..."
	@. $(VENV_NAME)/bin/activate && python manage.py migrate

.PHONY: makemigrations
makemigrations:
	@echo "Creating new migrations..."
	@. $(VENV_NAME)/bin/activate && python manage.py makemigrations

.PHONY: run
run:
	@echo "Starting development server..."
	python manage.py runserver

.PHONY: test
test:
	@echo "Running tests..."
	@. $(VENV_NAME)/bin/activate && python manage.py test

.PHONY: shell
shell:
	@echo "Opening Django shell..."
	@. $(VENV_NAME)/bin/activate && python manage.py shell