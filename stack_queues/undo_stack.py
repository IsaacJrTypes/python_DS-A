class TextOperations:
    def __init__(self):
        self.input_stack = []
        self.undo_stack = []

    def add_text(self,text):
        for char in text:
            self.input_stack.append(char)
    def delete_text(self):
        if not self.input_stack: return print("No text to remove")
        removed = self.input_stack.pop()
        self.undo_stack.append(removed)
        print("Removed: " + removed)
    def undo(self):
        if not self.undo_stack: return 'No characters to undue'
        get_last_char = self.undo_stack.pop()
        self.input_stack.append(get_last_char)
        print( "Undo: "+ get_last_char)
    def display(self):
        print("text:", "".join(self.input_stack)," undo stack: ","".join(self.undo_stack))
def getInput():
    text = input("Type a word: ").lower().strip()
    return text
def main():
    app = TextOperations()
    app.add_text(getInput())
    app.display()
    app.delete_text()
    app.delete_text()
    app.delete_text()
    app.display()
    app.undo()
    app.display()

main()