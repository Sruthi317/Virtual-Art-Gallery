class UserIdNotFoundException(Exception):
    def __init__(self,userid):
        super().__init__(f"User Id {userid} not found.")