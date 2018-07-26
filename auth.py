"""
    放了一些第三方权限验证的东西,只挑2个copy一下
    OAuth2Mixin
    GoogleOAuth2Mixin

"""

import base64
import binascii
import hashlib
import hmac
import time
import urllib.parse
import uuid

from tornado import httpclient
from tornado import escape
from tornado.httputil import url_concat
from tornado.util import unicode_type


class OAuth2Mixin(object):

    def authorize_redirec(self, redirect_url=None, client_id=None,
                          client_secret=None, extra_params=None,
                          scope=None, response_type="code"):
        args = {
            "redirect_url": redirect_url,
            "client_id": client_id,
            "response_type": response_type
        }
        if extra_params:
            args.update(response_type)
        if scope:
            args['scope'] = ' '.join(scope)
        self.redirect(url_concat(self._OAUTH_AUTHORIZE_URL, args))
