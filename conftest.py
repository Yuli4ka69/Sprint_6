import pytest
import random

@pytest.fixture
def generate_user_data():
    """Генерирует существующие данные для заполнения формы."""
    names = ["Анна", "Иван", "Ольга", "Дмитрий", "Мария"]
    surnames = ["Иванова", "Петров", "Сидоров", "Кузнецова", "Смирнов"]
    addresses = [
        "ул. Ленина, д. 10",
        "ул. Пушкина, д. 15",
        "ул. Гагарина, д. 5",
        "ул. Тверская, д. 12",
        "ул. Советская, д. 20"
    ]
    phones = ["+79161234567", "+79161234568", "+79161234569", "+79161234570", "+79161234571"]

    return {
        "name": random.choice(names),
        "surname": random.choice(surnames),
        "address": random.choice(addresses),
        "phone": random.choice(phones)
    }
