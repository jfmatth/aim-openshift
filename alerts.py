from alerter.views import  generate_alerts, email_alerts

if __name__ == "__main__":

    try:
        generate_alerts()
        email_alerts()
    except:
        print "faiulre on alerts.py"