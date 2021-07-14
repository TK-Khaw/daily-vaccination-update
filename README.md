# Daily SMS-based Delivery of Data Processed off Malaysia's National Covid-19 Immunisation Programme

This is an automated processing pipeline quickly slapped together using some Bash and Python script that you can hosted on a Linux node anywhere to ingest and process data off [here](https://github.com/citf-malaysia/citf-public) and have the processed data send to you as SMS. Once setup, the script will listen for changes on the open data repo and trigger data processing should one is needed. Note that this repository uses Twilio. 

---
## Usage

Simply use the [`env_template`](/env_template) as a guide to export needed environment variable for the script to function.

```bash
cp env_template env
vim env #Or any of your favourite editor.
```
Then insert a line into your cron service so that [`trigger.sh`](/trigger.sh) will be called every minutes, or any interval you like.

```
* * * * * . <project_dir>/env; <project_dir>/trigger.sh
```

## Customising

If you have any special metrics you would like to apply on the dataset (e.g. Custom Discrete Convolution Filter), you can do so by adding a Python module within the [`analyser`](/analyser) directory. 

Within the module, please ensure that there is a `compute` function which takes a FIFO array consisting of most recent 100 days Malaysian vaccination data and churn out a string which will be append to the list of message to be send to your device.

Example:
```python
# analyser/module.py

def compute(fifo):
	# Some computation magic.
	# ...
	# ...
	# returns a string contained processed data.
	return "Data: {} ".format(data)

```

If you want to add another output stream, for instance to Google Sheets, feel free to add a module in [`distributor`](/distributor) directory. Make sure that the module implements a function `distribute` that takes a string of messages churned out by all the analysers so that it can distribute the message to downstream services you intended for accordingly. No return value is expected.

Example:
```python
# distributor/module.py

def distribute(msg_body):
	# Implementation for distribution of message...
	# ...
	# ...
	# Done!
```
To tell the program which analysers and distributors to be included, you can export the environment variables `DVU_ANALYSERS` and `DVU_DISTRIBUTORS`. Both environment variables are comma-separated list of modules to be included in the program flow. Not exporting either variable renders the program to call all the modules available within the corresponding directory.

Example:
```bash
export DVU_ANALYSERS=ra,minmax #Only rolling-average and min-max analyser will be called.
export DVU_DISTRIBUTORS= #All distributors will be called.
```

---

Feel free to use this repo but I am not responsible for any losses or charges incur upon you. 
