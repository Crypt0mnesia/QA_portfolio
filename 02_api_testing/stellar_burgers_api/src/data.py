class StatusCodes:
    SUCCESS = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    INTERNAL_SERVER_ERROR = 500


class ResponseMessages:

    USER_EXISTS = {"success": False, "message": "User already exists"}
    MISSING_FIELDS = {"success": False, "message": "Email, password and name are required fields"}
    INVALID_CREDENTIALS = {"success": False, "message": "email or password are incorrect"}
    INGREDIENTS_REQUIRED = {"success": False, "message": "Ingredient ids must be provided"}


class ExpectedResponses:

    SUCCESSFUL_REGISTRATION = (StatusCodes.SUCCESS, None)
    USER_ALREADY_EXISTS = (StatusCodes.FORBIDDEN, ResponseMessages.USER_EXISTS)
    MISSING_REGISTRATION_FIELDS = (StatusCodes.FORBIDDEN, ResponseMessages.MISSING_FIELDS)
    SUCCESSFUL_LOGIN = (StatusCodes.SUCCESS, None)
    INVALID_LOGIN_CREDENTIALS = (StatusCodes.UNAUTHORIZED, ResponseMessages.INVALID_CREDENTIALS)
    SUCCESSFUL_ORDER_CREATION = (StatusCodes.SUCCESS, None)
    ORDER_WITHOUT_INGREDIENTS = (StatusCodes.BAD_REQUEST, ResponseMessages.INGREDIENTS_REQUIRED)
    ORDER_INVALID_INGREDIENT = (StatusCodes.INTERNAL_SERVER_ERROR, None)


class TestData:
    TEST_INGREDIENT_IDS = [
        "61c0c5a71d1f82001bdaaa6d",  # Флюоресцентная булка R2-D3
        "61c0c5a71d1f82001bdaaa72",  # Соус Spicy-X
        "61c0c5a71d1f82001bdaaa6f",  # Мясо бессмертных моллюсков Protostomia
    ]

    INVALID_INGREDIENT_IDS = [
        "invalid_hash_1234567890",
        "61c0c5a71d1f82001bdaaa6d_invalid",
        "non_existent_hash",
    ]


