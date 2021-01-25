from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# cloudwatch settings
CLOUDWATCH_AWS_ID = config('CLOUDWATCH_AWS_ID')
CLOUDWATCH_AWS_KEY = config('CLOUDWATCH_AWS_KEY')
AWS_DEFAULT_REGION = config('region')
logger_boto3_session = Session(
    aws_access_key_id=CLOUDWATCH_AWS_ID,
    aws_secret_access_key=CLOUDWATCH_AWS_KEY,
    region_name=AWS_DEFAULT_REGION,
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "aws": {
            "format": "%(asctime)s [%(levelname)-8s] %(message)s [%(pathname)s:%(lineno)d]",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "watchtower": {
            "level": "INFO",
            "class": "watchtower.CloudWatchLogHandler",
            # From step 2
            "boto3_session": logger_boto3_session,
            "log_group": "<<Your log Group>>",
            # Different stream for each environment
            "stream_name": "logs",
            "formatter": "aws",
        },
        "console": {"class": "logging.StreamHandler", "formatter": "aws", },
    },
    "loggers": {
        # Use this logger to send data just to Cloudwatch
        "django": {"level": "INFO", "handlers": ["watchtower"],
                   "propogate": False, }
    },
}
