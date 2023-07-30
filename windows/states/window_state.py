from abc import ABC, abstractmethod


class WindowState(ABC):
    @abstractmethod
    def handle_event(self, window, event):
        pass

    @abstractmethod
    def draw(self, window):
        pass
