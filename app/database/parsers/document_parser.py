from app.object_definition import Object


def document_parse(node):
    document = Object()
    document.title = node.properties["title"]
    document.content = node.properties["content"]
    document.id = node.id

    return document
