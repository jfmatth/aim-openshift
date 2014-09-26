#!/bin/bash
# this runs once per hour, so assume it's sometime in the 9th hour

if [ $(date +%H) == 19 ]; then 
	cd $OPENSHIFT_REPO_DIR
	python manage.py loadprices

	python manage.py advice	
	 
 fi