class FilesMapper:
    @staticmethod
    def get():
        return {
            "migrate": "Database.migrate",
            "seed": "Database.Seeders.seed",
            "start": "Console.start",
            "serve": "serve",
        }
