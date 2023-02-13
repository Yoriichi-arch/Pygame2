import pygame
import sys
import os
import random

left = 1000 // 2 - 630 // 2
top = 700 // 2 - 630 // 2
all_sprites_rect = pygame.sprite.Group()

level1 = '../resources/map.txt'
level2 = '../resources/map2.txt'
level3 = '../resources/map3.txt'
level4 = '../resources/map4.txt'


class Cube(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(left=x, top=y)
        event = False
        move = False

    def move(self, key, spisok, symbols):
        x = self.rect.x
        y = self.rect.y
        coords = f'({x}, {y})'
        if key == 'down':
            coords = f'({x}, {y + 70})'
            if (spisok[3].colliderect(self.rect) is False) and symbols[coords] != '#':
                self.rect.y += 70
        elif key == 'up':
            coords = f'({x}, {y - 70})'
            if (spisok[1].colliderect(self.rect) is False) and symbols[coords] != '#':
                self.rect.y -= 70
        elif key == 'left':
            coords = f'({x - 70}, {y})'
            if (spisok[0].colliderect(self.rect) is False) and symbols[coords] != '#':
                self.rect.x -= 70
        elif key == 'right':
            coords = f'({x + 70}, {y})'
            if (spisok[2].colliderect(self.rect) is False) and symbols[coords] != '#':
                self.rect.x += 70

    def get_coords_cube(self):
        x = self.rect.x
        y = self.rect.y
        return x, y


def load_image(name, colorkey=None):
    fullname = os.path.join('../resources', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Barrier(pygame.sprite.Sprite):
    image = load_image('barrier.png')

    def __init__(self, x, y):
        super().__init__(all_sprites_rect)
        self.image = Barrier.image
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect(left=x, top=y)
        self.mask = pygame.mask.from_surface(self.image)

    def get_coords_cube(self):
        x = self.rect.x
        y = self.rect.y
        coords = (x, y)
        return coords


border_left = pygame.sprite.Sprite()
border_left.image = pygame.Surface([1, 630])
border_left.image.fill(pygame.Color('white'))
border_left.rect = border_left.image.get_rect(left=left, top=top)
border_left.mask = pygame.mask.from_surface(border_left.image)

border_top = pygame.sprite.Sprite()
border_top.image = pygame.Surface([630, 1])
border_top.image.fill(pygame.Color('white'))
border_top.rect = border_top.image.get_rect(left=left, top=top)
border_top.mask = pygame.mask.from_surface(border_left.image)

border_right = pygame.sprite.Sprite()
border_right.image = pygame.Surface([1, 630])
border_right.image.fill(pygame.Color('white'))
border_right.rect = border_right.image.get_rect(left=left + 560, top=top)
border_right.mask = pygame.mask.from_surface(border_left.image)

border_down = pygame.sprite.Sprite()
border_down.image = pygame.Surface([630, 1])
border_down.image.fill(pygame.Color('white'))
border_down.rect = border_down.image.get_rect(left=left, top=top + 560)
border_down.mask = pygame.mask.from_surface(border_left.image)

spisok = [border_left.rect, border_top.rect, border_right.rect, border_down.rect]


class Board:
    # создание поля
    def __init__(self, filename):
        self.left1 = 1000 // 2 - 630 // 2
        self.top1 = 700 // 2 - 630 // 2
        x, y = 70, 70
        self.list_coordinates = []
        self.filename = filename
        for i in range(10):
            s = []
            for j in range(10):
                s.append((x * j + 185, y * i + 35))
            self.list_coordinates.append(s)
        self.slovar = {}
        self.filename = filename
        # читаем уровень, убирая символы перевода строки
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]
        # и подсчитываем максимальную длину
        max_width = max(map(len, level_map))
        # дополняем каждую строку пустыми клетками ('.')
        self.level = list(level_map)
        n = 0
        # создаём словарь с символами и их координатами
        for (i, j) in zip(self.list_coordinates, level_map):
            for (g, h) in zip(i, j):
                self.slovar[str(g)] = h

    def generate_level(self, surface, left, top):
        for y in range(len(self.level)):
            for x in range(len(self.level[y])):
                if self.level[y][x] == '#':
                    barrier = Barrier(left + 70 * x, top + 70 * y)
                    screen.blit(barrier.image, barrier.rect)

    def slov(self):
        return self.slovar

    def spawn_x(self):
        if self.filename == '../resources/map4.txt':
            self.left1 += 70
        return self.left1

    def spawn_y(self):
        return self.top1


def terminate():
    pygame.quit()
    sys.exit()


def check_click(x, y, width, height, position):
    if x <= position[0] <= x + width and y <= position[1] <= y + height:
        return True


def production():
    prod2 = load_image('prod3.png')
    prod = load_image('production.png')
    prod4 = load_image('prod4.png')
    screen.blit(prod, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return
        screen.blit(prod, (0, 0))
        screen.blit(prod2, (1000 // 2 - prod2.get_width() // 2, 100))
        pygame.display.flip()


def production2():
    prod5 = load_image('prod5.png')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return
        screen.blit(prod5, (0, 0))
        pygame.display.flip()


def select_level():
    pass

particles = []


def emit_purticle(x, y, x_vel, y_vel, radius):
    particles.append([[x, y], [x_vel, y_vel], radius])


def update_particle():
    for i, particle in reversed(list(enumerate(particles))):
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1

        reversed_particle = particles[len(particles) - i - 1]
        pygame.draw.circle(screen, 'orange', (int(reversed_particle[0][0]), int(reversed_particle[0][1])),
                           reversed_particle[2])

        if particle[2] <= 0:
            particles.pop(i)


# заставка
def start_screen(screen, width1):
    logo = load_image('Logo.png')
    name = load_image('name.png')
    play = load_image('play.png')
    play2 = load_image('play2.png')
    flag = False
    screen.fill('#5008b7')
    width = play.get_width()
    height = play.get_height()
    x = 1000 // 2 - play.get_width() // 2
    y = 800 // 2 - play.get_height() // 2
    x1 = 1000 // 2 - 210 // 2
    y1 = 700 // 2 - 70 // 2
    screen.blit(logo, (830, 620))
    screen.blit(name, (1000 // 2 - name.get_width() // 2, 400 // 2 - name.get_height() // 2))
    screen.blit(play, (1000 // 2 - play.get_width() // 2, 800 // 2 - play.get_height() // 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not flag and check_click(x, y, width, height, event.pos):
                    screen.blit(play2, (1000 // 2 - play.get_width() // 2, 800 // 2 - play.get_height() // 2))
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                screen.blit(play, (1000 // 2 - play.get_width() // 2, 800 // 2 - play.get_height() // 2))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def score(count):
    font = pygame.font.Font('../resources/helvetica_regular.otf', 20)
    text = font.render(f'Ходы: {count}', 1, 'white')
    screen.blit(text, (40, 40))


def score_final(count):
    font = pygame.font.Font('../resources/helvetica_regular.otf', 20)
    text = font.render(f'Счёт: {count}', 1, 'white')
    screen.blit(text, (1000 // 2 - text.get_width() // 2, 100))


if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    pygame.mixer.music.load('../resources/sound/музыка которая не напрягает.mp3')
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('Puzzle')
    pygame.display.set_icon(pygame.image.load('../resources/cube.png'))
    s = pygame.mixer.Sound('../resources/sound/столкновение.wav')
    production()
    production2()
    key = None
    clock = pygame.time.Clock()
    move = None
    FPS = 60
    side = 70
    width = 1000
    height = 700
    start_screen(screen, width)
    board = Board(level1)
    board.generate_level(screen, left, top)
    cube = Cube(board.spawn_x(), board.spawn_y(), '../resources/cube.png')
    screen.fill('#5008b7')
    pygame.draw.rect(screen, 'white', (left, top, 630, 630))
    count = 0
    count1 = 0
    flag = False
    pygame.draw.rect(screen, 'white', (left, top, 630, 630))
    x2, y2 = 0, 0
    x3, y3 = 0, 0
    xy = []
    n = False
    final = load_image('final.png')
    pygame.mixer.music.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    flag = True
                    key = 'down'
                elif event.key == pygame.K_UP:
                    flag = True
                    key = 'up'
                elif event.key == pygame.K_LEFT:
                    flag = True
                    key = 'left'
                elif event.key == pygame.K_RIGHT:
                    flag = True
                    key = 'right'
        if not n:
            x, y = cube.rect.x, cube.rect.y
            if board.slov()[str((x, y))] == '.':
                board.slov()[str((x, y))] = 'y'
            xy.append((x, y))
            x3, y3 = cube.get_coords_cube()
            if key:
                cube.move(key, spisok, board.slov())
            x2, y2 = cube.rect.x, cube.rect.y

            screen.fill('#5008b7')
            pygame.draw.rect(screen, 'white', (left, top, 630, 630))
            for i in xy:
                pygame.draw.rect(screen, 'yellow', (i[0], i[1], 70, 70))
            all_sprites_rect.draw(screen)
            score(count)
            if flag and x != x2:
                s.play()
                count += 1
            elif flag and y != y2:
                s.play()
                count += 1
            screen.blit(cube.image, cube.rect)

            if key == 'down':
                emit_purticle(x + 5, y, random.uniform(0, 5), -5, 4)
                emit_purticle(x + 35, y, random.uniform(-2, 2), -5, 4)
                emit_purticle(x + 65, y, random.uniform(-5, 0), -5, 4)
                update_particle()
            elif key == 'up':
                emit_purticle(x + 5, y + 70, random.uniform(0, 5), 5, 4)
                emit_purticle(x + 35, y + 70, random.uniform(-2, 2), 5, 4)
                emit_purticle(x + 65, y + 70, random.uniform(-5, 0), 5, 4)
                update_particle()
            elif key == 'left':
                emit_purticle(x + 70, y + 5, 5, random.uniform(0, 5), 4)
                emit_purticle(x + 70, y + 35, 5, random.uniform(-2, 2), 4)
                emit_purticle(x + 70, y + 65, 5, random.uniform(-5, 0), 4)
                update_particle()
            elif key == 'right':
                emit_purticle(x + 0, y + 5, -5, random.uniform(0, 5), 4)
                emit_purticle(x + 0, y + 35, -5, random.uniform(-2, 2), 4)
                emit_purticle(x + 0, y + 65, -5, random.uniform(-5, 0), 4)
                update_particle()
            flag = False
        if n:
            screen.blit(final, (0, 0))
            score_final(count)
        pygame.display.update()
        clock.tick(FPS)
        if '.' not in list(board.slov().values()):
            n = True


