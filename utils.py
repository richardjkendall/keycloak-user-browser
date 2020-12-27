import urllib, json, requests
import logging
from flask import make_response, jsonify

logger = logging.getLogger(__name__)

def post_to_url(url, **kwargs):
  r = requests.post(url, data=kwargs)
  return r.content

def get_from_url(url, token, **kwargs):
  headers = {
    "Authorization": "Bearer {t}".format(t=token)
  }
  r = requests.get(url, params=kwargs, headers=headers)
  return r.content

def get_keycloak_token(server, client_id, client_secret):
  """
  Gets a token to use to all the admin API
  """
  resp = post_to_url(
    url="https://{server}/auth/realms/master/protocol/openid-connect/token".format(server=server),
    grant_type="password",
    username=client_id,
    password=client_secret,
    client_id="admin-cli"
  )
  resp = json.loads(resp)
  return resp["access_token"]

def get_keycloak_realms(server, token):
  """
  Get a list of available realms
  """
  realms = get_from_url(
    url="https://{server}/auth/admin/realms".format(server=server),
    token=token
  )
  realms = json.loads(realms)
  realms = [realm["id"] for realm in realms]
  return realms

def get_keycloak_users(server, realm, token, **kwargs):
  """
  Get list of users from keycloak
  """
  users = get_from_url(
    url="https://{server}/auth/admin/realms/{realm}/users".format(server=server, realm=realm),
    token=token,
    **kwargs
  )
  return json.loads(users)

def success_json_response(payload):
    """
    Turns payload into a JSON HTTP200 response
    """
    response = make_response(jsonify(payload), 200)
    response.headers["Content-type"] = "application/json"
    return response