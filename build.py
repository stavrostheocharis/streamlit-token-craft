import os

modules = os.listdir("token_craft")

for module in modules:
    path = os.path.join("token_craft", "frontend")
    if os.path.exists(path):
        print(f"Preparing {path}")
        os.system(f"cd {path} && npm i && npm run build")
