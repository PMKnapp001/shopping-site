"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(
        self,
        first_name,
        last_name,
        email,
        password
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


    def __repr__(self):

        return (
            f"<Customer: {self.first_name}, {self.last_name}, {self.email}>"
        )


def read_customers_from_file(filepath):

    all_customers = {}

    with open(filepath) as file:
        for line in file:
            (
                first_name,
                last_name,
                email,
                password
            ) = line.strip().split("|")

            all_customers[email] = Customer(
                                        first_name,
                                        last_name,
                                        email,
                                        password
                                        )

    return all_customers


def get_by_email(email):
    if customers.get(email) == None:
        print("returning false")
        return False
    
    else:
        return customers[email]
    
customers = read_customers_from_file("customers.txt")

