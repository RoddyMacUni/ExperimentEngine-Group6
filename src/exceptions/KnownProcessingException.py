class KnownProcessingException(Exception):
    message: str
    experimentId: str
    ownerId: int
    partner: str

    def __init__(self, experimentId: str, message: str, ownerId: int = -1, partner: str = ""):
        super().__init__(message)
        self.message = message
        self.experimentId = experimentId
        self.ownerId = ownerId
        self.partner = partner