import json
import logging
import os

from flask import Flask, render_template, request
from utils import success_json_response, get_keycloak_token, get_keycloak_users, get_keycloak_realms

app = Flask(__name__,
            static_url_path="/static",
            static_folder="static")

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] (%(threadName)-10s) %(message)s')
logger = logging.getLogger(__name__)

SERVER = os.getenv("KC_SERVER")
CLIENTID = os.getenv("KC_CLIENT_ID")
CLIENTSECRET = os.getenv("KC_CLIENT_SECRET")

if SERVER == None:
  logger.error("Missing KC_SERVER environment variable.")

if CLIENTID == None:
  logger.error("Missing KC_CLIENT_ID environment variable.")

if CLIENTSECRET == None:
  logger.error("Missing KC_CLIENT_SECRET environment variable.")

@app.route("/")
def main():
  return render_template("index.html")

@app.route("/api/users")
def get_users():
  realm = request.args.get("realm")
  token = get_keycloak_token(
    server = SERVER,
    client_id = CLIENTID,
    client_secret = CLIENTSECRET
  )
  users = get_keycloak_users(
    server = SERVER,
    realm = realm,
    token = token,
    briefRepresentation = True,
    max = 1000
  )
  return success_json_response({
    "data": users
  })

@app.route("/api/realms")
def get_realms():
  token = get_keycloak_token(
    server = SERVER,
    client_id = CLIENTID,
    client_secret = CLIENTSECRET
  )
  realms = get_keycloak_realms(
    server = SERVER,
    token = token
  )
  return success_json_response({
    "data": realms
  })