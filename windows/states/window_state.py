from abc import ABC, abstractmethod


class WindowState(ABC):
    @abstractmethod
    def handle_event(self, window, event):
        pass

    @abstractmethod
    def draw(self, window):
        pass

    @abstractmethod
    def draw_static_background(self, window):
        pass
