import glob

from bottle import get, post, request, redirect, run, static_file
from jinja2 import Environment, PackageLoader
import numpy


# Index redirects to page 1
@get('/')
def index():
    redirect('/p=1')


# Renders the video gui.
@get('/p=<page_num:int>')
def index(page_num):
    clips_per_page = 25
    env = Environment(loader=PackageLoader('video-labeling-gui', 'templates'))
    template = env.get_template('video.html')

    videos = numpy.sort(glob.glob('./static/*.mp4'))

    num_pages = len(videos) / clips_per_page
    indices = slice(clips_per_page * (page_num - 1), clips_per_page * page_num)
    page = template.render(num_pages=num_pages, page_num=page_num,
                           videos=videos[indices])

    return page


# Parses the form output.
@post('/form/p=<page_num:int>')
def form(page_num):
    checked_list = request.forms.keys()

    # Determine which checkboxes are active.
    lip_move = [checked for checked in checked_list if 'lip_move' in checked]
    speech = [checked for checked in checked_list if 'speech' in checked]

    lip_move_files = numpy.sort([request.forms.get(item) for item in lip_move])
    speech_files = numpy.sort([request.forms.get(item) for item in speech])

    # Save results to file.
    print 'Saving...'
    f = open('./results/lip_move_%03d.txt' % page_num, 'w')
    for filename in lip_move_files:
        f.write('%s\n' % filename)
    f.close()

    f = open('./results/speech_%03d.txt' % page_num, 'w')
    for filename in speech_files:
        f.write('%s\n' % filename)
    f.close()
    print 'Done.'

    redirect('/p=%d' % (page_num + 1))


# Boilerplate to serve static files.
# In this case that means video files.
@get('/static/<filename>')
def server_static(filename):
    # Expects files to be in './static'.
    return static_file(filename, root='./static')

run(host='localhost', port=8080)
