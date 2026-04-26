# Weather Data Pipeline

A Docker Compose-based local weather data ETL pipeline that ingests weather data, transforms it with dbt, and exposes analytics through Superset.

## Overview

This project demonstrates a modern data pipeline using:
- **Apache Airflow** - Orchestration framework for scheduling and monitoring workflows
- **Docker Compose** - Container orchestration for local development
- **PostgreSQL** - Data persistence for raw and transformed data
- **Redis** - Cache layer used by Superset
- **Superset** - Analytics visualization and dashboarding
- **dbt** - Data transformation and modeling
- **Python** - Custom ingestion and insertion logic

## Features

- **Automated Data Ingestion** - Airflow runs data ingestion from the weather service
- **Mock-safe Execution** - Placeholder weather API setup for local development
- **Data Loading** - Stores weather records in PostgreSQL
- **Transformation** - dbt transforms and models ingested data
- **Containerized Environment** - Single-command startup using Docker Compose
- **Web UIs** - Airflow and Superset web interfaces for monitoring and analytics

## Architecture

The pipeline consists of three main stages:

1. **Extract** (`ingest_data_task`)
   - `airflow/dags/orchestrator.py` triggers `api-request/insert_records.py`
   - `api-request/api_request.py` currently provides mock weather data
2. **Transform** (`transform_data_task`)
   - Runs `dbt` inside a Docker container against the PostgreSQL database
3. **Load**
   - `insert_records.py` writes data into `dev.raw_weather_data`
   - Superset can query the same database for dashboards

```
Extract (insert_records.py / mock fetch)
    ↓
Transform (dbt run)
    ↓
Load (PostgreSQL table dev.raw_weather_data)
```

## Prerequisites

- Docker
- Docker Compose
- 4GB minimum available RAM
- Linux, macOS, or Windows with WSL2
- Python (optional, for local development and editing)

## Installation

1. **Clone the repository**
   ```bash
git clone https://github.com/yourusername/weather-data-project.git
cd weather-data-project
```

2. **Create local environment configuration**
   ```bash
cp docker/.env.example docker/.env
```
   If `docker/.env.example` is not present, copy `docker/.env` to a separate local file and keep it out of git.

3. **Start the stack**
   ```bash
docker compose up -d
```

4. **Verify services**
   - Airflow UI: `http://localhost:8000`
   - Superset UI: `http://localhost:8088`

## Configuration

### Environment variables

The project loads runtime configuration from `docker/.env`.

Key variables include:

```bash
POSTGRES_DB=superset_db
POSTGRES_USER=superset
POSTGRES_PASSWORD=superset
DATABASE_USER=superset
DATABASE_PASSWORD=superset
EXAMPLES_USER=examples
EXAMPLES_PASSWORD=examples
SUPERSET_SECRET_KEY=TEST_NON_DEV_SECRET
MAPBOX_API_KEY=''
```

### Database connection

- Airflow uses the local `db` PostgreSQL service
- dbt connects via `dbt/profiles.yml`:
  - host: `db`
  - user: `db_user`
  - password: `db_password`
  - dbname: `db`
  - schema: `dev`

## Usage

### Running the pipeline

1. Open the Airflow UI at `http://localhost:8000`
2. Enable the DAG `weather-api-dbt-orchestrator`
3. Trigger the DAG manually or wait for the scheduled run
4. View task logs and DAG status in Airflow

### Accessing analytics

- Superset UI: `http://localhost:8088`
- Connect Superset to the PostgreSQL service if needed using the credentials from `docker/.env`

### Running dbt manually

```bash
docker compose run --rm dbt
```

## Project Structure

```text
weather-data-project/
├── airflow/                  # Airflow DAG definitions
│   └── dags/orchestrator.py   # Main ETL workflow
├── api-request/              # Python ingestion and DB loading code
│   ├── api_request.py        # Weather API fetch logic (mock-ready)
│   └── insert_records.py     # Database insert and table creation
├── dbt/                      # dbt project and profiles
│   ├── my_project/
│   └── profiles.yml
├── docker/                   # Superset scripts and config
│   ├── docker-init.sh
│   ├── docker-bootstrap.sh
│   ├── superset_config.py
│   └── .env
├── postgres/                 # PostgreSQL init scripts and runtime paths
│   ├── airflow_init.sql
│   └── superset_init.sql
├── docker-compose.yaml       # Service orchestration for local development
└── README.md                 # This file
```

## Development

### Local Python development

If you want to edit the Python code without Docker:

```bash
python3 -m venv venv
source venv/bin/activate
pip install requests psycopg2-binary
```

Then run your scripts against the containerized database if needed.

### Adding a new Airflow task

Edit `airflow/dags/orchestrator.py` and add a new `PythonOperator` or `DockerOperator`.

Example:

```python
from airflow.operators.python import PythonOperator

def my_new_task():
    pass

new_task = PythonOperator(
    task_id='my_new_task',
    python_callable=my_new_task,
    dag=dag,
)

# Set dependencies
existing_task >> new_task
```

## Customization

### Use a real weather API

Replace the placeholder in `api-request/api_request.py` with an environment variable:

```python
import os
api_key = os.getenv('WEATHERSTACK_API_KEY')
```

Then add `WEATHERSTACK_API_KEY` to your local `docker/.env`.

### Change the Airflow schedule

Update the DAG schedule in `airflow/dags/orchestrator.py`:

```python
dag = DAG(
    dag_id='weather-api-dbt-orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=1),
)
```
```

## Troubleshooting

### Container startup issues

```bash
docker compose logs -f
```

If services fail, restart:

```bash
docker compose down
docker compose up --build
```

### Database connection issues

```bash
docker compose exec db psql -U db_user -d db -c 'SELECT 1;'
```

### Airflow issues

If the DAG is not visible, verify the Airflow scheduler and webserver logs.

## Security Best Practices

⚠️ This project is for local development only. Do not use these defaults in production.

- Never commit `docker/.env` or real credentials to GitHub
- Keep `postgres/data/` and other runtime directories out of version control
- Use environment variables for secrets
- Rotate credentials before any public deployment
- Enable HTTPS and secure authentication in production

## Contributing

Contributions are welcome:
1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a pull request

## License

This project does not include a license file. Add a `LICENSE` if you want to define reuse terms.

## Support

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Superset Documentation](https://superset.apache.org/docs/)
- [dbt Documentation](https://docs.getdbt.com/)

## Disclaimer

This repository is intended for learning and development. Respect API terms of service, local laws, and ethical guidelines when using any external data sources.

---

**Last Updated**: April 2026
