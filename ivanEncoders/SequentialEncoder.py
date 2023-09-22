from ivanEncoders import TextEncoder

class SequentialEncoder(TextEncoder):
    def __init__(self) -> None:
        super().__init__()

    def transform(self, input: list[str]):
        if not self.fitted:
            raise LookupError("Use the .fit() method before using this")
        
        sequence = []
        for text in input:
            text = text.lower().split()
            sequence.append([self.getIndexOf(x) for x in text])

        return sequence
            