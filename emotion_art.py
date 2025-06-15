import pygame
import sys
import random
import math
from pygame import gfxdraw
import os
from pygame import mixer

# Initialize pygame
pygame.init()
mixer.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Emotion-Based Art Generator")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Emotion color palettes
EMOTION_PALETTES = {
    "Happy": [(255, 223, 0), (255, 117, 24), (255, 236, 179), (252, 194, 0), (255, 138, 101)],
    "Sad": [(66, 134, 244), (123, 175, 222), (52, 73, 94), (174, 182, 191), (129, 164, 205)],
    "Angry": [(194, 24, 7), (255, 71, 26), (120, 40, 31), (255, 99, 97), (183, 65, 14)],
    "Calm": [(144, 224, 239), (33, 150, 243), (171, 235, 198), (83, 160, 255), (129, 212, 250)],
    "Excited": [(255, 0, 110), (131, 56, 236), (58, 134, 255), (255, 159, 243), (253, 230, 138)]
}

# Emotion music tracks (optional - add your own sound files)
MUSIC_FILES = {
    "Happy": "happy_music.mp3",
    "Sad": "sad_music.mp3",
    "Angry": "angry_music.mp3",
    "Calm": "calm_music.mp3",
    "Excited": "excited_music.mp3"
}

# Font
font = pygame.font.SysFont('Arial', 24)
title_font = pygame.font.SysFont('Arial', 36, bold=True)


