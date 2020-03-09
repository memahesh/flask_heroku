# views.py

from flask import flash, redirect, render_template, request, session, abort, url_for
from functools import wraps
import logging
import json


import os
from app import app
from .models import *


@app.route('/')
def index():

    dependencies = open('requirements.txt', 'r').readlines()

    return render_template('index.html', data=dependencies)