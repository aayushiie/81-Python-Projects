import os

for i in range(1,82):
    if os.path.exists(f"#{i}.py"):
        pass
    else:
        open(f"#{i}.py", "x")
