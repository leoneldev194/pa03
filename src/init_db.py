from src.database import Base, engine
Base.metadata.create_all(bind=engine)
print("¡Tablas creadas exitosamente!")