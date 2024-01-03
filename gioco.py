import pygame
import random
import time
from pygame.locals import *

# Definizione della classe Bird (Uccello)
class Bird(pygame.sprite.Sprite):
    def __init__(self, speed, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)

        # Caricamento delle immagini per le diverse fasi del battito d'ala
        self.images =  [pygame.image.load('sprites/bird-1.png').convert_alpha(),
                        pygame.image.load('sprites/bird-2.png').convert_alpha(),
                        pygame.image.load('sprites/bird-3.png').convert_alpha()]

        self.speed = speed  # Velocità dell'uccello
        self.current_image = 0  # Indice dell'immagine attuale
        self.image = pygame.image.load('sprites/bird-1.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)  # Maschera per la collisione precisa

        # Posizione iniziale dell'uccello sullo schermo
        self.rect = self.image.get_rect()
        self.rect[0] = screen_width / 6
        self.rect[1] = screen_height / 2

    # Metodo per l'aggiornamento dell'uccello (movimento e animazione)
    def update(self, gravity):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.speed += gravity  # Applicazione della gravità

        # Aggiornamento dell'altezza dell'uccello
        self.rect[1] += self.speed

    # Metodo per far rimbalzare l'uccello verso l'alto
    def rimbalzo(self, speed):
        self.speed = -speed

    # Metodo chiamato all'inizio del gioco per impostare l'immagine dell'uccello
    def inizio(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

# Definizione della classe Tubo 
class Tubo(pygame.sprite.Sprite):
    def __init__(self, inverted, xpos, ysize, tubo_width, tubo_height, screen_height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('sprites/tubo.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (tubo_width, tubo_height))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - ysize)
        else:
            self.rect[1] = screen_height - ysize

        self.mask = pygame.mask.from_surface(self.image)

    def update(self, game_speed):
        self.rect[0] -= game_speed 

# Definizione della classe Base 
class Base(pygame.sprite.Sprite):
    def __init__(self, xpos, base_width, base_height, screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (base_width, base_height))

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = screen_height - base_height

    def update(self, game_speed):
        self.rect[0] -= game_speed

# Funzione per verificare se lo sprite è fuori dallo schermo
def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

# Funzione per ottenere coppie casuali di tubi (superiore e inferiore)
def get_random_tubi(xpos, tubo_width, tubo_height, screen_height):
    size = random.randint(100, 300)
    tubo_spazio = random.randint(120, 150)
    tubo = Tubo(False, xpos, size, tubo_width, tubo_height, screen_height)
    tubo_invertito = Tubo(True, xpos, screen_height - size - tubo_spazio, tubo_width, tubo_height, screen_height)
    return tubo, tubo_invertito

# Funzione per visualizzare il punteggio
def visualizza_punteggio(punteggio, screen):
    punti_unita = [pygame.image.load('sprites/0.png').convert_alpha(),
                   pygame.image.load('sprites/1.png').convert_alpha(),
                   pygame.image.load('sprites/2.png').convert_alpha(),
                   pygame.image.load('sprites/3.png').convert_alpha(),
                   pygame.image.load('sprites/4.png').convert_alpha(),
                   pygame.image.load('sprites/5.png').convert_alpha(),
                   pygame.image.load('sprites/6.png').convert_alpha(),
                   pygame.image.load('sprites/7.png').convert_alpha(),
                   pygame.image.load('sprites/8.png').convert_alpha(),
                   pygame.image.load('sprites/9.png').convert_alpha()]
    punti_decine = punti_unita
    punti_centinaia = punti_unita
    
    # Estrai le cifre del punteggio
    centinaia = punteggio // 100
    decine = (punteggio % 100) // 10
    unita = punteggio % 10

    # Disegna le cifre sullo schermo
    screen.blit(punti_centinaia[centinaia], (145, 160))
    screen.blit(punti_decine[decine], (185, 160))
    screen.blit(punti_unita[unita], (225, 160))


def main():
    pygame.mixer.init()
    pygame.init()
    
    punteggio = 0
    screen_width = 400
    screen_height = 600
    speed = 20
    gravity = 2.5
    game_speed = 20
    base_width = 2 * screen_width
    base_height = 100
    tubo_width = 80
    tubo_height = 500
    
    volo = 'audio/volo.wav'
    collisione = 'audio/collisione.wav'
    
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Flappy Bird')

    background = pygame.image.load('sprites/background.png')
    background = pygame.transform.scale(background, (screen_width, screen_height))
    img_inizio = pygame.image.load('sprites/inizio.png').convert_alpha()
    img_inizio = pygame.transform.scale(img_inizio, (screen_width, screen_height))
    game_over = pygame.image.load('sprites/game_over.png').convert_alpha()
    
    bird_group = pygame.sprite.Group()
    bird = Bird(speed, screen_width, screen_height)
    bird_group.add(bird)
    base_group = pygame.sprite.Group()

    for i in range (2):
        base = Base(base_width * i, base_width, base_height, screen_height)
        base_group.add(base)
        
    tubo_group = pygame.sprite.Group()
    for i in range (2):
        tubi = get_random_tubi(screen_width * i + 800, tubo_width, tubo_height, screen_height)
        tubo_group.add(tubi[0])
        tubo_group.add(tubi[1])

    clock = pygame.time.Clock()
    inizio = True
    while inizio:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE or event.key == K_UP:
                    bird.rimbalzo(speed)
                    pygame.mixer.music.load(volo)
                    pygame.mixer.music.play()
                    inizio = False

        screen.blit(background, (0, 0))
        screen.blit(img_inizio, (0, 0))

        if is_off_screen(base_group.sprites()[0]):
            base_group.remove(base_group.sprites()[0])

            new_ground = Base(base_width - 20, base_width, base_height, screen_height)
            base_group.add(new_ground)

        bird.inizio()
        base_group.update(game_speed)
        bird_group.draw(screen)
        base_group.draw(screen)
        
        pygame.display.update()

    while True:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE or event.key == K_UP:
                    bird.rimbalzo(speed)
                    pygame.mixer.music.load(volo)
                    pygame.mixer.music.play()

        screen.blit(background, (0, 0))

        if is_off_screen(base_group.sprites()[0]):
            base_group.remove(base_group.sprites()[0])
            new_base = Base(base_width - 20, base_width, base_height, screen_height)
            base_group.add(new_base)

        if is_off_screen(tubo_group.sprites()[0]):
            tubo_group.remove(tubo_group.sprites()[0])
            tubo_group.remove(tubo_group.sprites()[0])
            tubi = get_random_tubi(screen_width * 2, tubo_width, tubo_height, screen_height)
            tubo_group.add(tubi[0])
            tubo_group.add(tubi[1])
            punteggio += 1

        bird_group.update(gravity)
        base_group.update(game_speed)
        tubo_group.update(game_speed)
        bird_group.draw(screen)
        tubo_group.draw(screen)
        base_group.draw(screen)

        pygame.display.update()

        if (pygame.sprite.groupcollide(bird_group, base_group, False, False, pygame.sprite.collide_mask) or
                pygame.sprite.groupcollide(bird_group, tubo_group, False, False, pygame.sprite.collide_mask)):
            pygame.mixer.music.load(collisione)
            pygame.mixer.music.play()
            screen.blit(game_over,(105,100))
            visualizza_punteggio(punteggio, screen)
            pygame.display.update()
            time.sleep(1.5)
            break
    
    print(f"Punteggio: {punteggio}")
    
if __name__ == "__main__":
    main()