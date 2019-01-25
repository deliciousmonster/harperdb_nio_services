# HarperDB Demo Services

This project is comprised of several services demonstrating the use of the suite of [HarperDB blocks](https://github.com/deliciousmonster/harperdb_nio_blocks) for nio systems.

## Prerequisites

- [Python3](https://www.python.org/downloads/)
  - Remember to run the Install Certificates command as detailed in the install instructions
- [HarperDB](https://harperdbhelp.zendesk.com/hc/en-us/articles/115008571247-Getting-Started)
  - Start HarperDB
  - Create the `dev` schema
  - Create three tables: `dog`, `breed`, `metrics`
  - Insert stub data for dog and breed: https://docs.harperdb.io
- nio
  - [Create a free account](https://account.n.io/signup/community)
  - Download the latest [nio Binary](https://account.n.io/binaries/download)
  - Install nio:
  ```
  pip3 install /path/to/the/nio/wheel/nio_full-XXXXXX.1-py3-none-any.whl
  ```

## Create a new project

- Log into the [nio System Designer](https://app.n.io)
  - Add a new system
  - Add a new local instance, name it "harperdb"
  - Change the host:port to use SSL: https://localhost:8181
  - Copy the CLI command from the bottom of the modal window
- Start a new instance of nio
  - Open a new terminal window
  - Paste the CLI command from the system designer at the cursor, adding `--template https://github.com/deliciousmonster/harperdb_nio_services.git` to the end of the line:
   ```
    nio new harperdb \
    --port 8181 \
    --username Admin \
    --password Admin \
    --pubkeeper-hostname xxxxxxxx-xxxxxx-xxxxxxxx-xxxxxxxxx-xxxxxx.pubkeeper.nio.works \
    --pubkeeper-token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
    --template https://github.com/deliciousmonster/harperdb_nio_services.git
    ````
  - Enter the project directory and start nio: `cd harperdb && niod`
- Return to the nio System Designer
  - Click on the `harperdb` instance in the left-hand nav
  - You should see six services in your new instance
  - The default HarperDB host/port/username/password are included as environment variables. Click the edit icon in the top bar to edit them if necessary

## Explore each of the services
- Start and stop each service independently
- Each service runs exactly one time when started
  - You can change this behavior by editing the Interval Simulator, changing the total number of signal to -1
  - Changing it in one service will change it in all services (you could drag a new instance of the Interval Simulator to change this behavior)

#### bulk
 - bulk covers data importation via CSV
 - The `csv_file_load` location is relative to the DB instance, not nio
 - If you wanted to monitor a file accessible to nio for changes, you could add a filewatcher block, then read in the file with a CSV block, then bulk insert the data using the `csv_data_load` setting

#### delete
  - `delete` accepts comma-delimited hash_values

#### insert
  - `insert` populates the `metrics` table with a variety of host-related stats every second. The HostMetrics block could easily be swapped out with any [nio hardware block](http://blocks.n.io/?category=Hardware) to pump sensor data into HarperDB

#### search
  - `search` demonstrates how Value or Hash searches could be parameterized using variables that came from a sensor or another service

#### sql
  - `sql` demonstrates the raw SQL query capability of HarperDB

#### update
  - `update` demonstrates how a service could update records using variables that came from a sensor or another service
