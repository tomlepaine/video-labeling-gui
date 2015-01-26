import argparse

import numpy
from moviepy import editor

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('filepath', help='Path to movie file. Should be mp4.')

args = parser.parse_args()

# MAX_CLIPS = 10  # Remove this for the real thing.

clip = editor.VideoFileClip(args.filepath)

# Logic for determining when to sample. Could be read from file instead.
# In seconds.
duration = clip.duration
times = numpy.arange(0, duration, 5.0)[1::]
# times = numpy.arange(0, duration, 5.0)[1:MAX_CLIPS]

# The sample times are the center of the window.
# This is how much padding to get before and after.
# In seconds.
offset = 1.0

# Generate clips
for i, time in enumerate(times):
    print i
    print time - offset
    print time + offset
    filename = './static/video_%05d.mp4' % round(time)
    subclip = clip.subclip(time - offset, time + offset)
    subclip.write_videofile(filename)