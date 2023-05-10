from functools import partial

import carb
import omni.ext
import omni.kit.ui

from .window import MyCustomWindow, WINDOW_TITLE


class WindowMenuAddExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        carb.log_info("[maticodes.example.window.add] WindowMenuAddExtension startup")

        # Note the "Window" part of the path that directs the new menu item to the "Window" menu.
        self._windows = {
            "My First Window": None,
            "My Second Window": None
        }
        self._menus = []
        for window_title in self._windows:
            menu = omni.kit.ui.get_editor_menu().add_item(f"Window/{window_title}", partial(self._on_menu_click, window_title), True)
            self._menus.append(menu)

    def on_shutdown(self):
        carb.log_info("[maticodes.example.window.add] WindowMenuAddExtension shutdown")

        for menu in self._menus:
            omni.kit.ui.get_editor_menu().remove_item(menu)
        for window_title, window in self._windows.items():
            if window is not None:
                window.destroy()
        self._windows = None
        self._menus = None

    def _on_menu_click(self, window_title, menu, toggled):
        """Handles showing and hiding the window from the 'Windows' menu."""
        if toggled:
            if self._windows[window_title] is None:
                self._windows[window_title] = MyCustomWindow(window_title, menu)
            else:
                self._windows[window_title].show()
        else:
            if self._windows[window_title] is not None:
                self._windows[window_title].hide()
