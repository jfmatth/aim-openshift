#!/bin/bash


cookie='ctl00_tsm_HiddenField=%3B%3BAjaxControlToolkit%2C+Version%3D3.0.20820.16598%2C+Culture%3Dneutral%2C+PublicKeyToken%3D28f01b0e84b6d53e%3Aen-US%3A707835dd-fa4b-41d1-89e7-6df5d518ffb5%3A865923e8%3A9b7907bc%3A411fea1c%3Ae7c87f07%3A91bd373d%3Abbfda34c%3A30a78ec5%3A9349f837%3Ad4245214&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKMTE1NDAyMjA0OQ9kFgJmD2QWAgIDD2QWAgIHD2QWCAIBD2QWAmYPZBYCZg9kFgICBQ9kFhwCAw8PFgIeB1Zpc2libGVoZBYCAgEPEA8WAh4HQ2hlY2tlZGcWAh4Fc3R5bGUFEW1hcmdpbi1sZWZ0OjMwcHg7ZGRkAgUPDxYCHwBoZBYCAgMPEA8WBh4NRGF0YVRleHRGaWVsZAUETmFtZR4ORGF0YVZhbHVlRmllbGQFD0V4Y2hhbmdlR3JvdXBJZB4LXyFEYXRhQm91bmRnFgIfAgURbWFyZ2luLWxlZnQ6MzBweDsQFQILVVMgRXF1aXRpZXMKVVMgRnV0dXJlcxUCATEBMxQrAwJnZxYBZmQCBw9kFgICAw8QDxYGHwMFBE5hbWUfBAUEQ29kZR8FZxYCHwIFEW1hcmdpbi1sZWZ0OjMwcHg7EBUgF0FtZXJpY2FuIFN0b2NrIEV4Y2hhbmdlHkF1c3RyYWxpYW4gU2VjdXJpdGllcyBFeGNoYW5nZRZDaGljYWdvIEJvYXJkIG9mIFRyYWRlGENoaWNhZ28gRnV0dXJlcyBFeGNoYW5nZRxDaGljYWdvIE1lcmNoYW50aWxlIEV4Y2hhbmdlFkVVUkVYIEZ1dHVyZXMgRXhjaGFuZ2USRXVyb25leHQgQW1zdGVyZGFtEUV1cm9uZXh0IEJydXNzZWxzD0V1cm9uZXh0IExpc2Jvbg5FdXJvbmV4dCBQYXJpcxBGb3JlaWduIEV4Y2hhbmdlDkdsb2JhbCBJbmRpY2VzGEhvbmcgS29uZyBTdG9jayBFeGNoYW5nZRpLYW5zYXMgQ2l0eSBCb2FyZCBvZiBUcmFkZRlMSUZGRSBGdXR1cmVzIGFuZCBPcHRpb25zFUxvbmRvbiBTdG9jayBFeGNoYW5nZRVNYWRyaWQgU3RvY2sgRXhjaGFuZ2UUTWlsYW4gU3RvY2sgRXhjaGFuZ2UaTWlubmVhcG9saXMgR3JhaW4gRXhjaGFuZ2UMTXV0dWFsIEZ1bmRzFU5BU0RBUSBTdG9jayBFeGNoYW5nZRdOZXcgWW9yayBCb2FyZCBvZiBUcmFkZRtOZXcgWW9yayBDb21tb2RpdHkgRXhjaGFuZ2UdTmV3IFlvcmsgTWVyY2hhbnRpbGUgRXhjaGFuZ2UXTmV3IFlvcmsgU3RvY2sgRXhjaGFuZ2UUTmV3IFplYWxhbmQgRXhjaGFuZ2UST1RDIEJ1bGxldGluIEJvYXJkGFNpbmdhcG9yZSBTdG9jayBFeGNoYW5nZRZUb3JvbnRvIFN0b2NrIEV4Y2hhbmdlGFRvcm9udG8gVmVudHVyZSBFeGNoYW5nZQpVUyBPcHRpb25zG1dpbm5pcGVnIENvbW1vZGl0eSBFeGNoYW5nZRUgBEFNRVgDQVNYBENCT1QDQ0ZFA0NNRQVFVVJFWANBTVMDQlJVA0xJUwNQQVIFRk9SRVgFSU5ERVgESEtFWARLQ0JUBUxJRkZFA0xTRQNNU0UETUxTRQRNR0VYBFVTTUYGTkFTREFRBU5ZQk9UBUNPTUVYBU5ZTUVYBE5ZU0UDTlpYBU9UQ0JCA1NHWANUU1gEVFNYVgRPUFJBA1dDRRQrAyBnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAgsPEA8WBh8DBQROYW1lHwQFDERhdGFGb3JtYXRJZB8FZxYCHwIFEW1hcmdpbi1sZWZ0OjMwcHg7EBUXDjNGIFZJUCBUcmFkaW5nEkFkdmFuY2VkIEdldCBBU0NJSQpBR2V0IEFTQ0lJFkFJUSBUcmFkaW5nIEV4cGVydCBQcm8KQW1pIEJyb2tlchVBbWkgQnJva2VyIHdpdGggTmFtZXMJQW5kcm9tZWRhEEFTQ0lJIChJbnRyYWRheSkJRXp5Q2hhcnRzB0ZDaGFydHMSRkNoYXJ0cyAoSW50cmFkYXkpGk1ldGFTdG9jayBBU0NJSSAoNyBjb2x1bW4pGk1ldGFTdG9jayBBU0NJSSAoOCBjb2x1bW4pGk1ldGFzdG9jayBBU0NJSSAoSW50cmFkYXkpGk1ldGFTdG9jayBBU0NJSSB3aXRoIE5hbWVzF1BlcnNvbmFsIFN0b2NrIFN0cmVhbWVyB1F1aWNrZW4XU3ByZWFkc2hlZXQgKGVnOiBFeGNlbCkMU3RhbmRhcmQgQ1NWElN0b2NrIFNjcmVlbmVyIFBybxFTdXBlckNoYXJ0cyBBU0NJSRFXYWwgRGF0YSBQbGF0aW51bRVXaW5kb3dzIG9uIFdhbGxzdHJlZXQVFwIxNwEyAjM2AjE2AjI3AjI4AjMzAjMyATgCMjQCMzUBOQExAjM5AjExAjE0ATYBNQE0AjEyATMCMjYCMTUUKwMXZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dkZAIPDxAPZBYCHwIFEW1hcmdpbi1sZWZ0OjMwcHg7EBUHCkVuZCBvZiBEYXkNMSBNaW51dGUgQmFycw01IE1pbnV0ZSBCYXJzDjEwIE1pbnV0ZSBCYXJzDjE1IE1pbnV0ZSBCYXJzDjMwIE1pbnV0ZSBCYXJzDjYwIE1pbnV0ZSBCYXJzFQcBMAExATIBMwE0ATUBNhQrAwdnZ2dnZ2dnZGQCEQ8QD2QWAh8CBRFtYXJnaW4tbGVmdDozMHB4O2RkZAITD2QWAgIBDxAPFgIfAWcWAh8CBRFtYXJnaW4tbGVmdDozMHB4O2RkZAIVDxYCHwBoFgRmD2QWAgIBD2QWAmYPD2QWAh8CBRFtYXJnaW4tbGVmdDozMHB4O2QCAQ9kFgICAQ9kFgQCAQ9kFgICAQ8PFgIeBFRleHQFCjA2LzI0LzIwMTIWAh8CBRFtYXJnaW4tbGVmdDozMHB4O2QCAw9kFgICAQ8PZBYCHwIFEW1hcmdpbi1sZWZ0OjMwcHg7ZAIXDw8WAh8GBQVEYXRlOmRkAhkPD2QWAh8CBRFtYXJnaW4tbGVmdDozMHB4O2QCGw8PZBYCHwIFEW1hcmdpbi1sZWZ0OjMwcHg7ZAIdDw9kFgIfAgURbWFyZ2luLWxlZnQ6MzBweDtkAh8PDxYCHwZlZGQCIQ8WAh8AaGQCAw9kFgJmD2QWAmYPZBYCAgEPZBYEAgMPEA8WBh8DBQROYW1lHwQFBENvZGUfBWdkEBUgF0FtZXJpY2FuIFN0b2NrIEV4Y2hhbmdlHkF1c3RyYWxpYW4gU2VjdXJpdGllcyBFeGNoYW5nZRZDaGljYWdvIEJvYXJkIG9mIFRyYWRlGENoaWNhZ28gRnV0dXJlcyBFeGNoYW5nZRxDaGljYWdvIE1lcmNoYW50aWxlIEV4Y2hhbmdlFkVVUkVYIEZ1dHVyZXMgRXhjaGFuZ2USRXVyb25leHQgQW1zdGVyZGFtEUV1cm9uZXh0IEJydXNzZWxzD0V1cm9uZXh0IExpc2Jvbg5FdXJvbmV4dCBQYXJpcxBGb3JlaWduIEV4Y2hhbmdlDkdsb2JhbCBJbmRpY2VzGEhvbmcgS29uZyBTdG9jayBFeGNoYW5nZRpLYW5zYXMgQ2l0eSBCb2FyZCBvZiBUcmFkZRlMSUZGRSBGdXR1cmVzIGFuZCBPcHRpb25zFUxvbmRvbiBTdG9jayBFeGNoYW5nZRVNYWRyaWQgU3RvY2sgRXhjaGFuZ2UUTWlsYW4gU3RvY2sgRXhjaGFuZ2UaTWlubmVhcG9saXMgR3JhaW4gRXhjaGFuZ2UMTXV0dWFsIEZ1bmRzFU5BU0RBUSBTdG9jayBFeGNoYW5nZRdOZXcgWW9yayBCb2FyZCBvZiBUcmFkZRtOZXcgWW9yayBDb21tb2RpdHkgRXhjaGFuZ2UdTmV3IFlvcmsgTWVyY2hhbnRpbGUgRXhjaGFuZ2UXTmV3IFlvcmsgU3RvY2sgRXhjaGFuZ2UUTmV3IFplYWxhbmQgRXhjaGFuZ2UST1RDIEJ1bGxldGluIEJvYXJkGFNpbmdhcG9yZSBTdG9jayBFeGNoYW5nZRZUb3JvbnRvIFN0b2NrIEV4Y2hhbmdlGFRvcm9udG8gVmVudHVyZSBFeGNoYW5nZQpVUyBPcHRpb25zG1dpbm5pcGVnIENvbW1vZGl0eSBFeGNoYW5nZRUgBEFNRVgDQVNYBENCT1QDQ0ZFA0NNRQVFVVJFWANBTVMDQlJVA0xJUwNQQVIFRk9SRVgFSU5ERVgESEtFWARLQ0JUBUxJRkZFA0xTRQNNU0UETUxTRQRNR0VYBFVTTUYGTkFTREFRBU5ZQk9UBUNPTUVYBU5ZTUVYBE5ZU0UDTlpYBU9UQ0JCA1NHWANUU1gEVFNYVgRPUFJBA1dDRRQrAyBnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAgUPEA8WBh8DBQROYW1lHwQFDERhdGFGb3JtYXRJZB8FZ2QQFRcOM0YgVklQIFRyYWRpbmcSQWR2YW5jZWQgR2V0IEFTQ0lJCkFHZXQgQVNDSUkWQUlRIFRyYWRpbmcgRXhwZXJ0IFBybwpBbWkgQnJva2VyFUFtaSBCcm9rZXIgd2l0aCBOYW1lcwlBbmRyb21lZGEQQVNDSUkgKEludHJhZGF5KQlFenlDaGFydHMHRkNoYXJ0cxJGQ2hhcnRzIChJbnRyYWRheSkaTWV0YVN0b2NrIEFTQ0lJICg3IGNvbHVtbikaTWV0YVN0b2NrIEFTQ0lJICg4IGNvbHVtbikaTWV0YXN0b2NrIEFTQ0lJIChJbnRyYWRheSkaTWV0YVN0b2NrIEFTQ0lJIHdpdGggTmFtZXMXUGVyc29uYWwgU3RvY2sgU3RyZWFtZXIHUXVpY2tlbhdTcHJlYWRzaGVldCAoZWc6IEV4Y2VsKQxTdGFuZGFyZCBDU1YSU3RvY2sgU2NyZWVuZXIgUHJvEVN1cGVyQ2hhcnRzIEFTQ0lJEVdhbCBEYXRhIFBsYXRpbnVtFVdpbmRvd3Mgb24gV2FsbHN0cmVldBUXAjE3ATICMzYCMTYCMjcCMjgCMzMCMzIBOAIyNAIzNQE5ATECMzkCMTECMTQBNgE1ATQCMTIBMwIyNgIxNRQrAxdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAgcPZBYEAgMPZBYCAgcPDxYCHwZlZGQCBw8PFgIfAGhkZAIJD2QWBAIBDw8WAh8GBQ4xMDguMjE3LjEwOS43OWRkAgMPDxYCHwZlZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgMFFGN0bDAwJGNwaDEkZDEkY2hrWmlwBRtjdGwwMCRjcGgxJGQxJGNoa0FsbFN5bWJvbHMFGmN0bDAwJGNwaDEkbHMxJGNoa1JlbWVtYmVyOC4H%2FSQBnC9KXZUEoGCihkb9tB0DUZDVRBGjIxHamro%3D&__EVENTVALIDATION=%2FwEdAIQBlN%2BbyIl4VvEpmYHaSQj22Mfgsyp%2FYLLDWibMINT1pLCXdttwb5io%2B97XavTPfGaN3TCWuOFSVeQkO98%2BSOIfRX7iomXeduR2M55ox%2FTrsBsjRrzX%2FcWXI0m%2F25M8XF56v02bTA4VQ2%2BaRNUUEyFyzaaDypJe9GsTjf6zUI3zmnRJWYhA%2FenIFr2X4xkA5uOYfY%2BalBt8U099wCHQ8Gwv5yoASOKoGWiKN5MHQUX3mkUqR1%2Fi0q%2F%2BF%2BImyA6bpJy4Rg3LkbRz0IwLmluHdveYv2bP%2BchFdKkv6JiI%2FCC%2F%2FQhbmxdg4Z1Z552sSU4mu2Eb3c4Bo7AWGdG5k0V86I0bkQPvhMtfxSu6t9NrH7miNYn%2BTWMAMNzmIoA175LlsrN84Zb4wfx%2B53beI73tksqtWXlqp046twLObqTp7rMKdbrzM1EAjcMXopItCzjIEeB%2F4BiCLP1x34tpAycf6Jq2hH91F83N7wLLdapLQ5f12qWu0VbLoccJ9t4gMS48ZZVQCHyvUYWe6EmAhXIQQvBtZZQr5rP5J7jBbFKQQS%2B6cJTVDKwuSQDcmy8WgsycQaX3LwhNsKi%2F4ILyfYlOnTOmrNdGMlszaA7BUam5EEfyIacgp0ve2ThrFzJHQbEpj1QE4JDG3DxQDez%2BwlkDEgNLJB7FES7Qe5%2F2N4Pik5ypj%2ByMssIOT%2BbtSbqHotQYv4aijU9g095QgHOZyncnii3hM4%2BQbV1m5bN%2FPP00e96wfZbRFhOMgJuRvE24GZntixSod4qAfhaJdwZU8HEDo4ILAlngKAZv0osx74JY3hYeU%2BTHK%2Bh27Q75ia%2Fu3qhiuLtzI2jSjFvetVZSiYxcWV0FXvaFbRmICJvvfRRluXvxixmfyuHO04JynAfcCzOc6KRjaS%2B95yeCivs7JRjzUEiNNhboZccXr5TJcIe7BtSUwdVDzcFDe1wePv%2FD8B7%2Bk%2BhB7TsoTny0TuChC2hoXt9j%2FN7roFRdPD9Z895zstgdW3RgXyHGWG1vts%2B1%2FiN4TG8ygRHaNYUGBa32Jd52Iq5QkodgyNxoi9Sg%2BU1B%2B0Xonqau6HhIWFzDhFJjHhr3VMnmCGu%2FdHjBAuLYtkbT0I1YRzCNTpsbsWG%2BfO6EwqiDsOuFOKRSzCnDTn1CuYQ4SiFqoLZ%2Fo8soFe6vI03wQpHyzdXwj7WFxR0UjMgemoSoVLCbKYCsco8RZ4OREmUjIJlvO0tp%2BCbcLJU0z22nUhIY2WH2F2UpYLi0J8%2BpsaRgq4SeniHWTK5JtS7ZgnVf7giMkDQyYwH%2BI0uaEP5XxB7T%2FncYByNWwYmyWlw3szgHqjJVvmk%2FMcyW78y5GAvnbAcK3SydIf4JcMp67QTIE8C2WnXRtNMYBH3fDjbkf3y27XtrRS4dZucI9IPEQ9ZUhBeVkZAh4OZOqFosyXE%2B8HUkTYZFZMubRTinPzsXiy0qijnFNo%2BiOPKXGfBwW0h24B9CpxxNEdfq60558lYhYGsHMQa6YfMFwgpxDzWk%2FBlJT1yBnErydMBrQ9eUqekZBUhXCOMls0k6SzhrFB9rmK7ohEEUYB%2BO%2FxngRji0KpplciyyEUV2GKPKldUzFBL2dK2cUDSv8DjloRr765a40O279eIlSA9QJE2ptXakKY7%2F3lHCy%2B3J3bzkBKwf2AoEFH5iDkdzbxbuRco2iyFSNjMrQHDUFNYJ%2FVQJ%2FUP7nRy4OkDvWh%2B99YOVUYiaGsWPl%2B6kw11XE4hKWnkCxcBqCbZbe%2BeQXi9D2tX9fXIMvnStsvtqirTly4PBtBrBcaa6Ap8cWzy6JoEkPYwk9rouCxRkn6sNM4D%2Fy2YzPNki1CLIgO4fZ12WU%2FCste6SgoLhuxotd19M3wo6AgA4eU6SUweUaGHzyF4D1vEUBlLazkbPE0itA3dj1FwLYHMhWzfsd0q0aHXUvUZ8gtkV8ULXhVgHpHnaGrnSHQztGAz9gYfcQl%2B7uBvl5jmSjPK%2BOL9x4oFDprWu1ziy9tWiiW5KIJLGUHJ9GYbVlBaVSLnOpNLawujkQ%2FAjOon7KwczYMUhAmwopzWPa0mcHCl53mBLjFMOKL3Dtjp6suDbouAFaqLRmPK9FKYD%2BkfJhngBSvxmpS2z8MF0PfpfBwNO6ltop4d7ZBiwN0OLU%2Bq5tp%2F5ajoeJNexRbwLOAVCN7YCNUmcLchVz6bQuhqRsfmXBBRucaNDbv01jllCG65F0D1do4LecEwpuSv4S6P6fzT%2FBLRDGqRbE34DeUYVnASG78egszudb8dJF1ERwkBDQYAl8AJ%2F%2FKQc5OFJrHC1Bkm3coAbnHgpCPvxKGQgQVaIsF2dVhqjr%2BdxaGAUrjzvCuTw4bN9eiEIaPvBVC8%2Fek4x%2B0QmkKffALLXc0bx564FOsGnFuz6mrJVyjx%2FJQLmDI2EA0628YPN4TxPOxLUiYe5w1WQpI1v%2BEsRew35HqrJjDgugo0tkQO690G%2FwPU12ntnnJ8M4LsRZJsxMLN%2BwWVIZIy09inqF1utYYVxN%2FtT30tWjxWwOOf%2FAprJ7HJEF%2BmhTbwkZOiNKfHMbA%2BzefbpECeDtwVGjMhgAYDrretf%2F2sNQqhhe0wkJAzWrmd3VEcqKGETd4cpKzqmYXC3fhE34RPgh49G928l%2FEps6rqIPMHqa3X%2B5sWXx2EIy6SfxA8881O59V4qjo00biSEG0UiaibrXV1M%2F8OnwSV6P425rFPN4M7y7oHagwOV8%2BGsp2%2FFU5SeboNqilZ2uAcDVmVyafaXEsVcjaiE2BawLKjKZNCTcafTOHNMSQOGhLKG2l0Dczeice4aHmkqWnkl%2Bq%2BNp8xVjbLHIta5INEED5X7d7y%2BOOOrJe8nVwH6WhKs9ey5%2F93IqSE%3D&ctl00%24Menu1%24s1%24txtSearch=&ctl00%24cph1%24d1%24cboExchange=INDEX&ctl00%24cph1%24d1%24cboDataFormat=9&ctl00%24cph1%24d1%24cboPeriod=0&ctl00%24cph1%24d1%24chkAllSymbols=on&ctl00%24cph1%24d1%24txtEndDate=06%2F23%2F2014&ctl00%24cph1%24hd1%24cboExchange=INDEX&ctl00%24cph1%24hd1%24cboDataFormat=9&ctl00%24cph1%24ls1%24txtEmail=jfmatth&ctl00%24cph1%24ls1%24txtPassword=password&ctl00%24cph1%24ls1%24btnLogin=Login'

