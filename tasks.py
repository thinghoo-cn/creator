from invoke import task


@task
def docs(c):
    c.run('mkdocs serve')
