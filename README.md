# keycloak-user-browser

This is a small tool that allows you to see the users in your Keycloak realms

It is packaged as a container image and available 

## Caution

* This is not designed to be production-ready, it was created for a small use-case on an instance with a small number of users
* This does not implement any kind of authentication, it should be deployed behind a some kind of user-aware reverse proxy for example this one: https://github.com/richardjkendall/oidc-rproxy

## Running this

It expects the following environment variables to be set

| Variable | Purpose |
|---|---|
| KC_SERVER | The hostname for the Keycloak server |
| KC_CLIENT_ID | Username to access the Keycloak API |
| KC_CLIENT_SECRET | Password to access the Keycloak API |
