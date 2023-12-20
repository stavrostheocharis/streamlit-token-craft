import os

modules = os.listdir("token_manager")

for module in modules:
    path = os.path.join("token_manager", "frontend")
    if os.path.exists(path):
        print(f"Preparing {path}")
        os.system(f"cd {path} && npm i && npm run build")
