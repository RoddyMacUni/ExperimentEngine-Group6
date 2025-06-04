class KnownProcessingException(Exception):
    message: str
    experimentId: str

    def __init__(self, message: str, experimentId: str):
        super().__init__(message)
        self.message = message
        self.experimentId = experimentId