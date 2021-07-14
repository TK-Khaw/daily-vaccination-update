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

Feel free to use this repo but I am not responsible for any losses or charges incur upon you. 
