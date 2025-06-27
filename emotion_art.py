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

# Screen dimensions (initial, but will be dynamic)
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)

# UI Colors
BUTTON_BG = (240, 240, 240)
BUTTON_HOVER = (200, 200, 200)
BUTTON_TEXT = (50, 50, 50)
BUTTON_BORDER_RADIUS = 10

# Modern color palette
SIDEBAR_BG = (245, 248, 255)
SIDEBAR_ACCENT = (120, 170, 255)
SIDEBAR_SHADOW = (180, 200, 230)
ART_SHADOW = (180, 200, 230, 60)

# Emotion color palettes
EMOTION_PALETTES = {
    "Happy": [(255, 223, 0), (255, 117, 24), (255, 236, 179), (252, 194, 0), (255, 138, 101)],
    "Sad": [(66, 134, 244), (123, 175, 222), (52, 73, 94), (174, 182, 191), (129, 164, 205)],
    "Angry": [(194, 24, 7), (255, 71, 26), (120, 40, 31), (255, 99, 97), (183, 65, 14)],
    "Calm": [(144, 224, 239), (33, 150, 243), (171, 235, 198), (83, 160, 255), (129, 212, 250)],
    "Excited": [(255, 0, 110), (131, 56, 236), (58, 134, 255), (255, 159, 243), (253, 230, 138)]
}

# Emotion music tracks (actual sound files)
MUSIC_FILES = {
    "Happy": "happy-kids-background-music-364459.mp3",
    "Sad": "sad-dramatic-piano-sad-alone-drama-262415.mp3",
    "Angry": "intense-battle-scene-115478.mp3",
    "Calm": "calm-soft-background-music-357212.mp3",
    "Excited": "exciting-upbeat-background-music-300654.mp3"
}

# Modern font (fallback to Arial if not found)
try:
    font = pygame.font.SysFont('Segoe UI', 24)
    title_font = pygame.font.SysFont('Segoe UI', 40, bold=True)
except:
    font = pygame.font.SysFont('Arial', 24)
    title_font = pygame.font.SysFont('Arial', 40, bold=True)


