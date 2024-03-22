from invoke import Context, task


@task(aliases=["example"])
def example_command(c: Context, parameter: str):
    c.run(f"echo 'Echoing {parameter}'")
