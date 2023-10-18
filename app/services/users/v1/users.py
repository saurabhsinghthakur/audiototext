"""Users"""
from passlib.context import CryptContext
from app.libraries.database import Dao

class Users():
    """Users"""
    def __init__(self, body) -> None:
        self.body = body
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.conn = Dao().conn()

    def post(self):
        """Create User"""
        # username = self.body.get('username')
        # hashed_password = self.pwd_context.hash(self.body.get('password'))

        # # Await the result of insert_one
        # result = await self.conn.users.insert_one({
        #     "username": username,
        #     "password": hashed_password
        # })

        # # Retrieve the inserted_id from the result
        # inserted_id = result.inserted_id

        return {"username": "username", "id": str("inserted_id")}
