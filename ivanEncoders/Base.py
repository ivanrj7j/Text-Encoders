class TextEncoder:
    """
    Base class for all the encoders
    """
    def __init__(self) -> None:
        self.vocabulary = []
        self.fitted = False
        
    def fit(self, data:list[str]):
        self.fitted = True
        vocabulary = " ".join(data).lower().split()
        vocabulary = list(set(vocabulary))

        self.vocabulary = vocabulary
    
    def transform(self, input:list[str]):
        raise NotImplementedError("Should be implemented by the child")
    
    def fitTransform(self, data:list[str]):
        self.fit(data)
        return self.transform(data)
    
    def getIndexOf(self, token:str):
        return self.vocabulary.index(token)
    
    def getWord(self, index:int):
        return self.vocabulary[index]