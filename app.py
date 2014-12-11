import glob

from bottle import get, post, request, run, static_file
from jinja2 import Environment, PackageLoader
import numpy

# Renders the video gui.
@get('/')
def index():
    env = Environment(loader=PackageLoader('app', 'templates'))
    template = env.get_template('video.html')

    videos = numpy.sort(glob.glob('./static/*.mp4'))

    page = template.render(videos = videos[0:25])

    return page

# Parses the form output.
@post('/form')
def form():
    checked_list = request.forms.keys()

    # Determine which checkboxes are active.
    lip_move = [checked for checked in checked_list if 'lip_move' in checked]
    speech = [checked for checked in checked_list if 'speech' in checked]

    lip_move_files = numpy.sort([request.forms.get(item) for item in lip_move])
    speech_files = numpy.sort([request.forms.get(item) for item in speech])

    # Save results to file.
    print 'Saving...'
    f = open('lip_move.txt', 'w')
    for filename in lip_move_files:
        f.write('%s\n' % filename)
    f.close()

    f = open('speech.txt', 'w')
    for filename in speech_files:
        f.write('%s\n' % filename)
    f.close()
    print 'Done.'

    return 'Thanks.'

# Boilerplate to serve static files.
# In this case that means video files.
@get('/static/<filename>')
def server_static(filename):
    # Expects files to be in './static'.
    return static_file(filename, root='./static')

run(host='localhost', port=8080)