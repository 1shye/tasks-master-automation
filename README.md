# Tasks Master testing   

Automation for tasks master API

## Usage
Tests execution:
- Build the image by running the command below: 

```cmd 
docker build -t <image-name>:<tag> . 
```
- Create a configuration.json file locally with the server configuration (for configuration parameters use the configuration template.json file in the configurations folder)
- Edit the run_docker_locally.sh script with your image name and your configuration.json file folder location 
- Run the script
- Check the folder that you set as configuration.json file location for the report.html                  




