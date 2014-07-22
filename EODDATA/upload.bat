:main

	set x=1

	:: check for a path to where to upload to
	set URLPATH=127.0.0.1:8000/loader
	IF NOT x%1==x set URLPATH=%1

	:: load all exchanges.
	FOR %%a IN (*.txt) DO CALL :exchange %%a
	
	REM :: load symbols and prices 
	REM curl -3 %URLPATH%/
	REM echo %errorlevel%
	
	GOTO :end

:exchange
	:: upload to server
	curl -3 -F formdata=@%~1 %URLPATH%/raw/exchange/%~n1
	echo %errorlevel%
		
	:: find all the prices and upload
	FOR %%b IN (%~n1_*.csv) DO CALL :price %~n1 %%b 
	
	:: move to archive.
	MOVE %1 archive\%1
	
	GOTO :eof

:price
	:: Upload to server (prices)
	curl -3 -F formdata=@%2 %URLPATH%/raw/prices/%1
	echo %errorlevel%
	
	REM set /A x+=1
	REM if %x%==3 (
		REM curl -m 360 -3 %URLPATH%/
		REM echo %errorlevel%
		REM set x=1
	REM )
	
	:: archive
	MOVE %2 archive\%2
	
	GOTO :eof
	

:end 
	GOTO :eof