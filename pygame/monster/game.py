import random
import pygame
from config import WIN_HEIGHT, WIN_WIDTH


class Game:
    def __init__(self, player, monster_group):
        self.score = 0
        self.round_number = 0
        self.round_time = 0

        self.player = player
        self.monster_group = monster_group
        self.next_level_sound = pygame.mixer.Sound("assets/next_level.wav")
        self.font = pygame.font.Font("assets/Abrushow.ttf", 24)

        blue_monster = pygame.image.load("assets/blue_monster.png")
        green_monster = pygame.image.load("assets/green_monster.png")
        purple_monster = pygame.image.load("assets/purple_monster.png")
        yellow_monster = pygame.image.load("assets/yellow_monster.png")

        self.target_monster_images = [
            blue_monster, green_monster, purple_monster, yellow_monster]
        self.target_monster_type = random.randint(0, 3)
        self.target_monster_image = self.target_monster_images[self.target_monster_type]
        self.target_monster_rect = self.target_monster_image.get_rect()
        self.target_monster_rect.centerx = WIN_WIDTH/2
        self.target_monster_rect.top = 30

    def update(self):
        self.check_collisions()

    def draw(self, display_surface):
        # Define Some Colors with list
        # Render these texts:
        # Score text
        # Lives text
        # round text
        # time text
        # warps_text

        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        PURPLE = (226, 73, 243)
        YELLOW = (243, 157, 20)
        colors = [BLUE, GREEN, PURPLE, YELLOW]

        score_text = self.font.render(
            f"Score: {self.score}", True, (255, 0, 0))
        score_rect = score_text.get_rect()
        score_rect.topleft = (5, 5)
        pygame.draw.rect(
            display_surface, colors[self.target_monster_type], (WIN_WIDTH/2 - 32, 30, 64, 64), 3)
        pygame.draw.rect(
            display_surface, colors[self.target_monster_type], (0, 100, WIN_WIDTH, WIN_HEIGHT-200), 3)

        # and blit theme into the display surface

        # TODO draw rect around monster target
        # pygame.draw.rect(display_surface, )
        # draw rect around arena (game world)
        display_surface.blit(score_text, score_rect)
        display_surface.blit(self.target_monster_image,
                             self.target_monster_rect)

    def check_collisions(self):
        collided_monster = pygame.sprite.spritecollideany(self.player, self.monster_group)
        """
        check if player collides with target => add score
        if collides with wrong monsters => decrese the lives
        """

    def start_new_round(self):
        """starts a new round
           update the score base of round_number
           reset round values

           for first round => 4 monsters  1 * 4
           for second round => 8 monsters 2 * 4
           for third round => 12 monsters 3 * 4


            for i in range():
                self.monster_group.add(Monster())
                self.monster_group.add(Monster())
                self.monster_group.add(Monster())
                self.monster_group.add(Monster())


            

        """
