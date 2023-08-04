from concurrent.futures import ThreadPoolExecutor

import mrwood


def create_account():
    wood = mrwood.MrWood()

    wood.create_account()

    line = f"{wood.email}:{wood.password}"

    print(f"Created: {line}")

    with open("accounts.txt", "a+") as f:
        f.write(line + "\n")


threadpool = ThreadPoolExecutor(50)

for i in range(int(input("Accounts: "))):
    threadpool.submit(create_account)
