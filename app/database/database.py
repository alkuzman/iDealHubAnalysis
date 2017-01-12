from app.database.neo4j_base_repository import Neo4jBaseRepository
from instance.config import DATABASE_HOST, DATABASE_PASSWORD, DATABASE_USERNAME


database = Neo4jBaseRepository(DATABASE_HOST, DATABASE_USERNAME,
                               DATABASE_PASSWORD)
