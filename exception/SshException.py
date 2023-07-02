class SshException(Exception):
    def __init__(self, text, value):
        super().__init__(text, value)
        self._value = value
        
    @property
    def value(self):
        return self._value
    def __str__(self):
        return f'{self.args[0]} -> [{self.value}]'