from crawler import model
from pipes import start
import ruamel.yaml as yaml

print("started")

print("Creating database")
model.init()

session = model.session()
print("Inserting Moscow Times")
moscow_times_source = model.Source(name="Moscow Times")
session.add(moscow_times_source)
session.commit()

print("Seeding first task")
pipe_definition_path = "moscow_times.yaml"
with open(pipe_definition_path) as stream:
    pipe_definition = yaml.load(stream, Loader=yaml.Loader)

start(pipe_definition)

print("DONE")
