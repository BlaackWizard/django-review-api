from ninja import Router

from .products.handlers import router as product_router

router = Router(tags=['v1'])

router.add_router('products/', product_router)
