from ninja import Schema


class ProductFilter(Schema):
    search: str | None = None
