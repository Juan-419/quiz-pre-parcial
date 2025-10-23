from sqlmodel import Field, SQLModel


class bus (SQLModel, table=True)
    id: int | None = Field(default=None, primary_key=True)
    placa:
    conductor: