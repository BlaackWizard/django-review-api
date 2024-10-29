from django.http import HttpRequest
from ninja import (
    Query,
    Router,
)

from core.api.filters import (
    PaginationIn,
    PaginationOut,
)
from core.api.schemas import (
    ApiResponse,
    ListPaginatedResponse,
)
from core.api.v1.products.filters import ProductFilter
from core.api.v1.products.schemas import ProductSchema
from core.apps.customers.containers import get_container
from core.apps.products.services.products import (
    BaseProductServices,
    ORMProductServices,
)


router = Router(tags=['Products'])


@router.get('', response=ApiResponse[ListPaginatedResponse[ProductSchema]])
def get_product_list_handler(
    request: HttpRequest,
    filters: Query[ProductFilter],
    pagination_in: Query[PaginationIn],
) -> ApiResponse[ListPaginatedResponse[ProductSchema]]:
    container = get_container()
    service: BaseProductServices = container.resolve(BaseProductServices)
    product_list = service.get_product_list(filters=filters, pagination=pagination_in)
    product_count = service.get_product_count(filters=filters)
    items = [ProductSchema.from_entity(obj) for obj in product_list]

    pagination = PaginationOut(
        offset=pagination_in.offset,
        limit=pagination_in.limit,
        total=product_count,
    )
    return ApiResponse(data=ListPaginatedResponse(items=items, pagination=pagination))
