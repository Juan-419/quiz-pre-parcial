from sqlmodel import Field, SQLModel

class conductor(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str
    buses: List["Bus"] = Relationship(back_populates="conductor")



class bus (SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    placa: str
    conductor_id: int = Field(foreign_key="conductor.id")
    conductor: Optional[Bus] = Relationship(back_populates="bus")


class destino (SQLModel, table=True):
    id: int =(default=None, primary_key=True)
    lugar: str
    bus_id: int Field(foreign_key="bus.id")