from queue import Queue
from wikipedia import wikipedia, exceptions
from app.database.database import database


def insert_documents(document_limit, start_document_title, start_document_parent=""):
    counter = 0  # This counter counts the added documents
    visited_links = set()  # This set contains all visited links (documents)
    queue = Queue()  # This queue is used for implementing the BFS algorithm

    database.open_connection()

    start_node = {"title": start_document_title, "parent": start_document_parent}  # Creating the start node
    queue.put(start_node)

    # Start BFS algorithm
    while counter < document_limit:
        node = queue.get()  # Get the current node
        title = node['title']

        # Check if we have visited this link previously
        if title in visited_links:
            continue

        try:
            page = wikipedia.page(title)  # Get Wikipedia page for given title
        except exceptions.DisambiguationError as e:
            page = wikipedia.page(e.options[1])  # If there are multiple pages for that title, choose the first one
        # Add new document and the title as tag in the database for the given page
        database.query("CREATE (doc:Document {title: {title}, content: {content}})-[:TITLE]->"
                       "(tag:Tag:Title {value: {value}})",
                       {"title": title, "content": page.content, "value": title})

        # If there is known page from which we got the current page, create a relationship between the two documents
        if node['parent'] != '':
            database.query(
                "MATCH (doc1:Document {title: {title}}), (doc2:Document {title: {parent}}) "
                "CREATE (doc1)-[:LINK]->(doc2)",
                {"title": title, "parent": node['parent']})

        visited_links.add(title)  # Add the title of the document as visited

        # Pass all the links in the current page
        for link in page.links:
            # If the link is not visited add it in the Queue
            if link not in visited_links:
                queue.put({"title": link, "parent": title})
            # Otherwise add a relationship between the current page and the visited document in the database
            else:
                database.query(
                    "MATCH (doc1:Document {title: {title}}), (doc2:Document {title: {parent}}) "
                    "CREATE (doc1)-[:LINK]->(doc2)",
                    {"title": link, "parent": title})

        counter += 1  # Increase the counter of processed documents

    database.close_connection()
