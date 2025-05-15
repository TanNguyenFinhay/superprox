from faker import Faker


class IPGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_random_ip(self) -> str:
        """Generate a random IP address.

        Returns:
            A random IP address string.
        """
        return self.fake.ipv4_public()


# Create an instance and test the method
if __name__ == "__main__":
    ip_gen = IPGenerator()
    random_ip = ip_gen.generate_random_ip()
    print(f"Generated IP address: {random_ip}")