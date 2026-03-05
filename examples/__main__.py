from syrtis_python_client import SyrtisClient, Uesr


if __name__ == "__main__":
    client = SyrtisClient()
    repository = client.get_repository(Uesr)
    print(repository.__class__.__name__)
