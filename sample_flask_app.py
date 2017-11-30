# Import statements necessary
from flask import Flask, render_template
from flask_script import Manager
from datamuse_rhyme import *  # where find_rhyme_on_datamuse() lives

# Set up application
app = Flask(__name__)
manager = Manager(app)


# Routes
@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/user/<yourname>')
def hello_name(yourname):
    return '<h1>Hello {}</h1>'.format(yourname)

@app.route('/showvalues/<name>')
def basic_values_list(name):
    lst = ["hello","goodbye","tomorrow","many","words","jabberwocky"]
    if len(name) > 3:
        longname = name
        shortname = None
    else:
        longname = None
        shortname = name
    return render_template('values.html',word_list=lst,long_name=longname,short_name=shortname)


## PART 1: Add another route /word/<new_word> as the instructions describe.
@app.route('/word/<new_word>')
def datamuse_rhyme(new_word):
    new_word_rhyme = find_rhyme_on_datamuse(new_word)
    #return "Here's a rhyme for '" + new_word + "': " + new_word_rhyme
    return new_word_rhyme


## PART 2: Edit the following route so that the photo_tags.html template will render
@app.route('/flickrphotos/<tag>/<num>')
def photo_titles(tag, num):
    FLICKR_KEY = "b23d6858b305a0cb8cc8fbee65e655ad" # TODO: fill in a flickr key
    baseurl = 'https://api.flickr.com/services/rest/'
    params = {}
    params['api_key'] = FLICKR_KEY
    params['method'] = 'flickr.photos.search'
    params['format'] = 'json'
    params['tag_mode'] = 'all'
    params['per_page'] = num
    params['tags'] = tag
    response_obj = requests.get(baseurl, params=params)
    trimmed_text = response_obj.text[14:-1]
    flickr_data = json.loads(trimmed_text)
    # TODO: Add some code here that processes flickr_data in some way to get what you nested
    flickr_data_photo_list = flickr_data["photos"]["photo"]
    number = len(flickr_data_photo_list)
    photo_titles = []
    for photo in flickr_data_photo_list:
        photo_titles.append(photo["title"])
    # TODO: Edit the invocation to render_template to send the data you need
    return render_template('photo_info.html', number = number, photo_titles = photo_titles)


if __name__ == '__main__':
    manager.run() # Runs the flask server in a special way that makes it nice to debug
