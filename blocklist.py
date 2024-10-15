"""
blocklist.py


This file just contains the blocklist of JWT tokens. It will be imported by app
and the logout resource so that tokens can be added to the blocklist when the user logs out.

In realworld use REDIS for the blocklist
"""

BLOCKLIST = set()