# Project
from core.models import Category


def run():
    category_types = [
        "Ficção",
        "Não Ficção",
        "Autoajuda",
        "Romance",
        "Fantasia",
        "Terror",
        "Suspense",
        "Biografia",
        "História",
        "Ciência",
        "Tecnologia",
        "Artes",
        "Música",
        "Esportes",
        "Infantil",
        "Juvenil",
        "HQs",
        "Mangás",
        "Religião",
        "Filosofia",
        "Política",
        "Economia",
        "Direito",
        "Medicina",
        "Educação",
        "Culinária",
        "Viagens",
        "Casa e Jardim",
        "Hobbies",
    ]

    for cat in category_types:
        Category.objects.create(
            title=cat
        )
