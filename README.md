# Lip movement labeling demo

This is a few python scripts used to make a simple video labeling GUI.

## Note
Loading lots of video clips will take a lot of memory and potentially crash the gui (i.e. web browser). To fix this we should add pagination. Currently in `make_clips.py` there is a variable `MAX_CLIPS` that caps the number of clips to save to 10.

## Installing
This code relies on three python libraries. Two are easy to install:  
[jinja2][jinja2] - Used to make the html page.
```
pip install jinja2
```

[bottle][bottle] - A simple web framework. I used it here to make html forms work.
```
pip install bottle
```

One is hard to install:  
[moviepy][moviepy] - Wraps ffmpeg, used by `make_clips.py` to save out video clips. This is the hardest part to install. You need ffmpeg from [here][ffmpeg] installed with libmp3lame enabled. To install ffmpeg I followed the instructions [here][install]. 

Then I had to link to an uninstalled ffmpeg, and install moviepy by hand. This is explained [here][mpinstall]. 

Alternatively, you could ignore `make_clips.py` entirely and just use the ffmpeg cli directly. But I am not too familiar with it and when I tried that technique the videos would not play in my browser (chrome). Your mileage may vary.

## Getting started

First make the clips by running `make_clips.py`. Currently it grabs subclips every 5 seconds. The duration of the subclips is 2 seconds. Modify this if you want it to grab subclips based on our other labels.

```
python make_clips.py /path/to/movie.mp4
```

This will output a whole bunch of video files in `video-labeling-gui/static/` directory. The gui expects the files to be there. The video files will have names of the form `video_%05d.mp4`.

Then to start the gui run:

```
python app.py
```

And in your web browser go to `http://localhost:8080/`. You should set a webpage with the video subclips you just created. Under each video are checkboxes labeled `Lip movement` and `Speech`. To label, just watch each video, and click the appropriate checkboxes.

When you are done click `Submit` at the end of the webpage. This will create two log files:
+ `lip_move.txt`
+ `speech.txt`


### Example lip_move.txt:
```
./static/video_00005.mp4
./static/video_00010.mp4
```

These are all the videos you labeled as having lip movement.

[moviepy]:http://zulko.github.io/moviepy/
[mpinstall]:http://zulko.github.io/moviepy/install.html
[ffmpeg]:https://www.ffmpeg.org/
[jinja2]:http://jinja.pocoo.org/docs/dev/
[bottle]:http://bottlepy.org/docs/dev/index.html
[install]:https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu
