import json
import os

# getting current folder path
base_path = os.path.dirname(os.path.abspath(__file__))


# ---------- file handling ----------
def read_data(file):
    path = os.path.join(base_path, file)

    if not os.path.exists(path):
        # create file if not exists
        with open(path, 'w') as f:
            json.dump([], f)
        return []

    try:
        with open(path, 'r') as f:
            return json.load(f)
    except:
        print("Problem reading file...")
        return []


def write_data(file, data):
    path = os.path.join(base_path, file)
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


# ---------- user ----------
class User:
    def register(self):
        users = read_data("users.json")

        name = input("username: ")
        pwd = input("password: ")

        # checking if already exists
        for u in users:
            if u["username"] == name:
                print("username already taken")
                return

        users.append({
            "username": name,
            "password": pwd
        })

        write_data("users.json", users)
        print("registered successfully")

    def login(self):
        users = read_data("users.json")

        name = input("username: ")
        pwd = input("password: ")

        for u in users:
            if u["username"] == name and u["password"] == pwd:
                print("login done")
                return name

        print("wrong username/password")
        return None


# ---------- products ----------
class Product:
    def show(self):
        products = read_data("products.json")

        print("\nproducts list:")

        if len(products) == 0:
            print("nothing available")
            return

        for p in products:
            print(p["id"], "-", p["name"], "₹", p["price"])


# ---------- cart ----------
class Cart:
    def __init__(self):
        self.data = []

    def add(self):
        products = read_data("products.json")

        if not products:
            print("no items to add")
            return

        try:
            pid = int(input("enter id: "))
        except:
            print("enter number only")
            return

        for p in products:
            if int(p["id"]) == pid:
                self.data.append(p)
                print("added:", p["name"])
                return

        print("id not found")

    def show(self):
        if not self.data:
            print("cart empty")
            return

        total = 0
        print("\ncart:")

        for item in self.data:
            print(item["name"], "-", item["price"])
            total += item["price"]

        print("total =", total)


# ---------- order ----------
class Order:
    def place(self, user, cart):
        if not cart.data:
            print("cart is empty")
            return

        orders = read_data("orders.json")

        total = 0
        for i in cart.data:
            total += i["price"]

        orders.append({
            "user": user,
            "items": cart.data,
            "total": total
        })

        write_data("orders.json", orders)

        print("order placed, amount =", total)
        cart.data.clear()


# ---------- main ----------
def main():
    u = User()
    p = Product()
    c = Cart()
    o = Order()

    current_user = None

    while True:
        print("\n--- OneCart ---")
        print("1 register")
        print("2 login")
        print("3 products")
        print("4 add to cart")
        print("5 view cart")
        print("6 order")
        print("7 exit")

        ch = input("choice: ")

        if ch == "1":
            u.register()

        elif ch == "2":
            current_user = u.login()

        elif ch == "3":
            p.show()

        elif ch == "4":
            if current_user:
                c.add()
            else:
                print("login first")

        elif ch == "5":
            c.show()

        elif ch == "6":
            if current_user:
                o.place(current_user, c)
            else:
                print("please login")

        elif ch == "7":
            print("thank you for using OneCart")
            break

        else:
            print("invalid choice")


if __name__ == "__main__":
    main()
