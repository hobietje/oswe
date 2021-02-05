# JWT

Custom tools to mess with JWT tokens.

# Use Cases

__Parse a JWT token.__

Set the JWT variable in the `env` file.

Run `make jwt-parse`

__Create a token with a 'none' algorithm__

Set the `JWT_ALGO=none`, `JWT_SECRET=`, and the appropriate contents for the `JWT_BODY`.

Run `make jwt-create`

# TODO

* Crack using leaked JWT secrets from code examples, git repos, etc.
* Brute force JWTs