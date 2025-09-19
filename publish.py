import os
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
BUILD_DIR = BASE / "site"  # where generate_site.py outputs files

GIT_REMOTE = os.environ.get("GIT_REMOTE", "origin")
GIT_BRANCH = os.environ.get("GIT_BRANCH", "gh-pages")
COMMITTER_NAME = os.environ.get("COMMITTER_NAME", "daily-meme-bot")
COMMITTER_EMAIL = os.environ.get("COMMITTER_EMAIL", "meme-bot@example.com")


def run(cmd, **kwargs):
    print("+", " ".join(cmd))
    res = subprocess.run(cmd, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, **kwargs)
    if res.returncode != 0:
        print("ERROR:", res.stderr.strip())
        sys.exit(res.returncode)
    return res


def build_site():
    """Run fetch_memes.py and generate_site.py before publishing."""
    run([sys.executable, str(BASE / "fetch_memes.py")])
    run([sys.executable, str(BASE / "generate_site.py")])


def publish():
    if not BUILD_DIR.exists():
        print("No build directory found. Run generate_site.py first.")
        sys.exit(1)

    import tempfile, shutil
    tmp = Path(tempfile.mkdtemp(prefix="dm-"))
    try:
        # copy build files directly into temp dir root
        shutil.copytree(BUILD_DIR, tmp, dirs_exist_ok=True)

        cwd = tmp
        run(["git", "init"], cwd=str(cwd))
        run(["git", "config", "user.email", COMMITTER_EMAIL], cwd=str(cwd))
        run(["git", "config", "user.name", COMMITTER_NAME], cwd=str(cwd))
        run(["git", "add", "."], cwd=str(cwd))
        run(["git", "commit", "-m", "Daily update"], cwd=str(cwd))

        # get repo URL from your main repo
        repo_url = subprocess.run(
            ["git", "config", "--get", f"remote.{GIT_REMOTE}.url"],
            cwd=str(BASE),
            stdout=subprocess.PIPE,
            text=True
        ).stdout.strip()
        if not repo_url:
            print("Could not determine repo remote URL. Make sure git remote exists in your repo.")
            sys.exit(1)

        run(["git", "remote", "add", "origin", repo_url], cwd=str(cwd))
        run(["git", "push", "-f", "origin", f"master:{GIT_BRANCH}"], cwd=str(cwd))
        print("✅ Published build to branch", GIT_BRANCH)
    finally:
        shutil.rmtree(tmp)


if __name__ == "__main__":
    build_site()
    publish()