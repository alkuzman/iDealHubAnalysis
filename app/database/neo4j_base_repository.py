from neo4j.v1 import GraphDatabase, basic_auth


class Neo4jBaseRepository:
    def __init__(self, host, username, password):
        self.username = username
        self.host = host
        self.password = password
        self.driver = GraphDatabase.driver(self.host, auth=basic_auth(self.username, self.password))
        self.session = None

    def open_connection(self):
        self.session = self.driver.session()

    def close_connection(self):
        if self.session is not None:
            self.session.close()

    def query(self, query, parameters=None):
        result = self.session.run(query, parameters)
        return result

