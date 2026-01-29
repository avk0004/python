class Vscode:
    def fn(self):
        print("VS code ")
class Pycharam:
    def fn(self):
        print("Py charm")
def run(editor):
    editor.fn()
run(Vscode())
run(Pycharam())