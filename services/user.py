from models.user import User
from schemas.user import UserCreate, UserResponse, UserUpdate
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from core.security import get_password, verify_password
from rules.user import check_accronym, check_email

class UserService():

    @staticmethod
    def create_user(user: UserCreate, db: Session) -> User:
        if db.query(User).filter(User.email == user.email).first() is not None:
            raise ValueError("Usuário já cadastrado no sistema.")

        if db.query(User).filter(User.accronym == user.accronym).first():
            raise ValueError("Sigla já utilizada por outro petiano.")

        if not check_accronym(user.accronym, user.name):
            raise ValueError("Sigla fora dos padrões usuais.")

        if not check_email(user.email):
            raise ValueError("Email precisa ser do LABMETRO.")

        user_db = User(
            name=user.name,
            email=user.email,
            password_hash=get_password(user.password),
            accronym=user.accronym
        )

        db.add(user_db)
        db.commit()
        db.refresh(user_db)

        return user_db

    @staticmethod
    def get_user(user_id: int, db: Session) -> User:
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise ValueError("Usuário não encontrado.")

        return user

    @staticmethod
    def update_user(user_id: int, data: UserUpdate, db: Session) -> User:
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise ValueError("Usuário não encontrado.")

        if data.name is not None and check_accronym(user.accronym, data.name):
            user.name = data.name

        if data.email is not None and check_email(data.email):
            user.email = data.email

        if data.accronym is not None and check_accronym(data.accronym, user.name):
            user.accronym = data.accronym

        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def delete_user(user_id: int, db: Session) -> dict:
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise ValueError("Usuário não encontrado.")

        db.delete(user)
        db.commit()

        return {"message": "Usuário removido do sistema com sucesso."}