class EmotionArtGenerator:
    def __init__(self):
        self.current_emotion = None
        self.art_elements = []
        self.bg_color = WHITE
        self.music_enabled = False
        self.save_count = 0

    def generate_art(self, emotion):
        self.current_emotion = emotion
        self.art_elements = []
        self.bg_color = self.get_background_color(emotion)

        # Generate different art elements based on emotion
        if emotion == "Happy":
            self.generate_happy_art()
        elif emotion == "Sad":
            self.generate_sad_art()
        elif emotion == "Angry":
            self.generate_angry_art()
        elif emotion == "Calm":
            self.generate_calm_art()
        elif emotion == "Excited":
            self.generate_excited_art()

        # Play corresponding music if available
        if self.music_enabled and emotion in MUSIC_FILES:
            try:
                mixer.music.load(MUSIC_FILES[emotion])
                mixer.music.play(-1)  # Loop indefinitely
            except:
                pass

    def get_background_color(self, emotion):
        # Return a light version of the first color in the palette
        base_color = EMOTION_PALETTES[emotion][0]
        return tuple(min(255, c + 100) for c in base_color)

    def generate_happy_art(self):
        # Bright, bubbly elements
        for _ in range(15):
            x = random.randint(50, WIDTH - 50)
            y = random.randint(50, HEIGHT - 50)
            size = random.randint(20, 80)
            color = random.choice(EMOTION_PALETTES["Happy"])
            self.art_elements.append(("circle", x, y, size, color))

        for _ in range(10):
            points = []
            for _ in range(5):
                x = random.randint(100, WIDTH - 100)
                y = random.randint(100, HEIGHT - 100)
                points.append((x, y))
            color = random.choice(EMOTION_PALETTES["Happy"])
            self.art_elements.append(("polygon", points, color))

    def generate_sad_art(self):
        # Flowing, melancholic elements
        for _ in range(8):
            start_x = random.randint(100, WIDTH - 100)
            start_y = random.randint(100, HEIGHT - 100)
            length = random.randint(100, 300)
            thickness = random.randint(2, 8)
            color = random.choice(EMOTION_PALETTES["Sad"])
            segments = []

            for i in range(20):
                seg_x = start_x + (length / 20) * i
                seg_y = start_y + random.randint(-30, 30)
                segments.append((seg_x, seg_y))

            self.art_elements.append(("curve", segments, thickness, color))

    def generate_angry_art(self):
        # Sharp, jagged elements
        for _ in range(12):
            center_x = random.randint(100, WIDTH - 100)
            center_y = random.randint(100, HEIGHT - 100)
            size = random.randint(30, 100)
            points = []
            spikes = random.randint(3, 8)

            for i in range(spikes * 2):
                angle = (i * math.pi / spikes) + random.uniform(-0.2, 0.2)
                radius = size if i % 2 == 0 else size * 0.5
                x = center_x + radius * math.cos(angle)
                y = center_y + radius * math.sin(angle)
                points.append((x, y))

            color = random.choice(EMOTION_PALETTES["Angry"])
            self.art_elements.append(("polygon", points, color))

        for _ in range(15):
            x1 = random.randint(0, WIDTH)
            y1 = random.randint(0, HEIGHT)
            x2 = random.randint(0, WIDTH)
            y2 = random.randint(0, HEIGHT)
            thickness = random.randint(1, 5)
            color = random.choice(EMOTION_PALETTES["Angry"])
            self.art_elements.append(("line", x1, y1, x2, y2, thickness, color))

    def generate_calm_art(self):
        # Smooth, flowing elements
        for _ in range(5):
            center_x = random.randint(100, WIDTH - 100)
            center_y = random.randint(100, HEIGHT - 100)
            max_radius = random.randint(50, 150)
            rings = random.randint(3, 6)

            for i in range(rings):
                radius = max_radius * (i + 1) / rings
                color = random.choice(EMOTION_PALETTES["Calm"])
                alpha = random.randint(100, 200)
                self.art_elements.append(("ring", center_x, center_y, radius, color, alpha))

        for _ in range(8):
            points = []
            length = random.randint(150, 300)
            start_x = random.randint(100, WIDTH - 100)
            start_y = random.randint(100, HEIGHT - 100)

            for i in range(20):
                x = start_x + (length / 20) * i
                y = start_y + 30 * math.sin(i * 0.5) + random.randint(-10, 10)
                points.append((x, y))

            color = random.choice(EMOTION_PALETTES["Calm"])
            thickness = random.randint(2, 6)
            self.art_elements.append(("smooth_curve", points, thickness, color))

    def generate_excited_art(self):
        # Energetic, vibrant elements
        for _ in range(20):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            size = random.randint(5, 15)
            color = random.choice(EMOTION_PALETTES["Excited"])
            speed = random.uniform(0.02, 0.1)
            direction = random.uniform(0, 2 * math.pi)
            self.art_elements.append(("particle", x, y, size, color, speed, direction))

        for _ in range(10):
            x = random.randint(50, WIDTH - 50)
            y = random.randint(50, HEIGHT - 50)
            width = random.randint(30, 100)
            height = random.randint(30, 100)
            rotation = random.uniform(0, math.pi)
            color = random.choice(EMOTION_PALETTES["Excited"])
            self.art_elements.append(("rotated_rect", x, y, width, height, rotation, color))

    def update(self):
        # Update any animated elements
        updated_elements = []

        for element in self.art_elements:
            if element[0] == "particle":
                _, x, y, size, color, speed, direction = element
                # Move particle
                x += speed * math.cos(direction) * 10
                y += speed * math.sin(direction) * 10

                # Bounce off edges
                if x < 0 or x > WIDTH:
                    direction = math.pi - direction
                if y < 0 or y > HEIGHT:
                    direction = -direction

                updated_elements.append(("particle", x, y, size, color, speed, direction))
            else:
                updated_elements.append(element)

        self.art_elements = updated_elements

    def draw(self, surface):
        surface.fill(self.bg_color)

        for element in self.art_elements:
            if element[0] == "circle":
                _, x, y, size, color = element
                pygame.gfxdraw.filled_circle(surface, int(x), int(y), size, color)
                pygame.gfxdraw.aacircle(surface, int(x), int(y), size, color)

            elif element[0] == "polygon":
                _, points, color = element
                pygame.gfxdraw.filled_polygon(surface, points, color)
                pygame.gfxdraw.aapolygon(surface, points, color)

            elif element[0] == "curve":
                _, points, thickness, color = element
                if len(points) > 1:
                    pygame.draw.lines(surface, color, False, points, thickness)

            elif element[0] == "line":
                _, x1, y1, x2, y2, thickness, color = element
                pygame.draw.line(surface, color, (x1, y1), (x2, y2), thickness)

            elif element[0] == "ring":
                _, x, y, radius, color, alpha = element
                temp_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
                pygame.gfxdraw.circle(temp_surface, radius, radius, radius, (*color, alpha))
                surface.blit(temp_surface, (x - radius, y - radius))

            elif element[0] == "smooth_curve":
                _, points, thickness, color = element
                if len(points) > 1:
                    pygame.draw.lines(surface, color, False, points, thickness)

            elif element[0] == "particle":
                _, x, y, size, color, _, _ = element
                pygame.gfxdraw.filled_circle(surface, int(x), int(y), size, color)
                pygame.gfxdraw.aacircle(surface, int(x), int(y), size, color)

            elif element[0] == "rotated_rect":
                _, x, y, width, height, rotation, color = element
                temp_surface = pygame.Surface((width, height), pygame.SRCALPHA)
                pygame.draw.rect(temp_surface, color, (0, 0, width, height))
                rotated = pygame.transform.rotate(temp_surface, rotation * 180 / math.pi)
                surface.blit(rotated, (x - rotated.get_width() // 2, y - rotated.get_height() // 2))

    def save_artwork(self):
        # Save current artwork as PNG
        self.save_count += 1
        filename = f"emotion_art_{self.current_emotion}_{self.save_count}.png"

        # Create a surface to render the artwork without UI
        art_surface = pygame.Surface((WIDTH, HEIGHT))
        self.draw(art_surface)

        # Save the surface to file
        pygame.image.save(art_surface, filename)
        return filename


def draw_button(surface, x, y, width, height, text, color, hover_color, text_color=BLACK):
    mouse_pos = pygame.mouse.get_pos()
    clicked = False

    # Check if mouse is over button
    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
        pygame.draw.rect(surface, hover_color, (x, y, width, height))
        if pygame.mouse.get_pressed()[0]:
            clicked = True
    else:
        pygame.draw.rect(surface, color, (x, y, width, height))

    # Draw button text
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=(x + width // 2, y + height // 2))
    surface.blit(text_surf, text_rect)

    return clicked


def main():
    clock = pygame.time.Clock()
    generator = EmotionArtGenerator()
    running = True

    # UI state
    show_emotion_buttons = True
    save_message = None
    save_message_time = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_emotion_buttons = not show_emotion_buttons
                elif event.key == pygame.K_m:
                    generator.music_enabled = not generator.music_enabled
                    if not generator.music_enabled:
                        mixer.music.stop()
                    elif generator.current_emotion:
                        generator.generate_art(generator.current_emotion)
                elif event.key == pygame.K_s:
                    if generator.current_emotion:
                        filename = generator.save_artwork()
                        save_message = f"Saved as {filename}"
                        save_message_time = pygame.time.get_ticks()

        # Update art if animated
        if generator.current_emotion in ["Excited"]:
            generator.update()

        # Draw everything
        generator.draw(screen)

        # Draw UI elements
        if show_emotion_buttons:
            # Draw title
            title = title_font.render("Emotion-Based Art Generator", True, BLACK)
            screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

            # Draw emotion buttons
            button_width, button_height = 150, 50
            button_margin = 20
            start_x = WIDTH // 2 - (2 * button_width + button_margin) // 2
            start_y = 100

            emotions = list(EMOTION_PALETTES.keys())
            for i, emotion in enumerate(emotions):
                row = i // 2
                col = i % 2
                x = start_x + col * (button_width + button_margin)
                y = start_y + row * (button_height + button_margin)

                if draw_button(screen, x, y, button_width, button_height,
                               emotion, GRAY, (*EMOTION_PALETTES[emotion][0], 150), BLACK):
                    generator.generate_art(emotion)

            # Draw music toggle button
            music_text = "Music: ON" if generator.music_enabled else "Music: OFF"
            if draw_button(screen, WIDTH - 160, HEIGHT - 60, 150, 40,
                           music_text, GRAY, (100, 100, 100), BLACK):
                generator.music_enabled = not generator.music_enabled
                if not generator.music_enabled:
                    mixer.music.stop()
                elif generator.current_emotion:
                    generator.generate_art(generator.current_emotion)

            # Draw save button
            if generator.current_emotion and draw_button(screen, 10, HEIGHT - 60, 150, 40,
                                                         "Save Artwork", GRAY, (100, 100, 100), BLACK):
                filename = generator.save_artwork()
                save_message = f"Saved as {filename}"
                save_message_time = pygame.time.get_ticks()

        # Draw save message if exists
        if save_message and pygame.time.get_ticks() - save_message_time < 3000:
            msg_surf = font.render(save_message, True, BLACK)
            pygame.draw.rect(screen, WHITE, (WIDTH // 2 - msg_surf.get_width() // 2 - 10,
                                             HEIGHT - 50, msg_surf.get_width() + 20, 40))
            screen.blit(msg_surf, (WIDTH // 2 - msg_surf.get_width() // 2, HEIGHT - 40))
        else:
            save_message = None

        # Draw instructions
        if show_emotion_buttons:
            instr1 = font.render("Press ESC to hide/show controls", True, BLACK)
            instr2 = font.render("Press M to toggle music", True, BLACK)
            instr3 = font.render("Press S to save artwork", True, BLACK)

            screen.blit(instr1, (10, 10))
            screen.blit(instr2, (10, 40))
            screen.blit(instr3, (10, 70))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()