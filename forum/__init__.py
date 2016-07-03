from .models import graph
from flask import Flask
import os


app = Flask(__name__)
app.config.update(dict(
    APPLICATION_ROOT = os.path.dirname(os.path.abspath(__file__)),
    ))

from forum import views

def create_uniqueness_constraint(label, property):
    query = "CREATE CONSTRAINT ON (n:{label}) ASSERT n.{property} IS UNIQUE"
    query = query.format(label=label, property=property)
    graph.run(query)

create_uniqueness_constraint("User", "username")
create_uniqueness_constraint("Tag", "name")
create_uniqueness_constraint("Subject", "id")
