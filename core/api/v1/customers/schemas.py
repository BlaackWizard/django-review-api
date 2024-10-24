from ninja import Schema


class TokenOutSchema(Schema):
    token: str

class TokenInSchema(Schema):
    phone: str
    code: str

class AuthInSchema(Schema):
    phone: str

class AuthOutSchema(Schema):
    message: str

