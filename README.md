# OBS Lyrics Plugin

## Introduction

The OBS Lyrics Plugin allows you to display lyrics with a background image in your OBS streams. It supports loading lyrics from text files, customizable text styling, and easy navigation through lyrics during your stream.

## Features

- **Background Image Support**: Display lyrics over any image background
- **Flexible Lyrics Loading**: Load from a folder of .txt files or select individual files
- **Text Customization**:
  - Font selection, size, and weight
  - Text color with transparency support
  - Outline with customizable size and color
  - Shadow effects with offset control
- **Text Positioning**:
  - Horizontal alignment: Left, Center, Right
  - Vertical alignment: Top, Center, Bottom
  - Customizable text bounding box with word wrapping
- **Navigation Controls**:
  - Next/Previous buttons in source toolbar
  - Show/Hide text functionality
  - Hotkey support for all controls

## Installation

1. Download the latest release for your platform
2. Copy the plugin files to your OBS plugins directory:
   - **Windows**: `C:\Program Files\obs-studio\obs-plugins\64bit`
   - **macOS**: `/Library/Application Support/obs-studio/plugins`
   - **Linux**: `/usr/lib/obs-plugins`
3. Restart OBS Studio

## Usage

### Adding the Lyrics Source

1. In OBS, click the **+** button in Sources
2. Select **Lyrics Display** from the list
3. Give your source a name and click OK

### Configuring the Source

In the properties window, you can configure:

1. **Background Image**: Click Browse to select an image file that will serve as the background
2. **Lyrics Files**:
   - Check **Use Folder** to select a folder containing .txt files
   - Uncheck to select individual .txt files
3. **Text Position**:
   - Set horizontal and vertical alignment
   - Configure text width and height for word wrapping
4. **Text Style**:
   - Choose font, size, and weight
   - Set text color
   - Enable/configure outline and shadow effects

### Lyrics File Format

Create .txt files with your lyrics following this format:
- Each line in the file represents one slide/screen of lyrics
- Empty lines are ignored
- File names will be used as song titles

Example lyrics file (`amazing-grace.txt`):
```
Amazing grace, how sweet the sound
That saved a wretch like me
I once was lost, but now am found
Was blind, but now I see
```

### Navigation Controls

Once configured, you'll find three buttons in the source toolbar:
- **Previous**: Go to the previous lyric line (or previous song if at the beginning)
- **Show/Hide**: Toggle lyrics visibility (background remains visible)
- **Next**: Go to the next lyric line (or next song if at the end)

### Hotkeys

You can assign hotkeys for navigation in OBS Settings > Hotkeys:
- **Next Lyric**: Move to the next lyric
- **Previous Lyric**: Move to the previous lyric
- **Show/Hide Lyrics**: Toggle lyrics visibility

## Building from Source

### Prerequisites

- CMake 3.28 or higher
- OBS Studio development libraries
- Qt 6.x
- C++ compiler with C++17 support

### Build Instructions

1. Clone the repository
2. Configure the project:
   ```bash
   cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
   ```
3. Build the plugin:
   ```bash
   cmake --build build --config Release
   ```

## Troubleshooting

- **Lyrics not displaying**: Ensure your .txt files are properly formatted and saved in UTF-8 encoding
- **Text cut off**: Increase the text width/height in properties
- **Background not showing**: Check that the image file path is valid and the image format is supported

## License

This plugin is licensed under the GNU General Public License v2.0. See LICENSE for details.
