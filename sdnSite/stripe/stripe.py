import stripe
stripe.api_key = "sk_test_M30Prq2uTpNscIzcaKGclLym"

def request():
    try:
      # Use Stripe's library to make requests...
      pass
    except stripe.error.CardError as e:
      # Since it's a decline, stripe.error.CardError will be caught
      body = e.json_body
      err  = body['error']

      print "Status is: %s" % e.http_status
      print "Type is: %s" % err['type']
      print "Code is: %s" % err['code']
      # param is '' in this case
      print "Param is: %s" % err['param']
      print "Message is: %s" % err['message']
      
      print e
    except stripe.error.RateLimitError as e:
      # Too many requests made to the API too quickly
      print e
      pass
    except stripe.error.InvalidRequestError as e:
      # Invalid parameters were supplied to Stripe's API
      print e
      pass
    except stripe.error.AuthenticationError as e:
      # Authentication with Stripe's API failed
      # (maybe you changed API keys recently)
      print e
      pass
    except stripe.error.APIConnectionError as e:
      # Network communication with Stripe failed
      print e
      pass
    except stripe.error.StripeError as e:
      # Display a very generic error to the user, and maybe send
      # yourself an email
      print e
      pass
    except Exception as e:
      # Something else happened, completely unrelated to Stripe
      print e
      pass

