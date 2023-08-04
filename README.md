# YouTube Mashup Generator

This is a Python script for creating a mashup of audio tracks from YouTube videos. The script allows you to specify a search query, then it downloads multiple YouTube videos, extracts their audio, and concatenates the audio tracks into a single output file. The program utilizes the `pytube`, `moviepy`, `glob`, and `youtube_search` libraries, as well as Python's built-in `threading` and `multiprocessing` modules.

## How it works

1. **Input Parameters**

   The script takes command-line arguments to configure its behavior:

   - `singer_name`: The name of the singer for a search query for YouTube videos.
   - `num_videos`: The number of YouTube videos to download and process. (Should be more than 10)
   - `audio_duration`: The duration of the audio clip to be extracted from each video (in seconds). It should be between 20 and 90 seconds.
   - `output_filename`: The output file name for the final mashup audio in mp3 format.

2. **Video Download and Audio Extraction**

   The script searches for YouTube videos based on the input `search_query` using the `YoutubeSearch` library. It then proceeds to download each video in parallel using `threading`. The `pytube` library is used to download the highest resolution stream of each video. After downloading, the script extracts the audio from each video clip using `moviepy` and saves it as a separate mp3 file in the "Audios" directory.

3. **Mashup Generation**

   Once all the audio clips are extracted, the script concatenates them using `moviepy` to create a single audio file representing the mashup. The final audio file is saved in the output specified in the command-line arguments.

## Prerequisites

- Python 3.x
- The following Python libraries must be installed:
  - `pytube`
  - `moviepy`
  - `youtube_search`

  You can install these libraries using pip:
  ```
  pip install pytube moviepy youtube-search-python
  ```

## Usage

Run the script from the command line with the required parameters:

``` 
python Mashup.py <singer_name> <num_videos> <audio_duration> <output_filename>
```

## Notes

- For optimal runtime performance, it is recommended to set `num_videos` equal to the number of CPU cores in your machine. However, the script will run correctly even if this condition is not met.
- The script checks if the `output_filename` ends with `.mp3`. If not, it will display an error message and terminate.
- The "Videos" and "Audios" directories will be created automatically to store the downloaded video files and extracted audio clips, respectively.
- The final mashup audio will be saved with the specified `output_filename` in the current working directory.



