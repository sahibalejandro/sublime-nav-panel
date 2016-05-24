import sublime, sublime_plugin
import os

class OpenNavPanelCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Show files and folders within the current path.
        self.show(os.path.dirname(self.view.file_name()))

    def show(self, path):
        # Set the current path and options to display on the quick panel
        self.current_path = path
        self.options = self.populate_options(self.current_path)

        self.view.window().show_quick_panel(self.options, self.on_done)

    def on_done(self, index):
        # If no option is selected then we do nothing.
        if index == -1:
            return

        # The first option means "Go to parent directory".
        if index == 0:
            parent_dir = os.path.dirname(self.current_path)
            self.show(parent_dir)
            return

        # Generate the full path of the selected option.
        file_path = os.path.join(self.current_path, self.options[index])

        # If the selected option is a directory then we display its contents
        # otherwise we open the file.
        if os.path.isdir(file_path):
            self.show(file_path.rstrip('/'))
        else:
            self.view.window().open_file(file_path)

    def populate_options(self, path):
        options = ["../"]
        files = []
        dirs = []

        for entry in os.listdir(path):
            if os.path.isfile(os.path.join(path, entry)):
                files.append(entry)
            else:
                dirs.append(entry + "/")

        return options + dirs + files


