from voluptuous import Schema, PREVENT_EXTRA

user_schema = Schema(
            {
                "data":
                    {
                        "id": int,
                        "email": str,
                        "first_name": str,
                        "last_name": str,
                        "avatar": str
                    },
                "support":
                    {
                        "url": str,
                        "text": str
                    }
            },
            required= True,
            extra=PREVENT_EXTRA,
    )