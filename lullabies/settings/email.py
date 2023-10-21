from .env import env


AWS_SES_REGION_NAME = env("AWS_SES_REGION_NAME")

EMAIL_BACKEND = "django_ses.SESBackend"
