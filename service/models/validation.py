class ValidationModel:
    def __init__(self, is_error: bool, error_msg: str) -> None:
        self.is_error = is_error
        self.error_msg = error_msg
