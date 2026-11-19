from passlib.context import CryptContext

password_content = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def get_password(password: str) -> str:
    return password_content.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return password_content.verify(password, hashed_password)