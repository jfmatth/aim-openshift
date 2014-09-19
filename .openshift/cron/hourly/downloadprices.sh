#!/bin/bash
# this runs once per hour, so assume it's sometime in the 9th hour
if [ $(($(date +%H))) == 21 ];then 
	cd $OPENSHIFT_REPO_DIR/EODDATA
	bash ./working_curl_command.sh
	
	# run any alerts for the day too.
	cd $OPENSHIFT_REPO_DIR
	export DJANGO_SETTINGS_MODULE=mysite.settings
	python alerts.py
	 
 fi
