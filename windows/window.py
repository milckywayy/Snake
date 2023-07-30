import pygame
import sys


class Window:
    def __init__(self, resolution, fps, caption):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.fps = fps
        self.resolution = (resolution[0], resolution[1])
        self.screen = pygame.display.set_mode(self.resolution, pygame.DOUBLEBUF)
        pygame.display.set_caption(caption)

        self.image_library = {}
        self.UPDATE_BG_EVENT = pygame.USEREVENT + 1
        self.update_bg_event = pygame.event.Event(self.UPDATE_BG_EVENT)

        self.state = None

    def set_state(self, state):
        self.state = state
        pygame.event.post(self.update_bg_event)

    def refresh(self):
        self.update()
        self.clock.tick(self.framerate)

    def get_image(self, path):
        path = get_path(path)

        image = self.image_library.get(path)
        if image is None:
            canon_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canon_path).convert_alpha()
            self.image_library[path] = image
        return image

    def draw_image(self, path, position):
        self.blit(self.get_image(path), position)

    def exit(self, code):
        pygame.display.quit()
        sys.exit(code)

    def update(self):
        pygame.display.update()
        self.clock.tick(self.fps)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == self.UPDATE_BG_EVENT:
                    self.state.draw_static_background(self)
                self.state.handle_event(self, event)
            self.state.draw(self)
            self.update()
