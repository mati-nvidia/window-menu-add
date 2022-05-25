import omni.ext
import omni.kit.ui

from .window import MyCustomWindow, WINDOW_TITLE


class WindowMenuAddExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        print("[maticodes.example.window.add] WindowMenuAddExtension startup")

        # Note the "Window" part of the path that directs the new menu item to the "Window" menu.
        self._menu_path = f"Window/{WINDOW_TITLE}"
        self._window = None
        self._menu = omni.kit.ui.get_editor_menu().add_item(self._menu_path, self._on_menu_click, True)

    def on_shutdown(self):
        print("[maticodes.example.window.add] WindowMenuAddExtension shutdown")

        omni.kit.ui.get_editor_menu().remove_item(self._menu)
        if self._window is not None:
            self._window.destroy()
            self._window = None

    def _on_menu_click(self, menu, toggled):
        """Handles showing and hiding the window from the 'Windows' menu."""
        if toggled:
            if self._window is None:
                self._window = MyCustomWindow(WINDOW_TITLE, self._menu_path)
            else:
                self._window.show()
        else:
            if self._window is not None:
                self._window.hide()
