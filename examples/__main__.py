from syrtis_python_client import SyrtisClient


if __name__ == "__main__":
    client = SyrtisClient()
    print(sorted(client.get_entity_schemas().keys()))
