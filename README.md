# Video to Audio Converter

A simple tool to convert video files to audio (MP3) using Python, FFmpeg, and CustomTkinter.

## Features

- **Convert Videos to MP3:** Extract audio from video files in various formats (MP4, MKV, AVI).
- **Set Audio Bitrate:** Customize audio bitrate for output MP3 files.
- **Display Conversion Progress:** Real-time progress update during conversion.
- **User-Friendly Interface:** Built with CustomTkinter for an enhanced user experience.

## Requirements

- **Python 3.x**
- **FFmpeg**
- **customtkinter**

## Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/your-user/video-to-audio-converter.git
    cd video-to-audio-converter
    ```

2. **Install the Required Packages:**

    Make sure you have Python installed. Then, install FFmpeg and CustomTkinter:

    - **FFmpeg:** Download and install FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html).
    - **CustomTkinter:** Install via pip:

      ```sh
      pip install customtkinter
      ```

## Usage

1. **Run the Application:**

    ```sh
    python main.py
    ```

2. **Using the GUI:**
    - Click on `Browse` next to "Select Input Video File" to choose a video file (MP4, MKV, AVI).
    - Click on `Browse` next to "Select Output Audio File" to choose the location and name for the output MP3 file.
    - Optionally, set the desired audio bitrate (e.g., `192k`) in the "Set Audio Bitrate" field.
    - Click `Convert` to start the conversion process.
    - The conversion progress will be displayed in real-time in the status area.

## Contributing

Contributions are welcome! If you find any issues or want to contribute enhancements, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
