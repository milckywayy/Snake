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

    @abstractmethod
    def reset(self, window):
        pass

    @abstractmethod
    def play_sound(self, window):
        pass

    @abstractmethod
    def pause_sound(self, window):
        pass
