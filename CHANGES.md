### 12/19/14
- Modify email advice system.  Send all alerts to each user, not just one at a time.  Work on format of email

### 12/6/14
- aim/models.py - Adjust price.save() routine to have the model update it's currentprice pointer, instead of leaving that to the loader code.
- aim/tests.py - Start some tests for future use.  not very usable right now.
- loadprices.py - Adjust some debug logging calls, also tried to clear some variables in an effort to reduce memory leaking?  Remove code to update a prices' current price, moved to model above.
- loader/tests.py - attempt at starting to test.
- Holdingview.html - Updated some options for the graph.
- Mainview.html - changed the sorting for holdings in a portfolio.
- alerter\newadvice.py - New advice management command with new method of collecting which portfolios to email on
- alerter\\email_report.html - email body for above.
- CHANGES.txt - this file :)

