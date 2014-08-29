
## History

### (8/29/14)

aim/models.py
- add absolute_url() to the Holding

aim/urls.py

- remove some older comments

- move /graphdata view into debug only mode.

aim/views.py

- remove success_url from transaction, since Holding got absolute_url

alerter/views.py

- change the way email is sent, still needs work, HTML not working for some reason.

loader/views.py

- add some more detail to the email body of what just got loaded.

templates/aim/holdingview.html

- clean up some of the value detail for a holding.

- change the way we call transactions, we don't need to specify the ?next parameter since we 
now  have absolute_url on the Holding

- Add a delete link so you can delete a holding.

template/aim/mainview.html

- sort holdings within a portfolio alphabetically.

template/alerter/email.txt

- try to setup a link back to the holding.  Need HTML to work first :).