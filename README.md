# shopify_webhook_verify
Python Django Shopify Webhook hmac Verfication

# Set env values in settings.py
```sh
# shopify settings
SHOPIFY_SUBDOMAIN = env.str('SHOPIFY_SUBDOMAIN')
SHOPIFY_DOMAIN = env.str('SHOPIFY_DOMAIN')
SHOPIFY_API_VERSION = env.str('SHOPIFY_API_VERSION', '2020-04')
SHOPIFY_API_KEY = env.str('SHOPIFY_API_KEY', '')
SHOPIFY_APP_PASSWORD = env.str('SHOPIFY_APP_PASSWORD', '')
SHOPIFY_APP_SECRET = env.str('SHOPIFY_APP_SECRET', '')
SHOPIFY_WEBHOOK_SIGNED_KEY = env.str('SHOPIFY_WEBHOOK_SIGNED_KEY', '')
```
# Instruction
go to Shopify settings > Notifications > Webhook
You will find the signed key for webhook verify
set the key to #SHOPIFY_WEBHOOK_SIGNED_KEY = env.str('SHOPIFY_WEBHOOK_SIGNED_KEY', '')

