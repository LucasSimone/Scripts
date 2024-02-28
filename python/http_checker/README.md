# HTTP Checker Script

This script takes a list of domains provided in a text file and determines which domains can be accessed via HTTP printing the resulting domains.

## Features

- **Customizable Options:** There are additional options in the code that can be customized according to your needs. For example:
  - `only_show_http`: When set to `False`, it will display the results for all domains, not just the ones accessible via HTTP.

## Usage

To run the script, follow these instructions:

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/your_username/your_repository.git

2. **Run the Script(Configure domain_list.txt for your domains):**
   ```sh
   python httpChecker.py domain_list.txt

If no text file is given there is a default domain list that can be edited. 
