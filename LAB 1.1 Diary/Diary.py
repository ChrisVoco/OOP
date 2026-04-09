class Diary:
    def __init__(self):
        self.entries = []
        self.counter = 0

    def add_entry(self, text):
        self.counter += 1
        entry = f"{self.counter}: {text}"
        self.entries.append(entry)

    def remove_entry(self, index):
        if 0 <= index < len(self.entries):
            self.entries.pop(index)

    def __str__(self):
        return "\n".join(self.entries)
