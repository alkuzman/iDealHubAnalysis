from app.analyzers.similar_documents import similar_documents
from app.database.neo4j_base_service import get_tags_for_document, get_document_for_title


# This function returns tags for given text
def extract_tags_from_text(text, limit=5):
    list = similar_documents(text, 5) # Find the five most similar documents to the text
    tags = set()  # Set of all tags for the text

    # For every document get the tags it has and add them in the set
    for entry in list:
        document_tags = get_tags_for_document(entry["title"])
        for tag in document_tags:
            tags.add(tag.value)
        if len(tags) == limit:
            break

    return tags


def extract_tags_from_document_content(title):
    return extract_tags_from_text(get_document_for_title(title).content)
