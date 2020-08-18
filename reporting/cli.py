
import click
import os

from reporting import reporter
from reporting.utils import get_project_config, get_project_root


PROJECT_BASE_DIR = get_project_root()

DEFAULT_CONFIG_FILENAME = 'config.ini'
DEFAULT_CONFIG_FILE = os.path.join(PROJECT_BASE_DIR, DEFAULT_CONFIG_FILENAME)

READABLE_FILE_TYPE = click.Path(exists=True, readable=True, dir_okay=False)
WRITABLE_FILE_OR_STDOUT_TYPE = click.Path(writable=True, dir_okay=False,
                                          allow_dash=True)


@click.command()
@click.option('--config-file', type=click.File('r'),
              default=DEFAULT_CONFIG_FILE,
              help='Path of the config file.  [default: $PROJECT_ROOT/' +
                   DEFAULT_CONFIG_FILENAME + ']')
@click.argument('input_files', type=READABLE_FILE_TYPE, nargs=-1)
@click.argument('output_file', type=WRITABLE_FILE_OR_STDOUT_TYPE)
def genreport(config_file, input_files, output_file):
    config = get_project_config(config_file)
    reporter.generate_report(config, list(input_files), output_file)
