# Invoke tasks

from invoke import task, Context


@task
def dc_up(ctx):
    c = ctx  # type: Context
    c.run("docker compose -f docker-compose.prod.yml up")
