from concurrent.futures import ThreadPoolExecutor

import mrwood


def create_account():
    try:
        wood = mrwood.MrWood()

        wood.create_account()

        line = f"{wood.email}:{wood.password}"

        print(f"Created: {line}")

        wood.send_reset_password()

        print(f"Sent password reset: {line}")

        wood.login()

        print(f"Sent login request: {line}")

        with open("accounts.txt", "a+") as f:
            f.write(line + "\n")
    except Exception as e:
        print(f"error {e}")


threadpool = ThreadPoolExecutor(int(input("Thread Pool Size: ")))

for i in range(int(input("Accounts: "))):
    threadpool.submit(create_account)
