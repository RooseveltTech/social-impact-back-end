from drf_yasg import openapi

class ApiParams:
    plant_id = openapi.Parameter(
        'plant_id',
        openapi.IN_PATH,
        description="",
        required=True,
        type=openapi.TYPE_STRING,
    )

    blog_id = openapi.Parameter(
        'blog_id',
        openapi.IN_PATH,
        description="",
        required=True,
        type=openapi.TYPE_STRING,
    )

    page = openapi.Parameter(
        'page',
        openapi.IN_PATH,
        description="",
        required=True,
        type=openapi.TYPE_NUMBER,
    )