#!/usr/bin/python3


__version__ = (0, 0, 1)


def format_response(acct, *, mastodon_server, mastodon_user):
    return {
      "subject": acct,
      "aliases": [
        f"https://{mastodon_server}/@{mastodon_user}",
        f"https://{mastodon_server}/users/{mastodon_user}"
      ],
      "links": [
        {
          "rel": "http://webfinger.net/rel/profile-page",
          "type": "text/html",
          "href": f"https://{mastodon_server}/@{mastodon_user}"
        },
        {
          "rel": "self",
          "type": "application/activity+json",
          "href": f"https://{mastodon_server}/users/{mastodon_user}"
        },
        {
          "rel": "http://ostatus.org/schema/1.0/subscribe",
          "template":
          f"https://{mastodon_server}/authorize_interaction?uri={{uri}}"
        }
      ]
    }