def draw_gradient_background(surface, top_color, bottom_color):
    """Draw a vertical gradient background"""
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        color = (
            int(top_color[0] * (1 - ratio) + bottom_color[0] * ratio),
            int(top_color[1] * (1 - ratio) + bottom_color[1] * ratio),
            int(top_color[2] * (1 - ratio) + bottom_color[2] * ratio)
        )
        pygame.draw.line(surface, color, (0, y), (WIDTH, y))


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
        # Smooth, flowing elements with improved visuals
        # Add gentle ripple effect
        for _ in range(4):
            center_x = random.randint(100, WIDTH - 100)
            center_y = random.randint(100, HEIGHT - 100)
            max_radius = random.randint(60, 180)
            rings = random.randint(4, 7)

            for i in range(rings):
                radius = max_radius * (i + 1) / rings
                color = random.choice(EMOTION_PALETTES["Calm"])
                alpha = int(255 * (1 - (i / rings) * 0.7))  # Fade out effect
                self.art_elements.append(("ring", center_x, center_y, radius, color, alpha))

        # Add flowing curves
        for _ in range(6):
            points = []
            length = random.randint(200, 400)
            start_x = random.randint(50, WIDTH - 50)
            start_y = random.randint(50, HEIGHT - 50)
            amplitude = random.randint(20, 40)
            frequency = random.uniform(0.2, 0.4)

            for i in range(30):
                progress = i / 29
                x = start_x + length * progress
                y = start_y + amplitude * math.sin(progress * math.pi * frequency * 10)
                points.append((x, y))

            color = random.choice(EMOTION_PALETTES["Calm"])
            thickness = random.randint(3, 8)
            self.art_elements.append(("smooth_curve", points, thickness, color))
            
        # Add floating circles for added serenity
        for _ in range(10):
            x = random.randint(50, WIDTH - 50)
            y = random.randint(50, HEIGHT - 50)
            size = random.randint(10, 25)
            color = random.choice(EMOTION_PALETTES["Calm"])
            alpha = random.randint(100, 180)
            self.art_elements.append(("circle_fade", x, y, size, color, alpha))

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
                pygame.gfxdraw.filled_circle(surface, int(x), int(y), int(size), color)
                pygame.gfxdraw.aacircle(surface, int(x), int(y), int(size), color)
            elif element[0] == "polygon":
                _, points, color = element
                int_points = [(int(px), int(py)) for px, py in points]
                pygame.gfxdraw.filled_polygon(surface, int_points, color)
                pygame.gfxdraw.aapolygon(surface, int_points, color)
            elif element[0] == "curve":
                _, points, thickness, color = element
                if len(points) > 1:
                    int_points = [(int(px), int(py)) for px, py in points]
                    pygame.draw.lines(surface, color, False, int_points, int(thickness))
            elif element[0] == "line":
                _, x1, y1, x2, y2, thickness, color = element
                pygame.draw.line(surface, color, (int(x1), int(y1)), (int(x2), int(y2)), int(thickness))
            elif element[0] == "ring":
                _, x, y, radius, color, alpha = element
                r = int(radius)
                temp_surface = pygame.Surface((r * 2 + 4, r * 2 + 4), pygame.SRCALPHA)
                pygame.gfxdraw.filled_circle(temp_surface, r + 2, r + 2, r + 2, (*color, int(alpha // 4)))
                pygame.gfxdraw.aacircle(temp_surface, r + 2, r + 2, r, (*color, int(alpha)))
                surface.blit(temp_surface, (int(x - r - 2), int(y - r - 2)))
            elif element[0] == "circle_fade":
                _, x, y, size, color, alpha = element
                s = int(size)
                temp_surface = pygame.Surface((s * 2 + 4, s * 2 + 4), pygame.SRCALPHA)
                for r in range(s, 0, -1):
                    a = int(alpha * (r / s))
                    pygame.gfxdraw.filled_circle(temp_surface, s + 2, s + 2, r, (*color, a))
                surface.blit(temp_surface, (int(x - s - 2), int(y - s - 2)))
            elif element[0] == "smooth_curve":
                _, points, thickness, color = element
                if len(points) > 1:
                    int_points = [(int(px), int(py)) for px, py in points]
                    pygame.draw.lines(surface, color, False, int_points, int(thickness))
            elif element[0] == "particle":
                _, x, y, size, color, _, _ = element
                pygame.gfxdraw.filled_circle(surface, int(x), int(y), int(size), color)
                pygame.gfxdraw.aacircle(surface, int(x), int(y), int(size), color)
            elif element[0] == "rotated_rect":
                _, x, y, width, height, rotation, color = element
                w, h = int(width), int(height)
                temp_surface = pygame.Surface((w, h), pygame.SRCALPHA)
                pygame.draw.rect(temp_surface, color, (0, 0, w, h))
                rotated = pygame.transform.rotate(temp_surface, float(rotation) * 180 / math.pi)
                surface.blit(rotated, (int(x - rotated.get_width() // 2), int(y - rotated.get_height() // 2)))

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


def draw_button(surface, x, y, width, height, text, color, hover_color, text_color=BUTTON_TEXT):
    mouse_pos = pygame.mouse.get_pos()
    clicked = False
    is_hovered = x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height

    # Create button surface with alpha for smooth edges
    button_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    
    # Draw button with rounded corners
    if is_hovered:
        pygame.draw.rect(button_surface, (*hover_color, 255), (0, 0, width, height), border_radius=BUTTON_BORDER_RADIUS)
        if pygame.mouse.get_pressed()[0]:
            clicked = True
    else:
        pygame.draw.rect(button_surface, (*color, 255), (0, 0, width, height), border_radius=BUTTON_BORDER_RADIUS)

    # Add subtle shadow effect
    shadow_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    pygame.draw.rect(shadow_surface, (0, 0, 0, 30), (2, 2, width, height), border_radius=BUTTON_BORDER_RADIUS)
    surface.blit(shadow_surface, (x, y))

    # Draw button
    surface.blit(button_surface, (x, y))

    # Draw button text with slight shadow for depth
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=(x + width // 2, y + height // 2))
    surface.blit(text_surf, text_rect)

    return clicked


# Load icons (optional, fallback to text if not found)
def load_icon(path, size):
    try:
        icon = pygame.image.load(path)
        icon = pygame.transform.smoothscale(icon, (size, size))
        return icon
    except:
        return None


def draw_sidebar(surface, width, height, selected_emotion, music_on, on_emotion, on_music, on_save, can_save, sidebar_width=240):
    # Sidebar background
    sidebar = pygame.Surface((sidebar_width, height), pygame.SRCALPHA)
    pygame.draw.rect(sidebar, SIDEBAR_BG, (0, 0, sidebar_width, height), border_radius=0)
    # Sidebar shadow
    shadow = pygame.Surface((12, height), pygame.SRCALPHA)
    pygame.draw.rect(shadow, SIDEBAR_SHADOW, (0, 0, 12, height), border_radius=0)
    surface.blit(shadow, (sidebar_width, 0))
    surface.blit(sidebar, (0, 0))

    # Title at the very top, centered
    title = title_font.render("Emotion Art", True, (40, 60, 120))
    title_x = (sidebar_width - title.get_width()) // 2
    title_y = 24
    surface.blit(title, (title_x, title_y))

    # Emotion buttons start below the title
    button_y = title_y + title.get_height() + 32
    button_h = 48
    button_gap = 18
    button_w = sidebar_width - 50
    for emotion in EMOTION_PALETTES.keys():
        is_selected = (emotion == selected_emotion)
        btn_color = EMOTION_PALETTES[emotion][0] if is_selected else BUTTON_BG
        btn_text_color = (255, 255, 255) if is_selected else BUTTON_TEXT
        if draw_button(surface, 25, button_y, button_w, button_h, emotion, btn_color, SIDEBAR_ACCENT, btn_text_color):
            on_emotion(emotion)
        button_y += button_h + button_gap

    # Music toggle and save button below emotion buttons
    action_gap = 24
    music_btn_y = button_y + action_gap
    if draw_button(surface, 25, music_btn_y, button_w, 40, "Music: ON" if music_on else "Music: OFF", BUTTON_BG, (100, 200, 100) if music_on else (200, 100, 100), BUTTON_TEXT):
        on_music()
    save_btn_y = music_btn_y + 40 + 14
    if can_save and draw_button(surface, 25, save_btn_y, button_w, 40, "Save Artwork", BUTTON_BG, (100, 100, 200), BUTTON_TEXT):
        on_save()

    # Instructions at the very bottom
    instr_font = pygame.font.SysFont('Segoe UI', 16)
    instr1 = instr_font.render("ESC: Hide/Show UI", True, (80, 80, 80))
    instr2 = instr_font.render("M: Toggle Music", True, (80, 80, 80))
    instr3 = instr_font.render("S: Save Artwork", True, (80, 80, 80))
    instr_height = instr1.get_height() + instr2.get_height() + instr3.get_height() + 16
    instr_y = height - instr_height - 18
    surface.blit(instr1, (25, instr_y))
    surface.blit(instr2, (25, instr_y + instr1.get_height() + 4))
    surface.blit(instr3, (25, instr_y + instr1.get_height() + instr2.get_height() + 8))


def main():
    clock = pygame.time.Clock()
    generator = EmotionArtGenerator()
    running = True
    show_sidebar = True
    save_message = None
    save_message_time = 0
    gradient_top = (230, 245, 255)
    gradient_bottom = (180, 210, 255)

    # Initialize screen locally in main
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Emotion-Based Art Generator")

    def on_emotion(emotion):
        generator.generate_art(emotion)
        # Play music if enabled and file exists
        mixer.music.stop()
        if generator.music_enabled and emotion in MUSIC_FILES and os.path.exists(MUSIC_FILES[emotion]):
            try:
                mixer.music.load(MUSIC_FILES[emotion])
                mixer.music.play(-1)
            except Exception as e:
                print(f"Music error: {e}")

    def on_music():
        generator.music_enabled = not generator.music_enabled
        if not generator.music_enabled:
            mixer.music.stop()
        elif generator.current_emotion:
            on_emotion(generator.current_emotion)

    def on_save():
        nonlocal save_message, save_message_time
        filename = generator.save_artwork()
        save_message = f"Saved as {filename}"
        save_message_time = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_sidebar = not show_sidebar
                    if not show_sidebar:
                        mixer.music.stop()
                elif event.key == pygame.K_m:
                    on_music()
                elif event.key == pygame.K_s:
                    if generator.current_emotion:
                        on_save()
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

        WIDTH, HEIGHT = screen.get_size()
        sidebar_width = 240 if show_sidebar else 0
        art_x = sidebar_width
        art_w = WIDTH - sidebar_width
        art_h = HEIGHT

        draw_gradient_background(screen, gradient_top, gradient_bottom)
        if generator.current_emotion in ["Excited"]:
            generator.update()

        art_shadow = pygame.Surface((art_w + 16, art_h + 16), pygame.SRCALPHA)
        pygame.draw.rect(art_shadow, ART_SHADOW, (8, 8, art_w, art_h), border_radius=24)
        screen.blit(art_shadow, (art_x - 8, -8))
        art_surface = screen.subsurface((art_x, 0, art_w, art_h))
        generator.draw(art_surface)

        if show_sidebar:
            draw_sidebar(screen, WIDTH, HEIGHT, generator.current_emotion, generator.music_enabled, on_emotion, on_music, on_save, generator.current_emotion is not None, sidebar_width)

        if save_message and pygame.time.get_ticks() - save_message_time < 3000:
            msg_surf = font.render(save_message, True, (30, 30, 30))
            pygame.draw.rect(screen, (255, 255, 255), (art_x + 40, HEIGHT - 60, msg_surf.get_width() + 20, 40), border_radius=10)
            screen.blit(msg_surf, (art_x + 50, HEIGHT - 50))
        else:
            save_message = None

        pygame.display.flip()
        clock.tick(60)

    mixer.music.stop()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()