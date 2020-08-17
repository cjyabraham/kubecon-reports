
import click
import os

from reporting.sponsors import reporter
from reporting.utils import get_project_config, get_project_root

PROJECT_BASE_DIR = get_project_root()

DEFAULT_CONFIG_FILENAME = 'config.ini'
DEFAULT_CONFIG_FILE = os.path.join(PROJECT_BASE_DIR, DEFAULT_CONFIG_FILENAME)

READABLE_FILE_TYPE = click.Path(exists=True, readable=True, dir_okay=False)
WRITABLE_FILE_OR_STDOUT_TYPE = click.Path(writable=True, dir_okay=False,
                                          allow_dash=True)


@click.group()
@click.option('--config-file', type=click.File('r'),
              default=DEFAULT_CONFIG_FILE,
              help='Path of the config file.  [default: $PROJECT_ROOT/' +
                   DEFAULT_CONFIG_FILENAME + ']')
@click.pass_context
def cli(context, config_file):
    context.ensure_object(dict)
    config = get_project_config(config_file)
    context.obj['config'] = config


# TODO specific sponsor functions (cisco, gitlab, etc...) may only be needed if
# they have specific config needs not passed in via command-line. In which case,
# this code could just be something like generate_2_input_output_report(),
# generate_3_input_output_report(),
@cli.command()
@click.argument('infile1', type=READABLE_FILE_TYPE)
@click.argument('infile2', type=READABLE_FILE_TYPE)
@click.argument('infile3', type=READABLE_FILE_TYPE)
@click.argument('outfile', type=WRITABLE_FILE_OR_STDOUT_TYPE)
@click.pass_context
def cisco(context, infile1, infile2, infile3, outfile):
    click.echo("Generating cisco report...")
    reporter.generate_report(
        context.obj['config'], [infile1, infile2, infile3], outfile)


@cli.command()
@click.argument('infile1', type=READABLE_FILE_TYPE)
@click.argument('infile2', type=READABLE_FILE_TYPE)
@click.argument('outfile', type=WRITABLE_FILE_OR_STDOUT_TYPE)
@click.pass_context
def gitlab(context, infile1, infile2, outfile):
    click.echo("Generating gitlab report...")
    reporter.generate_report(
        context.obj['config'], [infile1, infile2], outfile)


@cli.command()
@click.argument('infile1', type=READABLE_FILE_TYPE)
@click.argument('infile2', type=READABLE_FILE_TYPE)
@click.argument('outfile', type=WRITABLE_FILE_OR_STDOUT_TYPE)
@click.pass_context
def nebulon(context, infile1, infile2, outfile):
    click.echo("Generating nebulon report...")
    reporter.generate_report(
        context.obj['config'], [infile1, infile2], outfile)


@cli.command()
@click.argument('infile1', type=READABLE_FILE_TYPE)
@click.argument('infile2', type=READABLE_FILE_TYPE)
@click.argument('infile3', type=READABLE_FILE_TYPE)
@click.argument('outfile', type=WRITABLE_FILE_OR_STDOUT_TYPE)
@click.pass_context
def redhat(context, infile1, infile2, infile3, outfile):
    click.echo("Generating redhat report")
    reporter.generate_report(
        context.obj['config'], [infile1, infile2, infile3], outfile)
