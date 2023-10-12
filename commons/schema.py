from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


languages_param = openapi.Parameter(
    "Accept-Language",
    openapi.IN_HEADER,
    description="Translate content to language chosen by its code.",
    type=openapi.IN_HEADER,
)

languages_schema = swagger_auto_schema(manual_parameters=[languages_param])
