from django.http import HttpRequest
from ninja import (
    Router,
)
from ninja.errors import HttpError

from core.api.schemas import (
    ApiResponse,

)
from core.api.v1.customers.schemas import AuthOutSchema, AuthInSchema, TokenInSchema, TokenOutSchema
from core.apps.common.exceptions import ServiceException
from core.apps.customers.services.auth import AuthService
from core.apps.customers.services.codes import DjangoCacheCodeServices
from core.apps.customers.services.customers import ORMCustomerServices
from core.apps.customers.services.senders import DummySenderServices

router = Router(tags=['Customers'])


@router.post('auth', response=ApiResponse[AuthOutSchema], operation_id='authorize')
def auth_handler(request: HttpRequest,
                             schema: AuthInSchema) -> ApiResponse[AuthOutSchema]:
    service = AuthService(
        customer_service=ORMCustomerServices(),
        code_service=DjangoCacheCodeServices(),
        sender_service=DummySenderServices(),
    )
    service.authorize(schema.phone)

    return ApiResponse(data=AuthOutSchema(
        message=f"Code sent to {schema.phone}"
    ))

@router.post('confirm', response=ApiResponse[TokenOutSchema], operation_id='confirm_code')
def confirm_handler(request: HttpRequest,
                             schema: TokenInSchema) -> ApiResponse[TokenOutSchema]:
    service = AuthService(
        customer_service=ORMCustomerServices(),
        code_service=DjangoCacheCodeServices(),
        sender_service=DummySenderServices(),
    )
    try:
        token = service.confirm(schema.code, schema.phone)
    except ServiceException as exception:
        raise HttpError(
            status_code=400,
            message=exception.message
        )
    return ApiResponse(data=TokenOutSchema(token=token))

