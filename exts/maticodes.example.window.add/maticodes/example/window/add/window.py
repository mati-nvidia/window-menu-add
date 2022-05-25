import omni.kit.ui
import omni.ui as ui

WINDOW_TITLE = "My Custom Window"


class MyCustomWindow(ui.Window):
    def __init__(self, title, menu_path):
        super().__init__(title, width=640, height=480)
        self._menu_path = menu_path
        self.set_visibility_changed_fn(self._on_visibility_changed)
        self._build_ui()

    def on_shutdown(self):
        self._win = None

    def show(self):
        self.visible = True
        self.focus()

    def hide(self):
        self.visible = False

    def _build_ui(self):
        with self.frame:
            with ui.VStack():
                ui.Label("This is just an empty window", width=0, alignment=ui.Alignment.CENTER)

    def _on_visibility_changed(self, visible):
        if not visible:
            omni.kit.ui.get_editor_menu().set_value(self._menu_path, False)
