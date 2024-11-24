class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."

    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"

    def get_info(self):
        return f"{self.brand} {self.model} - {self.storage}GB, {self.battery_life} hours battery life"


class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, storage, battery_life, camera_megapixels):
        super().__init__(brand, model, storage, battery_life)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        return f"Taking a photo with {self.camera_megapixels}MP camera!"

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, {self.camera_megapixels}MP camera"


# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Apple", "iPhone 14", 128, 20)
    print(phone1.get_info())
    print(phone1.make_call("123-456-7890"))
    print(phone1.send_message("123-456-7890", "Hello!"))

    phone2 = SmartphoneWithCamera("Samsung", "Galaxy S21", 256, 22, 108)
    print(phone2.get_info())
    print(phone2.take_photo())