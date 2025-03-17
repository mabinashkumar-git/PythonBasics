import asyncio
import time


def task(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Finished {name}")

task("Abinash")
task("Mallick")
# Output:
# Starting Abinash
# Finished Abinash
# Starting Mallick
# Finished Mallick

print("*****************************************************************")

async def main():
    await asyncio.gather( task("Abinash"), task("Mallick"))

asyncio.run(main())

# Output:
# Starting Abinash
# Starting Mallick
# Finished Abinash
# Finished Mallick