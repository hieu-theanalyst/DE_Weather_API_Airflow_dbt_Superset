# Weather Data Project

This repository contains a weather data pipeline project built with:

- Docker Compose orchestration
- Apache Airflow DAGs for workflow orchestration
- PostgreSQL for local data storage
- Superset configuration for analytics visualization
- dbt for modeling and transformation
- Python scripts for API requests and record insertion

## Repository structure

- `airflow/` - Airflow DAGs and orchestration logic
- `api-request/` - Python scripts for calling APIs and inserting records
- `dbt/` - dbt project and profiles
- `docker/` - Docker helper scripts and Superset configuration
- `postgres/` - local PostgreSQL runtime data and configuration
- `docker-compose.yaml` - Docker Compose service definitions

## Privacy and upload guidance

This repository contains local runtime and environment files that should not be uploaded to GitHub.

Do not commit:

- `.env`
- `docker/.env`
- Local PostgreSQL data directories under `postgres/`
- Local Python virtual environments such as `.venv/`
- Editor or IDE state files

The included `.gitignore` protects these paths.

## Setup

1. Create or activate the Python virtual environment if needed.
2. Add your local secrets and environment variables to `.env` or `docker/.env`.
3. Start services with Docker Compose:

```bash
docker-compose up -d
```

4. Use Airflow and Superset as configured in the project.

## Notes

- The `postgres/` directory in this repository contains PostgreSQL runtime data and should remain excluded from source control.
- If you need to publish the project, keep secret credentials out of version control and only commit code/configuration that is safe to share.

## Recommended cleanup before upload

Before pushing to GitHub, verify that the following files and directories are not committed:

- `.env`, `docker/.env`
- `.venv/`, `__pycache__/`, `*.py[cod]`
- `dbt/my_project/target/`, `dbt/my_project/logs/`
- editor and IDE files such as `.vscode/`, `.idea/`
