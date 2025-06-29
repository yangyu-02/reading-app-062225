# Reading App Backend Makefile

.PHONY: help install dev-up dev-down dev-clean dev-logs dev-rebuild format lint test clean

help:  ## Show this help message
	@echo "Reading App Backend Development Commands:"
	@echo ""
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Development Environment

install:  ## Install dependencies
	uv sync

dev-up:  ## Start development services (PostgreSQL + Redis + Backend)
	docker compose up -d
	@echo "✅ Services started:"
	@echo "  - PostgreSQL: localhost:5432"
	@echo "  - Redis: localhost:6379"
	@echo "  - Backend API: http://localhost:8000"
	@echo "  - Backend Health: http://localhost:8000/health"

dev-down:  ## Stop development services
	docker compose down
	@echo "✅ Services stopped"

dev-logs:  ## View development services logs
	docker compose logs -f

dev-rebuild:  ## Rebuild and restart the backend service
	docker compose up -d --build backend

dev-clean:  ## Stop services and remove volumes/networks
	docker compose down -v --remove-orphans
	@echo "✅ Services stopped and volumes removed"

##@ Code Quality

format:  ## Format code with Ruff
	ruff format .
	ruff check . --fix

lint:  ## Lint code with Ruff
	ruff check .

lint-fix:  ## Lint and fix code issues
	ruff check . --fix

##@ Database
##@ Application

run:  ## Run the FastAPI application
	uvicorn core.main:app --reload --host 0.0.0.0 --port 8000

##@ Utilities

clean:  ## Clean up cache files
	find . -type d -name __pycache__ -delete
	find . -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov .ruff_cache 