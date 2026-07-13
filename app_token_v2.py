import base64
import importlib
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request


APP_ID = "4281903"
OWNER = "ekhamis"
REPO = "institutional-trading-academy"
PRIVATE_KEY_PATH = r"C:\Users\ekham\Downloads\ita-academy-builder-ek.2026-07-12.private-key.pem"
GITHUB_API = "https://api.github.com"


def log(message):
    print(message, file=sys.stderr)


def ensure_cryptography():
    try:
        importlib.import_module("cryptography")
        return
    except Exception:
        log("cryptography is missing or broken. Repairing it now...")

    commands = [
        [sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"],
        [sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", "cryptography"],
    ]
    for command in commands:
        log("Running: " + " ".join(command))
        subprocess.check_call(command)

    importlib.import_module("cryptography")


def b64url(data: bytes) -> bytes:
    return base64.urlsafe_b64encode(data).rstrip(b"=")


def make_jwt(app_id: str, private_key_path: str) -> str:
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding

    now = int(time.time())
    header = {"alg": "RS256", "typ": "JWT"}
    payload = {"iat": now - 60, "exp": now + 540, "iss": app_id}

    signing_input = b".".join(
        [
            b64url(json.dumps(header, separators=(",", ":")).encode("utf-8")),
            b64url(json.dumps(payload, separators=(",", ":")).encode("utf-8")),
        ]
    )

    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None)

    signature = private_key.sign(signing_input, padding.PKCS1v15(), hashes.SHA256())
    return (signing_input + b"." + b64url(signature)).decode("utf-8")


def request_json(method: str, url: str, token: str, body=None):
    data = None
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "ita-github-app-publisher-v2",
        "Authorization": token if token.startswith(("Bearer ", "token ")) else f"Bearer {token}",
    }

    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            text = response.read().decode("utf-8")
            return json.loads(text) if text else {}
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API error {error.code} for {url}:\n{detail}") from error


def main() -> int:
    if not os.path.exists(PRIVATE_KEY_PATH):
        print(f"ERROR: Private key file not found: {PRIVATE_KEY_PATH}", file=sys.stderr)
        return 1

    ensure_cryptography()
    jwt_token = make_jwt(APP_ID, PRIVATE_KEY_PATH)
    installation = request_json(
        "GET",
        f"{GITHUB_API}/repos/{OWNER}/{REPO}/installation",
        jwt_token,
    )
    installation_id = installation["id"]

    token_response = request_json(
        "POST",
        f"{GITHUB_API}/app/installations/{installation_id}/access_tokens",
        jwt_token,
        {},
    )
    print(token_response["token"])
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(f"ERROR: dependency command failed: {' '.join(exc.cmd)}", file=sys.stderr)
        raise SystemExit(exc.returncode)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)

