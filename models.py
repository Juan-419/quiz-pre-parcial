from sqlmodel import Field, SQLModel

class conductor(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str
    buses: List["Bus"] = Relationship(back_populates="conductor")



class bus (SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    placa: str
    conductor: str = Field (foreign_key="")