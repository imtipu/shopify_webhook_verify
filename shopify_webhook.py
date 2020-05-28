import hmac
import hashlib
import base64

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


def computed_hmac(secret, body):
    hash_code = hmac.new(secret.encode('utf-8'), body, hashlib.sha256)
    return base64.b64encode(hash_code.digest()).decode()


def verify_hmac(secret, body, shopify_hmac):
    return get_hmac(secret, body) == shopify_hmac
    

@csrf_exempt
@api_view(['POST'])
def cart_webhook(request):
    shopify_hmac = request.headers.get('X-Shopify-Hmac-Sha256')
    if hmac_is_valid(settings.SHOPIFY_WEBHOOK_SIGNED_KEY, request.body, shopify_hmac):
        print('valid')
    else:
        print('invalid')
    return Response(status=status.HTTP_200_OK)
