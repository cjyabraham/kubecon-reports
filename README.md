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


# Environment Setup
1. Checkout out the code by cloning the github repo: `git clone git@github.com:cjyabraham/kubecon-reports.git`
2. Cd into the project base dir: `cd $PATH_TO_PROJECT/kubecon-reports`
3. Create a virtual environment for the project: `python3 -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate`
5. Install the project's dependencies: `pip install --editable .`


# Steps for processing raw CSVs
1. Make sure all CSV files have the correct KEY_COLUMN label.  In the initial case it's `EMail_Address`.
2. Remove any strange chars from the start of the files.
3. run `genreport [main input file] [subsequent input files...] [output file]`. The main input file will provide all the required metadata about the user.  Subsequent input files are just searched for the existence of the email in the main input file.  The output file will contain the intersect of the set of all emails in each of the input files.

Run `genreport --help` for more CLI usage info.

