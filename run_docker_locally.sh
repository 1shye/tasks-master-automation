#!/bin/bash

docker run -it \
--net=host \
-e CONF_FILE="/opt/configuration.json" \
-v "<path to your configuration file location>"/:/opt/ \
 <image_name>:<image_tag> /bin/bash