from app.object_definition import Object


def word_parse(node):
    word = Object()
    word.word = node.properties["word"]

    return word
