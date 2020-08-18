
import click
import os
import pandas

from reporting.utils import get_project_root


KEY_COLUMN = 'Email'
COLUMNS_IN_ORDER = ['First Name', 'Last Name', 'Job Title', 'Company Name',
                    KEY_COLUMN, 'Country', 'City', 'State/Province', 'Postal Code',
                    'Address 1', 'Address 2', 'Address 3', 'Company Size', 'Job Function',
                    'Industry']


def generate_report(config, input_filenames, output_csv_filename):
    click.echo('Reading input files: ' + ', '.join(input_filenames))

    # calculate a data field containing a subset of emails in all input files
    master_df = read_file(input_filenames.pop(0))

    for input_filename in input_filenames:
        df = read_file(input_filename)

        master_df = master_df[master_df[KEY_COLUMN].isin(df[KEY_COLUMN])]

    output_dir = config.get('DEFAULT', 'outputdir')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_csv_filename = os.path.join(
        get_project_root(), output_dir, output_csv_filename)

    click.echo('Writing output file: ' + output_csv_filename)

    master_df.to_csv(output_csv_filename)


def read_file(filename):
    df = pandas.read_csv(filename, names=COLUMNS_IN_ORDER,
                         header=0, usecols=COLUMNS_IN_ORDER)

    if get_file_extension(filename) == '.csv':
        df = pandas.read_csv(filename, names=COLUMNS_IN_ORDER,
                             header=0, usecols=COLUMNS_IN_ORDER)

    return df.drop_duplicates(subset=KEY_COLUMN)


def get_file_extension(filename):
    return os.path.splitext(filename)[-1]


if not os.path.exists('my_folder'):
    os.makedirs('my_folder')
