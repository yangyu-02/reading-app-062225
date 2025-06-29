"""Application configuration using environment variables."""

import os
from pathlib import Path


class Settings:
    """Application settings loaded from environment variables."""

    # Application
    app_name: str = os.getenv("APP_NAME", "Reading App")
    app_version: str = os.getenv("APP_VERSION", "0.1.0")
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    environment: str = os.getenv("ENVIRONMENT", "production")

    # Database
    database_url: str = os.getenv("DATABASE_URL", "")

    # Redis
    redis_url: str = os.getenv("REDIS_URL", "")

    # Authentication & Security
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "")
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM", "HS256")
    jwt_expire_minutes: int = int(os.getenv("JWT_EXPIRE_MINUTES", "30"))
    jwt_refresh_expire_minutes: int = int(
        os.getenv("JWT_REFRESH_EXPIRE_MINUTES", "10080")
    )

    # Password hashing
    password_salt_rounds: int = int(os.getenv("PASSWORD_SALT_ROUNDS", "12"))

    # API Configuration
    api_v1_prefix: str = os.getenv("API_V1_PREFIX", "/api/v1")

    @property
    def cors_origins(self) -> list[str]:
        """Parse CORS origins from environment variable."""
        origins = os.getenv("CORS_ORIGINS", "*")
        if origins == "*":
            return ["*"]
        return [origin.strip() for origin in origins.split(",")]

    # File Upload (Future)
    aws_access_key_id: str = os.getenv("AWS_ACCESS_KEY_ID", "")
    aws_secret_access_key: str = os.getenv("AWS_SECRET_ACCESS_KEY", "")
    aws_region: str = os.getenv("AWS_REGION", "us-east-1")
    s3_bucket_name: str = os.getenv("S3_BUCKET_NAME", "")

    # AI Services (Future)
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")

    # Development
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


# Load environment variables from .env file if it exists
def load_env_file():
    """Load environment variables from .env file."""
    env_path = Path(".env")
    if env_path.exists():
        with env_path.open() as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ[key] = value.strip('"')


# Load .env file and create settings instance
load_env_file()
settings = Settings()
