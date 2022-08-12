[{
        "model": "products.product",
        "pk": 1,
        "fields": {
            "flavour": "Chocolate Whey Protein",
            "description": "Chocolate flavour with sweetener.",
            "size": "1",
            "price": "14.99"
        }
    },
    {
        "model": "products.product",
        "pk": 2,
        "fields": {
            "flavour": "Banana Whey Protein",
            "description": "Banana flavour with sweetener.",
            "size": "1",
            "price": "14.99"
        }
    },
    {
        "model": "products.product",
        "pk": 3,
        "fields": {
            "flavour": "Strawberry Whey Protein",
            "description": "Strawberry flavour with sweetener.",
            "size": "1",
            "price": "14.99"
        }
    },
    {
        "model": "products.product",
        "pk": 4,
        "fields": {
            "flavour": "Cookies & Cream Whey Protein",
            "description": "Cookies & cream flavour with sweetener.",
            "size": "1",
            "price": "14.99"
        }
    },
    {
        "model": "products.nutrition",
        "pk": 3,
        "fields": {
            "product": 1,
            "energy": 400.0,
            "fat": 7.4,
            "carbohydrate": 7.6,
            "sugars": 3.7,
            "protein": 75.0,
            "salt": 0.25
        }
    },
    {
        "model": "products.nutrition",
        "pk": 4,
        "fields": {
            "product": 2,
            "energy": 395.0,
            "fat": 6.2,
            "carbohydrate": 7.1,
            "sugars": 6.0,
            "protein": 77.0,
            "salt": 0.59
        }
    },
    {
        "model": "products.nutrition",
        "pk": 5,
        "fields": {
            "product": 3,
            "energy": 402.0,
            "fat": 6.7,
            "carbohydrate": 4.5,
            "sugars": 12.0,
            "protein": 73.0,
            "salt": 0.25
        }
    },
    {
        "model": "products.nutrition",
        "pk": 6,
        "fields": {
            "product": 4,
            "energy": 409.0,
            "fat": 7.2,
            "carbohydrate": 7.0,
            "sugars": 6.9,
            "protein": 79.0,
            "salt": 0.25
        }
    },
    {
        "model": "products.ingredient",
        "pk": 1,
        "fields": {
            "name": "Whey Protein - Milk (95%)",
            "product": [
                1,
                2,
                3,
                4
            ]
        }
    },
    {
        "model": "products.ingredient",
        "pk": 2,
        "fields": {
            "name": "Emulsifier (Soy Lecithin)",
            "product": [
                1,
                2,
                3,
                4
            ]
        }
    },
    {
        "model": "products.ingredient",
        "pk": 3,
        "fields": {
            "name": "Flavouring",
            "product": [
                1,
                2,
                3,
                4
            ]
        }
    },
    {
        "model": "products.ingredient",
        "pk": 4,
        "fields": {
            "name": "Sweetener (Sucralose)",
            "product": [
                1,
                2,
                3,
                4
            ]
        }
    },
    {
        "model": "products.ingredient",
        "pk": 5,
        "fields": {
            "name": "Cocoa Powder",
            "product": [
                1
            ]
        }
    },
    {
        "model": "products.ingredient",
        "pk": 6,
        "fields": {
            "name": "Colour (Curcumin)",
            "product": [
                2
            ]
        }
    },
    {
        "model": "products.ingredient",
        "pk": 7,
        "fields": {
            "name": "Colour (Beetroot Red)",
            "product": [
                3
            ]
        }
    },
    {
        "model": "products.ingredient",
        "pk": 10,
        "fields": {
            "name": "test",
            "product": []
        }
    }
]