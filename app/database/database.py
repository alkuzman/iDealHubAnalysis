from app.database.neo4j_base_repository import Neo4jBaseRepository


database = Neo4jBaseRepository("bolt://localhost:7687", "neo4j", "viki123")