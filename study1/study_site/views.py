"""
Routes and views for the flask application.
"""

from . import globals
from datetime import datetime
from flask import render_template
from study_site import app

@app.route('/')
def init():
    """Renders the init page."""
    return render_template(
        'init.html',
        title='Init Page',
        year=datetime.now().year,
    )
    
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/reset')
def reset():
    """Reset and home the ambient fixture."""
    globals.g_transport.home()
    return render_template('index.html', title='Reset complete', 
                           year=datetime.now().year, message='Reset complete.')

@app.route('/run')
def run():
    """Run the ambient fixture."""
    print(f'running file {globals.g_gcode_file}')
    globals.g_transport.run(globals.g_gcode_file, 2)
    globals.g_transport.waitfor_idle()
    return render_template('about.html', title='About', 
                           year=datetime.now().year, message= f'Ran gcode file = {globals.g_gcode_file}.')

@app.route('/run_multiple') 
def run_multiple():
    for i in range(2):
        globals.g_transport.run(globals.g_gcode_file, 1)
        globals.g_transport.run(globals.g_gcode_file2, 1)
    globals.g_transport.waitfor_idle()
    return render_template('about.html', title='About', 
                           year=datetime.now().year, 
        message= f'Ran gcode files = {globals.g_gcode_file} and {globals.g_gcode_file2}.')

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
