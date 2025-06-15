# Emotion-Based Art Generator 🎨✨

A Python application that generates unique abstract art based on selected emotions, using Pygame for visualization.


## Features 🌟

- Generates art for 5 emotions:
  - 😊 Happy (bright, bubbly shapes)
  - 😢 Sad (flowing, melancholic curves)
  - 😠 Angry (sharp, jagged lines)
  - 🧘 Calm (smooth, flowing rings)
  - 🎉 Excited (animated particles)
- Interactive UI with emotion selection buttons
- Save your favorite artworks as PNG files
- Optional background music for each emotion
- Keyboard shortcuts for quick control

## Requirements 🛠️

- Python 3.6+
- Pygame 2.0+

## Installation 📥

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/emotion-art-generator1.git
   cd emotion-art-generator
   ```

2. Install dependencies:
   ```bash
   pip install pygame
   ```

## Usage 🚀

Run the application:
```bash
python emotion_art.py
```

### Controls 🎮
- **Click buttons** to select emotions
- **ESC** - Toggle UI visibility
- **M** - Toggle music on/off
- **S** - Save current artwork

### Adding Music 🎵
Place these files in the project folder:
- `happy_music.mp3`
- `sad_music.mp3`
- `angry_music.mp3`
- `calm_music.mp3`
- `excited_music.mp3`

*(Or edit the `MUSIC_FILES` dictionary in the code to point to your files)*

## Code Structure 🏗️

```
emotion-art-generator/
├── emotion_art.py       # Main application
├── happy_music.mp3      # Example music files
├── saved_art/           # Where artworks are saved
└── README.md            # This file
```

## Customization 🎨

You can easily modify:
- Color palettes in `EMOTION_PALETTES`
- Art generation parameters in each `generate_*_art()` method
- Screen dimensions at the top of the file

## Troubleshooting ⚠️

**Problem**: Black screen after launch  
**Solution**: Click any emotion button to generate art

**Problem**: Music not playing  
**Solution**: 
1. Ensure music files exist and are named correctly
2. Check volume isn't muted
3. Press 'M' to enable music

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Created with ❤️ by Nikita  
Feel free to contribute or customize!
```

### Key Elements Included:
1. Visual Header with emojis and clear project name
2. Feature showcase of the 5 emotions
3. Step-by-step installation instructions
4. Usage instructions with keyboard controls
5. Music setup guidance
6. Troubleshooting common issues
7. Customization suggestions
8. Professional structure with license mention

To use this README:
1. Save as `README.md` in your project folder
2. Replace placeholder text (like GitHub URL and your name)
3. Add a screenshot named `demo_screenshot.png`
4. Commit to your repository

