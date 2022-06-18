from fastapi import FastAPI, APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from ezeats.token import ACCESS_TOKEN_EXPIRE_MINUTES
from .. import schemas, models, database, hashing, token, cbv
from sqlalchemy.orm import Session

app = FastAPI()

router = APIRouter(
    tags=['Authentication']
)

@cbv.cbv(router)
class Login:
    session: Session = Depends(database.get_db)

    @router.post('/login')
    def login(self, request: schemas.Login):
        user = self.session.query(models.User).filter(models.User.email == request.username).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Email not registered!")
        
        if not hashing.Hash.verify(user.password, request.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Incorrect Password!")

        access_token = token.create_access_token(data={'sub': user.email})
        return {"access token": access_token, "token_type":"bearer"}

app.include_router(router)