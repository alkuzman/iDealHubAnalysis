from typing import List, Tuple


class CandidateKeyword(object):
    def __init__(self, pos_tokens: List[Tuple[str, str]]):
        self.pos_tokens = pos_tokens

    def get_pos_tokens(self) -> List[Tuple[str, str]]:
        return self.pos_tokens

    def __str__(self):
        return str(self.pos_tokens)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, CandidateKeyword):
            return False
        if len(self.pos_tokens) != len(o.pos_tokens):
            return False
        for i in range(0, len(self.pos_tokens)):
            if self.pos_tokens[i] != o.pos_tokens[i]:
                return False

        return True

    def __hash__(self) -> int:
        return hash("".join([pos_token[0] for pos_token in self.pos_tokens]))


