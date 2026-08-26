from models import create_table
from user_repo import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user
)

def main():
    create_table()
    alice_id = create_user(name="Alice",email="alice@example.com")
    bob_id = create_user(name="Bob",email="bob@example.com")
    print(f"Created users:{alice_id},{bob_id}")
    users = get_all_users()
    for u in users:
        print(u)
    alice = get_user_by_id(alice_id)
    update_user(alice_id,name="Alice smith",email="alice.smith@workday.com")
    
    delete_user(bob_id)
    
if __name__ == "__main__":
    main()