# Problem Statement
Given 2 to 3 reports per sponsor in CSV format with data about actions attendees performed on the virtual event platform, create another custom report, per sponsor, containing attendees who attended all events for the that sponsor (eg: either 2 or 3 events).

Each attendee can be uniquely indentified in the reports via their email address. In the case of rows containing duplicate email addresses, duplicate rows will be removed.

The generated custom reports will be in CSV format.


# Sponsors' Input Reports

| Sponsors | Inputs                                               |
|----------|------------------------------------------------------------------|
| Nebulon  | Given 2 reports, determine which attendees are in both reports.  |
| Cisco    | Given 3 reports, determine which attendees are in all 3 reports. |
| Red Hat  | Given 3 reports, determine which attendees are in all 3 reports. |
| GitLab   | Given 2 reports, determine which attendees are in both reports.  |

# Output Report Data
| First Name | Last Name | Job Title | Company Name | Email            | Country | City     | State/Province | Postal Code | Address 1  | Address 2 | Address 3 | Company Size | Job Function | Industry |
|------------|-----------|-----------|--------------|------------------|---------|----------|----------------|-------------|------------|-----------|-----------|--------------|--------------|----------|
| John       | Doe       | Engineer  | example.com  | john@example.com | USA     | New York | NY             | 10021       | 123 Abc St | Apt 10Y   |           | 50 - 100     | Engineer     | IT       |


# Environment Setup
1. Checkout out the code by cloning the github repo: `git clone git@github.com:cjyabraham/kubecon-reports.git`
2. Cd into the project base dir: `cd $PATH_TO_PROJECT/kubecon-reports`
3. Create a virtual environment for the project: `python3 -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate`
5. Install the project's dependencies: `pip install --editable .`

# CLI Usage
After installing the project in your local environment the `genreport` command will be available. The `genreport` command can be run with 4 arguments: `cisco`, `gitlab`, `nebulon` and `redhat` requiring input CSV filenames and an output CSV filename. Using `-` in place of the output CSV filename can be used to write the output to STDOUT per UNIX conventions.

The project config file is `$PATH_TO_PROJECT/kubecon-reports/config.ini`. The config file used can be overriden using the `--config-file` CLI option.

Run `genreport --help` for more CLI usage info or or `genreport ARGUMENT --help` for more argument-specific CLI usage info.




