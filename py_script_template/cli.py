"""Console script for py_script_template."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for py_script_template."""
    click.echo("Replace this message by putting your code into "
               "py_script_template.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
