from queue import Queue
from wikipedia import wikipedia, exceptions
from app.database.database import database


def insert_documents(document_limit, start_document_title, start_document_parent=""):
    counter = 0
    visited_links = set()
    queue = Queue()

    database.open_connection()

    start_node = {"title": start_document_title, "parent": start_document_parent}
    queue.put(start_node)
    while counter < document_limit:
        node = queue.get()
        title = node['title']
        try:
            page = wikipedia.page(title)
        except exceptions.DisambiguationError as e:
            page = wikipedia.page(e.options[1])
        database.query("CREATE (doc:Document {title: {title}, content: {content}})",
                       {"title": title, "content": page.content})
        if node['parent'] != '':
            database.query(
                "MATCH (doc1:Document {title: {title}}), (doc2:Document {title: {parent}}) "
                "CREATE (doc1)-[:LINK]->(doc2)",
                {"title": title, "parent": node['parent']})

        for link in page.links:
            if link not in visited_links:
                queue.put({"title": link, "parent": title})
            else:
                database.query(
                    "MATCH (doc1:Document {title: {title}}), (doc2:Document {title: {parent}}) "
                    "CREATE (doc1)-[:LINK]->(doc2)",
                    {"title": link, "parent": title})

        counter += 1

    database.close_connection()