curl -A "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0" -b cookiejar.txt -c cookiejar.txt -d $cookie http://www.eoddata.com/download.aspx > datafile.html
curl -A "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0" -b cookiejar.txt -c cookiejar.txt http://www.eoddata.com/download.aspx > datafile.html

DATE=$(date '+%Y%m%d')
FIELD=$(sed -n -e 's/.*\<a href="\/data\/filedownload\.aspx?e=INDEX&sd='${DATE}'&ed='${DATE}'&d=4&k=\([a-zA-Z0-9]*\)&o=d&ea=1&p=0">.*/\1/ p' datafile.html)

#URL1="http://www.eoddata.com/data/filedownload.aspx?e=AMEX&sd=${DATE}&ed=${DATE}&d=4&k=fyqzhg7fd7&o=d&ea=1&p=0"
#URL2='http://www.eoddata.com/data/filedownload.aspx?e=AMEX&sd=20140623&ed=20140623&d=4&k=acrsrwhm82&o=d&ea=1&p=0'
#http://www.eoddata.com/data/filedownload.aspx?e=INDEX&sd=20140623&ed=20140623&d=4&k=acrsrwhm82&o=d&ea=1&p=0
#http://www.eoddata.com/data/filedownload.aspx?e=INDEX&sd=20140624&ed=20140624&d=4&k=acrsrwhm82&o=d&ea=1&p=0
#http://www.eoddata.com/data/filedownload.aspx?e=INDEX&sd=20140611&ed=20140611&d=4&k=vkrceksx2d&o=d&ea=1&p=0

