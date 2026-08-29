#!/usr/bin/env python3
"""Serve the built site for local development.

Sends Cache-Control: no-store so edits show up on reload without fighting the
browser cache. Note this cannot override JupyterLite's service worker, which
is scoped to /app/ — if app assets look stale, tick "Bypass for network" under
DevTools > Application > Service Workers.
"""
import argparse
import functools
import http.server
import socketserver
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "_site"


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, fmt, *args):
        if "404" in (fmt % args):
            super().log_message(fmt, *args)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--port", type=int, default=8321)
    args = ap.parse_args()

    if not ROOT.exists():
        raise SystemExit(f"no site at {ROOT} — run ./site/build.sh first")

    # Resolve the directory per request rather than chdir-ing into it: the
    # build removes and recreates _site, which would leave a chdir-ed server
    # serving a deleted directory until restarted.
    handler = functools.partial(Handler, directory=str(ROOT))
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", args.port), handler) as httpd:
        print(f"serving {ROOT} at http://localhost:{args.port}/  (no-store; ctrl-c to stop)")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
