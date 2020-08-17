
import click
import pandas


# TODO replace this with the desired email header name
KEY_COLUMN = 'EMail_Address'

# TODO rename these columns to conform with the desired output csv file values
KEEP_COLUMNS = ['First_Name', 'Last_Name', 'Job_Title', 'Company_Name',
                KEY_COLUMN, 'Country', 'City', 'State_-_Prov',
                'Postal_Code', 'Address_1', 'Address_2', 'Address_3',
                'Company_Size', 'Job_Function', 'Industry']


ATTENDED_ALL_NAME = 'Attended All'
ATTENDED_ALL_VALUE = True


def generate_report(config, input_csv_files, output_csv_file):
    click.echo('config = ' + str(config.defaults()))
    click.echo('input_csv_files = ' + ', '.join(input_csv_files))
    click.echo('output_csv_file = ' + output_csv_file)

    click.echo('datadir = ' + config.defaults()['datadir'])

    # TODO drop the headers in the sample CSV files provided as they contain weird
    # characters and replace with KEEP_COLUMNS
    master_df = read_csv_file(input_csv_files.pop(0), usecols=KEEP_COLUMNS,
                              drop_duplicates_subset=KEY_COLUMN)

    # TODO this is the meat of the code. should be very straightforward from here.
    # maybe 10 - 20 min of pandas API reading and applying its API to the algorithm
    # described in the README
    master_df[ATTENDED_ALL_NAME] = ATTENDED_ALL_VALUE

    for i in input_csv_files:
        df = read_csv_file(input_csv_files[i], usecols=KEEP_COLUMNS,
                           drop_duplicates_subset=KEY_COLUMN)

        if not master_df[KEY_COLUMN].isin(df[KEY_COLUMN]):
            # remove the row from master_df
            None


def read_csv_file(csv_file, usecols=None, drop_duplicates_subset=None):
    df = pandas.read_csv(csv_file, usecols=KEEP_COLUMNS)

    if drop_duplicates_subset is not None:
        df.drop_duplicates(subset=drop_duplicates_subset, inplace=True)

    return df