URLa='http://www.eoddata.com/data/filedownload.aspx?e=AMEX&sd='$DATE'&ed='$DATE'&d=4&k='$FIELD'&o=d&ea=1&p=0'
URLn='http://www.eoddata.com/data/filedownload.aspx?e=NASDAQ&sd='$DATE'&ed='$DATE'&d=4&k='$FIELD'&o=d&ea=1&p=0'
URLq='http://www.eoddata.com/data/filedownload.aspx?e=NYSE&sd='$DATE'&ed='$DATE'&d=4&k='$FIELD'&o=d&ea=1&p=0'

echo $URL

curl -A "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0" -b cookiejar.txt -c cookiejar.txt -L $URLa -o AMEX_prices.csv
curl -A "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0" -b cookiejar.txt -c cookiejar.txt -L $URLn -o NYSE_prices.csv
curl -A "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0" -b cookiejar.txt -c cookiejar.txt -L $URLq -o NASDAQ_prices.csv

curl -3 -F formdata=@AMEX_prices.csv $OPENSHIFT_APP_DNS/loader/raw/prices/AMEX
curl -3 -F formdata=@NASDAQ_prices.csv $OPENSHIFT_APP_DNS/loader/raw/prices/NASDAQ
curl -3 -F formdata=@NYSE_prices.csv $OPENSHIFT_APP_DNS/loader/raw/prices/NYSE

curl $OPENSHIFT_APP_DNS/loader

rm cookiejar.txt
rm datafile.html
 