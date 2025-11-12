from .models import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from .schemas import UserCreateModel
from .utils import generate_password_hash as hash_password


class UserService:
    async def get_user_by_email(self,email:str,session:AsyncSession) -> User | None:
      statement = select(User).where(User.email == email)
      result = await session.execute(statement)
      user = result.scalar_one_or_none()
      return user


    async def user_exists(self,email:str,session:AsyncSession) -> bool:
      user = await self.get_user_by_email(email,session)
      return True if user  is not None else False

    async def create_user(self,user_data:UserCreateModel,session:AsyncSession) -> User:
        user_data_dict = user_data.model_dump()
        user_data_dict["first_name"] = user_data_dict.get("first_name") or ""
        user_data_dict["last_name"] = user_data_dict.get("last_name") or ""

        new_user = User(
           **user_data_dict,
        )  
        new_user.password_hash = hash_password(user_data_dict["password"])
        session.add(new_user)
        await session.commit()  

        return new_user



    
