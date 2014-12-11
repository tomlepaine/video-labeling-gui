import glob

from bottle import get, post, request, run, static_file
from jinja2 import Environment, PackageLoader
import numpy

@get('/')
def index():
    env = Environment(loader=PackageLoader('app', 'templates'))
    template = env.get_template('video.html')

    videos = numpy.sort(glob.glob('./static/*.mp4'))

    page = template.render(videos = videos[0:25])
    print page
    return page

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

@get('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

run(host='localhost', port=8080)