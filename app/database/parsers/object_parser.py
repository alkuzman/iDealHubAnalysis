from app.object_definition import Object


def document_parse(node):
    document = Object()
    document.title = node.properties["title"]
    document.content = node.properties["content"]
    document.id = node.id

    return document


def word_parse(node):
    word = Object()
    word.word = node.properties["word"]

    return word


def tag_parse(node):
    tag = Object()
    tag.value = node.properties["value"]

    return tag
