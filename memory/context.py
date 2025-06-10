class WorkingContext:
    def __init__(self, max_size=5):
        self.max_size = max_size
        self.context = []

    def add(self, entry: str):
        if len(self.context) >= self.max_size:
            self.context.pop(0)
        self.context.append(entry)

    def get_context(self):
        return self.context

    def clear(self):
        self.context = []

    def __str__(self):
        return "\\n".join(self.context)